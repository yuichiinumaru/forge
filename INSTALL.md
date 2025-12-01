# Installation Guide - FORGE

This guide explains how to install and use **FORGE** instead of the public Spec Kit.

---

## 🎯 Overview

FORGE is a private fork of GitHub Spec Kit with enhanced multi-agent capabilities. Since it's in active development (currently preparing M0), it's not yet published to PyPI. You'll install directly from the GitHub repository.

---

## 📋 Prerequisites

- **Python 3.11 or higher**
- **Git**
- **GitHub account** with access to the repository
- **One or more AI assistants** (Claude Code, GitHub Copilot, Cursor, Gemini CLI, etc.)

---

## 🚀 Installation Methods

### Method 1: Install from GitHub (Recommended for Development)

This method installs FORGE in "editable" mode, allowing you to modify the code and see changes immediately.

```bash
# Clone the repository
git clone https://github.com/suportesaude/forge.git
cd forge

# Install in editable mode with pip
pip install -e .
```

**Verify installation:**
```bash
forge --version
```

You should see version `0.1.0` or higher.

---

### Method 2: Install from GitHub (Production Mode)

This installs FORGE as a regular package without keeping the source code editable.

```bash
# Install directly from GitHub
pip install git+https://github.com/suportesaude/forge.git
```

**Verify installation:**
```bash
forge --version
```

---

### Method 3: Install in Virtual Environment (Recommended for Isolation)

Using a virtual environment prevents conflicts with other Python packages.

```bash
# Create a virtual environment
python -m venv forge-env

# Activate the virtual environment
# On macOS/Linux:
source forge-env/bin/activate
# On Windows:
forge-env\Scripts\activate

# Install FORGE
pip install git+https://github.com/suportesaude/forge.git

# Verify
forge --version
```

---

## 🔧 Post-Installation Setup

### 1. Check Dependencies

Run the built-in check command to verify all tools are installed:

```bash
forge check
```

This will check for:
- Git
- AI assistant CLIs (Claude, Gemini, Cursor, etc.)

### 2. Configure Your AI Assistant

FORGE supports multiple AI assistants. Make sure you have at least one installed:

