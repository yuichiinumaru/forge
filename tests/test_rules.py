import pytest
from pathlib import Path
from forge.rules import detect_stack, load_rule_block

def test_detect_stack_python(tmp_path):
    (tmp_path / "pyproject.toml").touch()
    tags = detect_stack(tmp_path)
    assert "languages/python" in tags

def test_detect_stack_java(tmp_path):
    (tmp_path / "pom.xml").touch()
    tags = detect_stack(tmp_path)
    assert "languages/java" in tags

def test_detect_stack_react_tailwind(tmp_path):
    (tmp_path / "package.json").write_text('{"dependencies": {"react": "18", "tailwindcss": "3"}}')
    tags = detect_stack(tmp_path)
    assert "frameworks/react" in tags
    assert "frameworks/tailwind" in tags

def test_load_rule_block_missing(monkeypatch, tmp_path):
    # Mock rules dir
    def mock_get_rules_dir():
        return tmp_path

    import forge.rules
    monkeypatch.setattr(forge.rules, "get_rules_dir", mock_get_rules_dir)

    content = load_rule_block("core", "missing")
    assert "Missing rule block" in content
