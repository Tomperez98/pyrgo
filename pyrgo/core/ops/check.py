"""check operation."""
import pathlib
from typing import List, Tuple

from result import Err, Ok, Result

from pyrgo.core.models.pyproject import Pyproject
from pyrgo.core.utilities.command import PythonExecCommand, inform_and_run_program


def execute(
    *,
    cwd: pathlib.Path,
    add_noqa: bool,
    ignore_noqa: bool,
) -> Result[None, Exception]:
    """Execute check operation."""
    pyproject = Pyproject(cwd=cwd)
    read_pyproject = pyproject.read_pyproject_toml()

    if not isinstance(read_pyproject, Ok):
        return Err(read_pyproject.err())

    relevant_paths = pyproject.extract_relevant_paths(
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

    for program, program_args in program_with_args:
        inform_and_run_program(
            command=PythonExecCommand(program=program).add_args(
                args=program_args,
            ),
        )

    return Ok()
