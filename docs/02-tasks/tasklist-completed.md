# Completed Tasks Archive

## Phase 1: Consolidation & Branding
- [x] Rename package from `specify_cli` to `forge`.
- [x] Modularize `src/forge/__init__.py`.
- [x] Implement `forge rules` compiler.
- [x] Implement `forge plan`, `tasks`, `implement` commands (Spec-Flow integration).
- [x] Create `AGENTS.md` and `docs/06-rules.md`.
- [x] Refactor documentation to FORGE v2 structure.
- [x] Update GitHub Actions workflows.

## Phase 2: Technical Debt & Stability

### Operation "Slice the Monolith" (CDD Compliance)
*Goal: Reduce file sizes to <300 lines.*
- [x] **Task 2.1.1**: Refactor `src/forge/utils.py`. Split into `logging.py`, `filesystem.py`, `shell.py`.
- [x] **Task 2.1.2**: Refactor `src/forge/downloader.py`. Create `services/fetcher.py`.
- [x] **Task 2.1.3**: Refactor `src/forge/commands/init.py`. Extract `Scaffolder` class to `services/scaffolder.py`.

### Operation "Safety Net" (TDD Compliance)
*Goal: Achieve >80% test coverage on core logic.*
- [x] **Task 2.2.1**: specific test suite for `src/forge/state.py` (verify persistence, corruption handling).
- [x] **Task 2.2.2**: specific test suite for `src/forge/rules.py` (verify tag detection, compilation).
- [x] **Task 2.2.3**: specific test suite for `src/forge/commands/workflow.py` (verify command flow, template loading).
- [x] **Task 2.2.4**: specific test suite for `src/forge/utils.py` (after refactor).

### Operation "Local First" (DX)
- [x] **Task 2.3.1**: Debug `forge init --local`. Identify path mismatch between repo structure and deployed structure.
- [x] **Task 2.3.2**: Implement fix for `forge init --local` to allow self-hosted development.
- [x] **Task 2.3.3**: Add integration test for `--local` flag.

## Phase 2.5: Governance & Standardization
*Focus: Enforcing Atomic Design and Naming Conventions.*
- [x] **Task 2.5.1**: Create `templates/rules/patterns/naming-conventions.md`.
- [x] **Task 2.5.2**: Update `templates/rules/patterns/atomic-design.md` & create `templates/docs/ui-screen.md`.
- [x] **Task 2.5.3**: Create `templates/docs/user-guide.md` & `templates/docs/dev-guide.md`.
- [x] **Task 2.5.4**: Update `src/forge/rules.py` & `AGENTS.md` to enforce new rules.
- [x] **Task 2.5.5**: Document Forge's CLI Design System in `docs/design-system.md`.

## Phase 3: Content & Compatibility Expansion

### Language Support
- [x] **Task 3.1.1**: Create `templates/rules/languages/java.md`.
- [x] **Task 3.1.2**: Create `templates/rules/languages/go.md`.
- [x] **Task 3.1.3**: Create `templates/rules/languages/rust.md`.
- [x] **Task 3.1.4**: Update `src/forge/rules.py` detection logic for new languages.

### CI/CD
- [x] **Task 3.2.1**: Add `windows-latest` runner to GitHub Actions.
- [x] **Task 3.2.2**: Add `macos-latest` runner to GitHub Actions.
- [x] **Task 3.2.3**: Create matrix testing for Python versions (3.10, 3.11, 3.12).

### Agent Templates
- [x] **Task 3.3.1**: Create/Update templates for Qwen Code.
- [x] **Task 3.3.2**: Create/Update templates for Amazon Q.

### Waterfall Gates
- [x] **Task 3.4.1**: Implement `optimize` command quality gates (auto-run tests/linters).
- [x] **Task 3.4.2**: Verify gates pass before marking as optimized.
