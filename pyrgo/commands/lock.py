"""lock command."""
import pathlib
import sys
from typing import List, Tuple

import click

from pyrgo.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)
from pyrgo.utilities.project import Pyproject


def dynamic_group_choices() -> List[str]:
    """Dynamic markers for options."""
    pyproject = Pyproject(cwd=pathlib.Path().cwd())
    pyproject.read_pyproject_toml()
    return list(pyproject.extract_optional_dependencies().keys())


@click.command()
@click.option(
    "-g",
    "--group",
    "groups",
    type=click.Choice(choices=dynamic_group_choices()),
    multiple=True,
    default=None,
    help="Name of an extras_require group to install.\n"
    "By default only core requirements.",
)
def lock(groups: Tuple[str]) -> None:
    """Lock dependencies using `piptools`."""
    cwd = pathlib.Path().cwd()

    req_path = cwd.joinpath("requirements")
    req_path.mkdir(
        parents=False,
        exist_ok=True,
    )

    if not groups:
        inform_and_run_program(
            command=PythonExecCommand(program="piptools").add_args(
                args=[
                    "compile",
                    "--resolver=backtracking",
                    "-o",
                    f"{req_path!s}/core.lock",
                    "pyproject.toml",
                ],
            ),
        )
        sys.exit(0)

    for group in groups:
        inform_and_run_program(
            command=PythonExecCommand(program="piptools").add_args(
                args=[
                    "compile",
                    "--extra",
                    group,
                    "--resolver=backtracking",
                    "-o",
                    f"{req_path!s}/{group}.lock",
                    "pyproject.toml",
                ],
            ),
        )

    sys.exit(0)
