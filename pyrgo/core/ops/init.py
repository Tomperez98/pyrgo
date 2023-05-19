"""init operation."""
import subprocess
from typing import List

from result import Result

from pyrgo.core.models.command import PythonExecCommand
from pyrgo.core.models.config import Config
from pyrgo.core.utilities.command import inform_and_run_program
import tempfile


def execute(app_config: Config) -> Result[None, List[subprocess.CalledProcessError]]:
    """Execute init operation."""
    with tempfile.TemporaryDirectory() as temp_dir:
        print(temp_dir)
        cookiecutter_command = PythonExecCommand(program="cookiecutter").add_args(
            args=[
                "--accept-hooks",
                "yes",
                "--output-dir",
                temp_dir,
                str(app_config.starter_project),
            ],
        )

        return inform_and_run_program(
            commands=[
                cookiecutter_command,
            ],
        )
