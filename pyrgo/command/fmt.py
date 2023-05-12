"""fmt command."""

import click


@click.command()
def fmt() -> None:
    """Format all files of the current project using `black` and `ruff`."""
