"""Test command models."""
from __future__ import annotations

import itertools
import sys

import pytest

from pyrgo.core.models.command import PythonExecCommand


@pytest.mark.integration()
def test_execute_command() -> None:
    """Test execute command."""
    PythonExecCommand(program="ruff").add_args(
        args=["--version"],
    ).run()


@pytest.mark.unit()
@pytest.mark.parametrize(
    argnames=["program", "commands"],
    argvalues=[
        (
            "program",
            [
                ["command-1", "command-2"],
            ],
        ),
        (
            "program",
            [
                ["command-1"],
                ["command-2"],
            ],
        ),
    ],
)
def test_args_building(program: str, commands: list[list[str]]) -> None:
    """Test args building works as expected."""
    command = PythonExecCommand(program=program)
    for set_of_commands in commands:
        command.add_args(args=set_of_commands)

    assert command.args == [
        sys.executable,
        "-m",
        program,
        *itertools.chain.from_iterable(commands),
    ]
