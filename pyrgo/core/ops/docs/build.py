"""docs build operation."""
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
    theme: str,
    strict: bool,
) -> Result[None, list[subprocess.CalledProcessError]]:
    """Execute docs build operation."""
    build_command = PythonExecCommand(
        program="mkdocs",
    ).add_args(
        args=[
            "build",
        ],
    )
    if strict:
        build_command.add_args(args=["--strict"])

    build_command.add_args(args=["--theme", theme])

    return inform_and_run_program(
        commands=[build_command],
    )
