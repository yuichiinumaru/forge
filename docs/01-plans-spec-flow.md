# 01 Plan: Spec-Flow Harvesting

**Status**: Versioned
**Purpose**: Integration plan for harvesting advanced workflow capabilities from `marcusgoll/Spec-Flow`.

## 1. Analysis of Spec-Flow

`Spec-Flow` is a mature "Workflow Toolkit" for Claude Code that implements a rigorous Spec-Driven Development (SDD) process.

### Key Concepts & Strengths

1.  **State Management (`state.yaml`)**:
    - Maintains the "Truth" of the current feature/epic workflow.
    - Tracks: Phase (`spec`, `plan`, `implement`), Status (`in_progress`, `blocked`), Artifact paths, and Quality Gate results.
    - **Benefit**: Makes the workflow resumable and context-aware. The tool knows "what to do next" without user prompting.

2.  **Phase Isolation (Distinct Agents)**:
    - Instead of one "God Mode" agent, it spawns specialized agents for each phase.
    - **Architecture**: `Task(agent_prompt)` pattern.
    - **Benefit**: Reduces context window pollution, ensures strict adherence to phase-specific rules (e.g., "Planner" cannot write code, only plans).

3.  **Imperative Task Architecture ("Workers")**:
    - The "Main" agent orchestrates "Worker" agents.
    - Workers are ephemeral: Pick ONE task -> Implement -> Test -> Update State -> Exit.
    - **Benefit**: Prevents "doom loops" where long sessions degrade performance. Ensures atomicity.

4.  **Quality Gates (`/optimize`)**:
    - Explicit phase for validation before shipping.
    - Checks: Linting, Unit Tests, Coverage, Security, Accessibility.
    - **Benefit**: Enforces quality standards programmatically.

5.  **Perpetual Learning (Memory)**:
    - Stores "Learnings" in `.spec-flow/memory/` and injects them into future sessions.
    - **Benefit**: The tool gets smarter over time, remembering specific project quirks.

6.  **Documentation Bootloader (`CLAUDE.md`)**:
    - A highly structured, progressive disclosure prompt that loads context on demand.
    - **Benefit**: Reduces initial token cost while keeping all rules accessible.

## 2. Gap Analysis: FORGE vs. Spec-Flow

| Feature | FORGE (Current) | Spec-Flow (Target) | Gap |
| :--- | :--- | :--- | :--- |
| **Workflow State** | Implicit (User remembers) | Explicit (`state.yaml`) | **High** |
| **Agent Architecture** | Monolithic (`.cursorrules`) | Isolated Agents (Phase-based) | **High** |
| **Context Management** | Static Templates | Dynamic Loading + Compaction | **Medium** |
| **Quality Control** | Manual Pre-commit | Automated Gates (`/optimize`) | **Medium** |
| **Learning** | None | `.spec-flow/memory` | **Low** |
| **Commands** | `init`, `rules` | `plan`, `tasks`, `implement`, `ship` | **High** |

## 3. Integration Plan

We will adopt the **State Management**, **Phase Isolation**, and **Workflow Commands** from Spec-Flow. We will implement them natively in Python within `src/forge`, avoiding the bash script dependency of Spec-Flow.

### Phase 1: The Foundation (State & Structure)

1.  **Implement `forge state`**:
    - Create `src/forge/models.py` to define `State` schema (Pydantic).
    - Create `src/forge/state.py` to manage `.forge/state.yaml`.
    - Track: `current_phase`, `active_feature`, `completed_steps`.

2.  **Implement "Agent Modes"**:
    - Refactor `templates/commands/` into `templates/agents/`.
    - Create distinct prompts for:
        - `agent-spec.md`
        - `agent-plan.md`
        - `agent-tasks.md`
        - `agent-implement.md` (The Worker)
        - `agent-optimize.md`

### Phase 2: The Workflow Commands

1.  **`forge plan`**:
    - Initializes feature state.
    - Loads `agent-plan.md`.
    - Generates `docs/01-plan.md`.

2.  **`forge tasks`**:
    - Reads `docs/01-plan.md`.
    - Loads `agent-tasks.md`.
    - Generates `docs/02-tasks.md`.

3.  **`forge implement` (The Orchestrator)**:
    - Reads `docs/02-tasks.md`.
    - **Loop**:
        - Pick next unchecked task.
        - Spawn "Worker" (simulated via new context or `Task()` if supported, otherwise just context switching).
        - Run Test -> Code -> Refactor.
        - Mark task complete in `docs/02-tasks.md`.
        - Update `state.yaml`.

4.  **`forge optimize`**:
    - Runs configured checks (lint, test).
    - Updates `docs/08-audit-report.md`.

### Phase 3: The Bootloader

1.  **Enhanced `CLAUDE.md` / `.cursorrules`**:
    - Update `forge rules compile` to generate a Spec-Flow style bootloader.
    - Use "Progressive Disclosure": Link to reference docs instead of dumping everything.

## 4. Modules/Components to Copy

1.  **`state.yaml` Schema**: Copy the structure (Phase, Status, Gates).
2.  **Agent Prompts**: Adapt `references/Spec-Flow/.claude/commands/phases/*.md` into `templates/agents/`.
3.  **Quality Gate Logic**: Adapt `references/Spec-Flow/.spec-flow/scripts/bash/gate-check.sh` logic into Python (using `subprocess` or native libs).
4.  **Memory Structure**: Adopt the `.forge/memory` folder convention.

## 5. Architectural Changes

### New Directory: `src/forge/workflow/`
Will contain the logic for the phases:
- `manager.py`: Main orchestrator.
- `state.py`: State persistence.
- `gates.py`: Quality checks.

### New Templates
- `templates/agents/spec.md`
- `templates/agents/plan.md`
- `templates/agents/worker.md`
- `templates/agents/optimize.md`

## 6. Implementation Principles
- **Python-First**: Do not copy Bash/Powershell scripts directly. Re-implement logic in Python.
- **Typer CLI**: Expose all phases as `forge <phase>` commands.
- **Backwards Compatibility**: Ensure `forge init` still works for basic setups.
