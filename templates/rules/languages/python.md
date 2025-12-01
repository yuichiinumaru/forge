# Python Development Rules

- **Type Hinting**: All function signatures must be type-hinted.
- **Docstrings**: Use Google-style docstrings for all modules, classes, and functions.
- **Formatting**: Adhere to Black code style.
- **Linting**: Ensure code passes `ruff` or `flake8` checks.
- **Dependencies**: Manage dependencies via `uv` or `pip` and update `pyproject.toml` or `requirements.txt` immediately.
- **Pathing**: Use `pathlib` over `os.path` where possible.
