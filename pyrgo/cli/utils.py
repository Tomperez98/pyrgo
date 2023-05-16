"""Cli utilitites."""
import pathlib
import sys
from typing import List

import click

from pyrgo.core.utilities.text import colorize_text


def add_commands(
    cli: click.Group,
    commands: List[click.Command],
) -> None:
    """Add commands to CLI group."""
    for command in commands:
        cli.add_command(cmd=command)


def dynamic_available_environments() -> List[str]:
    """Dynamic available environments in `requirements/`."""
    cwd = pathlib.Path().cwd()
    req_path = cwd.joinpath("requirements")
    wanted_prefix = ".lock"
    if not req_path.exists():
        click.echo(
            colorize_text(
                text="No folder `requirements/`.",
                color="red",
            ),
        )
        sys.exit(1)

    return [
        x.name.rstrip(wanted_prefix)
        for x in req_path.glob(f"*{wanted_prefix}")
        if x.is_file()
    ]
