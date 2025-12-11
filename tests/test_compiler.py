import pytest
from pathlib import Path
from forge.compiler.markdown import process_template, strip_frontmatter

def test_strip_frontmatter():
    content = "---\ntitle: Test\n---\n# Header"
    assert strip_frontmatter(content).strip() == "# Header"

    content_no_fm = "# Header"
    assert strip_frontmatter(content_no_fm) == "# Header"

def test_process_template_transclusion(tmp_path):
    # Setup
    templates_dir = tmp_path / "templates"
    templates_dir.mkdir()

    (templates_dir / "block.md").write_text("Block Content")
    (templates_dir / "nested.md").write_text("Nested ![[block]]")

    content = "Start ![[nested]] End"
    search_paths = [templates_dir]

    result = process_template(content, search_paths)
    assert "Start Nested Block Content End" in result

def test_process_template_wikilink(tmp_path):
    # Setup
    templates_dir = tmp_path / "templates"
    templates_dir.mkdir()
    (templates_dir / "ref.md").write_text("Reference")

    content = "See [[ref]]"
    search_paths = [templates_dir]

    # We need to change CWD to tmp_path to test relative path resolution,
    # or just expect absolute path if not relative.
    # process_template uses Path.cwd().

    import os
    original_cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        result = process_template(content, search_paths)
        assert "See @templates/ref.md" in result
    finally:
        os.chdir(original_cwd)

def test_recursion_limit(tmp_path):
    templates_dir = tmp_path / "templates"
    templates_dir.mkdir()
    (templates_dir / "loop.md").write_text("![[loop]]")

    content = "![[loop]]"
    search_paths = [templates_dir]

    result = process_template(content, search_paths, max_depth=2)
    assert "Recursion depth exceeded" in result
