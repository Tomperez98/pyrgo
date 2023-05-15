"""fmt command."""

import pathlib
import sys

import click
from result import Ok

from pyrgo.core import ops


@click.command()
def fmt() -> None:
    """Format all files of the current project using `black` and `ruff`."""
    executed = ops.fmt.execute(cwd=pathlib.Path().cwd())
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)

    sys.exit(0)
