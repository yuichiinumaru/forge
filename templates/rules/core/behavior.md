# Core Behavior Rules

- **Be Concise**: Do not offer extensive explanations unless asked. Focus on code.
- **Atomic Changes**: Keep changes small and isolated.
- **No Hallucinations**: Do not import libraries that are not installed. Check `pyproject.toml` or `package.json` first.
- **Preserve Context**: Do not remove comments or code unless explicitly instructed or if it's dead code.
- **Reasoning**: When solving complex problems, use "Chain of Thought" reasoning before outputting the solution.
