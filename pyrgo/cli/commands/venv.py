"""activate command."""

import pathlib
import sys

import click
from result import Ok

from pyrgo.core import ops


@click.command
def venv() -> None:
    """Create project virtual environment."""
    cwd = pathlib.Path().cwd()
    executed = ops.venv.execute(cwd=cwd)
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)

    sys.exit(0)
