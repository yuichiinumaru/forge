import pytest
from pathlib import Path
from forge.utils import is_git_repo, check_tool
from forge.config import AGENT_CONFIG

def test_check_tool_git(mocker):
    """Test check_tool returns True when git is found."""
    mocker.patch("shutil.which", return_value="/usr/bin/git")
    assert check_tool("git") is True

def test_check_tool_missing(mocker):
    """Test check_tool returns False when tool is missing."""
    mocker.patch("shutil.which", return_value=None)
    assert check_tool("nonexistent_tool") is False

def test_agent_config_integrity():
    """Ensure AGENT_CONFIG has required keys."""
    for agent, config in AGENT_CONFIG.items():
        assert "name" in config
        assert "folder" in config
        assert "requires_cli" in config
        if config["requires_cli"]:
             assert "install_url" in config
             assert config["install_url"] is not None

def test_is_git_repo_true(mocker, tmp_path):
    """Test is_git_repo returns True inside a git repo."""
    # Mock subprocess.run to succeed
    mocker.patch("subprocess.run")
    assert is_git_repo(tmp_path) is True

def test_is_git_repo_false(mocker, tmp_path):
    """Test is_git_repo returns False outside a git repo."""
    # Mock subprocess.run to fail
    mocker.patch("subprocess.run", side_effect=FileNotFoundError)
    assert is_git_repo(tmp_path) is False
