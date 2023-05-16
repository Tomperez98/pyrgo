"""check operation."""
from typing import List, Tuple

from result import Ok, Result

from pyrgo.core.config import app_config
from pyrgo.core.utilities.command import PythonExecCommand, inform_and_run_program


def execute(
    *,
    add_noqa: bool,
    ignore_noqa: bool,
) -> Result[None, Exception]:
    """Execute check operation."""
    relevant_paths = app_config.pyproject_toml.extract_relevant_paths(
        paths_type="all",
    )
    ruff_args: List[str] = []
    if add_noqa:
        ruff_args.append("--add-noqa")
    if ignore_noqa:
        ruff_args.append("--ignore-noqa")

    ruff_args.extend(relevant_paths)

    program_with_args: List[Tuple[str, List[str]]] = [
        ("ruff", ruff_args),
        ("mypy", relevant_paths),
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