| Assistant | Installation | Documentation |
|-----------|--------------|---------------|
| **Claude Code** | [Install Claude CLI](https://docs.anthropic.com/claude/docs) | Recommended for full feature support |
| **GitHub Copilot** | Built into VS Code | No CLI needed |
| **Cursor** | [Install Cursor](https://cursor.sh/) | Install `cursor-agent` CLI |
| **Gemini CLI** | [Install Gemini](https://ai.google.dev/gemini-api/docs/cli) | Requires API key |
| **Windsurf** | Built into Windsurf IDE | No CLI needed |

### 3. Initialize Your First Project

```bash
# Interactive mode (recommended for first time)
forge init my-project

# Or specify options directly
forge init my-project --ai claude --script sh
```

This will:
- Download the FORGE template
- Set up directory structure
- Configure slash commands for your AI assistant
- Initialize a git repository (unless `--no-git`)

---

## 📦 What Gets Installed

When you initialize a project, FORGE creates:

```
my-project/
├── .forge/               # FORGE configuration and scripts
│   ├── templates/          # All templates (spec, plan, tasks, etc.)
│   └── scripts/           # Automation scripts (bash/PowerShell)
├── .claude/               # Claude Code commands (if using Claude)
│   └── commands/
├── .github/               # GitHub-specific files
│   └── prompts/          # GitHub Copilot prompts (if using Copilot)
├── docs/                  # Documentation
├── features/              # BDD feature files (Gherkin)
├── graphs/                # Repository Planning Graphs (RPG)
├── specs/                 # Feature specifications
├── memory/                # Shared memory configuration
│   └── constitution.md
└── README.md
```

---

## 🎮 Basic Usage

### 1. Start a New Feature

```bash
# In your project directory
# Use your AI assistant to run:
/forge.specify "Add user authentication"
```

This creates a new feature branch and specification.

### 2. Create a Plan

```bash
/forge.plan
```

This generates a technical implementation plan.

### 3. Generate Tasks

```bash
/forge.tasks
```

This breaks down the plan into actionable tasks.

### 4. Implement

```bash
/forge.implement
```

This guides you through implementation.

---

## 🔄 Updating FORGE

### If Installed in Editable Mode

```bash
cd forge
git pull origin main
```

Changes are immediately available.

### If Installed in Production Mode

```bash
pip install --upgrade git+https://github.com/suportesaude/forge.git
```

---

## 🆚 Differences from Original Spec Kit

If you're familiar with GitHub Spec Kit, here are the key differences:

| Aspect | Spec Kit | FORGE |
|--------|----------|------------|
| **Command prefix** | `/speckit.*` | `/forge.*` |
| **Repository** | `github/spec-kit` | `suportesaude/forge` |
| **Version** | 0.0.20 | 0.1.0+ |
| **Package name** | `forge` | `forge` |
| **Slash commands** | 8 commands | 8 + 8 new FORGE commands |
| **Templates** | 5 templates | 5 + 11 new FORGE templates |
| **Focus** | Spec-Driven Development | Multi-agent orchestration + SDD |

**Backward Compatibility**: Original `/speckit.*` commands still work. New FORGE features use `/forge.*` prefix.

---

## 🐛 Troubleshooting

### "forge: command not found"

**Solution**: Ensure pip's bin directory is in your PATH.

```bash
# On macOS/Linux:
export PATH="$HOME/.local/bin:$PATH"

# On Windows:
# Add %APPDATA%\Python\Python311\Scripts to PATH
```

Or reinstall with `pip install --user`:

```bash
pip install --user -e .
```

### "No matching release asset found"

This error occurs if you're trying to use the original Spec Kit download URLs. FORGE uses a different repository.

**Solution**: Ensure you're running version 0.1.0+ of FORGE:

```bash
forge --version
```

If you see 0.0.x, you have the old Spec Kit installed. Uninstall and reinstall:

```bash
pip uninstall specify-cli
pip install git+https://github.com/suportesaude/forge.git
```

### SSL/TLS Certificate Errors

If you encounter certificate errors:

```bash
forge init my-project --skip-tls
```

**Warning**: Only use `--skip-tls` in trusted environments.

### Git Credential Issues on Linux

See: [Troubleshooting Git Credentials](README.md#git-credential-manager-on-linux)

---

## 🔒 Authentication

### GitHub Token (Optional but Recommended)

For higher API rate limits and access to private repositories:

```bash
# Set environment variable
export GITHUB_TOKEN=your_token_here

# Or pass directly
forge init my-project --github-token your_token_here
```

Generate a token at: https://github.com/settings/tokens

Required scopes: `repo`, `workflow`

---

## 🧪 Verify Installation

Run this quick test to ensure everything works:

```bash
# 1. Check version
forge --version

# 2. Run system check
forge check

# 3. Initialize a test project
forge init test-project --ai claude --script sh

# 4. Navigate to project
cd test-project

# 5. Verify structure
ls -la .forge/
```

You should see the `.forge/` directory with templates and scripts.

---

## 📚 Next Steps

Once installed:

1. **Read the Documentation**: Start with [README-FIRST.md](../README-FIRST.md)
2. **Understand the Philosophy**: Read [AGENTS.md](AGENTS.md)
3. **Follow M0 Guide**: See [11-M0-ACTION-PLAN.md](../11-M0-ACTION-PLAN.md) if contributing
4. **Initialize a Project**: Run `forge init my-project`
5. **Try Slash Commands**: Use `/forge.specify`, `/forge.plan`, etc.

---

## 💡 Tips

- **Use `--debug`**: Add `--debug` flag to any command for verbose output
- **Check logs**: The CLI shows detailed progress during initialization
- **Multiple agents**: You can initialize for different AI assistants in the same project
- **Update regularly**: FORGE is in active development (M0-M3 phases)

---

## 🆘 Getting Help

- **Issues**: https://github.com/suportesaude/forge/issues
- **Documentation**: See all MD files in the root directory
- **Status Report**: Read `00-STATUS-REPORT.md` for current project state

---

## 📄 License

FORGE is released under the MIT License, maintaining compatibility with the original GitHub Spec Kit license.

See: [LICENSE](LICENSE) and [ATTRIBUTION.md](ATTRIBUTION.md)

---

**Happy developing with FORGE!** 🚀