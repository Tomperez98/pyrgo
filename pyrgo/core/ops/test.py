"""test operation."""
import subprocess
from typing import List, Optional

from result import Result

from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.models.config import Config
from pyrgo.core.utilities.command import inform_and_run_program


def execute(
    *,
    marker: Optional[str],
    app_config: Config,
) -> Result[None, List[subprocess.CalledProcessError]]:
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
