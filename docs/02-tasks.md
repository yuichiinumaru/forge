# 02 Tasks: The Execution Queue

**Status**: Live
**Purpose**: The "What" and "When". Granular, actionable tasks.
**Rules**: Work on ONE task at a time. Mark with [x] when done.

## Priority 0: Documentation & Governance (Current)
- [x] Create `AGENTS.md` (Constitution).
- [x] Refactor `docs/` to FORGE v2 structure.
- [ ] Rewrite `README.md` in Protoss lexicon.
- [ ] Update `docs/03-architecture.md` with domain boundaries.
- [ ] Create `docs/06-rules.md`.

## Priority 1: Core CLI Refactoring
- [x] Rename package from `specify_cli` to `forge` in `pyproject.toml` and source.
- [x] Modularize `src/forge/__init__.py` into `cli.py`, `config.py`, `utils.py`.
- [ ] Implement `forge init --local` to use local `templates/` folder (enables self-hosting dev).
- [ ] Add unit tests for argument parsing.

## Priority 2: Templates & Agent Integration
- [x] Create `forge rules` module (Analysis & Implementation).
  - [x] Analyze external rule repos (`docs/00-analysis-rules-integration.md`).
  - [x] Create `templates/rules/` directory structure.
  - [x] Implement `src/forge/rules.py` compiler.
- [ ] Update all markdown templates in `templates/` to use "FORGE" terminology.
- [ ] Verify slash commands format (`/forge.*`).
- [ ] Update shell scripts (`scripts/`) to reflect new paths.

## Priority 3: Release Engineering
- [ ] Update GitHub Actions workflows for "Forge" branding.
- [ ] Verify release asset generation.

## Archive (Completed)
*(None yet)*
