
#! /usr/bin/env python3

# This script is used to make a temporary copy the documents from the central repository to the projects directory using the ids.json file

import pathlib
import json
import argparse
import hashlib 
from collections import defaultdict
from labelrepo import database

connection = database.get_database_connection()
doc_path = pathlib.Path('documents')


def _load_md5s(project_name):
    """ Loads ids annotated in the project """
    # Get all ids for each project
    q = f"""SELECT project_name, pmcid, pmid, doc_md5 FROM
                                detailed_annotation
                                WHERE project_name = '{project_name}'
                                """
    cur = connection.execute(q)

    # Write out pmcids for each project
    md5s = defaultdict(set)
    for row in cur.fetchall():
        if row['pmcid']:
            _id = f"pmcid_{row['pmcid']}"
        else:
            _id = f"pmid_{row['pmid']}"

        md5s[_id].add(row['doc_md5'])

    # Set to list
    md5s = {k: list(v) for k, v in md5s.items()}

    return md5s


def checkout_docs(project_name, batch_size=200):
    project_dir = pathlib.Path('projects') / project_name
    all_md5s = _load_md5s(project_name)

    # Load documents from central repository
    docs = []
    for id, ann_md5s in all_md5s.items():
        doc_file = doc_path / f"{id}.jsonl"
        if doc_file.exists():
            with open(doc_file, 'r') as f:
                for line in f:
                    doc = json.loads(line)
                    doc_md5 = hashlib.md5(doc["text"].encode("utf-8")).hexdigest()
                    if doc_md5 in ann_md5s:
                        docs.append(doc)


    # Write the documents to the project directory
    docs_dir = project_dir / 'documents'
    docs_dir.mkdir(exist_ok=True)

    for i in range(0, len(docs), batch_size):
        batch = docs[i:i+batch_size]
        batch_file = docs_dir / f"{i}_{i+batch_size}.jsonl"
        with open(batch_file, 'w') as f:
            for doc in batch:
                f.write(json.dumps(doc))
                f.write('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Copy documents for a project from the central repository."
    )
    parser.add_argument("project_name")
    parser.add_argument("--batch_size", type=int, default=200)
    args = parser.parse_args()

    checkout_docs(args.project_name, args.batch_size)
