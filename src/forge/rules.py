import os
from pathlib import Path
from typing import List, Optional
import typer

app = typer.Typer()

RULES_DIR = Path(__file__).parent.parent.parent / "templates" / "rules"

def load_rule_block(category: str, name: str) -> str:
    """Load a specific rule block from templates."""
    # In a real installed package, this would look in package data or a user config dir
    # For now, we assume we are running in the repo context
    path = RULES_DIR / category / f"{name}.md"
    if not path.exists():
        return f"<!-- Missing rule block: {category}/{name} -->"
    return path.read_text()

def detect_stack(project_path: Path) -> List[str]:
    """Auto-detect the tech stack based on files."""
    tags = []

    # Python
    if (project_path / "pyproject.toml").exists() or (project_path / "requirements.txt").exists():
        tags.append("languages/python")

        # Frameworks detection (naive)
        content = ""
        if (project_path / "pyproject.toml").exists():
            content += (project_path / "pyproject.toml").read_text()
        if (project_path / "requirements.txt").exists():
            content += (project_path / "requirements.txt").read_text()

        if "fastapi" in content:
            tags.append("frameworks/fastapi")
        if "django" in content:
            tags.append("frameworks/django")

    # Node/JS
    if (project_path / "package.json").exists():
        content = (project_path / "package.json").read_text()
        if "typescript" in content:
            tags.append("languages/typescript")
        if "next" in content:
            tags.append("frameworks/nextjs")
        if "react" in content:
            tags.append("frameworks/react")
        if "tailwindcss" in content:
            tags.append("frameworks/tailwind")

    return tags

@app.command()
def compile(
    output: Path = Path(".cursorrules"),
    role: str = "developer",
    tags: Optional[List[str]] = None,
):
    """
    Compile a .cursorrules file from the rules library.
    """
    if tags is None:
        tags = detect_stack(Path.cwd())

    print(f"Detected tags: {tags}")

    content = []

    # 1. Role / Persona
    content.append(load_rule_block("roles", role))

    # 2. Core Rules (Always included)
    content.append(load_rule_block("core", "behavior"))
    content.append(load_rule_block("core", "tdd"))

    # 3. Stack Rules
    for tag in tags:
        category, name = tag.split("/")
        content.append(load_rule_block(category, name))

    # Write output
    final_output = "\n\n".join([c for c in content if c.strip()])
    output.write_text(final_output)
    print(f"Generated {output}")

if __name__ == "__main__":
    app()
