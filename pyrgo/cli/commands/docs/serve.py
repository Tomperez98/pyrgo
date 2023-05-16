"""docs serve command."""
import sys

from result import Ok

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


import click

from pyrgo.core import ops


@click.command()
@click.option(
    "-a",
    "--dev-addr",
    "dev_addr",
    metavar="<IP:PORT>",
    default="localhost:8000",
    type=str,
    help="IP address and port to serve documentation locally (default: localhost:8000)",
)
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
def serve(
    *,
    dev_addr: str,
    theme: Literal[
        "material",
        "mkdocs",
        "readthedocs",
    ],
    strict: bool,
) -> None:
    """Serve project documentation."""
    executed = ops.docs.serve.execute(
        dev_address=dev_addr,
        theme=theme,
        strict=strict,
    )
    if not isinstance(executed, Ok):
        click.echo(message=executed.err())
        sys.exit(1)

    sys.exit(0)