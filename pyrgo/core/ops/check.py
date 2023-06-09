"""check operation."""
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
    add_noqa: bool,
    ignore_noqa: bool,
    deamon_time_out: int,
    app_config: Config,
    typing: bool,
) -> Result[None, list[subprocess.CalledProcessError]]:
    """Execute check operation."""
    if typing:
        ruff_command = PythonExecCommand(
            program="ruff",
        )
        mypy_command = PythonExecCommand(
            program="mypy.dmypy",
        ).add_args(args=["run", "--timeout", str(deamon_time_out), "--"])

        if add_noqa:
            ruff_command.add_args(args=["--add-noqa"])
        if ignore_noqa:
            ruff_command.add_args(args=["--ignore-noqa"])

        for command in [ruff_command, mypy_command]:
            command.add_args(
                args=app_config.relevant_paths,
            )

        return inform_and_run_program(
            commands=[
                ruff_command,
                mypy_command,
            ],
        )

    ruff_command = PythonExecCommand(
        program="ruff",
    )

    if add_noqa:
        ruff_command.add_args(args=["--add-noqa"])
    if ignore_noqa:
        ruff_command.add_args(args=["--ignore-noqa"])

    for command in [ruff_command]:
        command.add_args(
            args=app_config.relevant_paths,
        )
    return inform_and_run_program(
        commands=[
            ruff_command,
        ],
    )
