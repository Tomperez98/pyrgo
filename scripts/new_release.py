"""New release."""
import pathlib
import webbrowser
from urllib.parse import urlencode

import tomli


def project_version(cwd: pathlib.Path) -> str:
    """Read `Cargo.toml` current package version."""
    try:
        cargo_toml = tomli.loads(
            cwd.joinpath(
                "Cargo.toml",
            ).read_text(encoding="utf-8"),
        )
    except FileNotFoundError:
        raise
    except Exception:
        raise

    return cargo_toml["package"]["version"]


def project_source(cwd: pathlib.Path) -> str:
    """Read `Source` from `pyproject.toml`."""
    try:
        pyproject_toml = tomli.loads(
            cwd.joinpath(
                "pyproject.toml",
            ).read_text(encoding="utf-8"),
        )
    except FileNotFoundError:
        raise
    except Exception:
        raise

    return pyproject_toml["project"]["urls"]["Source"]


def main() -> None:
    """Prepare new release."""
    cwd = pathlib.Path().cwd()
    version = project_version(cwd=cwd)
    params = urlencode(
        query={
            "title": f"v{version}",
            "tag": f"v{version}",
        },
    )
    package_source = project_source(cwd=cwd)

    webbrowser.open_new_tab(url=f"{package_source}/releases/new?{params}")


if __name__ == "__main__":
    main()
