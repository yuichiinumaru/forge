# Parallel Development Plan

This document outlines how development can be parallelized across different modules.

## Module 1: Core CLI Refactoring
**Owner**: CLI Engineer
**Scope**: `src/forge/` (formerly `src/specify_cli/`)
**Tasks**:
- [ ] Rename package from `specify_cli` to `forge`.
- [ ] Modularize `__init__.py` into `cli.py`, `config.py`, `utils.py`.
- [ ] Implement `forge init --local` to use local `templates/` folder.
- [ ] Add unit tests for argument parsing and tool checks.

**Conflict Warning**: Changes to `AGENT_CONFIG` in `config.py` may conflict with Module 2 if new agents are added simultaneously.

## Module 2: Templates & Agent Integration
**Owner**: Prompt Engineer / Agent Specialist
**Scope**: `templates/`, `.github/workflows/scripts/`
**Tasks**:
- [ ] Update all markdown templates to use "Forge" terminology.
- [ ] Verify slash commands in `templates/commands/`.
- [ ] Update shell scripts (`scripts/bash/`, `scripts/powershell/`) to reflect new paths/names.

**Conflict Warning**: Modifying `templates/commands/` is safe, but changing the shell scripts used by the CLI (which are inside the templates or `scripts/` folder) requires coordination with Module 1.

## Module 3: Documentation & Governance
**Owner**: Technical Writer
**Scope**: `docs/`, `memory/`
**Tasks**:
- [ ] Maintain `docs/` up to date with code changes.
- [ ] Refine `constitution.md` and other governance artifacts.

## Module 4: Release Engineering
**Owner**: DevOps Engineer
**Scope**: `.github/workflows/`, `pyproject.toml`
**Tasks**:
- [ ] Update `pyproject.toml` with new package name and entry point.
- [ ] Update GitHub Actions to build "Forge" packages.
- [ ] Ensure release assets (ZIPs) are generated correctly from `templates/`.

**Integration Point**: All modules converge at `pyproject.toml` and the release workflow.
