"""check operation."""
import subprocess
from typing import List

from result import Result

from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.models.config import Config
from pyrgo.core.utilities.command import inform_and_run_program


def execute(
    *,
    add_noqa: bool,
    ignore_noqa: bool,
    app_config: Config,
) -> Result[None, List[subprocess.CalledProcessError]]:
    """Execute check operation."""
    ruff_command = PythonExecCommand(
        program="ruff",
    )
    mypy_command = PythonExecCommand(
        program="mypy",
    )

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
