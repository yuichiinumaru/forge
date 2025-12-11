import re
from pathlib import Path
from typing import List, Optional

def strip_frontmatter(content: str) -> str:
    """Remove YAML frontmatter from content."""
    # Match start of file --- ... ---
    # DOTALL to match newlines
    if content.startswith("---"):
        pattern = r'^---\s*\n.*?\n---\s*\n'
        return re.sub(pattern, '', content, flags=re.DOTALL)
    return content

def find_file_in_paths(filename: str, search_paths: List[Path]) -> Optional[Path]:
    """Find a file (with .md extension if missing) in search paths."""
    name = filename if filename.endswith(".md") else f"{filename}.md"

    for path in search_paths:
        candidate = path / name
        if candidate.exists():
            return candidate
    return None

def process_template(content: str, search_paths: List[Path], depth: int = 0, max_depth: int = 10) -> str:
    """
    Process markdown template:
    1. Resolve transclusions ![[...]] recursively.
    2. Resolve wikilinks [[...]] to paths.
    """
    if depth > max_depth:
        return content + "\n<!-- Error: Recursion depth exceeded -->"

    # 1. Resolve Transclusions ![[filename]]
    def replace_transclusion(match):
        ref = match.group(1).strip()
        found_path = find_file_in_paths(ref, search_paths)
        if found_path:
            file_content = found_path.read_text(encoding="utf-8")
            # Strip frontmatter from the INCLUDED file
            stripped_content = strip_frontmatter(file_content)
            # Recursively process the included content
            return process_template(stripped_content, search_paths, depth + 1, max_depth)
        else:
            return f"<!-- Error: Transclusion not found: {ref} -->"

    # Regex for ![[...]]
    # Non-greedy match for content inside brackets
    content = re.sub(r'!\[\[(.*?)\]\]', replace_transclusion, content)

    # 2. Resolve WikiLinks [[filename]]
    # Replace with @path/to/filename.md (relative to CWD or absolute? Claude Code likes relative)
    # We should probably resolve to a relative path from the project root if possible.
    def replace_wikilink(match):
        ref = match.group(1).strip()
        found_path = find_file_in_paths(ref, search_paths)
        if found_path:
            # Try to make relative to CWD
            try:
                rel_path = found_path.resolve().relative_to(Path.cwd().resolve())
                return f"@{rel_path}"
            except ValueError:
                return f"@{found_path}"
        else:
            return f"[[{ref}]]" # Keep original if not found

    # Regex for [[...]] but NOT ![[...]]
    # Using negative lookbehind (?<!!) is tricky if ! is separated by space, but usually it is ![[
    content = re.sub(r'(?<!\!)\[\[(.*?)\]\]', replace_wikilink, content)

    return content
