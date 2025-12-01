# 02 Tasks: The Execution Queue

**Status**: Live
**Purpose**: The "What" and "When". Granular, actionable tasks.
**Rules**: Work on ONE task at a time. Mark with [x] when done.

## Active Tasks (Incomplete)

### Priority 1: Core CLI Refactoring
- [ ] Add unit tests for argument parsing.

### Priority 2: Templates & Agent Integration
- [ ] Update all markdown templates in `templates/` to use "FORGE" terminology.
- [ ] Verify slash commands format (`/forge.*`).
- [ ] Update shell scripts (`scripts/`) to reflect new paths.

### Priority 3: Release Engineering
- [ ] Update GitHub Actions workflows for "Forge" branding.
- [ ] Verify release asset generation.

## Archive (Completed)

### Documentation & Governance
- [x] Create `AGENTS.md` (Constitution).
- [x] Refactor `docs/` to FORGE v2 structure.
- [x] Rewrite `README.md` in Protoss lexicon.
- [x] Update `docs/03-architecture.md` with domain boundaries.
- [x] Create `docs/06-rules.md`.

### Core CLI Refactoring
- [x] Rename package from `specify_cli` to `forge` in `pyproject.toml` and source.
- [x] Modularize `src/forge/__init__.py` into `cli.py`, `config.py`, `utils.py`.
- [x] Implement `forge init --local` to use local `templates/` folder (enables self-hosting dev).

### Templates & Agent Integration
- [x] Create `forge rules` module (Analysis & Implementation).
  - [x] Analyze external rule repos (`docs/00-analysis-rules-integration.md`).
  - [x] Create `templates/rules/` directory structure.
  - [x] Implement `src/forge/rules.py` compiler.
