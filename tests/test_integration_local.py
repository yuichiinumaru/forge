import pytest
import subprocess
import shutil
import os
from pathlib import Path

def test_init_local(tmp_path):
    """Integration test for `forge init --local`."""
    # Setup
    project_name = "test_project"
    project_path = tmp_path / project_name

    # We need to run `forge init` from the repo root to access templates
    repo_root = Path.cwd()

    # Command
    cmd = [
        "python3", "-m", "forge", "init",
        str(project_path),
        "--local",
        "--ai", "copilot",
        "--no-git",
        "--ignore-agent-tools",
        "--script", "sh" # force script type to avoid interaction
    ]

    # Run
    # Set PYTHONPATH to repo_root/src
    env = os.environ.copy()
    env["PYTHONPATH"] = str(repo_root / "src")

    result = subprocess.run(cmd, env=env, capture_output=True, text=True, cwd=repo_root)

    # Verify
    if result.returncode != 0:
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

    assert result.returncode == 0, f"Init failed: {result.stderr}"
    assert project_path.exists()
    assert (project_path / ".forge").exists()
    assert (project_path / ".github" / "prompts").exists() # Copilot config
