"""Cli utilitites."""
from typing import List

import click

from pyrgo.core.config import app_config


def add_commands(
    cli: click.Group,
    commands: List[click.Command],
) -> None:
    """Add commands to CLI group."""
    for command in commands:
        cli.add_command(cmd=command)


def dynamic_available_environments() -> List[str]:
    """Dynamic available environments in `requirements/`."""
    return [
        x.name.rstrip(f".{app_config.lock_file_format}")
        for x in app_config.requirements_path.glob(f"*.{app_config.lock_file_format}")
        if x.is_file()
    ]


def dynamic_marker_choices() -> List[str]:
    """Dynamic markers for options."""
    return app_config.pyproject_toml.list_pytest_markers()


def dynamic_group_choices() -> List[str]:
    """Dynamic markers for options."""
    return [
        app_config.core_dependecies_name,
        *app_config.pyproject_toml.extract_optional_dependencies().keys(),
    ]
