import os
import pathlib
import subprocess
import socket
from typing import Optional

from labelrepo import _utils


def is_repo_root(dir_path: pathlib.Path) -> bool:
    return (dir_path / ".labelbuddy-annotations-repository").is_file()


def repo_root() -> pathlib.Path:
    repo_env = os.environ.get("LABELBUDDY_ANNOTATIONS_REPO")
    pwd = pathlib.Path(".")
    package_parent = _utils.package_root().parents[3]
    for candidate in (repo_env, pwd, package_parent):
        if candidate is not None and is_repo_root(pathlib.Path(candidate)):
            return pathlib.Path(candidate)
    try:
        git_output = (
            subprocess.run(
                ["git", "rev-parse", "--show-toplevel"], capture_output=True
            )
            .stdout.strip()
            .decode("utf-8")
        )
        candidate = pathlib.Path(git_output)
        if is_repo_root(candidate):
            return candidate
    except Exception:
        pass
    raise FileNotFoundError(
        "Could not find labelbuddy-annotations repository."
    )


def data_dir() -> pathlib.Path:
    data_dir = repo_root() / "analysis" / "data"
    data_dir.mkdir(exist_ok=True, parents=True)
    return data_dir


def annotator_name(suggested_name: Optional[str] = None) -> str:
    if suggested_name:
        return suggested_name
    name = os.environ.get("LABELBUDDY_ANNOTATOR_NAME", "")
    if name:
        return name
    try:
        name = (
            subprocess.run(["git", "config", "User.Name"], capture_output=True)
            .stdout.decode("utf-8")
            .strip()
            .replace(" ", "_")
        )
        if name:
            return name
    except Exception:
        pass
    user_name = pathlib.Path.home().name
    host_name = socket.gethostname()
    return f"{user_name}_{host_name}"
