"""activate command."""

import sys

import click
from result import Ok

from pyrgo.core import ops


@click.command
def venv() -> None:
    """Create project virtual environment."""
    executed = ops.venv.execute()
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)
    sys.exit(0)
