"""activate command."""

import sys

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.config import app_config


@click.command
def venv() -> None:
    """Create project virtual environment."""
    executed = ops.venv.execute(
        app_config=app_config,
    )
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)
    sys.exit(0)
