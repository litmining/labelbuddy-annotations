import pathlib
import json
from collections import defaultdict
from labelrepo import repo, _utils
from labelrepo import database
import hashlib


def _load_documents(keep_docs):
    docs = defaultdict(lambda: defaultdict(dict))
    docs_paths = list(pathlib.Path('projects').glob('*/documents/*.jsonl'))
    for file in docs_paths:
        with open(file, 'r') as f:
            for line in f:
                doc_info = json.loads(line)
                processed_doc = _utils.process_doc_info(doc_info)

                if 'pmcid' in processed_doc['metadata']:
                    id = f"pmcid_{processed_doc['metadata']['pmcid']}"
                elif 'pmid' in processed_doc['metadata']:
                    id = f"pmid_{processed_doc['metadata']['pmid']}"

                if processed_doc['md5'] in keep_docs:
                    docs[id][processed_doc['md5']] = doc_info

    return docs, docs_paths


def _project_documents(project_name, delete=True):
    project_root_dir = repo.repo_root() / "projects" / project_name

    annotation_files = (project_root_dir / "annotations").glob("*.jsonl")

    # Load all documents that are annotated
    annotated_docs = set()
    for f in annotation_files:
        annotations = _utils.read_json(f)
        for doc_info in annotations:
            annotated_docs.add(doc_info["utf8_text_md5_checksum"])
                    
    docs, docs_paths = _load_documents(annotated_docs)

    # Write out documents in central location
    central_documents = repo.repo_root() / "documents"
    central_documents.mkdir(exist_ok=True)
    for id, doc_md5s in docs.items():
        for md5, doc_info in doc_md5s.items():
            file = central_documents / f'{id}.jsonl'
            # Read file, check if doc exists
            if file.exists():
                with open(file, 'r') as f:
                    for line in f:
                        existing_doc = json.loads(line)
                        if existing_doc['text'] == doc_info['text']:
                            break
                    else:
                        with open(file, 'a') as f:
                            f.write(json.dumps(doc_info) + '\n')
            else:
                with open(file, 'w') as f:
                    f.write(json.dumps(doc_info) + '\n')


def checkin_docs(project_name=None, delete=True):
    """ Centralize annotated documents in the projects """
    if project_name is None:
        # Exclude "template_project"
        all_project_dirs = [
            p for p in pathlib.Path('projects').glob("*") if p.name != "template_project"
        ]

        for project_dir in all_project_dirs:
            _project_documents(project_dir.name, delete)


def _load_md5s(project_name):
    """ Loads ids annotated in the project """
    # Get all ids for each project
    connection = database.get_database_connection()

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

    doc_path = repo.repo_root() / 'documents'

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
