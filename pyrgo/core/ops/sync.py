"""sync operation."""
from typing import List

from result import Ok, Result

from pyrgo.core.config import app_config
from pyrgo.core.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)


def execute(
    *,
    environment: str,
    editable: bool,
) -> Result[None, Exception]:
    """Execute sync operation."""
    inform_and_run_program(
        command=PythonExecCommand(program="piptools").add_args(
            args=[
                "sync",
                f"{app_config.requirements_path!s}/{environment}.lock",
            ],
        ),
    )

    project_install_args: List[str] = [
        "install",
        "--no-deps",
    ]

    if editable:
        project_install_args.append("-e")

    project_install_args.append(".")

    inform_and_run_program(
        command=PythonExecCommand(program="pip").add_args(
            args=project_install_args,
        ),
    )
    return Ok()
