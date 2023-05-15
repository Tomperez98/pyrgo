"""add command."""

import click


@click.command
def add() -> None:
    """Add dependencies to a pyproject.toml manifest file."""
