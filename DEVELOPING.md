# Developing

## Getting Started

This project requires:
- python (>= 3.7)
- pip (>= 22.2)
- poetry (>= 1.2): see [installation instructions](https://python-poetry.org/docs/#installation)

Once you have python and poetry installed, get the project bootstrapped:

```bash
# get basic project tooling
make bootstrap

# get a persistent virtual environment to work within
poetry shell

# install project dependencies
poetry install
```

[Pre-commit](https://pre-commit.com/) is used to help enforce static analysis checks with git hooks:

```bash
poetry run pre-commit install --hook-type pre-push
```

To jump into a poetry-managed virtualenv run `poetry shell`, this will prevent the need for `poetry run...` prefix for each command.

## Developing

If you want to use a locally-editable copy of vulnstick while you develop:

```bash
poetry shell
pip uninstall vulnstick  #... if you already have vulnstick installed in this virtual env
pip install -e .
```

To run all static-analysis and tests:

```bash
make
```

Or run them individually:

```bash
make static-analysis
make unit
make cli
```

If you want to see all of the things you can do:

```bash
make help
```
