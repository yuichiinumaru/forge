# 09 Analysis: Compatibility Audit

**Date**: 2024-05-24
**Topic**: Compatibility (Agents, IDEs, OS, Stacks)
**Status**: Final Analysis
**Author**: Senior PRD Architect
**Scope**: `docs/`, `src/forge/rules.py`, `src/forge/commands/workflow.py`, `scripts/`

---

## 1. Executive Summary

This document analyzes the compatibility profile of the **Forge** project. We evaluate compatibility across four dimensions:
1.  **AI Agents**: Which AI coding assistants can "drive" Forge?
2.  **Development Environments (IDEs)**: Where can Forge run?
3.  **Operating Systems**: Which platforms are supported?
4.  **Target Tech Stacks**: What kind of projects can Forge bootstrap and manage?

**Verdict**: **High Agent Compatibility, Medium Stack Support**.
Forge achieves broad agent compatibility by using "Markdown Prompts" as the universal interface, avoiding proprietary API dependencies. However, its "Target Stack" detection (`rules.py`) is currently limited to Python and JavaScript ecosystems.

---

## 2. AI Agent Compatibility

The core promise of Forge is to be an "Operating System for AI Agents". It achieves this by abstracting the agent interaction into markdown templates.

### 2.1. The "Universal Interface" Strategy
Instead of integrating with Agent APIs (like the OpenAI API directly), Forge outputs **Prompts** (`forge plan`, `forge tasks`) that the user copies to the Agent.
- **Mechanism**: `src/forge/commands/workflow.py` loads templates from `templates/agents/`.
- **Implication**: This makes Forge **forward-compatible** with *any* text-based AI agent, including future ones, without code changes. If a new agent "SuperGPT-5" is released, the user simply feeds it the output of `forge plan`.

### 2.2. Supported Agents (Official List)
According to `docs/01-plan.md`, the following agents are explicitly supported via the `forge init` command (which likely scaffolds agent-specific config folders):

| Agent | Config Path | CLI Tool | Status |
| :--- | :--- | :--- | :--- |
| **Claude Code** | `.claude/commands/` | `claude` | ✅ Native Support |
| **Gemini CLI** | `.gemini/commands/` | `gemini` | ✅ Native Support |
| **GitHub Copilot** | `.github/prompts/` | N/A | ✅ Via Chat |
| **Cursor** | `.cursor/commands/` | `cursor-agent` | ✅ Deep Integration |
| **Windsurf** | `.windsurf/workflows/` | N/A | ✅ Rule Support |
| **Qwen Code** | `.qwen/commands/` | `qwen` | ⚠️ Template pending |
| **OpenCode** | `.opencode/command/` | `opencode` | ⚠️ Template pending |
| **Amazon Q** | `.amazonq/prompts/` | `q` | ⚠️ Template pending |

### 2.3. Code Evidence
In `src/forge/commands/workflow.py`:
```python
def load_agent_template(agent_name: str) -> str:
    # ...
    # Priority 1: User customized template in .forge/templates/agents
    local_template = Path.cwd() / ".forge" / "templates" / "agents" / f"{agent_name}.md"
    # ...
```
This code proves that users can customize the "personality" of the agent driving the workflow. If "Claude" requires a different prompting style than "Cursor", the user can create `.forge/templates/agents/plan.md` tailored to Claude.

---

## 3. IDE & Tool Compatibility

### 3.1. IDEs as Platforms
Forge is primarily designed for **Cursor** and **Windsurf**, the new generation of "AI-Native IDEs".
- **Cursor**: Supported via `.cursorrules` generation. `src/forge/rules.py` explicitly has a `compile` command that targets `.cursorrules`.
- **Windsurf**: Supported via `.windsurfrules` (mentioned in drafts, likely shares logic with `.cursorrules`).
- **VSCode**: Supported as the underlying platform for Cursor/Windsurf.
- **Terminal**: Since Forge is a CLI (`typer`), it is IDE-agnostic. It can run in Vim, Emacs, or IntelliJ terminals.

### 3.2. Configuration Generation (`forge rules`)
The `forge rules compile` command is the bridge between Forge and the IDE.
- **Function**: It reads the project state and generates the "System Prompt" for the IDE's AI.
- **Code Analysis** (`src/forge/rules.py`):
    - It combines `roles`, `core` rules, and `stack` rules.
    - It processes "Wikilinks" (embedding content).
    - **Result**: A `.cursorrules` file that makes the IDE "aware" of Forge's methodology (RDD/TDD/CDD).

