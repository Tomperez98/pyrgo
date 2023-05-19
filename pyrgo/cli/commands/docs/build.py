"""docs build documentation."""
from __future__ import annotations

import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    if sys.version_info >= (3, 9):
        from typing import Literal
    else:
        from typing_extensions import Literal

import click
from result import Ok

from pyrgo.core import ops


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
    executed = ops.docs.build.execute(
        theme=theme,
        strict=strict,
    )
    if not isinstance(executed, Ok):
        sys.exit(1)

    sys.exit(0)
