# Local Development Guide

This guide shows how to iterate on the **Forge CLI** locally.

## 1. Clone the Repository

```bash
git clone https://github.com/suportesaude/forge.git
cd forge
```

## 2. Run the CLI Directly

You can execute the CLI via the module entrypoint without installing anything:

```bash
# From repo root
python -m src.forge --help
python -m src.forge init demo-project --ai claude --ignore-agent-tools --script sh
```

## 3. Use Editable Install

Create an isolated environment using `uv`:

```bash
# Create & activate virtual env
uv venv
source .venv/bin/activate  # or .venv\Scripts\Activate.ps1 on Windows

# Install project in editable mode
uv pip install -e .

# Now 'forge' entrypoint is available
forge --help
```

## 4. Invoke with uvx Directly From Git

You can simulate user flows using `uvx` with the local path:

```bash
uvx --from . forge init demo-uvx --ai copilot --ignore-agent-tools
```

## 5. Testing Script Permissions

After running an `init`, check that shell scripts are executable on POSIX systems:

```bash
ls -l scripts | grep .sh
```

## 6. Build a Wheel Locally

Validate packaging before publishing:

```bash
uv build
ls dist/
```

## 7. Cleaning Up

Remove build artifacts / virtual env:

```bash
rm -rf .venv dist build *.egg-info
```
