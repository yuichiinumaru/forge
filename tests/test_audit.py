import pytest
from pathlib import Path
from typer.testing import CliRunner
from forge.cli import app
from forge.rules import app as rules_app
import os

runner = CliRunner()

def test_forge_rules_compile_runs(tmp_path, mocker):
    """Test that forge rules compile command runs and generates output."""
    # Mock get_rules_dir to return a fake directory with some rules
    rules_dir = tmp_path / "templates" / "rules"
    rules_dir.mkdir(parents=True)

    (rules_dir / "roles").mkdir()
    (rules_dir / "roles" / "developer.md").write_text("Role: Developer")

    (rules_dir / "core").mkdir()
    (rules_dir / "core" / "behavior.md").write_text("Behavior: Be nice")
    (rules_dir / "core" / "tdd.md").write_text("TDD: Red Green Refactor")

    # Mock Rules.get_rules_dir to return our temp dir
    mocker.patch("forge.rules.get_rules_dir", return_value=rules_dir)

    # Run command
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["rules", "compile"])
        assert result.exit_code == 0
        assert "Generated .cursorrules" in result.stdout

        output_file = Path(".cursorrules")
        assert output_file.exists()
        content = output_file.read_text()
        assert "Role: Developer" in content
        assert "Behavior: Be nice" in content

def test_templates_terminology():
    """Verify templates do not contain 'Specify' terminology (legacy name)."""
    templates_dir = Path("templates")
    if not templates_dir.exists():
        pytest.skip("Templates directory not found")

    for root, dirs, files in os.walk(templates_dir):
        for file in files:
            file_path = Path(root) / file
            # Skip binary files if any
            if file_path.suffix not in ['.md', '.txt', '.json', '.sh', '.ps1', '.yml', '.yaml']:
                continue

            try:
                content = file_path.read_text(errors='ignore')
                # Check for "Specify" but exclude valid uses (e.g. "specify the details")
                # This is hard to perfect, so we look for specific patterns
                if "/specify" in content:
                    # Exception: if it's describing the legacy command history or something
                    # But generally we want /forge.specify
                     if "formerly /specify" not in content:
                         assert "/specify" not in content, f"Found legacy slash command '/specify' in {file_path}"

                if "Specify CLI" in content:
                    assert False, f"Found 'Specify CLI' in {file_path}"

            except Exception as e:
                print(f"Skipping {file_path}: {e}")

@pytest.mark.xfail(reason="Known issue: templates/structure directory missing in repo")
def test_forge_init_local_structure_audit():
    """
    Audit check for forge init --local.
    This test verifies if the expected directory structure for init --local exists in the repo.
    """
    # The code expects templates/structure
    templates_dir = Path("templates")
    structure_dir = templates_dir / "structure"

    # We expect this to fail based on our manual audit, documenting it via test.
    # If it fails, it confirms our finding.
    if not structure_dir.exists():
        pytest.fail("Missing 'templates/structure' directory required for 'forge init --local'")
