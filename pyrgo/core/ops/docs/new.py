"""docs new operation."""

import subprocess
from typing import List

from result import Result

from pyrgo.core.config import Config
from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.utilities.command import inform_and_run_program


def execute(app_config: Config) -> Result[None, List[subprocess.CalledProcessError]]:
    """Execute docs new operation."""
    new_command = PythonExecCommand(program="mkdocs").add_args(
        args=[
            "new",
        ],
    )
    new_command.add_args(args=[str(app_config.cwd)])
    return inform_and_run_program(
        commands=[new_command],
    )
