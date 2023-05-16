"""test operation."""
from typing import Optional

from result import Ok, Result

from pyrgo.core.utilities.command import PythonExecCommand, inform_and_run_program


def execute(*, marker: Optional[str]) -> Result[None, Exception]:
    """Execute test operation."""
    pytest_command = PythonExecCommand(program="pytest")
    if marker:
        pytest_command.add_args(args=["-m", marker])

    inform_and_run_program(
        commands=[
            pytest_command,
        ],
    )
    return Ok()
