"""venv operation."""

import click
from result import Ok, Result

from pyrgo.core.config import app_config
from pyrgo.core.utilities.command import PythonExecCommand, inform_and_run_program


def execute() -> Result[None, Exception]:
    """Execute venv operation."""
    venv_command = PythonExecCommand(program="venv").add_args(
        args=[
            app_config.venv_path.name,
        ],
    )
    if app_config.venv_path.exists():
        if app_config.venv_path.is_dir():
            click.echo(
                message="Project already has a virtual enviroment located at `.venv`",
            )
        elif app_config.venv_path.is_file():
            app_config.venv_path.unlink()
            inform_and_run_program(
                commands=[venv_command],
            )

    else:
        inform_and_run_program(
            commands=[venv_command],
        )

    click.echo(
        message=app_config.venv_activation_msg,
    )
    return Ok()
