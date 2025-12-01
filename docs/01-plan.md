# 01 Plan: The Strategic Vision

**Status**: Versioned
**Purpose**: The "Why" and "How". Strategic alignment, technical choices, and feature scope.

## 1. Project Identity
**Name**: FORGE (formerly Ai Max / Spec Kit)
**Type**: CLI Tool & Methodology
**Goal**: Bootstrap Spec-Driven Development (SDD) projects with AI Agent support.

## 2. Strategic Roadmap

### Phase 1: Consolidation & Branding (Current)
- [ ] Rename package and artifacts to "Forge".
- [ ] Implement local template usage for development.
- [ ] Refactor monolithic `__init__.py`.

### Phase 2: Methodology V2 Integration
- [ ] Fully adopt FORGE v2 documentation structure (this file is part of it).
- [ ] Update templates to reflect V2 methodology (RDD -> DDD -> TDD -> CDD).

### Phase 3: Expansion
- [ ] Add support for more agents.
- [ ] Implement "Waterfall Gates" for regulated projects.

## 3. Technical Architecture (The "How")

### Stack
- **Language**: Python 3.10+
- **Distribution**: PyPI (future), GitHub Releases (current)
- **Dependencies**: Minimal (typer/click, rich, requests).

### Supported Agents
The following agents are supported via the `forge init` command:

| Agent | Directory | CLI Tool |
|-------|-----------|----------|
| **Claude Code** | `.claude/commands/` | `claude` |
| **Gemini CLI** | `.gemini/commands/` | `gemini` |
| **GitHub Copilot** | `.github/prompts/` | N/A |
| **Cursor** | `.cursor/commands/` | `cursor-agent` |
| **Qwen Code** | `.qwen/commands/` | `qwen` |
| **OpenCode** | `.opencode/command/` | `opencode` |
| **Codex CLI** | `.codex/commands/` | `codex` |
| **Windsurf** | `.windsurf/workflows/` | N/A |
| **Kilo Code** | `.kilocode/rules/` | N/A |
| **Auggie CLI** | `.augment/rules/` | `auggie` |
| **Roo Code** | `.roo/rules/` | N/A |
| **CodeBuddy** | `.codebuddy/commands/` | `codebuddy` |
| **Amazon Q** | `.amazonq/prompts/` | `q` |

## 4. Known Gaps
- **Local Dev**: `forge init` fetches from remote by default. Need flag for local templates.
- **Testing**: Python unit test coverage is low.
