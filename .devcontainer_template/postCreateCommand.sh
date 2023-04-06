#!/usr/bin/env bash
set -e

# if the .venv directory was mounted as a named volume, it needs the ownership changed
sudo chown vscode .venv || true

# make the python binary location predictable
poetry config virtualenvs.in-project true
poetry init -n --python=~3.11 || true
poetry add ruff --group=dev || true  # fast flake8 alternative
poetry install || true
