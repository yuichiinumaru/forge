import json
from pathlib import Path
from typing import Optional
from forge.models import FeatureState, Phase, Status

STATE_FILE_NAME = "state.json"
FORGE_DIR = ".forge"

def get_forge_path() -> Path:
    """Get the path to the .forge directory in the current project."""
    # Assuming CWD is project root.
    # In a real scenario we might want to traverse up to find it.
    return Path.cwd() / FORGE_DIR

def get_state_path() -> Path:
    """Get the path to the state file."""
    return get_forge_path() / STATE_FILE_NAME

def load_state() -> FeatureState:
    """Load the current workflow state. If not found, returns a default state."""
    state_path = get_state_path()
    if not state_path.exists():
        return FeatureState(name="Project")

    try:
        with open(state_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return FeatureState.from_dict(data)
    except (json.JSONDecodeError, KeyError):
        # Fallback if state is corrupted
        return FeatureState(name="Project", status=Status.FAILED)

def save_state(state: FeatureState) -> None:
    """Save the workflow state to disk."""
    state_path = get_state_path()
    # Ensure .forge exists
    if not state_path.parent.exists():
        state_path.parent.mkdir(parents=True, exist_ok=True)

    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(state.to_dict(), f, indent=2)

def update_phase(phase: Phase) -> None:
    """Update the current phase in the state."""
    state = load_state()
    state.phase = phase
    state.updated_at = __import__("datetime").datetime.now().isoformat()
    save_state(state)
