#!/usr/bin/env python3
"""
Script to run the generation template.

To test, just create an empty directory then run this script from that directory.
"""
import shutil
from pathlib import Path

# the directory this script is running out of
source_directory = Path(__file__).parent.absolute()

# workspace directory
workspace_directory = Path(".").absolute()

# project name
project_name = workspace_directory.name

files_to_mutate: list[Path] = []

DIRECTORIES_TO_CREATE = [
    "tests",
    ".dev_container_logs",
]

for d in DIRECTORIES_TO_CREATE:
    target_path: Path = workspace_directory / d
    if not target_path.exists():
        target_path.mkdir()

DIRECTORIES_TO_COPY = [
    (".devcontainer_template", ".devcontainer"),
    (".vscode", ".vscode"),
]
for source, target in DIRECTORIES_TO_COPY:
    source_path: Path = source_directory / source
    target_path: Path = workspace_directory / target
    if not target_path.exists():
        shutil.copytree(source_path, target_path)
        for f in target_path.glob("*.*"):
            files_to_mutate.append(f)


FILES_TO_COPY = [
    (".gitignore", ".gitignore"),
    ("pyproject.toml.template", "pyproject.toml"),
]

for source, target in FILES_TO_COPY:
    source_path: Path = source_directory / source
    target_path: Path = workspace_directory / target
    if not target_path.exists():
        shutil.copy(source_path, target_path)
        files_to_mutate.append(f)

for f in files_to_mutate:
    incoming = f.read_text()
    outgoing = incoming.replace("<<WORKSPACE DIRECTORY>>", str(workspace_directory))
    outgoing = outgoing.replace("<<PROJECT NAME>>", project_name)
    f.write_text(outgoing)
