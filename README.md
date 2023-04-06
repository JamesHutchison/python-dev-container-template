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
