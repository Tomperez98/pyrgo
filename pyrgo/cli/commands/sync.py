"""sync command."""
import sys

import click
from result import Ok

from pyrgo.cli.utils import dynamic_available_environments
from pyrgo.core import ops
from pyrgo.core.config import app_config


@click.command()
@click.option(
    "-e",
    "--env",
    "environment",
    type=click.Choice(choices=dynamic_available_environments()),
    required=True,
    help="Sync to one of available enviroments.",
)
@click.option(
    "--editable/--no-editable",
    "editable",
    type=bool,
    default=True,
    help="Wheter or not to install current project in editable mode.\n"
    "Defaults to `true`",
)
def sync(*, environment: str, editable: bool) -> None:
    """Synchronize virtual environment with requirements.txt."""
    executed = ops.sync.execute(
        environment=environment,
        editable=editable,
        app_config=app_config,
    )
    if not isinstance(executed, Ok):
        sys.exit(1)
    sys.exit(0)
