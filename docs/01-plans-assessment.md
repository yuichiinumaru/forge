# Assessment of FORGE (formerly Ai Max / Spec Kit)

## 1. Project Overview & Status

**Current State**:
The project, currently transitioning to the name **FORGE**, is a CLI tool (`specify`) designed to bootstrap Spec-Driven Development (SDD) projects. It functions primarily as a scaffolder that downloads agent-specific templates from a remote repository (`yuichiinumaru/aimax-kit`) and initializes a project environment.

**Code vs. Documentation Discrepancies**:
- **Naming**: Documentation largely refers to "Spec Kit" and "Specify". The codebase (`src/specify_cli/__init__.py`) refers to itself as "IA MAX Kit" and "aimax-kit".
- **Commands**:
  - Documentation focuses on `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`.
  - The codebase (via `templates/commands` and `__init__.py` logic) and `AGENTS.md` imply a broader set of commands including `/aimaxkit.constitution`, `/aimaxkit.implement`, `/aimaxkit.clarify`, `/aimaxkit.analyze`, and `/aimaxkit.checklist`.
- **Templates**:
  - The repository contains a `templates/` directory with seemingly up-to-date command definitions (`constitution.md`, `implement.md`, etc.).
  - **Critical Finding**: The CLI tool (`specify init`) **does not use these local templates**. Instead, it downloads a ZIP file from a GitHub release (`yuichiinumaru/aimax-kit`). This creates a disconnect where local changes to `templates/` are not reflected in the CLI's behavior unless a new release is pushed to the remote repo.

## 2. Implementation vs. Documentation

| Feature | Documentation Status | Implementation Status | Notes |
| :--- | :--- | :--- | :--- |
| **CLI Initialization** | Documented (`specify init`) | Implemented | CLI correctly handles project creation, git init, and tool checks. |
| **Agent Support** | Partially Documented | Implemented (Extensive) | Code supports many more agents (Qwen, OpenCode, Codex, Windsurf, etc.) than listed in main docs. |
| **Local Development** | Documented | Partially Implemented | `local-development.md` suggests using `uvx --from .`, but this only runs the *CLI code*, not the *local templates*. |
| **SDD Workflow** | Documented (4 steps) | Implemented (via Templates) | The core value (SDD) is delivered via the downloaded templates, not the Python CLI itself. |
| **Scripts** | Documented (sh/ps) | Implemented | CLI selects correct script type. |

## 3. Missing Features & Details

1.  **Local Template Usage**: There is no flag (e.g., `--local-templates`) to initialize a project using the `templates/` directory in the repo. This hinders development of the templates themselves.
2.  **Configuration**: The project relies on hardcoded `AGENT_CONFIG` in `__init__.py`. External configuration would be better.
3.  **Offline Mode**: The `init` command requires internet access to fetch templates.
4.  **Test Coverage**: No visible Python tests for the CLI logic itself (only `memory` and `templates` exist as assets).

## 4. Architectural Improvements

1.  **Modularization**:
    - Split `src/specify_cli/__init__.py` (currently ~700 lines) into modules: `cli.py`, `config.py`, `downloader.py`, `utils.py`.
2.  **Template Management**:
    - Implement a mechanism to bundle templates with the package or allow a local override path. This aligns the repository content with the tool's behavior.
3.  **Renaming & Branding**:
    - Consistently rename "Ai Max" / "IA MAX" to "FORGE".
    - Update the download target in the CLI (if a "Forge" repo is established) or maintain the link but update the display text.
4.  **Testing Strategy**:
    - Add unit tests for the CLI logic (argument parsing, tool checking).
    - Add integration tests that verify template generation using the local `templates/` folder.

## 5. Next Steps

- Refactor documentation to reflect the "Forge" branding and the complete command set.
- Rename the project artifacts.
- Plan for parallel execution of modularization and template decoupling.
