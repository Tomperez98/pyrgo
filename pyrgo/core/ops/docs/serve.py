"""docs serve operation."""
from typing import List

from result import Ok, Result

from pyrgo.core.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)


def execute(*, dev_address: str, theme: str, strict: bool) -> Result[None, Exception]:
    """Execute docs serve operation."""
    command_args: List[str] = ["serve"]
    if strict:
        command_args.append("--strict")

    command_args.extend(["--theme", theme])
    command_args.extend(["--dev-addr", dev_address])
    inform_and_run_program(
        command=PythonExecCommand(
            program="mkdocs",
        ).add_args(
            args=command_args,
        ),
    )
    return Ok()
