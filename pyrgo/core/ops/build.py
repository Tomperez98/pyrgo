"""build operation."""
from __future__ import annotations

from typing import TYPE_CHECKING

from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.utilities.command import inform_and_run_program

if TYPE_CHECKING:
    import subprocess

    from result import Result

    from pyrgo.core.models.config import Config


def execute(app_config: Config) -> Result[None, list[subprocess.CalledProcessError]]:
    """Execute build operation."""
    build_command = PythonExecCommand(
        program="build",
    )
    build_command.add_args(
        args=[
            app_config.cwd.as_posix(),
        ],
    )
    return inform_and_run_program(
        commands=[
            build_command,
        ],
    )
