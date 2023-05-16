"""test command."""

import sys
from typing import Optional

import click
from result import Ok

from pyrgo.cli.utils import dynamic_marker_choices
from pyrgo.core import ops
from pyrgo.core.config import app_config


@click.command()
@click.option(
    "-m",
    "--marked",
    "marker",
    type=click.Choice(
        choices=dynamic_marker_choices(),
    ),
    default=None,
    help="Run tests based on marks. By default all tests are executed.",
)
def test(
    *,
    marker: Optional[str],
) -> None:
    """Execute tests using `pytest`."""
    executed = ops.test.execute(
        marker=marker,
        app_config=app_config,
    )
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)
    sys.exit(0)
