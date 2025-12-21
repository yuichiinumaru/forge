# 01 Plan: The Strategic Vision

**Status**: Versioned
**Purpose**: The "Why" and "How". Strategic alignment, technical choices, and feature scope.

## 1. Project Identity
**Name**: FORGE (formerly Ai Max / Spec Kit)
**Type**: CLI Tool & Methodology
**Goal**: Bootstrap Spec-Driven Development (SDD) projects with AI Agent support.
**Methodology**: FORGE v2 (RDD -> DDD -> TDD -> CDD).

## 2. Strategic Roadmap

### Phase 1: Consolidation & Branding (Completed)
This phase successfully transitioned the project from `specify-cli` to `forge`, establishing the new brand and the "Constitution" (`AGENTS.md`). It also introduced the "Spec-Flow" inspired workflow commands (`plan`, `tasks`, `implement`).

### Phase 2: Technical Debt & Stability (Current)
*Focus: Adhering to CDD/TDD principles and ensuring reliability.*

#### Operation "Slice the Monolith" (CDD Compliance)
**Why**: Several core files (`utils.py`, `downloader.py`, `init.py`) have exceeded 400 lines, violating the CDD principle of "Atomic Components". This increases cognitive load for both humans and AI agents.
**How**: We will refactor these "God Objects" into smaller, single-purpose services (e.g., `services/fetcher.py`, `services/git.py`). This strictly enforces the <300 line limit.

#### Operation "Safety Net" (TDD Compliance)
**Why**: The transition to a stateful workflow manager introduced complex logic in `state.py` and `workflow.py` without corresponding test suites.
**How**: We will implement a comprehensive test suite targeting these new modules. The goal is to achieve >80% code coverage to prevent regressions in the core state machine.

#### Operation "Local First" (DX)
**Why**: The `forge init --local` command is critical for enterprise adoption (self-hosting templates) but is currently broken due to structural mismatches.
**How**: We will align the repository structure with the distribution structure to ensure that local development mirrors the production experience.

### Phase 3: Content & Compatibility Expansion
*Focus: Broadening support for languages and environments.*

#### Language Expansion
**Strategy**: Currently, `forge rules` only detects Python and JS/TS. To be a true "Universal Adapter", we must support major enterprise languages like Java, C#, Go, and Rust. We will ingest patterns from community repositories to build these rule templates.

#### CI/CD Matrix
**Strategy**: Since Forge claims cross-platform support (via Python/PowerShell), we must prove it. We will expand the GitHub Actions matrix to run tests on `windows-latest` and `macos-latest`.

#### Waterfall Gates
**Strategy**: To support regulated industries, we will implement strict "Quality Gates" in the `forge optimize` command. This will move beyond simple prompting to executing actual verification tools (SAST, Linters) before marking a feature complete.

### Phase 4: Advanced Features (Current)
*Focus: Extensibility and Developer Experience.*

#### Plugin Architecture
**Why**: To allow community extensions without bloating the core.
**How**: Implement a simple hook-based system for adding new Agent templates, Rule sets, or CLI commands.

#### Web Dashboard
**Why**: To provide a visual interface for the `state.json` workflow status.
**How**: A simple `fastapi` or `streamlit` dashboard reading `state.json`.

#### Telemetry (Opt-in)
**Why**: To understand agent usage patterns.
**How**: Minimal anonymous stats.

#### Community Health
**Why**: `CONTRIBUTING.md` is outdated.
**How**: Rewrite to align with Forge branding and V2 methodology.

## 3. Technical Architecture (The "How")

### Stack
- **Language**: Python 3.10+
- **CLI Framework**: `typer`
- **Output**: `rich`
- **Persistence**: JSON (`.forge/state.json`)

### Core Modules
- **`src/forge/cli.py`**: Entry point and command routing.
- **`src/forge/state.py`**: State machine persistence (Phase/Status tracking).
- **`src/forge/rules.py`**: Dynamic rule compilation (`.cursorrules` generation).
- **`src/forge/commands/workflow.py`**: Implementation of RDD->DDD->TDD flow.

### Supported Agents
The following agents are supported via `forge init` and `forge plan`:

| Agent | Config Path | CLI Tool |
|-------|-----------|----------|
| **Claude Code** | `.claude/commands/` | `claude` |
| **Gemini CLI** | `.gemini/commands/` | `gemini` |
| **Cursor** | `.cursor/commands/` | `cursor-agent` |
| **Windsurf** | `.windsurf/workflows/` | N/A |
| **GitHub Copilot** | `.github/prompts/` | N/A |

## 4. Known Gaps
- **CDD Violation**: `utils.py` and `init.py` are too large (>300 lines).
- **TDD Violation**: Core state logic lacks comprehensive unit tests.
- **Stack Detection**: `rules.py` only detects Python and JS/TS stacks.
- **Windows Testing**: No automated testing on Windows (though scripts exist).

## 5. Architectural Decisions (ADR Summary)
- **ADR-001**: Adopted "Forge Method" (RDD->DDD->TDD->CDD) as official doctrine.
- **ADR-002**: Dropped BDD (Gherkin) and FDD as strict requirements in favor of Markdown Specs (RDD) for better AI compatibility.
- **ADR-003**: Implemented State Machine (`.forge/state.json`) to decouple Agent memory from specific chat sessions.
