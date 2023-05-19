"""check command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.constants import app_config


@click.command()
@click.option(
    "--add-noqa",
    "add_noqa",
    is_flag=True,
    default=False,
    type=bool,
    help="Enable automatic additions of `noqa` directives to failing lines",
)
@click.option(
    "--ignore-noqa",
    "ignore_noqa",
    is_flag=True,
    default=False,
    type=bool,
    help="Ignore any `# noqa` comments",
)
def check(*, add_noqa: bool, ignore_noqa: bool) -> None:
    """Analyze the current package with `ruff` and `mypy`."""
    executed = ops.check.execute(
        add_noqa=add_noqa,
        ignore_noqa=ignore_noqa,
        app_config=app_config,
    )
    if not isinstance(executed, Ok):
        sys.exit(1)
    sys.exit(0)
