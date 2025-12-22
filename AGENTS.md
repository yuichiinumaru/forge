# AGENTS.md: The Forge Constitution

## 1. Mission
To provide a robust, Spec-Driven Development (SDD) CLI tool ("Forge") that empowers developers and AI agents to build high-quality software through rigorous specification, architecture, and testing.

## 2. Context
This repository contains the source code for the **Forge CLI** (formerly "Specify" / "Ai Max").
- **Language**: Python (CLI), Markdown (Templates).
- **Core Domain**: Scaffolding, Template Management, AI Agent Configuration.
- **Key Artifacts**:
  - `src/forge/`: The CLI source code.
  - `templates/`: The SDD templates and agent prompts distributed with the tool.

## 3. Governance & Laws

### The 10 Immutable Articles
1. **Library-First**: Every feature must begin as a standalone library/module.
2. **CLI Interface**: Every library must be usable via CLI/API.
3. **Test-First (TDD)**: No implementation without a failing test (Red -> Green -> Refactor).
4. **Simplicity**: Maximize leverage of existing framework features; avoid over-abstraction.
5. **Integration-First**: Prioritize realistic integration tests over extensive mocking.
6. **Documentation-Driven (RDD)**: Documentation (`docs/01-plans/01-plan.md`) is the source of truth, not the code.
7. **Domain Isolation (DDD)**: Respect domain boundaries defined in `docs/03-afs/03-architecture.md`.
8. **Task Atomicity**: Work on one task from `docs/02-tasks.md` at a time.
9. **Institutional Memory**: Log significant architectural decisions and mistakes in `docs/02-changelog.md`.
10. **Atomic UI**: All Frontend/Mobile implementations MUST follow the Atomic Design strictures defined in `templates/rules/patterns/atomic-design.md`. UI components must be decoupled to allow parallel agent execution.
11. **Naming Standards**: Enforce hierarchical naming (e.g., `Domain.Entity.State`) as defined in `templates/rules/patterns/naming-conventions.md`.
12. **Cycles Language**: Documentation must use "create, maintain, and update". New ideas must use "document, refine, and research". Implementation must use "following standards".

## 4. Methodology: FORGE v2
This project follows the **FORGE v2** methodology:

1. **RDD (Readme-Driven Development)**: We write `docs/01-plans/01-plan.md` and `docs/03-afs/03-architecture.md` before coding.
2. **DDD (Domain-Driven Design)**: We define folder structures and interfaces before implementation.
3. **TDD (Test-Driven Development)**: We write tests to validate specifications.
4. **CDD (Component-Driven Development)**: We build small, isolated, testable components (max 300 lines).

## 5. Development Loop
1. **Pick a Task**: Select the highest priority unchecked task from `docs/02-tasks.md`.
2. **Context**: Read `docs/01-plans/01-plan.md` and `docs/03-afs/03-architecture.md`.
3. **Test**: Write a failing test for the task.
4. **Implement**: Write minimal code to pass the test.
5. **Refactor**: Clean up.
6. **Log**: Update `docs/02-changelog.md` with what changed and why.
7. **Mark Complete**: Check [x] in `docs/02-tasks.md`.

## 6. Documentation Structure & Standards

### Organization
- `docs/00-archive/`: Deprecated or superseded files.
- `docs/01-plans/`: Strategic vision and roadmaps.
- `docs/02-tasks/`: Actionable task lists.
- `docs/03-afs/`: Architecture, Features, and Specs.
- `docs/04-rules/`: Governance and standards.
- `docs/05-ideas/`: Research and brainstorming.
- `docs/06-analysis/`: Audits and compatibility checks.
- `docs/07-guides/`: User and Developer guides.
- `docs/08-libs/`: Library documentation.
- `docs/name.md`: Synthesizes content of `docs/name/`.

### VITAL ASSET PRESERVATION
- **NEVER DELETE documentation info.** Always integrate new info. Only correct if data is objectively WRONG.
- **SEPARATE CONCERNS**:
  - `01-plan.md` = Why & How (Strategy, design, reasoning).
  - `02-tasks.md` = What & When (Granular implementation steps).
- **GRANULARITY**: Write tasks as detailed as possible. Use subtasks and sub-subtasks.
  - **NO DETAIL LEFT BEHIND**: Every technical detail counts. Use multi-step edits if necessary.
  - **HIERARCHICAL SCALING**: If a document exceeds 800 lines, create a subdirectory (e.g., `docs/01-plans/`) and move details there, keeping a synthetic version in the main file.
- **ARCHIVE FIRST**: Never delete files. Move them to `docs/00-archive/` before refactoring.
- **EXTRACTION PROTOCOL**: Archive first, then extract information to new files.

### Workflow Rules
1. **Context First**: When beginning a new session, read **every file** listed in `docs/tree.md` (if avail) to understand project goals, rules, and status.
2. **Think & Annotate**: Write down thoughts in `docs/thoughts/` (if enabled) to track progress. Read existing thoughts to prevent regression.
3. **Update Constitution**: Always update `AGENTS.md` with new rules as you progress. Never remove rules, only integrate/refine.
4. **Log Changes**: Always update `docs/02-changelog.md`. Write WHAT, WHY, and HOW. Focus on preventing repeated mistakes.
5. **Update Tasks**: Always update `docs/02-tasks.md`. Add new tasks to the top. Move completed phases to `docs/02-tasks/tasklist-completed.md`.

## 7. Documentation & Task Governance

### Size Limits & Synthesis
- **General Docs**: `docs/xx-type.md` must not exceed **150 lines**. It must synthesize contents of `docs/xx-type/*`.
- **Tasks File**: `docs/02-tasks.md` (or active list) must not exceed **200 lines**.
  - If > 200 lines: Synthesize macro tasks/phases into simplified items and link to subdocs in `docs/02-tasks/`.
  - **Never Empty**: Must always list all open tasks (or links to them).

### Task Lifecycle
- **Never Delete**: Completed tasks are moved to `docs/02-tasks/tasklist-completed.md`.
- **Harvesting**: When researching, create new `docs/01-plans/` and `docs/02-tasks/` files.
- **1:1 Pairing**: Every `docs/01-plans/x.md` must have a corresponding `docs/02-tasks/x.md`.

### Recursive Constitution
- **Locations**: An `AGENTS.md` file must exist in:
  - `docs/AGENTS.md`: Explaining documentation organization.
  - Major codebase folders (e.g., `src/forge/AGENTS.md`): Explaining code functioning.
- **Update Rule**: The root `AGENTS.md` is the master. Updates here trigger updates to sub-AGENTS.md files.
- **Symmetry**: Rules applying to FORGE apply to generated projects.
