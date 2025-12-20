# 06 Rules: The Law

**Status**: Versioned
**Purpose**: Coding standards, patterns, and "The 9 Articles".

## 1. The 12 Immutable Articles (from Constitution)

1. **Library-First**: Every feature must begin as a standalone library/module.
2. **CLI Interface**: Every library must be usable via CLI/API.
3. **Test-First (TDD)**: No implementation without a failing test (Red -> Green -> Refactor).
4. **Simplicity**: Maximize leverage of existing framework features; avoid over-abstraction.
5. **Integration-First**: Prioritize realistic integration tests over extensive mocking.
6. **Documentation-Driven (RDD)**: Documentation (`docs/01-plan.md`) is the source of truth, not the code.
7. **Domain Isolation (DDD)**: Respect domain boundaries defined in `docs/03-architecture.md`.
8. **Task Atomicity**: Work on one task from `docs/02-tasks.md` at a time.
9. **Institutional Memory**: Log significant architectural decisions and mistakes in `docs/04-changelog.md`.
10. **Atomic UI**: All Frontend/Mobile implementations MUST follow Atomic Design strictures.
11. **Naming Standards**: Enforce hierarchical naming (e.g., `Domain.Entity.State`).
12. **Cycles Language**: Strict vocabulary for documentation ("create, maintain, and update") and ideas ("document, refine, and research").

## 2. Coding Standards

### Python (`src/forge`)
- **Framework**: `typer` for CLI, `rich` for output.
- **Type Hinting**: Mandatory for all function signatures.
- **Docstrings**: Google Style.
- **Formatter**: Black / Ruff.
- **Imports**: Absolute imports preferred (e.g., `from forge.utils import ...`).

### Markdown (`docs/` & `templates/`)
- **Headers**: ATX style (`# Header`).
- **Lists**: Hyphens (`- item`).
- **Slash Commands**: Must follow `/forge.<command>` format (e.g., `/forge.plan`).

### Scripts (`scripts/`)
- **Bash**: `set -e` (exit on error) required.
- **PowerShell**: `$ErrorActionPreference = "Stop"` required.

## 3. Workflow Rules
- **Verify**: Always run `ls`, `grep`, or `read_file` after modification.
- **No Blind Debugging**: If a test fails, revert to the last known good state if the fix isn't obvious.
- **Pre-Commit**: Always run pre-commit checks before submitting.
