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
- [x] Rename package and artifacts to "Forge".
- [x] Implement core "Spec-Flow" workflow (`plan`, `tasks`, `implement`).
- [x] Establish Constitution (`AGENTS.md`) and Rules (`06-rules.md`).

### Phase 2: Technical Debt & Stability (Current)
*Focus: Adhering to CDD/TDD principles and ensuring reliability.*

#### Operation "Slice the Monolith" (CDD Compliance)
- [ ] Refactor `src/forge/utils.py` (>500 lines) into focused modules (`logging`, `git`, `fs`).
- [ ] Refactor `src/forge/downloader.py` (>400 lines) into `fetcher` service.
- [ ] Refactor `src/forge/commands/init.py` (>400 lines) into `scaffolding` service.

#### Operation "Safety Net" (TDD Compliance)
- [ ] Implement unit tests for `src/forge/state.py` (State persistence).
- [ ] Implement unit tests for `src/forge/rules.py` (Rule compilation).
- [ ] Implement unit tests for `src/forge/commands/workflow.py` (Command logic).
- [ ] Achieve >80% coverage on core modules.

#### Operation "Local First" (DX)
- [ ] Fix `forge init --local` structural mismatch (Critical for self-hosting).
- [ ] Verify offline capability.

### Phase 3: Content & Compatibility Expansion
*Focus: Broadening support for languages and environments.*

- [ ] **Language Expansion**: Add rule templates for Java, C#, Go, Rust, PHP, Ruby.
- [ ] **CI/CD Matrix**: Implement GitHub Actions runners for Windows and macOS.
- [ ] **Waterfall Gates**: Implement strict `forge optimize` checks (linting, SAST).
- [ ] **Agent Templates**: Tune prompts for Qwen, OpenCode, and Amazon Q.

### Phase 4: Advanced Features (Future)
- [ ] **Plugin System**: Allow third-party templates via pip plugins.
- [ ] **Web UI**: Optional dashboard for visualizing `state.json`.
- [ ] **Telemetry**: Opt-in stats on agent usage.

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
