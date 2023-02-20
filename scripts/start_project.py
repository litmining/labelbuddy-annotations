#! /usr/bin/env python3

import argparse
import pathlib
import subprocess
import sys

from labelrepo import repo, glob_json


def _start_project(
    project_dir: pathlib.Path, annotator_name: str
) -> pathlib.Path:
    db_path = project_dir / "annotations" / f"{annotator_name}.labelbuddy"
    if db_path.is_file():
        return db_path
    db_path.parent.mkdir(exist_ok=True)
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project_name", type=str)
    parser.add_argument("--annotator", type=str, default=None)
    args = parser.parse_args()

    # in case someone passes the path to the project instead of just the name
    # (convenient with tab completion)
    project_name = pathlib.Path(args.project_name).name
    project_path = repo.repo_root() / "projects" / project_name
    if not project_path.is_dir():
        print(f"Project {project_path} not found.")
        sys.exit(1)
    db_path = _start_project(
        project_path,
        repo.annotator_name(args.annotator),
    )
    print(
        f"\nYour .labelbuddy file for '{project_path.name}' is:\n\n{db_path}"
    )
