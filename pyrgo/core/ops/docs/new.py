"""docs new operation."""

from result import Ok, Result

from pyrgo.core.config import app_config
from pyrgo.core.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)


def execute() -> Result[None, Exception]:
    """Execute docs new operation."""
    inform_and_run_program(
        commands=[
            PythonExecCommand(program="mkdocs").add_args(
                [
                    "new",
                    str(app_config.cwd),
                ],
            ),
        ],
    )
    return Ok()
