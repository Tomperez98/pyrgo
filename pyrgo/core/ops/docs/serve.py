"""docs serve operation."""

import subprocess
from typing import List

from result import Result

from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.utilities.command import inform_and_run_program


def execute(
    *,
    dev_address: str,
    theme: str,
    strict: bool,
) -> Result[None, List[subprocess.CalledProcessError]]:
    """Execute docs serve operation."""
    serve_command = PythonExecCommand(program="mkdocs").add_args(
        args=[
            "serve",
        ],
    )
    if strict:
        serve_command.add_args(args=["--strict"])

    serve_command.add_args(
        args=[
            "--theme",
            theme,
            "--dev-addr",
            dev_address,
        ],
    )

    return inform_and_run_program(
        commands=[serve_command],
    )
