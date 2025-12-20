# Core Behavior Rules

- **Be Concise**: Do not offer extensive explanations unless asked. Focus on code.
- **Atomic Changes**: Keep changes small and isolated.
- **No Hallucinations**: Do not import libraries that are not installed. Check `pyproject.toml` or `package.json` first.
- **Preserve Context**: Do not remove comments or code unless explicitly instructed or if it's dead code.
- **Reasoning**: When solving complex problems, use "Chain of Thought" reasoning before outputting the solution.

## Cycles Design Rules
- **Documentation**: When creating documentation, you must always "create, maintain, and update".
- **New Ideas**: When dealing with new ideas, you must "document, refine, and research".
- **Implementation**: When implementing new features, you must always do so "following the project's standards and conventions".
