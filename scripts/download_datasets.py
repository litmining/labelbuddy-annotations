#! /usr/bin/env python3

import argparse
import pathlib
import sys

from labelrepo import datasets

parser = argparse.ArgumentParser(
    description="Download full pubget output for a project."
)
parser.add_argument("project_name")
args = parser.parse_args()

# in case someone passes the path to the project instead of just the name
# (convenient with tab completion)
project_name = pathlib.Path(args.project_name).name

stdout = sys.stdout
try:
    sys.stdout = sys.stderr
    print(f"Fetching datasets for project: {project_name}")
    project_datasets = datasets.get_project_datasets(project_name)
finally:
    sys.stdout = stdout
for directory in project_datasets:
    print(directory)
