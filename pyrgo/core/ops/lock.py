"""lock operation."""
from typing import List, Tuple

from result import Ok, Result

from pyrgo.core.config import Config
from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.utilities.command import inform_and_run_program
from pyrgo.core.utilities.text import path_to_lock_file


def execute(groups: Tuple[str], app_config: Config) -> Result[None, Exception]:
    """Execute lock operation."""
    app_config.requirements_path.relative_to(app_config.cwd)
    commands: List[PythonExecCommand] = []
    for group in groups:
        piptools_command = PythonExecCommand(program="piptools").add_args(
            args=["compile"],
        )
        if group != app_config.core_dependecies_name:
            piptools_command.add_args(args=["--extra", group])

        lock_file_path = path_to_lock_file(
            cwd=app_config.cwd,
            requirements_path=app_config.requirements_path,
            group=group,
            lock_file_format=app_config.lock_file_format,
        )
        piptools_command.add_args(
            args=[
                "--resolver=backtracking",
                "-o",
                lock_file_path,
                "pyproject.toml",
            ],
        )
        commands.append(piptools_command)

    inform_and_run_program(
        commands=commands,
    )

    return Ok()
