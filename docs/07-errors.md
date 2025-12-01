# 07 Errors: Known Issues & Patterns

**Status**: Live
**Purpose**: Documentation of known bugs, workarounds, and common error patterns to help the Agent self-correct.

## Known Issues

### CLI Template Download
- **Issue**: `forge init` fetches from remote GitHub release even in local dev.
- **Workaround**: Currently manual; future task to add `--local` flag.

### Agent Configuration
- **Issue**: `AGENT_CONFIG` is hardcoded in `__init__.py`.
- **Workaround**: Modify the python file directly to add new agents.
