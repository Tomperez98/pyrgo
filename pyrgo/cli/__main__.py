"""Pyrgo cli 'python -m pyrgo.cli' entrypoint."""
import sys

if __name__ == "__main__":
    from pyrgo.cli.cli import root

    sys.exit(root())
