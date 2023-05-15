"""check command."""


import pathlib
import sys

import click
from result import Ok

from pyrgo.core import ops


@click.command()
def check() -> None:
    """Analyze the current package with `ruff` and `mypy`."""
    executed = ops.check.execute(cwd=pathlib.Path().cwd())
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)

    sys.exit(0)
