"""lock operation."""
import pathlib
from typing import Tuple

from result import Ok, Result

from pyrgo.core.contants import CORE_DEPENDENCIES_NAME
from pyrgo.core.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)


def execute(cwd: pathlib.Path, groups: Tuple[str]) -> Result[None, Exception]:
    """Execute lock operation."""
    req_path = cwd.joinpath("requirements")
    req_path.mkdir(
        parents=False,
        exist_ok=True,
    )
    only_req = req_path.relative_to(cwd)
    for group in groups:
        if group == CORE_DEPENDENCIES_NAME:
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

    return Ok()
