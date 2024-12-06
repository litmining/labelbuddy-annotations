#! /usr/bin/env python3
# This script is used to centralize the documents in the projects
# Documents that are stores in {project_name}/documents/ and annotated are
# copies to the central location in documents/

from labelrepo.documents import checkin_docs
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--project', help='Project name to centralize')
    args = parser.parse_args()

    checkin_docs(args.project, args.delete)
