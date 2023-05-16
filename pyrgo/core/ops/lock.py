"""lock operation."""
from typing import List, Tuple

from result import Ok, Result

from pyrgo.core.config import app_config
from pyrgo.core.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)


def execute(groups: Tuple[str]) -> Result[None, Exception]:
    """Execute lock operation."""
    only_req = app_config.requirements_path.relative_to(app_config.cwd)
    commands: List[PythonExecCommand] = []
    for group in groups:
        if group == app_config.core_dependecies_name:
            commands.append(
                PythonExecCommand(program="piptools").add_args(
                    args=[
                        "compile",
                        "--resolver=backtracking",
                        "-o",
                        f"{only_req!s}/{group}.{app_config.lock_file_format}",
                        "pyproject.toml",
                    ],
                ),
            )

        else:
            commands.append(
                PythonExecCommand(program="piptools").add_args(
                    args=[
                        "compile",
                        "--extra",
                        group,
                        "--resolver=backtracking",
                        "-o",
                        f"{only_req!s}/{group}.{app_config.lock_file_format}",
                        "pyproject.toml",
                    ],
                ),
            )

    inform_and_run_program(
        commands=commands,
    )

    return Ok()
