# python-dev-container-template
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


## Roles and Responsibilities
The `.devcontainer/devcontainer.json` file defines the extensions, settings, etc that are the foundation.

This means `.vscode/settings.json` isn't generated yet. This allows for it to be used as user settings or as
additional settings. If you wish to have them be user settings, at `.vscode/settings.json` to the `.gitignore` file.

Poetry is used for dependency management. The virtual environment is under `.env`.
- Add production dependency: `poetry add <dependency>`
- Add development dependnecy: `poetry add <dependency> --group=dev`

Tests are to be located under the `tests` directory.

## Running
Currently there isn't a streamlined way.

Steps:
- Clone this repo into a temporary directory
- Change directory to where you want the project to live
- Run `py_dev_container_template.py` out of the temporary directory with the cwd set to the target directory.

You can do this from within an initial python dev container, then rebuild the container.
