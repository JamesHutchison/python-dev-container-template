# python-dev-container-template
An opinionated template for a Python dev container

## Features
- Likely extensions
- Poetry for management
- Mypy Daemon
- Ruff instead of flake8, uses Ruff extension which features an autofix command
- PostStartCommand and PostCreateCommand, with background script
- venv is under a named volume good performance
- Docker-in-docker


## Roles
The `.devcontainer/devcontainer.json` file defines the extensions, settings, etc that are the foundation.

This means `.vscode/settings.json` isn't generated yet. This allows for it to be used as user settings or as
additional settings.


## Running
Currently there isn't a streamlined way.

Steps:
- Clone this repo into a temporary directory
- Change directory to where you want the project to live
- Run `py_dev_container_template.py` out of the temporary directory with the cwd set to the target directory.

You can do this from within an initial python dev container, then rebuild the container.
