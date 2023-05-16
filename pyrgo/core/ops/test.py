"""test operation."""
from typing import List, Optional

from result import Ok, Result

from pyrgo.core.utilities.command import PythonExecCommand, inform_and_run_program


def execute(*, marker: Optional[str]) -> Result[None, Exception]:
    """Execute test operation."""
    base_command = PythonExecCommand(program="pytest")
    command_args: List[str] = []
    if marker:
        command_args.extend(["-m", marker])

    if command_args:
        base_command.add_args(command_args)

    inform_and_run_program(
        commands=[base_command],
    )
    return Ok()
