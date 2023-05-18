"""Cli utilitites."""
from typing import List

import click


def add_commands(
    cli: click.Group,
    commands: List[click.Command],
) -> None:
    """Add commands to CLI group."""
    for command in commands:
        cli.add_command(cmd=command)
