from typing import Protocol, List, Any
from pathlib import Path
import importlib.metadata

class Plugin(Protocol):
    """Protocol for Forge Plugins."""
    name: str
    version: str

    def register(self, app: Any):
        """Register commands or hooks with the main Forge app."""
        ...

def load_plugins(app: Any) -> List[Plugin]:
    """Load installed plugins using entry points."""
    plugins = []

    # Check for entry points "forge.plugins"
    try:
        # Python 3.10+
        entry_points = importlib.metadata.entry_points(group="forge.plugins")
    except TypeError:
        # Python 3.8/3.9 compatibility (entry_points() returned dict)
        all_eps = importlib.metadata.entry_points()
        entry_points = all_eps.get("forge.plugins", [])

    for ep in entry_points:
        try:
            plugin_factory = ep.load()
            plugin = plugin_factory()
            if hasattr(plugin, "register"):
                plugin.register(app)
                plugins.append(plugin)
        except Exception as e:
            # Silently fail or log if logging available
            pass

    return plugins
