import sys
import typer
from rich.align import Align

from forge.utils import console, show_banner
from forge.rules import app as rules_app
from forge.commands.init import init_command
from forge.commands.check import check_command

app = typer.Typer(
    name="forge",
    help="Setup tool for Forge spec-driven development projects",
    add_completion=False,
    invoke_without_command=True,
)

app.add_typer(rules_app, name="rules", help="Manage and compile project rules (.cursorrules, etc.)")

@app.callback()
def callback(ctx: typer.Context):
    """Show banner when no subcommand is provided."""
    if (
        ctx.invoked_subcommand is None
        and "--help" not in sys.argv
        and "-h" not in sys.argv
    ):
        show_banner()
        console.print(
            Align.center("[dim]Run 'forge --help' for usage information[/dim]")
        )
        console.print()

app.command(name="init")(init_command)
app.command(name="check")(check_command)

def main():
    app()

if __name__ == "__main__":
    main()
