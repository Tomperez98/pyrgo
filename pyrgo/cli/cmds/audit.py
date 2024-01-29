"""Audit command."""
from __future__ import annotations

import sys

import click
from result import Ok

from pyrgo.cli.utils import ensure_env_exist, inform_and_run_program
from pyrgo.core import PyrgoConf, PythonCommandExec


@click.command("audit")
@click.option(
    "-e",
    "--env",
    "env",
    type=click.STRING,
    required=True,
)
@click.option(
    "--fix/--no-fix",
    "fix",
    type=click.BOOL,
    default=False,
    show_default=True,
)
def audit(env: str, *, fix: bool) -> None:
    """Audit locked dependencies with `pip_audit`."""
    config = PyrgoConf.new()
    ensure_env_exist(env=env, config=config, where="lock-files")

    pip_audit_cmd = PythonCommandExec.new(
        program="pip_audit",
    ).add_args(
        args=[
            "-r",
            config.requirements.joinpath(f"{env}.txt")
            .relative_to(config.cwd)
            .as_posix(),
        ],
    )
    if fix:
        pip_audit_cmd.add_args(args=["--fix"])

    program_execution = inform_and_run_program(commands=[pip_audit_cmd])
    if not isinstance(program_execution, Ok):
        sys.exit(1)

    sys.exit(0)
