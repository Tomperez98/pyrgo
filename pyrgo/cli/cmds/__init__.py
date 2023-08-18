"""CLI commands."""
from __future__ import annotations

from pyrgo.cli.cmds._audit import audit
from pyrgo.cli.cmds._build import build
from pyrgo.cli.cmds._check import check
from pyrgo.cli.cmds._clean import clean
from pyrgo.cli.cmds._fmt import fmt
from pyrgo.cli.cmds._lock import lock
from pyrgo.cli.cmds._sync import sync
from pyrgo.cli.cmds._test import test

__all__ = ["lock", "fmt", "check", "sync", "build", "clean", "test", "audit"]
