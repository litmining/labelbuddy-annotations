
#! /usr/bin/env python3

# This script is used to make a temporary copy the documents from the central repository to the projects directory using the ids.json file

import pathlib
import json
import argparse
import hashlib 

doc_path = pathlib.Path('documents')

def checkout_docs(project_name, batch_size=200):

    project_dir = pathlib.Path('projects') / project_name
    ids_file = project_dir / 'ids.json'
    with open(ids_file, 'r') as f:
        ids = json.load(f)

    # Make a flat list of all the ids
    all_ids = []
    for id_type, id_value in ids.items():
        all_ids.extend([f"{id_type}_{id}" for id in id_value])

    # Load annotations in project
    annotations = list(project_dir.glob('annotations/*.jsonl'))
    # Make md5 checksums of the annotations
    ann_md5s = {}
    for annotation_file in annotations:
        with open(annotation_file, 'r') as f:
            for line in f:
                ann_info = json.loads(line)

                if isinstance(ann_info["metadata"], str):
                    ann_info["metadata"] = json.loads(ann_info["metadata"])

                if 'pmcid' in ann_info['metadata']:
                    id = f"pmcid_{ann_info['metadata']['pmcid']}"
                elif 'pmid' in ann_info['metadata']:
                    id = f"pmid_{ann_info['metadata']['pmid']}"

                ann_md5s[id] = ann_info['utf8_text_md5_checksum']

    # Load documents from central repository
    docs = []
    for id in all_ids:
        doc_file = doc_path / f"{id}.jsonl"
        if doc_file.exists():
            with open(doc_file, 'r') as f:
                for line in f:
                    doc = json.loads(line)
                    if id in ann_md5s:
                        if ann_md5s[id] == hashlib.md5(doc["text"].encode("utf-8")).hexdigest():
                            docs.append(doc)
                            break

    # Write the documents to the project directory
    docs_dir = project_dir / '_documents'
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
