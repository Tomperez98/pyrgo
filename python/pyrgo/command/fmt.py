"""fmt command."""
import subprocess

import click


@click.command()
@click.option(
    "--version",
    "version",
    is_flag=True,
    default=False,
    help="Print black version and exit.",
)
@click.option(
    "--check",
    "check",
    is_flag=True,
    default=False,
    help="Run black in check mode.",
)
def fmt(version: bool, check: bool) -> None:
    """This utility format all files of the current project using black."""
    root_args = ["black"]
    if version:
        root_args.append("--version")
        subprocess.run(args=root_args)
