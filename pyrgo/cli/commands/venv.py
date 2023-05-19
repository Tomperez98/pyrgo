"""activate command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.constants import app_config


@click.command
def venv() -> None:
    """Create project virtual environment."""
    executed = ops.venv.execute(
        app_config=app_config,
    )
    if not isinstance(executed, Ok):
        sys.exit(1)

    click.echo(
        message=app_config.venv_activation_msg,
    )
    sys.exit(0)
