"""venv operation."""

import subprocess
from typing import List

import click
from result import Ok, Result

from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.models.config import Config
from pyrgo.core.utilities.command import inform_and_run_program


def execute(app_config: Config) -> Result[None, List[subprocess.CalledProcessError]]:
    """Execute venv operation."""
    venv_command = PythonExecCommand(
        program="venv",
    ).add_args(
        args=[
            app_config.venv_dir.name,
        ],
    )
    if app_config.venv_dir.exists():
        if app_config.venv_dir.is_dir():
            click.echo(
                message="Project already has a virtual enviroment located"
                f" at `{app_config.venv_dir.name}`",
            )
            return Ok()
        if app_config.venv_dir.is_file():
            app_config.venv_dir.unlink()
            return inform_and_run_program(
                commands=[venv_command],
            )
        raise RuntimeError

    if not app_config.venv_dir.exists():
        return inform_and_run_program(
            commands=[venv_command],
        )
    raise RuntimeError
