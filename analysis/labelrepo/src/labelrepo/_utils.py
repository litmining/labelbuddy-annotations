import pathlib


def package_root() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parent


def package_data() -> pathlib.Path:
    return package_root() / "_data"
