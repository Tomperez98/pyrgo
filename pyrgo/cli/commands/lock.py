"""lock command."""
import sys
from typing import Tuple

import click
from result import Ok

from pyrgo.cli.utils import dynamic_group_choices
from pyrgo.core import ops


@click.command()
@click.option(
    "-g",
    "--group",
    "groups",
    type=click.Choice(choices=dynamic_group_choices()),
    multiple=True,
    required=True,
    help="Name of an extras_require group to install; may be used more than once",
)
def lock(groups: Tuple[str]) -> None:
    """Lock dependencies using `piptools`."""
    executed = ops.lock.execute(groups=groups)
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)
    sys.exit(0)
