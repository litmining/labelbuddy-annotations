#! /usr/bin/env python3

import argparse
import sys

from labelrepo import datasets

parser = argparse.ArgumentParser(
    description="Download full pubget output for a project."
)
parser.add_argument("project_name")
args = parser.parse_args()

stdout = sys.stdout
try:
    sys.stdout = sys.stderr
    doc_source_directories = datasets.get_project_document_sources(
        args.project_name
    )
finally:
    sys.stdout = stdout
for directory in doc_source_directories:
    print(directory)
