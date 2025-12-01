# Agent Reference & Integration

## About Forge and Agents

**Forge** supports multiple AI coding assistants, allowing teams to use their preferred tools while maintaining consistent project structure and development practices.

The **Forge CLI** bootstraps projects with agent-specific configurations.

## Supported Agents

| Agent | Directory | Format | CLI Tool | Description |
|-------|-----------|---------|----------|-------------|
| **Claude Code** | `.claude/commands/` | Markdown | `claude` | Anthropic's Claude Code CLI |
| **Gemini CLI** | `.gemini/commands/` | TOML | `gemini` | Google's Gemini CLI |
| **GitHub Copilot** | `.github/prompts/` | Markdown | N/A | GitHub Copilot in VS Code |
| **Cursor** | `.cursor/commands/` | Markdown | `cursor-agent` | Cursor CLI |
| **Qwen Code** | `.qwen/commands/` | TOML | `qwen` | Alibaba's Qwen Code CLI |
| **OpenCode** | `.opencode/command/` | Markdown | `opencode` | opencode CLI |
| **Codex CLI** | `.codex/commands/` | Markdown | `codex` | Codex CLI |
| **Windsurf** | `.windsurf/workflows/` | Markdown | N/A | Windsurf IDE workflows |
| **Kilo Code** | `.kilocode/rules/` | Markdown | N/A | Kilo Code IDE |
| **Auggie CLI** | `.augment/rules/` | Markdown | `auggie` | Auggie CLI |
| **Roo Code** | `.roo/rules/` | Markdown | N/A | Roo Code IDE |
| **CodeBuddy** | `.codebuddy/commands/` | Markdown | `codebuddy` | CodeBuddy CLI |
| **Amazon Q** | `.amazonq/prompts/` | Markdown | `q` | Amazon Q Developer CLI |

## Adding New Agent Support

### 1. Add to AGENT_CONFIG

Add the new agent to the `AGENT_CONFIG` dictionary in `src/forge/__init__.py`:

```python
AGENT_CONFIG = {
    "new-agent-cli": {  # Use ACTUAL CLI tool name
        "name": "New Agent Display Name",
        "folder": ".newagent/",
        "install_url": "https://example.com/install",
        "requires_cli": True,
    },
}
```

### 2. Update CLI Help

Update the `--ai` parameter help text in the `init()` command.

### 3. Update Release Scripts

Update `.github/workflows/scripts/create-release-packages.sh` and `create-github-release.sh` to include the new agent package.

### 4. Update Agent Context Scripts

Update `scripts/bash/update-agent-context.sh` and `scripts/powershell/update-agent-context.ps1`.

## Command File Formats

### Markdown Format
Used by: Claude, Cursor, OpenCode, Windsurf, Amazon Q.

```markdown
---
description: "Command description"
---

Command content with {SCRIPT} and $ARGUMENTS placeholders.
```

### TOML Format
Used by: Gemini, Qwen.

```toml
description = "Command description"

prompt = """
Command content with {SCRIPT} and {{args}} placeholders.
"""
```

## Directory Conventions

- **CLI agents**: Usually `.<agent-name>/commands/`
- **IDE agents**: Follow IDE-specific patterns (e.g., `.github/prompts/`).

## Common Pitfalls

1. **Shorthand Keys**: Always use the actual executable name as the `AGENT_CONFIG` key (e.g., `"cursor-agent"`, not `"cursor"`).
2. **Update Scripts**: Remember to update both Bash and PowerShell scripts.
3. **Requires CLI**: Set `requires_cli` to `False` for IDE-based agents.
