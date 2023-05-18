"""fmt operation."""

import subprocess
from typing import List

from result import Result

from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.models.config import Config
from pyrgo.core.utilities.command import inform_and_run_program


def execute(app_config: Config) -> Result[None, List[subprocess.CalledProcessError]]:
    """Execute fmt operation."""
    ruff_command = PythonExecCommand(program="ruff").add_args(args=["--fix-only"])
    black_command = PythonExecCommand(program="black")

    for command in [ruff_command, black_command]:
        command.add_args(
            args=app_config.relevant_paths,
        )

    return inform_and_run_program(
        commands=[
            ruff_command,
            black_command,
        ],
    )
