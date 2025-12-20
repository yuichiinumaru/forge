import os
import sys
import shutil
import ssl
import httpx
from pathlib import Path
from rich.panel import Panel
from rich.live import Live

from forge.config import AGENT_CONFIG
from forge.utils import (
    console, StepTracker, check_tool, is_git_repo, init_git_repo, ensure_executable_scripts, ssl_context
)
from forge.services.fetcher import copy_local_template, download_and_extract_template
from forge.state import save_state, FeatureState

class Scaffolder:
    def __init__(
        self,
        project_path: Path,
        project_name: str,
        ai_assistant: str,
        script_type: str,
        local_templates: bool = False,
        no_git: bool = False,
        here: bool = False,
        debug: bool = False,
        skip_tls: bool = False,
        github_token: str = None,
    ):
        self.project_path = project_path
        self.project_name = project_name
        self.ai_assistant = ai_assistant
        self.script_type = script_type
        self.local_templates = local_templates
        self.no_git = no_git
        self.here = here
        self.debug = debug
        self.skip_tls = skip_tls
        self.github_token = github_token

    def run(self):
        tracker = StepTracker("Initialize Forge Project")
        sys._forge_tracker_active = True

        tracker.add("precheck", "Check required tools")
        tracker.complete("precheck", "ok")
        tracker.add("ai-select", "Select AI assistant")
        tracker.complete("ai-select", f"{self.ai_assistant}")
        tracker.add("script-select", "Select script type")
        tracker.complete("script-select", self.script_type)

        if self.local_templates:
            tracker.add("copy-local", "Copy local template")
        else:
            tracker.add("fetch", "Fetch latest release")
            tracker.add("download", "Download template")
            tracker.add("extract", "Extract template")
            tracker.add("zip-list", "Archive contents")
            tracker.add("extracted-summary", "Extraction summary")
            tracker.add("cleanup", "Cleanup")

        for key, label in [
            ("chmod", "Ensure scripts executable"),
            ("state", "Initialize workflow state"),
            ("agents", "Copy agent templates"),
            ("git", "Initialize git repository"),
            ("final", "Finalize"),
        ]:
            tracker.add(key, label)

        git_error_message = None

        with Live(
            tracker.render(), console=console, refresh_per_second=8, transient=True
        ) as live:
            tracker.attach_refresh(lambda: live.update(tracker.render()))
            try:
                if self.local_templates:
                    copy_local_template(
                        self.project_path,
                        self.ai_assistant,
                        self.script_type,
                        self.here,
                        tracker=tracker,
                        debug=self.debug,
                    )
                else:
                    verify = not self.skip_tls
                    local_ssl_context = ssl_context if verify else False
                    local_client = httpx.Client(verify=local_ssl_context)

                    download_and_extract_template(
                        self.project_path,
                        self.ai_assistant,
                        self.script_type,
                        self.here,
                        verbose=False,
                        tracker=tracker,
                        client=local_client,
                        debug=self.debug,
                        github_token=self.github_token,
                    )

                ensure_executable_scripts(self.project_path, tracker=tracker)

                # Initialize State
                tracker.start("state")
                try:
                    original_cwd_state = Path.cwd()
                    os.chdir(self.project_path)
                    save_state(FeatureState(name=self.project_name or self.project_path.name or "Project"))
                    os.chdir(original_cwd_state)
                    tracker.complete("state")
                except Exception as e:
                    tracker.error("state", str(e))

                # Copy Agent Templates
                tracker.start("agents")
                try:
                    import sys
                    potential_roots = [
                        Path.cwd(),
                        Path(__file__).parent.parent.parent.parent,
                    ]
                    if hasattr(sys, 'prefix'):
                         potential_roots.append(Path(sys.prefix) / "share" / "forge")

                    templates_root = None
                    for root in potential_roots:
                        if (root / "templates").is_dir():
                            templates_root = root / "templates"
                            break

                    if templates_root:
                        src_agents = templates_root / "agents"
                        if src_agents.exists():
                             dst_agents = self.project_path / ".forge" / "templates" / "agents"
                             dst_agents.mkdir(parents=True, exist_ok=True)
                             copied_count = 0
                             for item in src_agents.glob("*.md"):
                                 shutil.copy2(item, dst_agents)
                                 copied_count += 1
                             tracker.complete("agents", f"copied {copied_count} templates")
                        else:
                             tracker.skip("agents", "source agents dir not found")
                    else:
                         dst_agents = self.project_path / ".forge" / "templates" / "agents"
                         if dst_agents.exists() and list(dst_agents.glob("*.md")):
                              tracker.complete("agents", "already present")
                         else:
                              tracker.skip("agents", "source not found")
                except Exception as e:
                    tracker.error("agents", str(e))

                if not self.no_git:
                    tracker.start("git")
                    if is_git_repo(self.project_path):
                        tracker.complete("git", "existing repo detected")
                    elif check_tool("git"):
                        success, error_msg = init_git_repo(self.project_path, quiet=True)
                        if success:
                            tracker.complete("git", "initialized")
                        else:
                            tracker.error("git", "init failed")
                            git_error_message = error_msg
                    else:
                        tracker.skip("git", "git not available")
                else:
                    tracker.skip("git", "--no-git flag")

                tracker.complete("final", "project ready")

                return True, git_error_message, tracker

            except Exception as e:
                tracker.error("final", str(e))
                if not self.here and self.project_path.exists():
                     shutil.rmtree(self.project_path)
                raise e
