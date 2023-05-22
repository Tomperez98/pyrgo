"""audit operation."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import subprocess

    from result import Result

    from pyrgo.core.models.config import Config

from pyrgo.core.models.command import PythonExecCommand
from pyrgo.core.utilities.command import inform_and_run_program
from pyrgo.core.utilities.text import path_to_lock_file


def execute(
    *,
    app_config: Config,
    environment: str,
    fix: bool,
) -> Result[None, list[subprocess.CalledProcessError]]:
    """Execute audit operation."""
    pipaudit_command = PythonExecCommand(
        program="pip_audit",
    )

    lock_file_path = path_to_lock_file(
        cwd=app_config.cwd,
        requirements_path=app_config.requirements_dir,
        group=environment,
        lock_file_format=app_config.lock_file_format,
    )

    pipaudit_command.add_args(
        args=[
            "-r",
            lock_file_path,
            "-l",
            "--desc",
        ],
    )
    if fix:
        pipaudit_command.add_args(
            args=[
                "--fix",
            ],
        )

    return inform_and_run_program(
        commands=[
            pipaudit_command,
        ],
    )
