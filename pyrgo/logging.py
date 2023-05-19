"""Library logger configuration."""
from __future__ import annotations

import sys

from loguru import logger


# https://github.com/Delgan/loguru/issues/109
def configure_logger() -> None:
    """Add custom configuration to the logger object."""
    logger.remove()
    fmt = (
        "<lvl>[{level}]</lvl> "
        "{message} "
        "<green>{name}:{function}:{line}</green> "
        "@ {time:HH:mm:ss}"
    )
    logger.add(sys.stderr, format=fmt)


configure_logger()

__all__ = [
    "logger",
]
