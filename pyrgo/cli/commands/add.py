"""add command."""
from __future__ import annotations

import click


@click.command
def add() -> None:
    """
    Add dependencies to a pyproject.toml manifest file and install.

    \b
    Install packages from:
    - PyPI (and other indexes) using requirement specifiers.
    - VCS project urls.
    - Local project directories.
    - Local or remote source archives.
    """  # noqa: D301
    raise NotImplementedError
