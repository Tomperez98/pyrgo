"""test command."""

import sys
from typing import Optional

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.constants import app_config


@click.command()
@click.option(
    "-m",
    "--marked",
    "marker",
    type=click.Choice(
        choices=app_config.pytest_makers,
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
        sys.exit(1)
    sys.exit(0)
