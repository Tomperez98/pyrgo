"""test operation."""
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


def execute(
    *,
    marker: str | None,
    app_config: Config,
) -> Result[None, list[subprocess.CalledProcessError]]:
    """Execute test operation."""
    pytest_command = PythonExecCommand(
        program="pytest",
    )
    if marker:
        pytest_command.add_args(
            args=[
                "-m",
                marker,
            ],
        )

    pytest_command.add_args(args=app_config.pytest_paths)
    return inform_and_run_program(
        commands=[
            pytest_command,
        ],
    )
