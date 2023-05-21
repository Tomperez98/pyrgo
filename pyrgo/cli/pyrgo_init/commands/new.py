"""new command."""
from __future__ import annotations

from pathlib import Path

import click


@click.command()
@click.argument("path", type=click.Path())
def new(path: str) -> None:
    """Initialize a new Pyrgo project."""
    path_as_path = Path(path)
    click.echo(f"new command to {path_as_path.absolute()}")
