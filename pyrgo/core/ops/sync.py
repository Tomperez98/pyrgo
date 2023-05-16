"""sync operation."""

from result import Ok, Result

from pyrgo.core.config import Config
from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.utilities.command import inform_and_run_program


def execute(
    *,
    environment: str,
    editable: bool,
    app_config: Config,
) -> Result[None, Exception]:
    """Execute sync operation."""
    piptools_command = PythonExecCommand(program="piptools")
    pip_command = PythonExecCommand(program="pip")

    piptools_command.add_args(
        args=[
            "sync",
            "{requirements_path}/{environment}.{lock_file_format}".format(
                requirements_path=app_config.requirements_path,
                environment=environment,
                lock_file_format=app_config.lock_file_format,
            ),
        ],
    )
    pip_command.add_args(
        args=[
            "install",
            "--no-deps",
        ],
    )
    if editable:
        pip_command.add_args(args=["-e"])

    pip_command.add_args(args=["."])

    inform_and_run_program(
        commands=[
            piptools_command,
            pip_command,
        ],
    )
    return Ok()
