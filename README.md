# pyrgo

Python project manager inspired in [Cargo](https://doc.rust-lang.org/cargo/).

`Pyrgo` does not reinvent the wheel. It's just a unified API that leverages popular libraries to improve your development experience.

- Testing:
  - [pytest](https://docs.pytest.org/en/7.3.x/)
- Code formatting:
  - [ruff](https://beta.ruff.rs/docs/)
  - [black](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html)
- Code checking:
  - [ruff](https://beta.ruff.rs/docs/)
  - [mypy](https://mypy.readthedocs.io/en/stable/config_file.html)
- Artifacts building:
  - [build](https://pypa-build.readthedocs.io/en/stable/)
- Package management:
  - [pip](https://pip.pypa.io/en/stable/)
  - [pip-tools](https://pip-tools.readthedocs.io/en/latest/)
- Code documentation:
  - [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
- Virtual enviroment:
  - [venv](https://virtualenv.pypa.io/en/latest/)

All behind a unified API.

```bash
pyrgo -h

# Usage: pyrgo [OPTIONS] COMMAND [ARGS]...

#   Pyrgo. Python package manager.

# Options:
#   -v, --version  Show the version and exit.
#   -h, --help     Show this message and exit.

# Commands:
#   audit  Scan project requirements for packages with known vulnerabilities.
#   build  Build project.
#   check  Analyze the current package with `ruff` and `mypy`.
#   clean  Remove artifacts that pyrgo has generated in the past.
#   docs   Document you project with `mkdocs-material`.
#   fmt    Format all files of the current project using `black` and `ruff`.
#   lock   Lock dependencies using `piptools`.
#   sync   Synchronize virtual environment with requirements.txt.
#   test   Execute tests using `pytest`.
#   venv   Create project virtual environment.
```

Use `pyrgo-new -n <project-name> [path]` to initialize your new project
