"""check command."""


import sys

import click
from result import Ok

from pyrgo.core import ops


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
    )
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)

    sys.exit(0)
