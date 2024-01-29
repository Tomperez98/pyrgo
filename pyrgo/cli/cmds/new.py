"""New command."""
from __future__ import annotations

import pathlib
import shutil
import sys

import click

from pyrgo.core import resources


@click.command("new")
@click.option("-n", "--name", "name", type=click.STRING, required=True)
@click.option("--path", "path", type=click.Path(), required=True)
def new(name: str, path: str) -> None:
    """Create a project."""
    path_path = pathlib.Path(path)

    package_name = name.strip().replace("-", "_")
    dir_components = [
        path_path.joinpath(package_name),
        path_path.joinpath("tests"),
    ]
    file_componens = [
        path_path.joinpath("README.md"),
        path_path.joinpath("pyproject.toml"),
    ]

    existing_dirs: list[str] = [
        dir_comp.as_posix()
        for dir_comp in dir_components
        if dir_comp.exists() and dir_comp.is_dir()
    ]
    existing_files: list[str] = [
        file_comp.as_posix()
        for file_comp in file_componens
        if file_comp.exists() and file_comp.is_file()
    ]

    if len(existing_dirs) > 0 or len(existing_files) > 0:
        if len(existing_dirs) > 0:
            click.echo(
                click.style(
                    f"Directories: {existing_dirs} already exists in path {path}",
                    fg="red",
                ),
            )
        if len(existing_files) > 0:
            click.echo(
                click.style(
                    f"Files: {existing_files} already exists in path {path}",
                    fg="red",
                ),
            )
        sys.exit(1)

    shutil.copytree(
        src=pathlib.Path(resources.__file__).parent.joinpath("new-project"),
        dst=path_path,
        dirs_exist_ok=True,
    )

    shutil.move(
        src=path_path.joinpath("new_project"),
        dst=path_path.joinpath(package_name),
    )
    file_paths = [
        path_path.joinpath("README.md"),
        path_path.joinpath("pyproject.toml"),
    ]
    for file_path in file_paths:
        new_data = file_path.read_text().replace("new-project", name)
        file_path.write_text(new_data)
