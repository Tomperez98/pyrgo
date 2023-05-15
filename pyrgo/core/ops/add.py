"""Add operation."""

import pathlib

from result import Err, Ok, Result

from pyrgo.core.contants import CORE_DEPENDENCIES_NAME
from pyrgo.core.models.pyproject import Pyproject
from pyrgo.core.utilities.command import PythonExecCommand, inform_and_run_program


def execute(
    cwd: pathlib.Path,
    new_dependency: str,
    group: str,
) -> Result[None, Exception]:
    """Execute add operation."""
    inform_and_run_program(
        command=PythonExecCommand(program="pip").add_args(
            [
                "install",
                new_dependency,
            ],
        ),
    )
    pyproject = Pyproject(cwd=cwd)
    read_pyproject = pyproject.read_pyproject_toml()
    if not pyproject.data:
        raise RuntimeError

    if not isinstance(read_pyproject, Ok):
        return Err(read_pyproject.err())

    pyproject.project_section()
    if group == CORE_DEPENDENCIES_NAME:
        ...
    else:
        ...

    return Ok()
