"""venv operation."""
import pathlib

import click
from result import Ok, Result

from pyrgo.core.contants import VENV_ACTIVATION_MSG
from pyrgo.core.utilities.command import PythonExecCommand, inform_and_run_program


def create_virtual_env(venv_path: pathlib.Path) -> None:
    """Create a virtual enviroment folder."""
    inform_and_run_program(
        command=PythonExecCommand(program="venv").add_args(
            args=[
                venv_path.name,
            ],
        ),
    )


def execute(cwd: pathlib.Path) -> Result[None, Exception]:
    """Execute venv operation."""
    venv_path = cwd.joinpath(".venv")
    if venv_path.exists():
        if venv_path.is_dir():
            click.echo(
                message="Project already has a virtual enviroment located at `.venv`",
            )
        elif venv_path.is_file():
            venv_path.unlink(missing_ok=False)
            create_virtual_env(venv_path=venv_path)
    else:
        create_virtual_env(venv_path=venv_path)

    click.echo(message=VENV_ACTIVATION_MSG)
    return Ok()
