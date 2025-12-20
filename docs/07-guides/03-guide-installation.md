# Installation Guide

## Prerequisites

- **Linux/macOS** (Windows supported via PowerShell)
- AI Coding Agent (one of):
  - [Claude Code](https://www.anthropic.com/claude-code)
  - [GitHub Copilot](https://code.visualstudio.com/)
  - [Gemini CLI](https://github.com/google-gemini/gemini-cli)
  - [CodeBuddy CLI](https://www.codebuddy.ai/cli)
  - [Qwen Code](https://github.com/QwenLM/qwen-code)
  - [OpenCode](https://opencode.ai)
  - [Amazon Q Developer](https://aws.amazon.com/developer/learning/q-developer-cli/)
- [uv](https://docs.astral.sh/uv/) for package management
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## Installation

### Initialize a New Project

The easiest way to get started is to initialize a new project using `uvx`:

```bash
uvx --from git+https://github.com/suportesaude/forge.git forge init <PROJECT_NAME>
```
*(Note: Replace URL with your actual repository URL)*

Or initialize in the current directory:

```bash
uvx --from git+https://github.com/suportesaude/forge.git forge init .
# or
uvx --from git+https://github.com/suportesaude/forge.git forge init --here
```

### Specify AI Agent

You can proactively specify your AI agent during initialization:

```bash
forge init <project_name> --ai claude
forge init <project_name> --ai gemini
forge init <project_name> --ai copilot
forge init <project_name> --ai qwen
```

### Script Type (Shell vs PowerShell)

Automation scripts are available in Bash (`.sh`) and PowerShell (`.ps1`). The CLI auto-selects based on your OS, but you can force a type:

```bash
forge init <project_name> --script sh  # Force POSIX shell
forge init <project_name> --script ps  # Force PowerShell
```

### Ignore Agent Tools Check

To bypass tool validation:

```bash
forge init <project_name> --ai claude --ignore-agent-tools
```

## Verification

After initialization, check for the available slash commands in your agent's context (e.g., by typing `/` or checking the `.forge` or `.forge` directory instructions):
- `/forge.constitution`
- `/forge.specify`
- `/forge.plan`
- `/forge.tasks`

## Troubleshooting

### Git Credential Manager on Linux
If you encounter Git authentication issues on Linux, consider installing Git Credential Manager.

```bash
# Example for Debian/Ubuntu
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
git config --global credential.helper manager
```
