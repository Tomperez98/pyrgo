"""build operation."""
from result import Ok, Result

from pyrgo.core.utilities.command import PythonExecCommand, inform_and_run_program


def execute() -> Result[None, Exception]:
    """Execute build operation."""
    inform_and_run_program(
        commands=[
            PythonExecCommand(program="build").add_args(
                args=[],
            ),
        ],
    )
    return Ok()
