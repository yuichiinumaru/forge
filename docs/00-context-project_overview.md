# FORGE: Spec-Driven Development Framework

*Where projects begin hard as steel.*

**FORGE** (formerly Ai Max / Spec Kit) is a comprehensive toolkit for implementing **Spec-Driven Development (SDD)**. It inverts the traditional power structure of software development: instead of specifications serving code, code serves specifications.

## What is Spec-Driven Development?

Spec-Driven Development (SDD) is a methodology where specifications are not just documentation, but **executable artifacts** that directly generate working implementations.

### The Power Inversion
For decades, code has been the source of truth. SDD changes this. The **Specification** becomes the primary artifact. Code becomes its expression in a particular language and framework.

- **Intent-Driven**: Specifications define the "what" and "why" using natural language.
- **Executable**: Implementation plans derived from specs are precise enough to generate code.
- **Continuous Refinement**: The process supports iterative 0 -> 1 development, parallel experimentation, and brownfield modernization.

## Core Philosophy

- **Specifications as Lingua Franca**: Maintaining software means evolving specifications.
- **Multi-Step Refinement**: Avoid one-shot code generation. Use a pipeline: `Specify` -> `Clarify` -> `Plan` -> `Task` -> `Implement`.
- **Bidirectional Feedback**: Production metrics and incidents feed back into specification updates.

## Development Phases

| Phase | Description |
| :--- | :--- |
| **0-to-1 ("Greenfield")** | Generate from scratch. Start with high-level requirements, generate specs, plan steps, and build production-ready apps. |
| **Creative Exploration** | Parallel implementations. Explore diverse solutions and tech stacks for the same spec. |
| **Iterative Enhancement** | Modernize legacy systems. Add features iteratively. |

## The FORGE Toolkit

FORGE provides a CLI tool (`specify`) and a set of AI agent templates to automate the SDD workflow.

- **Scaffolding**: Initialize projects with agent-specific configurations.
- **Commands**: Slash commands (e.g., `/forge.specify`, `/forge.plan`) to drive the AI.
- **Templates**: Structured prompts that guide Large Language Models (LLMs) to produce high-quality specs and code.

## Getting Started

- [Installation Guide](03-guide-installation.md)
- [Quick Start](03-guide-quickstart.md)
- [Local Development](03-guide-local_development.md)
