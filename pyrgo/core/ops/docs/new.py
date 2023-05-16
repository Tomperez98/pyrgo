"""docs new operation."""

from result import Ok, Result

from pyrgo.core.config import app_config
from pyrgo.core.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)


def execute() -> Result[None, Exception]:
    """Execute docs new operation."""
    new_command = PythonExecCommand(program="mkdocs").add_args(
        args=[
            "new",
        ],
    )
    new_command.add_args(args=[str(app_config.cwd)])
    inform_and_run_program(
        commands=[new_command],
    )
    return Ok()
