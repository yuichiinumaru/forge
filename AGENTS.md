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
6. **Documentation-Driven (RDD)**: Documentation (`docs/01-plan.md`) is the source of truth, not the code.
7. **Domain Isolation (DDD)**: Respect domain boundaries defined in `docs/03-architecture.md`.
8. **Task Atomicity**: Work on one task from `docs/02-tasks.md` at a time.
9. **Institutional Memory**: Log significant architectural decisions and mistakes in `docs/04-changelog.md`.
10. **Atomic UI**: All Frontend/Mobile implementations MUST follow the Atomic Design strictures defined in `templates/rules/patterns/atomic-design.md`. UI components must be decoupled to allow parallel agent execution.
11. **Naming Standards**: Enforce hierarchical naming (e.g., `Domain.Entity.State`) as defined in `templates/rules/patterns/naming-conventions.md`.
12. **Cycles Language**: Documentation must use "create, maintain, and update". New ideas must use "document, refine, and research". Implementation must use "following standards".

## 4. Methodology: FORGE v2
This project follows the **FORGE v2** methodology:

1. **RDD (Readme-Driven Development)**: We write `docs/01-plan.md` and `docs/03-architecture.md` before coding.
2. **DDD (Domain-Driven Design)**: We define folder structures and interfaces before implementation.
3. **TDD (Test-Driven Development)**: We write tests to validate specifications.
4. **CDD (Component-Driven Development)**: We build small, isolated, testable components (max 300 lines).

## 5. Development Loop
1. **Pick a Task**: Select the highest priority unchecked task from `docs/02-tasks.md`.
2. **Context**: Read `docs/01-plan.md` and `docs/03-architecture.md`.
3. **Test**: Write a failing test for the task.
4. **Implement**: Write minimal code to pass the test.
5. **Refactor**: Clean up.
6. **Log**: Update `docs/04-changelog.md` with what changed and why.
7. **Mark Complete**: Check [x] in `docs/02-tasks.md`.
