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
        try:
            data = {int(doc['metadata']['pmcid']): doc for doc in _d}
        except:
            print(f'Error loading {file}')
            return None
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


def get_new_documents(pmcids):
    # Create temporary directory using tempfile module
    temp_dir = tempfile.TemporaryDirectory()
    temp_dir_path = pathlib.Path(temp_dir.name)

    # Save pmids to a new file
    pmcids_file = temp_dir_path / 'pmcids.txt'
    pmcids = [str(pmcid) for pmcid in pmcids]
    pmcids_file.write_text('\n'.join(pmcids))

    # Run pubget run command using subprocess module
    out_dir = temp_dir_path / 'output'
    subprocess.run(['pubget', 'download', '--pmcids_file',
                    str(pmcids_file), str(out_dir)])

    res_dir = list(out_dir.glob('pmcidList*'))[0]

    subprocess.run(['pubget', 'extract_articles', 
                    str(res_dir / 'articlesets')])

    subprocess.run(['pubget', 'extract_data', 
                    str(res_dir / 'articles')])

    subprocess.run(['pubget', 'extract_labelbuddy_data',
                    str(res_dir / 'subset_allArticles_extractedData')])

    json_files = list(
        (res_dir / 'subset_allArticles_labelbuddyData').glob('*.jsonl'))

    # Load old and new documents
    new_docs = {}
    for file in json_files:
        new_docs.update(_load_jsonl(file))

    temp_dir.cleanup()

    return new_docs


def get_old_documents():
    old_docs = {}
    all_pmids = set()
    for file in pathlib.Path('projects').glob('*/documents/*.jsonl'):
        docs = _load_jsonl(file)

        if not docs:
            # Skip documents that don't have pmcids
            continue

        old_docs[file] = docs
        all_pmids.update(docs.keys())

    return old_docs, all_pmids


def update_all():
    old_docs, all_old_pmcids = get_old_documents()
    new_docs = get_new_documents(all_old_pmcids)

    # Check for document differences
    diff_docs = defaultdict(dict)
    for f_name, old_docs_vals in old_docs.items():
        for pmcid, old_doc_j in old_docs_vals.items():
            if pmcid in new_docs:
                old_text = old_doc_j['text']
                new_text = new_docs[pmcid]['text']

                if old_text != new_text:
                    diff_docs[pmcid] = (deepcopy(old_doc_j), new_docs[pmcid])
                    old_docs_vals[pmcid] = new_docs[pmcid]


    # If no differences, exit
    if not diff_docs:
        print('No differences found')
        sys.exit(0)

    print(f'{len(diff_docs)} documents need updating')

    # If differences, check if annotations are still valid
    # If not valid, raise an error and don't update
    annotations = pathlib.Path('projects').glob('*/annotations/*.json*')
    for a in annotations:
        if a.suffix == '.json':
            with open(a, 'r') as f:
                data = json.loads(f.read())
        else:
            data = [json.loads(line) for line in a.open()]

        for d in data:
            if 'pmid' in d['metadata']:
                pmcid = d['metadata']['pmid']
            else:
                print(f'Skipping annotation {d} without pmcid')
                continue
            if pmcid in diff_docs:
                if not check_annotations(d['annotations'], diff_docs[pmcid]):
                    raise ValueError(
                        "Incompatible annotation found. Can't update documents"
                    )

    # Write out updated documents
    for f_name, old_docs_vals in old_docs.items():
        print(f_name)
        with open(f_name, 'w') as f:
            for pmcid, doc in old_docs_vals.items():
                f.write(json.dumps(doc) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""Update documents for all projects"""
    )
    try:
        stdout = sys.stdout
        sys.stdout = sys.stderr
        update_all()
        print('Done')
    finally:
        sys.stdout = stdout
