"""docs serve operation."""

from result import Ok, Result

from pyrgo.core.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)


def execute(*, dev_address: str, theme: str, strict: bool) -> Result[None, Exception]:
    """Execute docs serve operation."""
    serve_command = PythonExecCommand(program="mkdocs").add_args(
        args=[
            "serve",
        ],
    )
    if strict:
        serve_command.add_args(args=["--strict"])

    serve_command.add_args(
        args=[
            "--theme",
            theme,
            "--dev-addr",
            dev_address,
        ],
    )

    inform_and_run_program(
        commands=[serve_command],
    )
    return Ok()
