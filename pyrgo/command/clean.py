"""clean command."""

import click


@click.command()
def clean() -> None:
    """Remove artifacts that pyrgo has generated in the past."""
