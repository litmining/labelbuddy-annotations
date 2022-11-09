import os
import pathlib

from annotutils import _utils


def _is_repo_root(dir_path: pathlib.Path) -> bool:
    return (dir_path / ".labelbuddy-annotations-repository").is_file()


def repo_root() -> pathlib.Path:
    repo_env = os.environ.get("LABELBUDDY_ANNOTATIONS_REPO")
    pwd = pathlib.Path(".")
    package_parent = _utils.package_root().parents[3]
    for candidate in (repo_env, pwd, package_parent):
        if candidate is not None and _is_repo_root(pathlib.Path(candidate)):
            return pathlib.Path(candidate)
    raise FileNotFoundError(
        "Could not find labelbuddy-annotations repository."
    )


def data_dir() -> pathlib.Path:
    return repo_root() / "analysis" / "data"
