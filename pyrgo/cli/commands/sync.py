"""sync command."""
import pathlib
import sys
from typing import List

import click
from result import Ok

from pyrgo.core import ops
from pyrgo.core.utilities.text import colorize_text


def dynamic_available_environments() -> List[str]:
    """Dynamic available environments in `requirements/`."""
    cwd = pathlib.Path().cwd()
    req_path = cwd.joinpath("requirements")
    wanted_prefix = ".lock"
    if not req_path.exists():
        click.echo(
            colorize_text(
                text="No folder `requirements/`.",
                color="red",
            ),
        )
        sys.exit(1)

    return [
        x.name.rstrip(wanted_prefix)
        for x in req_path.glob(f"*{wanted_prefix}")
        if x.is_file()
    ]


@click.command()
@click.option(
    "-env",
    "--environment",
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
    cwd = pathlib.Path().cwd()
    executed = ops.sync.execute(
        cwd=cwd,
        environment=environment,
        editable=editable,
    )
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)

    sys.exit(0)
