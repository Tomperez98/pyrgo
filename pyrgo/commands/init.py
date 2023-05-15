"""init command."""


import click


@click.command()
def init() -> None:
    """Create a new pyrgo project in an existing directory."""
