"""clean command."""

import sys

import click
from result import Ok

from pyrgo.core import ops


@click.command()
def clean() -> None:
    """Remove artifacts that pyrgo has generated in the past."""
    executed = ops.clean.execute()
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)
    sys.exit(0)
