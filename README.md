# pyrgo

Python project manager inspired in [Cargo](https://doc.rust-lang.org/cargo/).

**`pyrgo` does not reinvent the wheel**. It's just a unified API that leverages popular libraries to improve your development experience.

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

All behind a unified API.

```bash
Usage: pyrgo [OPTIONS] COMMAND [ARGS]...

  pyrgo. Python package manager.

Options:
  -v, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  audit  Audit locked dependencies with `pip_audit`.
  build  Build project with `build`.
  check  Check code with `mypy` and `ruff`.
  clean  Clean project repository.
  fmt    Format code with `ruff` and `black`.
  lock   Lock project dependencies with `piptools`.
  new    Create a project.
  sync   Sync current python environment to locked deps.
  test   Run tests with `pytest`.
```

The minimal pyrgo project structure, as well as python project structure is this one:

```bash
.
├── README.md
├── pkg
│   └── __init__.py
├── pyproject.toml
└── tests
    └── test_something.py
```