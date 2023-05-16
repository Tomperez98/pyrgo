"""fmt operation."""
from typing import List, Tuple

from result import Err, Ok, Result

from pyrgo.core.config import app_config
from pyrgo.core.models.pyproject import Pyproject
from pyrgo.core.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)


def execute() -> Result[None, Exception]:
    """Execute fmt operation."""
    pyproject = Pyproject()
    read_pyproject = pyproject.read_pyproject_toml(
        pyproject_path=app_config.pyproject_toml_path,
    )

    if not isinstance(read_pyproject, Ok):
        return Err(read_pyproject.err())

    relevant_paths = pyproject.extract_relevant_paths(paths_type="all")

    program_with_args: List[Tuple[str, List[str]]] = [
        ("ruff", ["--fix-only", *relevant_paths]),
        ("black", relevant_paths),
    ]

    commands: List[PythonExecCommand] = []
    for program, program_args in program_with_args:
        commands.append(
            PythonExecCommand(program=program).add_args(
                args=program_args,
            ),
        )

    inform_and_run_program(commands=commands)

    return Ok()
