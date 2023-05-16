"""Cli utilitites."""
from typing import List

import click

from pyrgo.core.config import app_config
from pyrgo.core.models.pyproject import Pyproject


def add_commands(
    cli: click.Group,
    commands: List[click.Command],
) -> None:
    """Add commands to CLI group."""
    for command in commands:
        cli.add_command(cmd=command)


def dynamic_available_environments() -> List[str]:
    """Dynamic available environments in `requirements/`."""
    wanted_prefix = ".lock"
    return [
        x.name.rstrip(wanted_prefix)
        for x in app_config.requirements_path.glob(f"*{wanted_prefix}")
        if x.is_file()
    ]


def dynamic_marker_choices() -> List[str]:
    """Dynamic markers for options."""
    pyproject = Pyproject()
    pyproject.read_pyproject_toml(pyproject_path=app_config.pyproject_toml_path)
    return pyproject.list_pytest_markers()
