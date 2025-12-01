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
│       ├── __init__.py       # Entry Point
│       ├── cli.py            # Typer CLI definition
│       ├── config.py         # Configuration & Constants
│       ├── downloader.py     # Template acquisition
│       └── utils.py          # Helper functions
├── templates/                # SDD Templates & Agent Prompts (Domain: Content)
│   ├── commands/             # Slash command templates (e.g., forge.plan.md)
│   ├── rules/                # Rule templates for .cursorrules
│   └── ...                   # Other templates
├── docs/                     # Documentation (Domain: Knowledge)
│   ├── 00-draft.md
│   ├── ...
│   └── 07-errors.md
├── scripts/                  # Helper scripts (Bash/PowerShell)
└── tests/                    # Tests
```

## 2. Domains & Boundaries

### Domain 1: The CLI (`src/forge`)
- **Responsibility**: Orchestration, file I/O, and scaffolding. The "muscle" of the operation.
- **Boundaries**:
  - **Must** not contain business logic for the SDD methodology itself (that belongs in Templates).
  - **Must** be agent-agnostic.
  - **Input**: User commands, `templates/`.
  - **Output**: File generation in the user's project (`.forge/` and project files).

### Domain 2: The Content (`templates/` & `scripts/`)
- **Responsibility**: The "brain" of the operation. Contains the SDD methodology, prompts, and agent instructions.
- **Boundaries**:
  - **Must** be decoupled from the CLI implementation details where possible.
  - **Must** support multiple agent contexts (via variable substitution).
  - **Structure**:
    - `commands/`: Markdown files defining slash commands (e.g., `/forge.plan`).
    - `rules/`: Reusable logic blocks for AI agents.

### Domain 3: The Knowledge (`docs/`)
- **Responsibility**: Meta-documentation for FORGE developers and context for AI agents working on FORGE itself.
- **Boundaries**:
  - **Source of Truth**: `docs/01-plan.md` and `docs/03-architecture.md` dictate code, not vice versa.

## 3. Runtime Architecture (Target Project)

When FORGE runs in a user's project, it establishes this structure:

```text
UserProject/
├── .cursorrules              # Compiled from templates/rules
├── .forge/                   # The runtime "brain"
│   ├── templates/            # Copied from repo templates/
│   ├── scripts/              # Copied from repo scripts/
│   └── memory/               # Context files (e.g., constitution.md)
├── docs/                     # SDD Artifacts
│   ├── 01-plan.md
│   └── ...
└── ...
```

- **.forge/ Directory**: The exclusive domain of the FORGE tool. Users should not manually edit files here unless they are customizing the methodology.
