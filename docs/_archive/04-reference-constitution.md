# The Forge Constitution

The Constitution acts as the architectural DNA of the system, ensuring that every generated implementation maintains consistency, simplicity, and quality.

## The Nine Articles of Development

### Article I: Library-First Principle

**Every feature must begin as a standalone library.**

```text
Every feature in Forge MUST begin its existence as a standalone library.
No feature shall be implemented directly within application code without
first being abstracted into a reusable library component.
```

### Article II: CLI Interface Mandate

**Every library must expose its functionality through a command-line interface.**

```text
All CLI interfaces MUST:
- Accept text as input (via stdin, arguments, or files)
- Produce text as output (via stdout)
- Support JSON format for structured data exchange
```

### Article III: Test-First Imperative

**NON-NEGOTIABLE: All implementation MUST follow strict Test-Driven Development.**

```text
No implementation code shall be written before:
1. Unit tests are written
2. Tests are validated and approved by the user
3. Tests are confirmed to FAIL (Red phase)
```

### Articles VII & VIII: Simplicity and Anti-Abstraction

**Combat over-engineering.**

```text
Section 7.3: Minimal Project Structure
- Maximum 3 projects for initial implementation
- Additional projects require documented justification

Section 8.1: Framework Trust
- Use framework features directly rather than wrapping them
```

### Article IX: Integration-First Testing

**Prioritize real-world testing over isolated unit tests.**

```text
Tests MUST use realistic environments:
- Prefer real databases over mocks
- Use actual service instances over stubs
- Contract tests mandatory before implementation
```

## Governance

Modifications to this constitution require:
- Explicit documentation of the rationale for change
- Review and approval by project maintainers
- Backwards compatibility assessment
