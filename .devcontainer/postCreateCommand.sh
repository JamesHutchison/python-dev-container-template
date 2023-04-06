#!/usr/bin/env bash
set -e

# if the .venv directory was mounted as a named volume, it needs the ownership changed
sudo chown vscode .venv || true

# make the python binary location predictable
poetry config virtualenvs.in-project true
poetry init -n --python=~3.11 || true
poetry add mypy --group=dev || true  # static type checking
poetry add ruff --group=dev || true  # fast flake8 and isort alternative
poetry add black --group=dev || true  # opinionated formatting
poetry add pytest --group=dev || true  # testing
poetry install --with=dev || true

mkdir -p /workspaces/testdir
