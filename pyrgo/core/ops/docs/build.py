"""docs build operation."""

from typing import List

from result import Ok, Result

from pyrgo.core.utilities.command import PythonExecCommand, inform_and_run_program


def execute(
    *,
    theme: str,
    strict: bool,
) -> Result[None, Exception]:
    """Execute docs build operation."""
    command_args: List[str] = ["build"]
    if strict:
        command_args.append("--strict")

    command_args.extend(["--theme", theme])

    inform_and_run_program(
        command=PythonExecCommand(
            program="mkdocs",
        ).add_args(
            args=command_args,
        ),
    )
    return Ok()
