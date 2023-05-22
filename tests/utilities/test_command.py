"""Test command utilities."""
from __future__ import annotations

import pytest

from pyrgo.core.models.command import PythonExecCommand
from pyrgo.core.utilities.command import inform_and_run_program


@pytest.mark.integration()
def test_inform_and_run_program() -> None:
    """Test inform and run program."""
    inform_and_run_program(
        commands=[
            PythonExecCommand(program="ruff").add_args(
                args=["--version"],
            ),
        ],
    ).unwrap()


@pytest.mark.integration()
def test_inform_and_run_program_fails() -> None:
    """Test inform and run program."""
    execution_err = inform_and_run_program(
        commands=[
            PythonExecCommand(program="ruff").add_args(
                args=["-abc"],
            ),
        ],
    ).err()
    assert execution_err
    assert len(execution_err) == 1
