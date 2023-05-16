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
    commands: List[PythonExecCommand] = []

    commands.append(
        PythonExecCommand(program="piptools").add_args(
            args=[
                "sync",
                f"{app_config.requirements_path!s}/{environment}{app_config.lock_file_format}",
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

    commands.append(
        PythonExecCommand(program="pip").add_args(
            args=project_install_args,
        ),
    )
    inform_and_run_program(
        commands=commands,
    )
    return Ok()
