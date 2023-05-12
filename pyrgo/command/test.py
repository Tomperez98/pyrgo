"""test command."""

import click


@click.command()
def test() -> None:
    """Execute all unit and integration tests."""
