import itertools
import json
import pathlib
from typing import List, Union, Any


def package_root() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parent


def package_data() -> pathlib.Path:
    return package_root() / "_data"


def read_json(json_file: Union[str, pathlib.Path]) -> Any:
    json_file = pathlib.Path(json_file)
    if json_file.suffix == ".json":
        return json.loads(json_file.read_text("UTF-8"))
    elif json_file.suffix == ".jsonl":
        with open(json_file, "r", encoding="UTF-8") as stream:
            return [json.loads(line) for line in stream]
    raise ValueError("File extension must be .json or .jsonl")


def glob_json(directory: pathlib.Path) -> List[pathlib.Path]:
    return sorted(
        itertools.chain(directory.glob("*.json"), directory.glob("*.jsonl"))
    )
