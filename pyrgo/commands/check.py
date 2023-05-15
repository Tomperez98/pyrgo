"""check command."""


import pathlib

import click

from pyrgo.utilities.command import PythonExecCommand, inform_and_run_program
from pyrgo.utilities.project import Pyproject


@click.command()
def check() -> None:
    """Analyze the current package with `ruff` and `mypy`."""
    pyproject = Pyproject(cwd=pathlib.Path().cwd())
    pyproject.read_pyproject_toml()
    relevant_paths = pyproject.extract_relevant_paths(
        paths_type="all",
    )
    inform_and_run_program(
        command=PythonExecCommand(program="ruff").add_args(
            args=relevant_paths,
        ),
    )
    inform_and_run_program(
        command=PythonExecCommand(program="mypy").add_args(
            args=relevant_paths,
        ),
    )
