"""check operation."""

from result import Ok, Result

from pyrgo.core.config import Config
from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.utilities.command import inform_and_run_program


def execute(
    *,
    add_noqa: bool,
    ignore_noqa: bool,
    app_config: Config,
) -> Result[None, Exception]:
    """Execute check operation."""
    relevant_paths = app_config.pyproject_toml.extract_relevant_paths(paths_type="all")
    ruff_command = PythonExecCommand(program="ruff")
    mypy_command = PythonExecCommand(program="mypy")

    if add_noqa:
        ruff_command.add_args(args=["--add-noqa"])
    if ignore_noqa:
        ruff_command.add_args(args=["--ignore-noqa"])

    for command in [ruff_command, mypy_command]:
        command.add_args(
            args=relevant_paths,
        )

    inform_and_run_program(
        commands=[
            ruff_command,
            mypy_command,
        ],
    )
    return Ok()
