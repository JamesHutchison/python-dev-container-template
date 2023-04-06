"""
Script to run the generation template.

To test, just create an empty directory then run this script from that directory.
"""
from pathlib import Path
import shutil
import os

# the directory this script is running out of
source_directory = Path(__file__).parent.absolute()

# workspace directory
workspace_directory = Path(".").absolute()

files_to_mutate: list[Path] = []

# def read_from_env_or_input(env_string: str, prompt: str) -> str:
#     while not (result := (os.env.get(env_string, "") or input(prompt.rstrip(" ") + " "))):
#         pass
#     return result

# while not Path(target_directory := read_from_env_or_input("DC_PROJECT_DIR", "Enter target directory")).exists():
#     pass

DIRECTORIES_TO_CREATE = [
    "tests",
    "dev container logs",
]

for d in DIRECTORIES_TO_CREATE:
    target_path: Path = workspace_directory / d
    if not target_path.exists():
        target_path.mkdir()

DIRECTORIES_TO_COPY = [
    (".devcontainer_template", ".devcontainer"),
    (".vscode", ".vscode"),
]
for source_target in DIRECTORIES_TO_COPY:
    source_path: Path = source_directory / source
    target_path: Path = workspace_directory / target
    if not target_path.exists():
        shutil.copytree(source_path, target_path)
        for f in target_path.glob("*.*"):
            files_to_mutate.append(f)


FILES_TO_COPY = [
    ".gitignore",
]

for f in FILES_TO_COPY:
    source_path: Path = source_directory / f
    target_path: Path = workspace_directory / f
    if not target_path.exists():
        shutil.copy(source_path, target_path)
        files_to_mutate.append(f)

for f in files_to_mutate:
    incoming = f.read_text()
    outgoing = incoming.replace("<<WORKSPACE DIRECTORY>>", workspace_directory)
    f.write_text(outgoing)
