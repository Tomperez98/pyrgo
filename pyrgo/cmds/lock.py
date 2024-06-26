"""Lock command."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Literal

import click
from result import Ok, Result
from typing_extensions import assert_never

from pyrgo.command_exec import PythonCommandExec
from pyrgo.conf import PyrgoConf
from pyrgo.utils import inform_and_run_program

if TYPE_CHECKING:
    import subprocess


def _initial_args(
    env: str,
    core_deps_alias: str,
    *,
    upgrade: bool,
) -> list[str]:
    base_args = ["pip", "compile"]
    if upgrade:
        base_args.append("--upgrade")

    if env == core_deps_alias:
        return base_args

    base_args.extend(["--extra", env])
    return base_args


def _complete_cmd(
    *,
    env: str,
    cmd: PythonCommandExec,
    generate_hashes: bool,
    cache: bool,
    config: PyrgoConf,
) -> PythonCommandExec:
    if generate_hashes:
        cmd.add_args(args=["--generate-hashes"])

    if not cache:
        cmd.add_args(args=["--no-cache"])

    cmd.add_args(
        args=[
            "-o",
            config.requirements.joinpath(f"{env}.txt")
            .relative_to(config.cwd)
            .as_posix(),
            "pyproject.toml",
        ],
    )
    return cmd


@click.command("lock")
@click.option(
    "--generate-hashes",
    "generate_hashes",
    is_flag=True,
    default=False,
    show_default=True,
    type=click.BOOL,
)
@click.option(
    "--upgrade",
    "upgrade",
    is_flag=True,
    default=False,
    show_default=True,
    type=click.BOOL,
)
@click.option(
    "-e",
    "--env",
    "envs",
    multiple=True,
    type=click.STRING,
    required=False,
)
@click.option("--cache/--no-cache", "cache", default=True, show_default=True)
def lock(
    *, generate_hashes: bool, envs: tuple[str, ...], upgrade: bool, cache: bool
) -> None:
    """Lock project dependencies with `uv`."""
    configuration = PyrgoConf()

    if not configuration.requirements.exists():
        configuration.requirements.mkdir()

    execution_mode: Literal["all", "specific-groups"] = (
        "all" if len(envs) == 0 else "specific-groups"
    )
    program_execution: Result[None, list[subprocess.CalledProcessError]]
    all_commands: list[PythonCommandExec] = []
    if execution_mode == "all":
        all_commands.extend(
            _complete_cmd(
                cmd=PythonCommandExec(
                    program="uv",
                ).add_args(
                    args=_initial_args(
                        env=env,
                        core_deps_alias=configuration.env_groups[0],
                        upgrade=upgrade,
                    ),
                ),
                generate_hashes=generate_hashes,
                config=configuration,
                env=env,
                cache=cache,
            )
            for env in configuration.env_groups
        )

        program_execution = inform_and_run_program(commands=all_commands)

    elif execution_mode == "specific-groups":
        for env in envs:
            if env in configuration.env_groups:
                all_commands.append(
                    _complete_cmd(
                        cmd=PythonCommandExec(
                            program="uv",
                        ).add_args(
                            args=_initial_args(
                                env=env,
                                core_deps_alias=configuration.env_groups[0],
                                upgrade=upgrade,
                            ),
                        ),
                        generate_hashes=generate_hashes,
                        config=configuration,
                        env=env,
                        cache=cache,
                    ),
                )

            else:
                click.echo(
                    message=click.style(
                        text=f"Optional deps for `{env}` not found in pyproject.toml.",
                        fg="red",
                    ),
                )
                sys.exit(1)

        program_execution = inform_and_run_program(commands=all_commands)
    else:
        assert_never(execution_mode)

    if not isinstance(program_execution, Ok):
        sys.exit(1)

    sys.exit(0)
