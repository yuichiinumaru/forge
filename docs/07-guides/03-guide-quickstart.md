# Quick Start Guide

This guide will help you get started with Spec-Driven Development using FORGE.

> **Note**: All automation scripts provide both Bash (`.sh`) and PowerShell (`.ps1`) variants. The CLI auto-selects based on OS unless you pass `--script sh|ps`.

## The Standard Workflow

### 1. Install Forge

Initialize your project depending on the coding agent you're using:

```bash
uvx --from git+https://github.com/suportesaude/forge.git forge init <PROJECT_NAME>
```

### 2. Create the Spec

Use the `/forge.specify` command to describe what you want to build. Focus on the **what** and **why**, not the tech stack.

```bash
/forge.specify Build an application that can help me organize my photos in separate photo albums. Albums are grouped by date and can be re-organized by dragging and dropping on the main page.
```

### 3. Create a Technical Implementation Plan

Use the `/forge.plan` command to provide your tech stack and architecture choices.

```bash
/forge.plan The application uses Vite with minimal number of libraries. Use vanilla HTML, CSS, and JavaScript as much as possible. Images are stored in a local SQLite database.
```

### 4. Break Down and Implement

Use `/forge.tasks` to create an actionable task list, then ask your agent to implement the feature.

```bash
/forge.tasks
```

## Detailed Example: Building Taskify

Here's a complete example of building a team productivity platform.

### Step 1: Define Requirements

```text
/forge.specify Develop Taskify, a team productivity platform. It should allow users to create projects, add team members, assign tasks, and move tasks between boards in Kanban style.
```

### Step 2: Clarify (Optional)

If the spec has `[NEEDS CLARIFICATION]` markers, you can use `/forge.clarify` to resolve them interactively.

### Step 3: Generate Technical Plan

Be specific about your tech stack:

```text
/forge.plan We are going to generate this using .NET Aspire, using Postgres as the database. The frontend should use Blazor server with drag-and-drop task boards.
```

### Step 4: Validate and Implement

Generate tasks and start implementation:

```text
/forge.tasks
```

Then, instruct your agent:

```text
Implement the first task from specs/001-taskify/tasks.md
```

## Pro Workflow: Using Constitution and Analysis

For rigorous projects, you can use additional commands:

1.  **`/forge.constitution`**: Establish project-wide architectural principles (The Nine Articles) before starting features.
2.  **`/forge.analyze`**: Run a consistency check between spec, plan, and implementation.
3.  **`/forge.checklist`**: Generate a quality checklist for the current feature.

## Key Principles

- **Be explicit** about what you're building and why.
- **Don't focus on tech stack** during the specification phase.
- **Iterate and refine** your specifications before implementation.
- **Validate** the plan before coding begins.
