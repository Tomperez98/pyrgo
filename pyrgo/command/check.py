"""check command."""


import pathlib

import click

from pyrgo.utilities.command import PythonExecCommand, inform_and_run_program
from pyrgo.utilities.project import extract_relevent_paths, read_pyproject


@click.command()
def check() -> None:
    """Analyze the current package with `ruff` and `mypy`."""
    cwd = pathlib.Path().cwd()
    content = read_pyproject(cwd=cwd)
    relevant_paths = extract_relevent_paths(content=content)
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