---

## 4. Operating System Compatibility

### 4.1. Cross-Platform Core (Python)
The CLI is written in **Python 3.10+** using `pathlib` for file system operations.
- **Path Handling**: The usage of `Path.cwd() / "folder"` ensures compatibility with both Windows (backslashes) and Unix (forward slashes).
- **Dependencies**: `typer`, `rich`, `requests` are pure Python and run everywhere.

### 4.2. Helper Scripts (`scripts/`)
The project includes a `scripts/` directory to handle shell-specific tasks (likely installation or bootstrap).
- **Linux/macOS**: `scripts/bash/` exists.
- **Windows**: `scripts/powershell/` exists.
- **Analysis**: This demonstrates a deliberate effort to support Windows users, who are often neglected in CLI tools. The presence of PowerShell scripts is a strong compatibility signal.

---

## 5. Target Stack Compatibility

What kind of projects can you build *with* Forge? This is determined by the `detect_stack` function in `src/forge/rules.py`.

### 5.1. Current Detection Logic
The code in `src/forge/rules.py` currently detects:

**Python Ecosystem**:
- **Core**: Python (detects `pyproject.toml`, `requirements.txt`)
- **Frameworks**:
    - **FastAPI** (looks for "fastapi" string)
    - **Django** (looks for "django" string)

**JavaScript/Node Ecosystem**:
- **Core**: TypeScript (detects "typescript" in `package.json`)
- **Frameworks**:
    - **Next.js** (detects "next")
    - **React** (detects "react")
    - **Tailwind** (detects "tailwindcss")

### 5.2. Limitations & Gaps
- **Missing Languages**: There is currently no detection logic for **Go**, **Rust**, **Java**, **C#**, **PHP**, or **Ruby**.
- **Implication**: While you *can* use Forge with these languages (by manually creating templates), the *automatic* rule compilation (`forge rules compile`) won't inject language-specific best practices for them.
- **Roadmap Item**: The `docs/00-analysis-rules-integration.md` mentions "Phase 3: Content Expansion" to ingest patterns for more languages. This is a critical compatibility growth area.

---

## 6. Compatibility Testing

### 6.1. Current State
- **Tests**: `tests/test_cli.py` runs on the host OS.
- **CI/CD**: `docs/02-tasks.md` mentions "Update GitHub Actions workflows". Standard GitHub Actions usually run on `ubuntu-latest`.
- **Gap**: There is no evidence of a "Matrix Strategy" in the CI to explicitly test on `windows-latest` or `macos-latest`.

### 6.2. Roadmap for Compatibility
Based on the analysis, a roadmap for compatibility testing should include:
1.  **OS Matrix**: Add Windows/Mac runners to GitHub Actions.
2.  **Stack Fixtures**: Create dummy projects (a Django project, a Next.js project) in `tests/fixtures/` and verify that `forge rules compile` correctly detects them.
3.  **Agent Output Verification**: Verify that the markdown output of `forge plan` renders correctly in different markdown parsers (GitHub vs Obsidian vs VSCode).

---

## 7. Conclusion

**Forge** is designed as a "Universal Adapter" between Human Intent (Specs) and AI Execution (Agents).

- **Strengths**:
    - **Agent Agnostic**: The decision to use Markdown Templates as the interface is brilliant. It creates nearly infinite forward compatibility with any LLM.
    - **IDE Integration**: Direct support for Cursor/Windsurf via rule compilation positions it well for the current "AI IDE" wave.
    - **OS Support**: Python + PowerShell support covers 99% of developers.

- **Weaknesses**:
    - **Stack Detection**: Currently limited to Python and JS/TS. It needs to broaden its `rules.py` logic to support the wider enterprise ecosystem (Java, C#, Go).
    - **Validation**: Lack of automated cross-platform testing.

**Overall**: The project is highly compatible by design (architecture), but the implementation (content/rules) is currently focused on the authors' preferred stacks (Python/JS). Expanding `rules.py` is the lowest-hanging fruit to increase adoption.

---
*End of Analysis*
