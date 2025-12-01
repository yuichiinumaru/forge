# 04 Changelog: Institutional Memory

**Status**: Append-Only
**Purpose**: Record what changed, WHY, and what we learned.

## Template
```markdown
### [YYYY-MM-DD] Title of Change
- **What**: Brief description of code changes.
- **Why**: The business or technical reason.
- **Mistake/Learning**: (Optional) What went wrong that we should avoid next time?
```

## Log

### 2024-05-22 Documentation Refactor
- **What**: Migrated documentation to FORGE v2 structure (`00-07` files). Created `AGENTS.md`.
- **Why**: To align the project with the new methodology and ensure AI Agents have precise context.
- **Learning**: The previous docs were fragmented; strict ordering helps agents ingest context sequentially.

### 2024-05-23 Core Refactor & Cleanup
- **What**: Finalized modularization of `src/forge/__init__.py`, cleaned up `src/forge/cli.py`, integrated `rules` module, and implemented `forge init --local`. Updated `docs/02-tasks.md`.
- **Why**: To complete the Priority 1 & 2 tasks and fix the broken CLI entry point.
- **Learning**: The "fat" `__init__.py` was a blocker for testing new features like `--local`. Separating concerns allowed for easier verification.

### 2024-05-23 Test Suite Expansion
- **What**: Added comprehensive unit tests for CLI argument parsing in `tests/test_cli.py`.
- **Why**: To validate `forge init` argument handling (valid/invalid AI, scripts, existing directories).
- **Learning**: Used `pytest-mock` to handle external dependencies in tests, ensuring isolation.
