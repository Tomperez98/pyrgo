"""Pyrgo cli 'python -m pyrgo.cli.pyrgo_init' entrypoint."""
from __future__ import annotations

import sys

if __name__ == "__main__":
    from pyrgo.cli.pyrgo_init.cli import root

    sys.exit(root())
