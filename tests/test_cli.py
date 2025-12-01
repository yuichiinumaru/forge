import pytest
from typer.testing import CliRunner
from forge.cli import app
from forge import __init__  # Verify import works

runner = CliRunner()

def test_init_help():
    result = runner.invoke(app, ["init", "--help"])
    assert result.exit_code == 0
    assert "Initialize a new Forge project" in result.stdout

def test_init_missing_args():
    """Test that running init without args shows error or help (depending on implementation)."""
    # The current implementation requires project_name OR --here
    result = runner.invoke(app, ["init"])
    # Typer usually shows Missing Argument error and exits with non-zero
    assert result.exit_code != 0
    assert "Missing argument" in result.stdout or "Error" in result.stdout

def test_check_command():
    result = runner.invoke(app, ["check"])
    assert result.exit_code == 0
    assert "Checking for installed tools" in result.stdout

def test_local_flag_help():
    """Test that the --local flag is visible in help."""
    result = runner.invoke(app, ["init", "--help"])
    assert "--local" in result.stdout
