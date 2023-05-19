"""new command."""
from __future__ import annotations

import click


@click.command()
def new() -> None:
    """Create a new pyrgo project."""
    raise NotImplementedError
