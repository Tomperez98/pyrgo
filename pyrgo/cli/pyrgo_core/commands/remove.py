"""remove command."""
from __future__ import annotations

import click


@click.command()
def remove() -> None:
    """Remove dependencies from the manifest file."""
    raise NotImplementedError
