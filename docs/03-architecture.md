# 03 Architecture: The Landscape

**Status**: Versioned
**Purpose**: The "Where". Folder structure, domain boundaries, and system design.

## 1. Directory Structure

```text
.
├── AGENTS.md                 # The Constitution
├── README.md                 # Public Entry Point
├── pyproject.toml            # Python Project Config
├── src/
│   └── forge/                # Core CLI Logic (Domain: Scaffolding)
│       ├── __init__.py       # Entry Point (To be refactored)
│       └── ...
├── templates/                # SDD Templates & Agent Prompts (Domain: Content)
│   ├── commands/             # Slash command templates (e.g., plan.md)
│   ├── structure/            # Project structure templates
│   └── [agent_dirs]/         # Agent-specific configs (e.g., .cursor/)
├── docs/                     # Documentation (Domain: Knowledge)
│   ├── 00-draft.md
│   ├── ...
│   └── 07-errors.md
├── scripts/                  # Helper scripts (Bash/PowerShell)
└── tests/                    # Tests
```

## 2. Domains

### CLI Domain (`src/forge`)
- **Responsibility**: User interaction, file downloading, project scaffolding.
- **Boundaries**: Should not contain template content directly (should read from `templates/` or remote).

### Content Domain (`templates/`)
- **Responsibility**: The actual intelligence/prompts provided to the user.
- **Boundaries**: agnostic of the CLI tool where possible.

### Knowledge Domain (`docs/`)
- **Responsibility**: Meta-documentation for the project developers (Context for AI Agents).
