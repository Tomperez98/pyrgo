"""build operation."""
from result import Ok, Result

from pyrgo.core.config import Config
from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.utilities.command import inform_and_run_program


def execute(app_config: Config) -> Result[None, Exception]:
    """Execute build operation."""
    build_command = PythonExecCommand(program="build")
    build_command.add_args(
        args=[
            str(app_config.cwd),
        ],
    )
    inform_and_run_program(
        commands=[build_command],
    )
    return Ok()
