"""Cli utilitites."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import click


def add_commands(
    cli: click.Group,
    commands: list[click.Command],
) -> None:
    """Add commands to CLI group."""
    for command in commands:
        cli.add_command(cmd=command)
