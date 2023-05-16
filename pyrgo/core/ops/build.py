"""build operation."""
from result import Ok, Result

from pyrgo.core.utilities.command import PythonExecCommand, inform_and_run_program


def execute() -> Result[None, Exception]:
    """Execute build operation."""
    build_command = PythonExecCommand(program="build")
    inform_and_run_program(
        commands=[build_command],
    )
    return Ok()
