"""venv operation."""
import pathlib

import click
from result import Ok, Result

from pyrgo.core.config import app_config
from pyrgo.core.utilities.command import PythonExecCommand, inform_and_run_program


def create_virtual_env(venv_path: pathlib.Path) -> None:
    """Create a virtual enviroment folder."""
    inform_and_run_program(
        commands=[
            PythonExecCommand(program="venv").add_args(
                args=[
                    venv_path.name,
                ],
            ),
        ],
    )


def execute() -> Result[None, Exception]:
    """Execute venv operation."""
    if app_config.venv_path.exists():
        if app_config.venv_path.is_dir():
            click.echo(
                message="Project already has a virtual enviroment located at `.venv`",
            )
        elif app_config.venv_path.is_file():
            app_config.venv_path.unlink()
            create_virtual_env(venv_path=app_config.venv_path)
    else:
        create_virtual_env(venv_path=app_config.venv_path)

    click.echo(message=app_config.venv_activation_msg)
    return Ok()
