"""docs new command."""

import pathlib
import sys

import click
from result import Ok

from pyrgo.core import ops


@click.command()
def new() -> None:
    """Create a new MkDocs project."""
    cwd = pathlib.Path().cwd()
    executed = ops.docs.new.execute(cwd=cwd)
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)

    sys.exit(0)
