"""fmt command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.constants import app_config


@click.command()
def fmt() -> None:
    """Format all files of the current project using `black` and `ruff`."""
    executed = ops.fmt.execute(
        app_config=app_config,
    )
    if not isinstance(executed, Ok):
        sys.exit(1)
    sys.exit(0)
