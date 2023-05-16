"""docs new operation."""

from result import Ok, Result

from pyrgo.core.config import Config
from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.utilities.command import inform_and_run_program


def execute(app_config: Config) -> Result[None, Exception]:
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
