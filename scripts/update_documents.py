#! /usr/bin/env python3

import argparse
import pathlib
import subprocess
import sys
import tempfile
import json

from copy import deepcopy
from labelrepo import database
from collections import defaultdict


def _load_jsonl(file):
    with open(file, 'r') as f:
        _d = [json.loads(line) for line in f]
        data = {doc['metadata']['pmcid']: doc for doc in _d}
    return data


def check_annotations(annotations, docs):
    """ Given an annotation like follows:

    {'end_byte': 20027,
    'end_char': 19906,
    'label_name': 'male',
    'start_byte': 20023,
    'start_char': 19902}

    check if the annotation is still valid in the new document.
    
    """
    for annotation in annotations:
        old_doc = docs[0]
        new_doc = docs[1]

        old_text = old_doc['text']
        new_text = new_doc['text']

        old_start = annotation['start_byte']
        old_end = annotation['end_byte']

        old_text = old_text[old_start:old_end]

        new_text = new_text[old_start:old_end]

        if old_text != new_text:
            return False

    return True


def update_all(project_name):
    connection = database.get_database_connection()

    project_dir = pathlib.Path('projects') / project_name
    if not project_dir.exists():
        raise FileNotFoundError(f'Project {project_name} not found')

    cur = connection.execute("""SELECT pmcid
                            FROM detailed_annotation
                            WHERE project_name = ?""",
                            (project_name,)
                            )


    pmcids = list(set([str(r['pmcid']) for r in cur.fetchall()]))

    # Create temporary directory using tempfile module
    temp_dir = tempfile.TemporaryDirectory()
    temp_dir_path = pathlib.Path(temp_dir.name)

    # Save pmids to a new file
    pmcids_file = temp_dir_path / 'pmcids.txt'
    pmcids_file.write_text('\n'.join(pmcids))

    # Run pubget run command using subprocess module
    # Command: pubget download --pmids-file pmids.txt output

    out_dir = temp_dir_path / 'output'
    subprocess.run(['pubget', 'download', '--pmcids_file', str(pmcids_file), str(out_dir)])

    out_dir = list(out_dir.glob('pmcidList*'))[0]

    articlesets = out_dir / 'articlesets'
    subprocess.run(['pubget', 'extract_articles', str(articlesets)])

    articles = out_dir / 'articles'
    subprocess.run(['pubget', 'extract_data', str(articles)])

    extracted = out_dir / 'subset_allArticles_extractedData'
    subprocess.run(['pubget', 'extract_labelbuddy_data', str(extracted)])


    labelbuddy_data = out_dir / 'subset_allArticles_labelbuddyData'
    batch_info = labelbuddy_data / 'batch_info.json'
    info = labelbuddy_data / 'info.json'    
    json_files = list(labelbuddy_data.glob('*.jsonl'))

    new_docs = {}
    for file in json_files:
        new_docs.update(_load_jsonl(file))

    # Load old documents one by one
    old_docs = {}
    for file in (project_dir / 'documents').glob('*.jsonl'):
        old_docs[str(file)] = _load_jsonl(file)

    # Check for document differences
    diff_docs = defaultdict(dict)
    for f_name, old_docs_vals in old_docs.items():
        for pmcid_old, old_doc_j in old_docs_vals.items():
            for pmcid_new, new_doc_j in new_docs.items():
                if pmcid_old == pmcid_new:
                    if old_doc_j['metadata']['text_md5'] != new_doc_j['metadata']['text_md5']:
                        diff_docs[pmcid_old] = (deepcopy(old_doc_j), new_doc_j)
                        # Update old docs
                        old_docs_vals[pmcid_old] = new_doc_j

    # If no differences, exit
    if not diff_docs:
        print('No differences found')
        sys.exit(0)

    # If differences, check if annotations are still valid
    # If not valid, raise an error and don't update
    annotations = (project_dir / 'annotations').glob('*.json*')
    for a in annotations:
        if a.suffix == '.json':
            with open(a, 'r') as f:
                data = json.loads(f.read())
        else:
            data = [json.loads(line) for line in a.open()]

        for d in data:
            pmcid = d['metadata']['pmcid']
            if pmcid in diff_docs:
                if check_annotations(d['annotations'], diff_docs[pmcid]):
                    d['metadata']['text_md5'] = diff_docs[pmcid][1]['metadata']['text_md5']
                    # utf8_text_md5_checksum - how to compute?
                else:
                    raise ValueError('Incompatible annotation found')

    # Write new annotations
    for a in annotations:
        with open(a, 'w') as f:
            for d in data:
                f.write(json.dumps(d) + '\n')

    # Write out updated documents
    for f_name, old_docs_vals in old_docs.items():
        with open(f_name, 'w') as f:
            for pmcid, doc in old_docs_vals.items():
                f.write(json.dumps(doc) + '\n')

    # Clean up
    temp_dir.cleanup()
    print('Done')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""Update documents for a project. 
        Checks for differences in documents and annotations,
        and only proceeds if annotations are still valid."""
    )
    parser.add_argument("project_name")
    args = parser.parse_args()

    project_name = pathlib.Path(args.project_name).name

    stdout = sys.stdout
    try:
        sys.stdout = sys.stderr
        print(f"Updating documents for project: {project_name}")
        update_all(project_name)
    finally:
        sys.stdout = stdout
