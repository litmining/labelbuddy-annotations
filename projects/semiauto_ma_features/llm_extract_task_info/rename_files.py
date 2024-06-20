import json
import os


def load_json_files():
    # Define the input directory and file names
    input_dir = "documents"
    with open(f"{input_dir}/documents_00001.jsonl", 'r') as json_file:
        json_list = list(json_file)

    for i, json_str in enumerate(json_list):
        json_list[i] = json.loads(json_str)

    return json_list


gpt_dirs = ['llm_extract_task_info/gpt-3.5-turbo-0125', 'llm_extract_task_info/gpt-4o']

json_list = load_json_files()

for gpt_dir in gpt_dirs:
    for paper in json_list:
        pmid = paper['metadata']['pmid']
        pmcid = paper['metadata']['pmcid']
        if os.path.exists(f"{gpt_dir}/{pmid}.json"):
            os.rename(f"{gpt_dir}/{pmid}.json", f"{gpt_dir}/{pmcid}.json")

