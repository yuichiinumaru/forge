import pytest
from pathlib import Path
from typer.testing import CliRunner
from forge.commands.workflow import workflow_app
from forge.state import load_state, Phase, save_state
from forge.models import FeatureState

runner = CliRunner()

@pytest.fixture
def mock_templates(tmp_path):
    d = tmp_path / "templates" / "agents"
    d.mkdir(parents=True)
    (d / "plan.md").write_text("Plan Template")
    (d / "tasks.md").write_text("Tasks Template")
    (d / "implement.md").write_text("Implement Template")
    (d / "optimize.md").write_text("Optimize Template")
    return d

def test_workflow_transitions(tmp_path, monkeypatch, mock_templates):
    monkeypatch.chdir(tmp_path)

    # Initialize state
    save_state(FeatureState(name="Init"))

    # Plan
    result = runner.invoke(workflow_app, ["plan", "NewFeature"])
    assert result.exit_code == 0
    state = load_state()
    assert state.phase == Phase.PLAN
    assert state.name == "NewFeature"

    # Tasks
    result = runner.invoke(workflow_app, ["tasks"])
    assert result.exit_code == 0
    assert load_state().phase == Phase.TASKS

    # Implement
    result = runner.invoke(workflow_app, ["implement"])
    assert result.exit_code == 0
    assert load_state().phase == Phase.IMPLEMENT

    # Optimize
    result = runner.invoke(workflow_app, ["optimize"])
    assert result.exit_code == 0
    assert load_state().phase == Phase.OPTIMIZE
