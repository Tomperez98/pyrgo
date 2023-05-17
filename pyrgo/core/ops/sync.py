"""sync operation."""

import subprocess
from typing import List

from result import Result

from pyrgo.core.config import Config
from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.utilities.command import inform_and_run_program
from pyrgo.core.utilities.text import path_to_lock_file


def execute(
    *,
    environment: str,
    editable: bool,
    app_config: Config,
) -> Result[None, List[subprocess.CalledProcessError]]:
    """Execute sync operation."""
    piptools_command = PythonExecCommand(program="piptools")
    pip_command = PythonExecCommand(program="pip")

    lock_file_path = path_to_lock_file(
        cwd=app_config.cwd,
        requirements_path=app_config.requirements_path,
        group=environment,
        lock_file_format=app_config.lock_file_format,
    )

    piptools_command.add_args(
        args=[
            "sync",
            lock_file_path,
        ],
    )
    pip_command.add_args(
        args=[
            "install",
            "--no-deps",
        ],
    )
    if editable:
        pip_command.add_args(args=["-e"])

    pip_command.add_args(args=["."])

    return inform_and_run_program(
        commands=[
            piptools_command,
            pip_command,
        ],
    )
