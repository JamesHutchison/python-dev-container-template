# The Python Dev Container Template
An opinionated template for a Python dev container

## Features
- Likely extensions installed
- Poetry for dependency management
- Mypy uses the Daemon for increased performance
- Ruff instead of flake8, uses Ruff extension which features an autofix command
- PostStartCommand and PostCreateCommand, with background script already configured and created
- The virtual environment is under a named volume for good performance
- Docker-in-docker enabled
- Line length: black wraps at the 98 soft limit, ruff errors at the 120 hard limit
- Format on save as well as organize imports
- Debug outside your code
  - Currently there is an issue where the restart button doesn't work.
  - https://github.com/microsoft/vscode-python/issues/19030

## Limitations
- Currently just VS Code configurations

## Roles and Responsibilities
The `.devcontainer/devcontainer.json` file defines the extensions, settings, etc that are the foundation.

This means `.vscode/settings.json` isn't generated yet. This allows for it to be used as user settings or as
additional settings. If you wish to have them be user settings, add `.vscode/settings.json` to the `.gitignore` file.

Poetry is used for dependency management. The virtual environment is under `.env`.
- Add production dependency: `poetry add <dependency>`
- Add development dependnecy: `poetry add <dependency> --group=dev`

Tests are to be located under the `tests` directory.

## Usage (inside your unconfigured dev container or codespace)

- Step 1 - `cd /workspaces/`
- Step 2 - `git clone https://github.com/JamesHutchison/python-dev-container-template.git`
- Step 3 - `cd /workspaces/my-project`
- Step 4 - `/workspaces/python-dev-container-template/py_dev_container_template.py` (script runs without args)
- Step 5 - `cmd/ctrl` + `shift` + `p` -> `Rebuild container`
