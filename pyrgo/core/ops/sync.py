"""sync operation."""
import pathlib

from result import Err, Ok, Result

from pyrgo.core.errors import RequirementsFolderNotFoundError
from pyrgo.core.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)


def execute(
    *,
    cwd: pathlib.Path,
    environment: str,
    editable: bool,
) -> Result[None, RequirementsFolderNotFoundError]:
    """Execute sync operation."""
    req_path = cwd.joinpath("requirements")
    if not req_path.exists() and req_path.is_dir():
        return Err(RequirementsFolderNotFoundError(cwd=cwd))

    inform_and_run_program(
        command=PythonExecCommand(program="piptools").add_args(
            args=[
                "sync",
                f"{req_path!s}/{environment}.lock",
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
    else:
        inform_and_run_program(
            command=PythonExecCommand(program="pip").add_args(
                args=[
                    "install",
                    ".",
                ],
            ),
        )
    return Ok()
