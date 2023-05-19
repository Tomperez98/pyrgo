"""lock command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.constants import app_config


@click.command()
@click.option(
    "-g",
    "--group",
    "groups",
    type=click.Choice(choices=app_config.dependency_groups),
    multiple=True,
    required=False,
    help="Name of an extras_require group to install; may be used more than once",
)
@click.option(
    "--generate-hashes",
    "generate_hashes",
    is_flag=True,
    default=False,
    show_default=True,
    help="Generate pip 8 style hashes in the resulting requirements file.",
)
def lock(*, groups: tuple[str, ...], generate_hashes: bool) -> None:
    """Lock dependencies using `piptools`."""
    executed = ops.lock.execute(
        groups=groups,
        app_config=app_config,
        generate_hashes=generate_hashes,
    )
    if not isinstance(executed, Ok):
        sys.exit(1)
    sys.exit(0)
