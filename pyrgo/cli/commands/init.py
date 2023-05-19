"""init command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.constants import app_config


@click.command()
@click.option(
    "-n",
    "--name",
    "name",
    required=True,
    type=click.STRING,
    help="Project name.",
)
def init(name: str) -> None:
    """Create a new pyrgo project in an existing directory."""
    executed = ops.init.execute(
        app_config=app_config,
        project_name=name,
    )
    if not isinstance(executed, Ok):
        sys.exit(1)
    sys.exit(0)
