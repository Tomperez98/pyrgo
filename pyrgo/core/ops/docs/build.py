"""docs build operation."""


from result import Ok, Result

from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.utilities.command import inform_and_run_program


def execute(
    *,
    theme: str,
    strict: bool,
) -> Result[None, Exception]:
    """Execute docs build operation."""
    build_command = PythonExecCommand(program="mkdocs").add_args(
        args=[
            "build",
        ],
    )
    if strict:
        build_command.add_args(args=["--strict"])

    build_command.add_args(args=["--theme", theme])

    inform_and_run_program(
        commands=[build_command],
    )
    return Ok()
