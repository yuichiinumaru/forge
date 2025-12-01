#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "typer",
#     "rich",
#     "platformdirs",
#     "readchar",
#     "httpx",
# ]
# ///
"""
Forge CLI - Setup tool for Forge projects

Usage:
    uvx forge.py init <project-name>
    uvx forge.py init .
    uvx forge.py init --here

Or install globally:
    uv tool install --from forge.py forge
    forge init <project-name>
    forge init .
    forge init --here
"""

from forge.cli import main

if __name__ == "__main__":
    main()
