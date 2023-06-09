"""check command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.constants import app_config


@click.command()
@click.option(
    "-t",
    "--timeout",
    "timeout",
    default=360,
    type=click.IntRange(min=0, max=None, min_open=True),
    help="To automatically shutdown mypy deamon after n seconds of inactivity",
)
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
@click.option(
    "--typing/--no-typing",
    "typing",
    is_flag=True,
    default=True,
    type=bool,
    help="Check typing with mypy.",
)
def check(*, timeout: int, add_noqa: bool, ignore_noqa: bool, typing: bool) -> None:
    """Analyze the current package with `ruff` and `mypy`."""
    executed = ops.check.execute(
        add_noqa=add_noqa,
        ignore_noqa=ignore_noqa,
        deamon_time_out=timeout,
        app_config=app_config,
        typing=typing,
    )
    if not isinstance(executed, Ok):
        sys.exit(1)
    sys.exit(0)
