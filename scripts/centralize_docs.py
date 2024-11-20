#! /usr/bin/env python3
# This script is used to centralize the documents in the projects
# Documents that are stores in {project_name}/documents/ are moved to
# the central location in documents/


import pathlib
import json
from collections import defaultdict
from labelrepo import database
import hashlib
import argparse


def centralize(project_name=None):
    connection = database.get_database_connection()

    # Select all documents where utf8_text_md5_checksum is in detailed_annotation.doc_id
    # joint filter on ut8_text_md5_checksum == detailed_annotation.doc_id

    query = """SELECT *
                    FROM document
                    WHERE id IN (
                            SELECT doc_id
                            FROM annotation
                """
    if project_name:
        query += f"WHERE project_name = '{project_name}'"

    query += ")"
    doc_rows = connection.execute(query)

    keep_docs = defaultdict(dict)
    for doc in doc_rows:
        id = f"pmcid_{doc['pmcid']}" if doc['pmcid'] else f"pmid_{doc['pmid']}"
        md5 = doc['utf8_text_md5_checksum']
        keep_docs[id][md5] = doc

    def load_documents(keep_docs):
        docs = defaultdict(dict)
        docs_paths = list(pathlib.Path('projects').glob('*/documents/*.jsonl'))
        for file in docs_paths:
            with open(file, 'r') as f:
                for line in f:
                    doc_info = json.loads(line)

                    if isinstance(doc_info["metadata"], str):
                        doc_info["metadata"] = json.loads(doc_info["metadata"])

                    if 'pmcid' in doc_info['metadata']:
                        id = f"pmcid_{doc_info['metadata']['pmcid']}"
                    elif 'pmid' in doc_info['metadata']:
                        id = f"pmid_{doc_info['metadata']['pmid']}"

                    md5 = hashlib.md5(doc_info["text"].encode("utf-8")).digest()

                    if id in keep_docs and md5 in keep_docs[id]:
                        docs[id][md5] = doc_info

        return docs, docs_paths
    
    docs, docs_paths = load_documents(keep_docs)

    # Write out documents in central location
    new_documents = pathlib.Path('documents')
    new_documents.mkdir(exist_ok=True)
    for id, doc_md5s in keep_docs.items():
        for md5 in doc_md5s:
            doc = docs[id][md5]
            file = new_documents / f'{id}.jsonl'
            # Read file, check if doc exists
            if file.exists():
                with open(file, 'r') as f:
                    for line in f:
                        existing_doc = json.loads(line)
                        if existing_doc['text'] == doc['text']:
                            break
                    else:
                        with open(file, 'a') as f:
                            f.write(json.dumps(doc) + '\n')
            else:
                with open(file, 'w') as f:
                    f.write(json.dumps(doc) + '\n')

    # Get all ids for each project
    q = """SELECT project_name, pmcid, pmid FROM
                                detailed_annotation"""
    if project_name:
        q += f" WHERE project_name = '{project_name}'"
    cur = connection.execute(q)

    # Write out pmcids for each project
    project_ids = defaultdict(lambda: defaultdict(set))
    for row in cur.fetchall():
        if row['pmcid']:
            project_ids[row['project_name']]['pmcid'].add(row['pmcid'])
        else:
            project_ids[row['project_name']]['pmid'].add(row['pmid'])

    # Sets to list
    for project, ids in project_ids.items():
        ids['pmcid'] = list(ids['pmcid'])
        ids['pmid'] = list(ids['pmid'])

    for project, ids in project_ids.items():
        project_dir = pathlib.Path(f'projects/{project}')
        datasets_json = project_dir / 'documents/datasets.json'
        if datasets_json.exists():
            # Move file to parent directory
            datasets_json.replace(project_dir / 'datasets.json')

        readme = project_dir / 'documents/README.md'
        if readme.exists():
            readme.unlink()

        # Write out ids for each project
        with open(project_dir / 'ids.json', 'w') as f:
            json.dump(ids, f)

    # Delete old documents
    for file in docs_paths:
        file.unlink()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--project', help='Project name to centralize')
    args = parser.parse_args()

    centralize(args.project)