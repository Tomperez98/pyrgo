"""fmt operation."""
from typing import List, Tuple

from result import Ok, Result

from pyrgo.core.config import app_config
from pyrgo.core.utilities.command import (
    PythonExecCommand,
    inform_and_run_program,
)


def execute() -> Result[None, Exception]:
    """Execute fmt operation."""
    relevant_paths = app_config.pyproject_toml.extract_relevant_paths(paths_type="all")

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

    inform_and_run_program(
        commands=commands,
    )

    return Ok()
