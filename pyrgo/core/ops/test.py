"""test operation."""
from typing import List, Optional

from result import Ok, Result

from pyrgo.core.utilities.command import PythonExecCommand, inform_and_run_program


def execute(*, marker: Optional[str]) -> Result[None, Exception]:
    """Execute test operation."""
    command_args: List[str] = []
    if marker:
        command_args.extend(["-m", marker])

    inform_and_run_program(
        commands=[
            PythonExecCommand(program="pytest").add_args(
                args=command_args,
            ),
        ],
    )
    return Ok()
