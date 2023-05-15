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
    return ["core", *pyproject.extract_optional_dependencies().keys()]


@click.command()
@click.option(
    "-g",
    "--group",
    "groups",
    type=click.Choice(choices=dynamic_group_choices()),
    multiple=True,
    required=True,
    help="Name of an extras_require group to install.",
)
def lock(groups: Tuple[str]) -> None:
    """Lock dependencies using `piptools`."""
    cwd = pathlib.Path().cwd()
    req_path = cwd.joinpath("requirements")
    req_path.mkdir(
        parents=False,
        exist_ok=True,
    )

    only_req = req_path.relative_to(cwd)

    for group in groups:
        if group == "core":
            inform_and_run_program(
                command=PythonExecCommand(program="piptools").add_args(
                    args=[
                        "compile",
                        "--resolver=backtracking",
                        "-o",
                        f"{only_req!s}/{group}.lock",
                        "pyproject.toml",
                    ],
                ),
            )
        else:
            inform_and_run_program(
                command=PythonExecCommand(program="piptools").add_args(
                    args=[
                        "compile",
                        "--extra",
                        group,
                        "--resolver=backtracking",
                        "-o",
                        f"{only_req!s}/{group}.lock",
                        "pyproject.toml",
                    ],
                ),
            )

    sys.exit(0)
