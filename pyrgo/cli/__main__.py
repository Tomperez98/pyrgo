"""Pyrgo cli 'python -m pyrgo.cli' entrypoint."""
from __future__ import annotations

import sys

if __name__ == "__main__":
    from pyrgo.cli.cli import root

    sys.exit(root())
