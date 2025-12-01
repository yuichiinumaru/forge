# 06 Rules: The Law

**Status**: Versioned
**Purpose**: Coding standards, patterns, and "The 9 Articles".

## 1. The 9 Immutable Articles (from Constitution)

1. **Library-First Principle**: Every feature must begin as a standalone library.
2. **CLI Interface Mandate**: Every library must expose functionality via CLI (stdin/stdout/JSON).
3. **Test-First Imperative**: NON-NEGOTIABLE. Red -> Green -> Refactor.
4. **Simplicity**: Minimal structure (max 3 projects initially).
5. **Anti-Abstraction**: Use framework features directly.
6. **Integration-First Testing**: Prefer real envs over mocks.
7. **Documentation-Driven**: `docs/01-plan.md` is the source of truth.
8. **Task Atomicity**: Do not multitask.
9. **Institutional Memory**: Always update the Changelog.

## 2. Coding Standards

### Python
- **Type Hinting**: Required for all function signatures.
- **Docstrings**: Google Style.
- **Formatter**: Black / Ruff.

### Markdown
- **Headers**: ATX style (`# Header`).
- **Lists**: Hyphens (`- item`).

## 3. Workflow Rules
- **Verify**: Always run `ls` or `grep` after file creation.
- **No Blind Debugging**: If a test fails, revert to the last known good state if the fix isn't obvious.
