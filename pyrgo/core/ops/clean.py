"""clean operation."""
from __future__ import annotations

import itertools
import shutil
from typing import TYPE_CHECKING

from result import Ok, Result

from pyrgo.core.models.command import PythonExecCommand
from pyrgo.core.utilities.command import inform_and_run_program

if TYPE_CHECKING:
    from pyrgo.core.models.config import Config


def execute(app_config: Config) -> Result[None, Exception]:
    """Execute clean operation."""
    for to_be_clean in itertools.chain(
        app_config.caches,
        app_config.artifacts,
    ):
        if to_be_clean.exists() and to_be_clean.is_dir():
            shutil.rmtree(to_be_clean)

    for relevant_path in app_config.relevant_paths:
        for pycaches in app_config.cwd.joinpath(relevant_path).rglob(
            pattern="__pycache__",
        ):
            shutil.rmtree(pycaches)

    for env_not_as_opt_dep in set(app_config.available_envs).difference(
        set(app_config.dependency_groups),
    ):
        app_config.requirements_dir.joinpath(
            f"{env_not_as_opt_dep}.{app_config.lock_file_format}",
        ).unlink()

    mypy_deamon_command = PythonExecCommand(
        program="mypy.dmypy",
    )
    mypy_deamon_command.add_args(args=["stop"])
    inform_and_run_program(
        commands=[
            mypy_deamon_command,
        ],
    )

    return Ok()
