"""lock operation."""
from __future__ import annotations

from typing import TYPE_CHECKING, Iterable

from pyrgo.core.models.command import (
    PythonExecCommand,
)
from pyrgo.core.utilities.command import inform_and_run_program
from pyrgo.core.utilities.text import path_to_lock_file

if TYPE_CHECKING:
    import subprocess

    from result import Result

    from pyrgo.core.models.config import Config


def execute(
    *,
    groups: Iterable[str],
    app_config: Config,
    generate_hashes: bool,
) -> Result[None, list[subprocess.CalledProcessError]]:
    """Execute lock operation."""
    app_config.requirements_dir.relative_to(app_config.cwd)
    commands: list[PythonExecCommand] = []

    if not groups:
        groups = app_config.dependency_groups

    for group in groups:
        piptools_command = PythonExecCommand(
            program="piptools",
        ).add_args(
            args=[
                "compile",
            ],
        )

        if group != app_config.core_deps_alias:
            piptools_command.add_args(
                args=[
                    "--extra",
                    group,
                ],
            )

        lock_file_path = path_to_lock_file(
            cwd=app_config.cwd,
            requirements_path=app_config.requirements_dir,
            group=group,
            lock_file_format=app_config.lock_file_format,
        )
        if generate_hashes:
            piptools_command.add_args(
                args=[
                    "--generate-hashes",
                ],
            )

        piptools_command.add_args(
            args=[
                "--resolver=backtracking",
                "-o",
                lock_file_path,
                "pyproject.toml",
            ],
        )
        commands.append(piptools_command)

    return inform_and_run_program(
        commands=commands,
    )
