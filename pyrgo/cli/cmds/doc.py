"""Doc command."""
from __future__ import annotations

import click

from pyrgo.cli.utils import inform_and_run_program
from pyrgo.core import PyrgoConf, PythonCommandExec


@click.command("doc")
@click.option(
    "-o",
    "output_dir",
    type=click.Path(
        exists=False,
        file_okay=False,
        dir_okay=True,
    ),
)
@click.option(
    "-p",
    "port",
    type=click.INT,
)
def doc(output_dir: str | None, port: int | None) -> None:
    """Build a package's documentation with `pdoc`."""
    configuration = PyrgoConf.new()
    pdoc_command = PythonCommandExec.new(program="pdoc").add_args(
        args=[
            configuration.project_name,
        ]
    )
    if port is not None:
        pdoc_command.add_args(args=["-p", str(port)])

    if output_dir is not None:
        pdoc_command.add_args(args=["-o", output_dir])

    inform_and_run_program(commands=[pdoc_command])
