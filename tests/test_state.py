import pytest
import json
from pathlib import Path
from forge.state import save_state, load_state, get_state_path
from forge.models import FeatureState, Phase, Status

def test_save_and_load_state(tmp_path, monkeypatch):
    # Mock CWD to tmp_path
    monkeypatch.chdir(tmp_path)

    state = FeatureState(name="TestProject", phase=Phase.PLAN)
    save_state(state)

    loaded = load_state()
    assert loaded.name == "TestProject"
    assert loaded.phase == Phase.PLAN
    assert loaded.status == Status.PENDING

def test_load_state_missing(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    state = load_state()
    # Should return default state
    assert state.name == "Project"
    assert state.phase == Phase.INIT

def test_load_state_corrupted(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    state_path = tmp_path / ".forge" / "state.json"
    state_path.parent.mkdir()
    state_path.write_text("{invalid json")

    state = load_state()
    assert state.status == Status.FAILED
