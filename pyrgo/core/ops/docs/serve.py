"""docs serve operation."""
from __future__ import annotations

from typing import TYPE_CHECKING

from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.utilities.command import inform_and_run_program

if TYPE_CHECKING:
    import subprocess

    from result import Result


def execute(
    *,
    dev_address: str,
    theme: str,
    strict: bool,
) -> Result[None, list[subprocess.CalledProcessError]]:
    """Execute docs serve operation."""
    serve_command = PythonExecCommand(
        program="mkdocs",
    ).add_args(
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

    return inform_and_run_program(
        commands=[serve_command],
    )
