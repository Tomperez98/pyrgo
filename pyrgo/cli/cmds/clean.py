"""Clean command."""
from __future__ import annotations

import itertools
import shutil
import sys

import click
from result import Ok

from pyrgo.cli.utils import inform_and_run_program
from pyrgo.core import PyrgoConf, PythonCommandExec


@click.command("clean")
def clean() -> None:
    """Clean project repository."""
    config = PyrgoConf.new()
    for folder in itertools.chain(config.artifacts, config.caches):
        if folder.exists():
            if folder.is_dir():
                shutil.rmtree(path=folder)
            else:
                folder.unlink()

    for path in config.relevant_paths:
        for pycache in config.cwd.joinpath(path).rglob(pattern="__pycache__"):
            shutil.rmtree(pycache)

    for outdated_file in config.locked_envs().difference(config.env_groups):
        config.requirements.joinpath(f"{outdated_file}.txt").unlink()

    program_execution = inform_and_run_program(
        commands=[
            PythonCommandExec.new(
                program="mypy.dmypy",
            ).add_args(args=["stop"])
        ],
    )
    if not isinstance(program_execution, Ok):
        sys.exit(1)
    sys.exit(0)
