"""init command."""


import click

from pyrgo.core import ops

from pyrgo.core.constants import app_config


@click.command()
def init() -> None:
    """Create a new pyrgo project in an existing directory."""
    ops.init.execute(
        app_config=app_config,
    )
