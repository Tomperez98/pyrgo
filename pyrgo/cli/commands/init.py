"""init command."""


import sys

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.constants import app_config


@click.command()
def init() -> None:
    """Create a new pyrgo project in an existing directory."""
    executed = ops.init.execute(
        app_config=app_config,
    )
    if not isinstance(executed, Ok):
        sys.exit(1)
    sys.exit(0)
