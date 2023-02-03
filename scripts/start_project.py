#! /usr/bin/env python3

import argparse
import os
import pathlib
import socket
import subprocess
import sys
from typing import Optional

from labelrepo import repo, glob_json, read_json


def _is_project_dir(dir_path: pathlib.Path) -> bool:
    for subdir in ("documents", "labels", "annotations"):
        if not (dir_path / subdir).is_dir():
            return False
    return True


def _find_project(search_start: pathlib.Path) -> Optional[pathlib.Path]:
    if _is_project_dir(search_start):
        return search_start
    for dir_path in search_start.parents:
        if repo.is_repo_root(dir_path):
            break
        if _is_project_dir(dir_path):
            return dir_path
    return None


def _start_project(
    project_dir: pathlib.Path, annotator_name: str
) -> pathlib.Path:
    db_path = project_dir / "annotations" / f"{annotator_name}.labelbuddy"
    if db_path.is_file():
        return db_path
    args = ["labelbuddy", str(db_path)]
    for labels_file in glob_json(project_dir / "labels"):
        args.extend(["--import-labels", str(labels_file)])
    for docs_file in sorted((project_dir / "documents").glob("*.jsonl")):
        args.extend(["--import-docs", str(docs_file)])
    # if this annotator has already exported annotations but the db was removed
    # for some reason, we import the annotations in the new db.
    for extension in ".json", ".jsonl":
        exported_annotations = db_path.with_suffix(extension)
        if exported_annotations.is_file():
            args.extend(["--import-docs", str(exported_annotations)])
    subprocess.run(args)
    return db_path


def _get_annotator_name(suggested_name: Optional[str]):
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project_path", type=str, nargs="?", default=".")
    parser.add_argument("--annotator", type=str, default=None)
    args = parser.parse_args()
    project_path = _find_project(pathlib.Path(args.project_path))
    if project_path is None:
        sys.exit(1)
    db_path = _start_project(
        project_path,
        _get_annotator_name(args.annotator),
    )
    print(
        f"\nYour .labelbuddy file for '{project_path.name}' is:\n\n{db_path}"
    )
