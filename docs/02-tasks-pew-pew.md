# 02 Tasks: Pew Pew Harvesting

**Status**: Active
**Purpose**: Implementation tasks for integrating modular prompting and markdown compilation.

## Phase 1: Compiler Engine

- [ ] **Create `src/forge/compiler/`**
  - Implement `markdown.py`.
  - Function `process_template(content: str, search_paths: List[Path]) -> str`.
  - Implement recursive embedding (`![[...]]`).
  - Implement path resolution (`[[...]]`).
  - Implement frontmatter stripping.
- [ ] **Unit Tests**
  - Create `tests/test_compiler.py`.
  - Test circular dependencies detection.
  - Test depth limits.
  - Test path resolution priority.

## Phase 2: Integration

- [ ] **Update `src/forge/commands/workflow.py`**
  - Modify `load_agent_template` to use `process_template`.
  - Define default search paths (`templates/blocks`, `templates/instructions`, etc.).
- [ ] **Update `src/forge/rules.py`**
  - Allow `.cursorrules` generation to also support `![[...]]` embeds (unifying the logic).

## Phase 3: Content Refactoring

- [ ] **Create Folder Structure**
  - `templates/blocks/`
  - `templates/instructions/`
  - `templates/personas/`
- [ ] **Migrate Content**
  - Extract common sections from `templates/agents/*.md` into blocks.
  - Example: `templates/instructions/anti-hallucination.md`.
  - Update `templates/agents/plan.md` to use `![[anti-hallucination]]`.

## Phase 4: Harvest Reference Blocks

- [ ] **Select Blocks**
  - Identify high-value blocks from `references/pew-pew-workspace/blocks/` (e.g., generic coding standards).
  - Port them to `templates/blocks/`.
