"""docs new operation."""
import pathlib

from result import Err, Ok, Result

from pyrgo.core.errors import PyProjectTOMLNotFoundError
from pyrgo.core.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)


def execute(*, cwd: pathlib.Path) -> Result[None, PyProjectTOMLNotFoundError]:
    """Execute docs new operation."""
    pyproject = cwd.joinpath("pyproject.toml")
    if not pyproject.exists():
        return Err(PyProjectTOMLNotFoundError(cwd=cwd))

    inform_and_run_program(
        command=PythonExecCommand(program="mkdocs").add_args(
            [
                "new",
                str(cwd),
            ],
        ),
    )
    return Ok()
