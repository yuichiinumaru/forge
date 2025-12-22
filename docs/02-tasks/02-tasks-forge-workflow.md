# 02 Tasks: Spec-Flow Harvesting

**Status**: Active
**Purpose**: Implementation tasks for integrating Spec-Flow capabilities into FORGE.

## Phase 1: Foundation (State & Agents)

- [ ] **Define State Model**
  - Create `src/forge/state.py`.
  - Define Pydantic model for `WorkflowState` (phase, feature_name, status, tasks_completed, etc.).
  - Implement `load_state()` and `save_state()` (target: `.forge/state.yaml`).
- [ ] **Refactor Templates**
  - Create `templates/agents/` directory.
  - Port `references/Spec-Flow/.claude/commands/phases/plan.md` to `templates/agents/plan.md`.
  - Port `references/Spec-Flow/.claude/commands/phases/tasks.md` to `templates/agents/tasks.md`.
  - Create `templates/agents/worker.md` (The implementation specialist).

## Phase 2: Workflow Commands

- [ ] **Implement `forge plan`**
  - Add `plan` command to `src/forge/cli.py`.
  - Logic: Check state -> Load `agent-plan.md` -> Prompt user/AI -> Save `docs/01-plan.md` -> Update state.
- [ ] **Implement `forge tasks`**
  - Add `tasks` command to `src/forge/cli.py`.
  - Logic: Read `01-plan.md` -> Load `agent-tasks.md` -> Generate `docs/02-tasks.md` -> Update state.
- [ ] **Implement `forge implement`**
  - Add `implement` command to `src/forge/cli.py`.
  - Logic: Parse `02-tasks.md` -> Find next task -> Load `worker.md` with task context -> (Simulate execution loop).
- [ ] **Implement `forge optimize`**
  - Add `optimize` command.
  - Implement `run_quality_gates()` function (wraps `pytest`, `ruff`, etc.).

## Phase 3: Integration

- [ ] **Update `forge init`**
  - Ensure `.forge/state.yaml` is initialized.
  - Ensure `templates/agents/` are copied to `.forge/templates/agents/`.
- [ ] **Update `forge rules`**
  - Update `.cursorrules` generation to reference the new state file and current phase.
- [ ] **Documentation**
  - Update `docs/03-architecture.md` to reflect the new "Stateful Workflow".
  - Create `docs/guides/workflow.md` explaining the `spec` -> `ship` cycle.

## Phase 4: Cleanup

- [ ] **Remove Legacy Templates**
  - Audit `templates/commands` and remove redundant files replaced by `templates/agents`.
