from forge.plugins import load_plugins
from unittest.mock import Mock

def test_load_plugins_empty():
    app = Mock()
    plugins = load_plugins(app)
    assert isinstance(plugins, list)
    # Since no plugins are installed in test env, it should be empty
    assert len(plugins) == 0
