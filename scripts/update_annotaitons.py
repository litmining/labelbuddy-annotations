#! /usr/bin/env python3
# This script is used to update the annotations in the projects

import pathlib
import json
import logging
import subprocess
from collections import defaultdict
from copy import deepcopy
from labelrepo import database
import regex


# Set up logging to file & console
logging.basicConfig(filename='centralize_docs.log', level=logging.INFO)
logger = logging.getLogger()
if len(logger.handlers) == 1:
    console = logging.StreamHandler()
    logger.addHandler(console)


def _load_jsonl(file):
    with open(file, 'r') as f:
        _d = [json.loads(line) for line in f]
        data = {int(doc['metadata']['pmcid']): doc for doc in _d if 'pmcid' in doc['metadata']}
        if not data:
            logging.info(f'No PMCIDs found in {file}')
    return data


def _iterative_fuzzy_search(target, text, max_diff=5):
    """ Find the target in the text with fuzzy matching. """
    for i in range(max_diff):
        patt = ["(?b)(", regex.escape(target), "){", f"i<=2,s<={i},d<={i}", "}"]
        m = regex.search(
            "".join(patt),
            text
            )
        if m:
            break
    else:
        return None, None
    return m.span(), m.captures()[0]


def _adjust_annotation(old_start, old_end, old_text, new_text, buffer=8):
    """ Adjust the annotations to the new text. """
    old_quote = old_text[old_start:old_end]

    if old_start == 0:
        logging.info('Annotation at the beginning of the text')
        new_start, new_end = (0, old_end)

    else:
        # Look for the annotation in the new text with fuzzy matching
        # With a context buffer
        qp = old_text[
            max(0, old_start-buffer):min(len(old_text), old_end+buffer)
            ]
        b_span, b_capture = _iterative_fuzzy_search(qp, new_text)
        if b_span is None:
            logging.info(f'Could not find {old_quote} in new text')
            return None, None

        t_span, _ = _iterative_fuzzy_search(old_quote, b_capture)
        new_start, new_end = b_span[0] + t_span[0], b_span[0] + t_span[1]

    logging.info('-------------------')
    new_quote = new_text[new_start:new_end]
    if new_quote != old_quote:
        logging.info(f'Adjusted: {old_quote} -> {new_quote}')
    else:
        logging.info(f'Unchanged: {old_quote}')
    logging.info(f'Old span: {old_start} - {old_end}')
    logging.info(f'New span: {new_start} - {new_end}')
    logging.info(f'Difference: {new_start - old_start}')
    logging.info('-------------------')
    return new_start, new_end


def adjust_annotations(ann_data, docs):
    """ Given an annotation like follows:

    {'end_byte': 20027,
    'end_char': 19906,
    'label_name': 'male',
    'start_byte': 20023,
    'start_char': 19902}

    check if the annotation is still valid in the new document.
    
    """
    annotations = ann_data['annotations']
    old_doc = docs[0]
    new_doc = docs[1]

    for annotation in annotations:
        old_start = annotation['start_char']
        old_end = annotation['end_char']

        old_quote = old_doc['text'][old_start:old_end]
        new_quote = new_doc['text'][old_start:old_end]

        if old_quote != new_quote:
            new_start, new_end = _adjust_annotation(
                old_start, old_end, old_doc['text'], new_doc['text'])
            
            if new_start is None:
                continue

            annotation['start_byte'] = new_start
            annotation['end_byte'] = new_end


def get_new_documents(temp_dir_path, pmcids):

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

    return json_files, new_docs


def get_old_documents():
    old_docs = {}
    for file in pathlib.Path('projects').glob('*/documents/*.jsonl'):
        # Skip symlinked files
        if file.is_symlink():
            continue
        docs = _load_jsonl(file)

        if not docs:
            # Skip documents that don't have pmcids
            continue

        old_docs[file] = docs

    return old_docs


def centralize_all(dry_run=False):
    connection = database.get_database_connection()

    cur = connection.execute("""SELECT pmcid
                            FROM detailed_annotation"""
                             )

    # PMCIDS with at least 1 annotation
    pmcids = list(set([str(r['pmcid']) for r in cur.fetchall()]))
    pmcids = [int(pmcid) for pmcid in pmcids if pmcid != 'None']

    old_docs = get_old_documents()
    temp_dir_path = pathlib.Path('/tmp/tmpk16sdkyw/')
    json_files, new_docs = get_new_documents(temp_dir_path, pmcids)

    # Check for document differences
    diff_docs = defaultdict(list)
    for f_name, old_docs_vals in old_docs.items():
        for pmcid, old_doc_j in old_docs_vals.items():
            if pmcid in new_docs:
                old_text = old_doc_j['text']
                new_text = new_docs[pmcid]['text']

                if old_text != new_text:
                    diff_docs[pmcid].append((deepcopy(old_doc_j), new_docs[pmcid]))

    # Check all annotations for compatibility
    annotations = pathlib.Path('projects').glob('*/annotations/*.json*')
    for a in annotations:
        if a.suffix == '.json':
            with open(a, 'r') as f:
                data = json.loads(f.read())
        else:
            data = [json.loads(line) for line in a.open()]

        for d in data:
            if 'pmcid' not in d['metadata']:
                continue

            pmcid = d['metadata']['pmcid']

            if pmcid in diff_docs:
                for docs in diff_docs[pmcid]:
                    if d['metadata']['text_md5'] != d['metadata']['text_md5']:
                        continue
                    elif docs[0]['text'] == '':
                        logging.info(f'Empty text for {docs[0]["metadata"]["pmcid"]}')
                        continue

                    logging.info(f'PMCID: {pmcid}')
                    adjust_annotations(d, docs)
                    logging.info('=======================') 

    if not dry_run:
        # Copy jsonl files to documents/
        new_doc_path = pathlib.Path('documents')
        new_doc_path.mkdir(exist_ok=True)
        for file in json_files:
            dest = new_doc_path / file.name
            file.replace(dest)

        # Compute unique PMCIDs for each project
        # and delete old documents
        project_pmids = defaultdict(set)
        for file in old_docs.keys():
            project_name = file.parts[1]
            old_pmcids = old_docs[file].keys()

            # Only keep pmcids that are in the new documents
            # i.e. with annotations
            keep_pmcids = set(old_pmcids) & set(pmcids)
            project_pmids[project_name].update(keep_pmcids)

            file.unlink()

        # Write out pmcids for each project
        for project, pmcids in project_pmids.items():
            project_dir = pathlib.Path(f'projects/{project}')
            datasets_json = project_dir / 'documents/datasets.json'
            if datasets_json.exists():
                # Move file to parent directory
                datasets_json.replace(project_dir / 'datasets.json')

            readme = project_dir / 'documents/README.md'
            if readme.exists():
                readme.unlink()

            # If parent directory now empty, delete
            if datasets_json.parent.is_dir() and not list(datasets_json.parent.iterdir()):
                datasets_json.parent.rmdir()

            pmcids_file = project_dir / 'pmcids.txt'
            pmcids = [str(pmcid) for pmcid in pmcids]
            pmcids_file.write_text('\n'.join(pmcids))


if __name__ == '__main__':
    centralize_all(dry_run=True)
