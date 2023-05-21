"""build command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.constants import app_config


@click.command
def build() -> None:
    """Build project."""
    executed = ops.build.execute(
        app_config=app_config,
    )
    if not isinstance(executed, Ok):
        sys.exit(1)
    sys.exit(0)
