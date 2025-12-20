# 00 Analysis: Automated Project Rules Module

**Status**: Draft / Analysis
**Date**: 2024-05-22
**Purpose**: Analysis of external rule repositories and implementation plan for the `forge rules` module.

## 1. Executive Summary
We propose a new module, `forge rules`, designed to automatically generate AI behavior configurations (e.g., `.cursorrules`, `.windsurfrules`) based on the project's documentation and technology stack. This ensures that the AI Agents working on the project adhere to strict, context-aware guidelines without manual configuration.

## 2. Analysis of External Resources

We analyzed several repositories to understand the state of the art in AI rule management.

### 2.1. Architectures & Frameworks
*   **`pew-pew-workspace`**: Represents a "Prompt Engineering Framework".
    *   **Key Insight**: Uses a modular "atomic design" for prompts: **Personas** (Who), **Instructions** (How), **Blocks** (Reusable content), and **Workflows** (Process).
    *   **Relevance**: We should adopt this modular approach. Instead of monolithic `.cursorrules` files, we should store small, reusable "Rule Blocks" and compile them.

### 2.2. Content Libraries
*   **`awesome-cursorrules` (PatrickJS)**: A massive collection of `.cursorrules` for specific stacks (Next.js, Python, Swift, etc.).
    *   **Key Insight**: Most rulesets follow a pattern:
        1.  **Persona**: "You are an expert Senior [Language] Developer."
        2.  **Style**: "Use [Framework] best practices."
        3.  **Naming**: "Use camelCase for variables."
        4.  **Behavior**: "Think step-by-step."
    *   **Redundancy**: There is significant duplication. For example, "Python Best Practices" is repeated across "Python FastAPI", "Python Django", and "Python Scripting" rulesets.
    *   **Relevance**: We can "normalize" this data. Extract the common "Python" rules into a base block, and "FastAPI" rules into an extension block.

## 3. Proposed Architecture: `forge rules`

### 3.1. Directory Structure (`templates/rules/`)
We will organize rules into a composable hierarchy:

```text
templates/rules/
├── core/                   # Universal rules (Forge Methodology, TDD, etc.)
│   ├── behavior.md         # "Don't be lazy", "Think step-by-step"
│   ├── tdd.md              # "Red-Green-Refactor" strictness
│   └── documentation.md    # "Update docs/04-changelog.md"
├── languages/              # Base language rules
│   ├── python.md           # PEP8, type hinting
│   ├── typescript.md       # Strong typing, interface vs types
│   └── rust.md
├── frameworks/             # Framework-specific extensions
│   ├── fastapi.md
│   ├── nextjs.md
│   ├── react.md
│   └── tailwind.md
└── roles/                  # Personas
    ├── architect.md        # Focus on structure, DDD
    └── developer.md        # Focus on implementation, clean code
```

### 3.2. The Resolution Engine (`src/forge/rules.py`)
The engine will function as a "Compiler":

1.  **Input**: Project Context.
    *   Primary: `docs/01-plan.md` (Tech Stack section).
    *   Secondary: Auto-detection (presence of `pyproject.toml`, `package.json`).
2.  **Selection**: Determine active tags (e.g., `["python", "fastapi", "developer"]`).
3.  **Assembly**: Concatenate blocks in a specific order:
    *   `roles/{role}.md` (Persona)
    *   `core/*.md` (Governance/Methodology)
    *   `languages/{lang}.md` (Base Syntax)
    *   `frameworks/{fw}.md` (Specific Patterns)
4.  **Output**: Write to `.cursorrules` (and others).

### 3.3. Conflict Resolution
If a specific framework rule contradicts a general language rule (e.g., "Don't use classes" in React vs "Use classes" in a general JS OOP rule), the **more specific** block (Framework) takes precedence or simply appends to the list. For `.cursorrules`, usually appending "latest instruction wins" works well, or we can use specific sections.

## 4. Implementation Plan

### Phase 1: Scaffolding (Immediate)
1.  Create the `templates/rules/` directory structure.
2.  Create the initial set of "Core" rules (Behavior, TDD) derived from `AGENTS.md`.
3.  Create "Language" rules for Python (since this is a Python project).

### Phase 2: Logic (Immediate)
1.  Implement `src/forge/rules.py` with a `compile_rules(tags: list[str]) -> str` function.
2.  Implement `forge rules gen` command.

### Phase 3: Content Expansion (Future)
1.  Ingest patterns from `awesome-cursorrules` to populate `frameworks/` and `languages/`.
