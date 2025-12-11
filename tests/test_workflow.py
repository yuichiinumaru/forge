import pytest
import json
from pathlib import Path
from typer.testing import CliRunner
from forge.cli import app

runner = CliRunner()

def test_plan_command_help():
    result = runner.invoke(app, ["plan", "--help"])
    assert result.exit_code == 0
    assert "Start the Planning Phase" in result.stdout

def test_plan_command_execution():
    with runner.isolated_filesystem():
        # Setup mock templates
        # Since logic loads from .forge or repo, isolated filesystem won't have it.
        Path(".forge/templates/agents").mkdir(parents=True)
        Path(".forge/templates/agents/plan.md").write_text("Mock Plan Template")

        result = runner.invoke(app, ["plan", "test-feature"])
        assert result.exit_code == 0
        assert "Mock Plan Template" in result.stdout
        assert "State updated to PLAN" in result.stdout

        # Check state file
        state = json.loads(Path(".forge/state.json").read_text())
        assert state["name"] == "test-feature"
        assert state["phase"] == "plan"

def test_tasks_command_execution():
    with runner.isolated_filesystem():
        Path(".forge/templates/agents").mkdir(parents=True)
        Path(".forge/templates/agents/tasks.md").write_text("Mock Tasks Template")

        # Init state first
        Path(".forge").mkdir(exist_ok=True)
        Path(".forge/state.json").write_text('{"name": "test", "phase": "plan"}')

        result = runner.invoke(app, ["tasks"])
        assert result.exit_code == 0
        assert "Mock Tasks Template" in result.stdout
        assert "State updated to TASKS" in result.stdout

        state = json.loads(Path(".forge/state.json").read_text())
        assert state["phase"] == "tasks"
