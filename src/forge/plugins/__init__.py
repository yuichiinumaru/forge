from typing import Protocol, List
from pathlib import Path

class Plugin(Protocol):
    """Protocol for Forge Plugins."""
    name: str
    version: str

    def register(self, app):
        """Register commands or hooks with the main Forge app."""
        ...

def load_plugins() -> List[Plugin]:
    """Load installed plugins (placeholder logic)."""
    # TODO: Implement entry_point based loading or directory scanning
    return []
