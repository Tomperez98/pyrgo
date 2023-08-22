"""CLI commands."""
from __future__ import annotations

from pyrgo.cli.cmds.audit import audit
from pyrgo.cli.cmds.build import build
from pyrgo.cli.cmds.check import check
from pyrgo.cli.cmds.clean import clean
from pyrgo.cli.cmds.fmt import fmt
from pyrgo.cli.cmds.lock import lock
from pyrgo.cli.cmds.new import new
from pyrgo.cli.cmds.sync import sync
from pyrgo.cli.cmds.test import test

__all__ = ["lock", "fmt", "check", "sync", "build", "clean", "test", "audit", "new"]
