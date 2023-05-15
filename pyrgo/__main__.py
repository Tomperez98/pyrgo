"""Python wrapper pyrgo entrypoint."""

import sys

from pyrgo.cli import cli

sys.exit(cli())
