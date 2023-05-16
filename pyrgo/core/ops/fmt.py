"""fmt operation."""

from result import Ok, Result

from pyrgo.core.config import Config
from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.utilities.command import inform_and_run_program


def execute(app_config: Config) -> Result[None, Exception]:
    """Execute fmt operation."""
    relevant_paths = app_config.pyproject_toml.extract_relevant_paths(paths_type="all")
    ruff_command = PythonExecCommand(program="ruff").add_args(args=["--fix-only"])
    black_command = PythonExecCommand(program="black")

    for command in [ruff_command, black_command]:
        command.add_args(
            args=relevant_paths,
        )

    inform_and_run_program(
        commands=[
            ruff_command,
            black_command,
        ],
    )

    return Ok()
