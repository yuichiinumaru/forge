# 01 Plan: Pew Pew Workspace Harvesting

**Status**: Versioned
**Purpose**: Integration plan for harvesting modular prompting and sync capabilities from `pew-pew-prompts/pew-pew-workspace`.

## 1. Analysis of Pew Pew Workspace

`pew-pew-workspace` is an "AI-powered project management framework" that focuses on modular prompt engineering and "Most Valuable Project Management" (MVPM).

### Key Concepts & Strengths

1.  **Modular Prompting**:
    - Deconstructs prompts into atomic components: `Persona`, `Request`, `Workflow`, `Instructions`, `Output Format`.
    - Stores these components in dedicated directories (`blocks/`, `personas/`, `instructions/`).
    - **Benefit**: Reusability, consistency, and easy maintenance.

2.  **WikiLink compilation (`sync` system)**:
    - Uses a Bash-based build system to "compile" markdown files.
    - **Transclusion**: `![[block-name]]` embeds the content of `block-name.md` inline.
    - **Referencing**: `[[doc-name]]` resolves to the file path (e.g., `@path/to/doc.md`) for AI context loading.
    - **Frontmatter Stripping**: Removes metadata from included blocks to keep the final prompt clean.
    - **Benefit**: Allows composing complex agents/commands from simple, shared blocks.

3.  **MVPM (Most Valuable Project Management)**:
    - A structured approach to organizing tasks/issues: `concept/milestone/step`.
    - **Benefit**: Scalable organization for complex projects.

4.  **Team/Phase Structure**:
    - Organizes work by "Teams" (Discovery, Requirements, Plan, Act, Review).
    - **Benefit**: Clear separation of concerns in the development lifecycle.

## 2. Gap Analysis: FORGE vs. Pew Pew

| Feature | FORGE (Current) | Pew Pew (Target) | Gap |
| :--- | :--- | :--- | :--- |
| **Prompt Composition** | Monolithic Markdown | Modular Blocks (`![[embed]]`) | **High** |
| **Template Engine** | Simple variable sub | Recursive Markdown Compilation | **High** |
| **Organization** | `templates/agents` | `templates/personas`, `blocks`, etc. | **Medium** |
| **Context Loading** | Manual or static | Dynamic via resolved paths | **Medium** |
| **Task Structure** | Flat `tasks.md` | Hierarchical MVPM | **Low** (Methodology choice) |

## 3. Integration Plan

We will adopt the **Modular Prompting** and **Markdown Compilation** (WikiLink resolution) system. We will implement the compiler in Python to avoid Bash dependencies.

### Phase 1: The Template Compiler

1.  **Implement `forge.compiler` module**:
    - `resolve_wikilinks(content, search_paths)`: Replaces `[[link]]` with paths.
    - `resolve_embeds(content, search_paths)`: Replaces `![[embed]]` with content (recursively).
    - `strip_frontmatter(content)`: Cleans up included content.
    - **Search Paths**: `templates/blocks`, `templates/personas`, `templates/instructions`, etc.

2.  **Update `load_agent_template`**:
    - In `src/forge/commands/workflow.py`, use the compiler to process the template before returning it.
    - This enables `templates/agents/plan.md` to use `![[planning-rules]]`.

### Phase 2: Modular Assets

1.  **Restructure `templates/`**:
    - Create `templates/blocks/` (reusable snippets).
    - Create `templates/personas/` (role definitions).
    - Create `templates/instructions/` (rules/conventions).
    - Create `templates/workflows/` (process definitions).

2.  **Refactor Existing Agents**:
    - Break down `plan.md`, `tasks.md`, `implement.md` into reusable blocks.
    - Example: Extract "Anti-Hallucination Rules" into `templates/instructions/anti-hallucination.md`.

### Phase 3: The Sync Command (Optional/Future)

- `forge template sync`: Compiles all templates to a build directory (e.g., `.forge/compiled/`) for inspection or usage by other tools (like Claude Code CLI directly).

## 4. Modules/Components to Copy

1.  **Compiler Logic**: Adapt the logic from `sync-claude-code-embedded-wikilinks.sh` (regex for `![[...] ]`) into Python.
2.  **Block Library**: Copy useful blocks from `pew-pew-workspace/blocks/` (e.g., standard coding rules, git conventions) if license permits (MIT).
3.  **Structure**: Adopt the folder structure for templates.

## 5. Architectural Changes

### New Directory: `src/forge/compiler/`
- `markdown.py`: The compilation logic.

### New Templates Structure
```text
templates/
├── agents/         # Top-level personas (entry points)
├── blocks/         # Reusable content
├── instructions/   # Rule sets
└── ...
```

## 6. Implementation Principles
- **Python-First**: Re-implement bash logic in Python.
- **On-Demand**: Compile templates when requested by `forge plan` etc., rather than requiring a separate sync step (though caching is an option).
- **Backward Compatible**: Standard markdown should still work.
