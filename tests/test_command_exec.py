from __future__ import annotations

import sys
from typing import TYPE_CHECKING

import pytest

from pyrgo.core._command_exec import PythonCommandExec

if TYPE_CHECKING:
    from pyrgo.typing import PyrgoProgram


@pytest.mark.unit()
class TestPythonCommandExec:
    @pytest.mark.parametrize(argnames="program", argvalues=["ruff", "pip"])
    def test_new(self, program: PyrgoProgram) -> None:
        assert PythonCommandExec.new(program=program).args == [
            sys.executable,
            "-m",
            program,
        ]

    @pytest.mark.parametrize(
        argnames=["command", "args", "expected"],
        argvalues=[
            (
                PythonCommandExec.new(program="pip"),
                ["1", "2"],
                ["pip", "1", "2"],
            ),
        ],
    )
    def test_add_args(
        self,
        command: PythonCommandExec,
        args: list[str],
        expected: list[str],
    ) -> None:
        base_args = [sys.executable, "-m"]
        base_args.extend(expected)
        assert command.add_args(args=args).args == base_args
