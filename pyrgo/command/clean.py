"""clean command."""

import click
from pyrgo import _pyrgo


@click.command()
def clean() -> None:
    """Clear projects caches."""
    _pyrgo.all_folders()
