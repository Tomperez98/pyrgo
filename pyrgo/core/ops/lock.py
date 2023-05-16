"""lock operation."""
from typing import Tuple

from result import Ok, Result

from pyrgo.core.config import app_config
from pyrgo.core.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)


def execute(groups: Tuple[str]) -> Result[None, Exception]:
    """Execute lock operation."""
    app_config.requirements_path.mkdir(
        parents=False,
        exist_ok=True,
    )
    only_req = app_config.requirements_path.relative_to(app_config.cwd)
    for group in groups:
        if group == app_config.core_dependecies_name:
            inform_and_run_program(
                command=PythonExecCommand(program="piptools").add_args(
                    args=[
                        "compile",
                        "--resolver=backtracking",
                        "-o",
                        f"{only_req!s}/{group}.lock",
                        "pyproject.toml",
                    ],
                ),
            )
        else:
            inform_and_run_program(
                command=PythonExecCommand(program="piptools").add_args(
                    args=[
                        "compile",
                        "--extra",
                        group,
                        "--resolver=backtracking",
                        "-o",
                        f"{only_req!s}/{group}.lock",
                        "pyproject.toml",
                    ],
                ),
            )

    return Ok()
