"""clean command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.constants import app_config


@click.command()
def clean() -> None:
    """Remove artifacts that pyrgo has generated in the past."""
    executed = ops.clean.execute(
        app_config=app_config,
    )
    if not isinstance(executed, Ok):
        sys.exit(1)
    sys.exit(0)
