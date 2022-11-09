import pathlib


def utils_package_root() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parent


def repo_root() -> pathlib.Path:
    return utils_package_root().parents[1]


def data_dir() -> pathlib.Path:
    return repo_root() / "analysis" / "data"
