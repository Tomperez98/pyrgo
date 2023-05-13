"""docs build documentation."""
import sys

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal

import click

from pyrgo.utilities.command import PythonExecCommand, inform_and_run_program


@click.command()
@click.option(
    "-t",
    "--theme",
    "theme",
    type=click.Choice(choices=["material", "mkdocs", "readthedocs"]),
    default="material",
    help="The theme to use when building your documentation.",
)
@click.option(
    "-s",
    "--strict",
    "strict",
    is_flag=True,
    default=False,
    help="Enable strict mode. This will cause MkDocs to abort the build on any warnings.",  # noqa: E501
)
def build(
    *,
    theme: Literal[
        "material",
        "mkdocs",
        "readthedocs",
    ],
    strict: bool,
) -> None:
    """Build project documentation."""
    args_to_add: list[str] = ["build"]
    if strict:
        args_to_add.append("--strict")
    args_to_add.extend(["--theme", theme])
    inform_and_run_program(
        command=PythonExecCommand(
            program="mkdocs",
        ).add_args(
            args=args_to_add,
        ),
    )
