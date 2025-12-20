# IA MAX Kit v0.1.0 - Initial Release

**Release Date**: 2025-01-XX

## 🎉 First Release

This is the initial release of **IA MAX Kit**, a fork of [GitHub Spec Kit](https://github.com/github/spec-kit) enhanced with multi-agent AI development capabilities.

## 🆕 What's New in IA MAX Kit

### Rebranding and Identity
- **New Name**: IA MAX Kit (AI-Driven Multi-Agent Development Framework)
- **Package Name**: `aimax-kit` (was `specify-cli`)
- **Version**: 0.1.0 (starting fresh from Spec Kit 0.0.20)
- **Repository**: `yuichiinumaru/aimax-kit` (private)

### Core Features (Inherited from Spec Kit)
- ✅ **Specification-Driven Development (SDD)** methodology
- ✅ **Multi-Agent Support**: Claude Code, GitHub Copilot, Cursor, Gemini CLI, Qwen, Windsurf, and more
- ✅ **Slash Commands**: `/speckit.*` commands for AI assistants
- ✅ **Template System**: Comprehensive templates for specs, plans, tasks, and checklists
- ✅ **Constitution Framework**: Nine Articles of Development for governance
- ✅ **Cross-Platform**: Bash and PowerShell scripts for all platforms

### IA MAX Enhancements (Planned for M0-M3)
The following features are **documented and planned** but not yet implemented:
- 🔄 Multi-agent orchestration with specialized roles (Dev, Reviewer, Refactor, Tester, Monitor, Resolver, Security, Docs)
- 🔄 Repository Planning Graphs (RPG) for code context
- 🔄 Shared memory systems (consensus, whiteboard, persona namespaces)
- 🔄 Deep observability (OpenTelemetry, structured logging, distributed tracing)
- 🔄 TEVV framework (Test, Evaluation, Verification & Validation)
- 🔄 SWE-Debate mechanism for conflict resolution
- 🔄 AI-TDD enhancements (type-constrained generation, ARCS-like retrieval)
- 🔄 AI PR package generation
- 🔄 Stack selection framework ("Marcha Analítica de Stack")

## 📦 Release Assets

This release includes template packages for **13 AI assistants** × **2 script types** = **26 total packages**:

### Supported AI Assistants
- Claude Code (`claude`)
- GitHub Copilot (`copilot`)
- Cursor (`cursor-agent`)
- Gemini CLI (`gemini`)
- Qwen Code (`qwen`)
- OpenCode (`opencode`)
- Windsurf (`windsurf`)
- Codex CLI (`codex`)
- Kilo Code (`kilocode`)
- Auggie CLI (`auggie`)
- Roo Code (`roo`)
- CodeBuddy CLI (`codebuddy`)
- Amazon Q Developer (`q`)

### Script Types
- **sh**: Bash scripts (Linux/macOS)
- **ps**: PowerShell scripts (Windows)

### Package Naming Convention
```
aimax-kit-template-{assistant}-{script}-v0.1.0.zip
```

Example: `aimax-kit-template-claude-sh-v0.1.0.zip`

## 🚀 Installation

### Method 1: From GitHub
```bash
pip install git+https://github.com/yuichiinumaru/aimax-kit.git
```

### Method 2: Development Mode
```bash
git clone https://github.com/yuichiinumaru/aimax-kit.git
cd aimax-kit
pip install -e .
```

### Verify Installation
```bash
specify --version
# Should show: 0.1.0
```

## 🔧 Usage

### Initialize a New Project
```bash
specify init my-project --ai claude --script sh
```

### Available Commands (via AI Assistant)
- `/speckit.constitution` - Establish project principles
- `/speckit.specify` - Create baseline specification
- `/speckit.clarify` - Ask structured questions (optional)
- `/speckit.plan` - Create implementation plan
- `/speckit.tasks` - Generate actionable tasks
- `/speckit.analyze` - Cross-artifact consistency check (optional)
- `/speckit.checklist` - Generate quality checklists (optional)
- `/speckit.implement` - Execute implementation

**Note**: Future releases will add `/aimaxkit.*` commands for IA MAX-specific features.

## 🙏 Attribution

IA MAX Kit is built upon [GitHub Spec Kit](https://github.com/github/spec-kit) by GitHub, Inc. We maintain the original MIT License and extend our gratitude to the original maintainers and contributors.

See [ATTRIBUTION.md](ATTRIBUTION.md) for full credits.

## 📚 Documentation

- **Installation Guide**: [INSTALL.md](INSTALL.md)
- **Attribution**: [ATTRIBUTION.md](ATTRIBUTION.md)
- **README**: [README.md](README.md)
- **Status Report**: See root directory `00-STATUS-REPORT.md`
- **M0 Action Plan**: See root directory `11-M0-ACTION-PLAN.md`

## 🗺️ Roadmap

### M0 (Current - In Progress)
- Create IA MAX-specific templates (11 new templates)
- Extend existing templates with IA MAX sections
- Update scripts for new artifact structure

### M1 (Next)
- Implement `/aimaxkit.stack` command
- Implement `/aimaxkit.memory` command
- Implement `/aimaxkit.orchestrate` command
- Implement `/aimaxkit.observe` command
- Implement `/aimaxkit.tevv` command

### M2 (Future)
- Implement `/aimaxkit.rpg` command
- Implement `/aimaxkit.debate` command
- Implement `/aimaxkit.pr` command

### M3 (Future)
- End-to-end testing and validation
- Multi-stack testing
- Documentation finalization

## ⚠️ Known Issues

- This is an initial release with rebranding only
- IA MAX-specific features (RPG, orchestration, observability, etc.) are **not yet implemented**
- Templates still use `/speckit.*` command prefix (will be updated to `/aimaxkit.*` in M0)
- Full IA MAX functionality will be available after M0-M3 milestones complete

## 🔄 Breaking Changes from Spec Kit

- Package name changed: `specify-cli` → `aimax-kit`
- Repository changed: `github/spec-kit` → `yuichiinumaru/aimax-kit`
- Download URLs changed to use new repository
- Command prefix will change: `/speckit.*` → `/aimaxkit.*` (backward compatible for now)

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for detailed history from the original Spec Kit.

See root `07-changelog.md` for IA MAX-specific changes.

## 🤝 Contributing

This is a private repository currently in active development. Contributions are welcome from team members with repository access.

## 📄 License

MIT License - See [LICENSE](LICENSE)

Maintained from the original GitHub Spec Kit project.

## 💬 Support

- **Issues**: https://github.com/yuichiinumaru/aimax-kit/issues
- **Documentation**: See root directory for comprehensive guides

---

**Thank you for using IA MAX Kit!** 🚀

This release establishes the foundation. Watch for M0-M3 releases to see the full multi-agent AI development framework come to life.