"""command utilities."""
import subprocess
import sys
from typing import List

from typing_extensions import Self

from pyrgo.logging import logger


class PythonExecCommand:
    """Command builder."""

    def __init__(self, program: str) -> None:
        """Python programs to be executed within current python interpreter."""
        self.program = program
        self.args = [sys.executable, "-m", program]

    def add_args(self, args: List[str]) -> Self:
        """Add args to execution."""
        self.args.extend(args)
        return self

    def run(self) -> None:
        """Run command."""
        logger.info("Running {command}", command=self.args)
        try:
            subprocess.run(args=self.args, check=True)
        except subprocess.CalledProcessError as e:
            logger.error(e)


def inform_and_run_program(command: PythonExecCommand) -> None:
    """Inform and run program."""
    command.run()
