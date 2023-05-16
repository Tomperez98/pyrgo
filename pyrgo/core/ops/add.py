"""Add operation."""

import pathlib

from result import Ok, Result


def execute(
    cwd: pathlib.Path,  # noqa: ARG001
    new_dependency: str,  # noqa: ARG001
    group: str,  # noqa: ARG001
) -> Result[None, Exception]:
    """Execute add operation."""
    # TODO: Add command must be complian with `pip` https://pip.pypa.io/en/stable/cli/pip_install/`

    return Ok()
