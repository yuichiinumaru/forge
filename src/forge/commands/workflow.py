import typer
from pathlib import Path
from datetime import datetime
from typing import List
from rich.markdown import Markdown
from forge.state import update_phase, load_state, Phase, save_state
from forge.utils import console
from forge.compiler.markdown import process_template

workflow_app = typer.Typer(help="Workflow management commands")

def get_search_paths() -> List[Path]:
    """Get search paths for template resolution."""
    paths = []

    # Priority 1: .forge/templates (User Customizations)
    base_local = Path.cwd() / ".forge" / "templates"
    paths.extend([
        base_local / "blocks",
        base_local / "instructions",
        base_local / "personas",
        base_local / "agents",
        base_local / "workflows",
    ])

    # Priority 2: Repo root templates (Dev environment)
    base_repo = Path.cwd() / "templates"
    paths.extend([
        base_repo / "blocks",
        base_repo / "instructions",
        base_repo / "personas",
        base_repo / "agents",
        base_repo / "workflows",
    ])

    # Filter only existing paths
    return [p for p in paths if p.exists()]

def load_agent_template(agent_name: str) -> str:
    """Load agent template and resolve wikilinks/embeds."""
    content = ""

    # Priority 1: User customized template in .forge/templates/agents
    local_template = Path.cwd() / ".forge" / "templates" / "agents" / f"{agent_name}.md"
    if local_template.exists():
        content = local_template.read_text(encoding="utf-8")
    else:
        # Priority 2: Dev environment (repo root)
        repo_template = Path.cwd() / "templates" / "agents" / f"{agent_name}.md"
        if repo_template.exists():
            content = repo_template.read_text(encoding="utf-8")
        else:
            return f"Error: Template for agent '{agent_name}' not found."

    # Process template
    return process_template(content, get_search_paths())

@workflow_app.command("plan")
def plan(feature: str = typer.Argument(None, help="Feature name or slug")):
    """
    Start the Planning Phase. Generates docs/01-plan.md.
    """
    console.print("[bold blue]Starting Planning Phase[/bold blue]")

    state = load_state()
    if feature:
        state.name = feature

    state.phase = Phase.PLAN
    state.updated_at = datetime.now().isoformat()
    save_state(state)

    template = load_agent_template("plan")
    console.print(Markdown(template))
    console.print("\n[bold green]State updated to PLAN. Copy the prompt above to your AI agent.[/bold green]")

@workflow_app.command("tasks")
def tasks():
    """
    Start the Task Breakdown Phase. Generates docs/02-tasks.md.
    """
    console.print("[bold blue]Starting Task Breakdown Phase[/bold blue]")

    update_phase(Phase.TASKS)

    template = load_agent_template("tasks")
    console.print(Markdown(template))
    console.print("\n[bold green]State updated to TASKS. Copy the prompt above to your AI agent.[/bold green]")

@workflow_app.command("implement")
def implement():
    """
    Start the Implementation Phase. Spawns workers for tasks.
    """
    console.print("[bold blue]Starting Implementation Phase[/bold blue]")

    update_phase(Phase.IMPLEMENT)

    template = load_agent_template("implement") # or worker.md
    console.print(Markdown(template))
    console.print("\n[bold green]State updated to IMPLEMENT. Copy the prompt above to your AI agent.[/bold green]")

@workflow_app.command("optimize")
def optimize():
    """
    Start the Optimization Phase. Runs quality gates.
    """
    console.print("[bold blue]Starting Optimization Phase[/bold blue]")

    update_phase(Phase.OPTIMIZE)

    template = load_agent_template("optimize")
    console.print(Markdown(template))
    console.print("\n[bold green]State updated to OPTIMIZE. Copy the prompt above to your AI agent.[/bold green]")
