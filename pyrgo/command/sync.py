"""sync command."""
import pathlib
import sys
from typing import List, Optional

import click

from pyrgo.utilities.command import (
    PythonExecCommand,
    colorize_text,
    inform_and_run_program,
)


def dynamic_available_environments() -> List[str]:
    """Dynamic available environments in `requirements/`."""
    cwd = pathlib.Path().cwd()
    req_path = cwd.joinpath("requirements")
    wanted_prefix = ".lock"
    if not req_path.exists():
        click.echo(
            colorize_text(
                text="No folder `requirements/`. Use `pyrgo lock` first",
                color="red",
            ),
        )
        sys.exit(1)
    content = req_path.glob(f"*{wanted_prefix}")
    return [x.name.removesuffix(wanted_prefix) for x in content if x.is_file()]


@click.command()
@click.option(
    "-g",
    "--group",
    "group",
    type=click.Choice(choices=dynamic_available_environments()),
    default=None,
    help="Sync to one of available enviroments.",
)
@click.option(
    "--editable/--no-editable",
    "editable",
    type=bool,
    default=True,
    help="Install current project as editable after sync.",
)
def sync(*, group: Optional[str], editable: bool) -> None:
    """Synchronize virtual environment with requirements.txt."""
    cwd = pathlib.Path().cwd()

    req_path = cwd.joinpath("requirements")
    inform_and_run_program(
        command=PythonExecCommand(program="piptools").add_args(
            args=[
                "sync",
                f"{req_path!s}/{group}.lock",
            ],
        ),
    )
    if editable:
        inform_and_run_program(
            command=PythonExecCommand(program="pip").add_args(
                args=[
                    "install",
                    "-e",
                    ".",
                ],
            ),
        )
        sys.exit(0)
    else:
        inform_and_run_program(
            command=PythonExecCommand(program="pip").add_args(
                args=[
                    "install",
                    ".",
                ],
            ),
        )
        sys.exit(0)
