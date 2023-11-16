# COBIDAS checklist

`<1-2 sentences describing the project>`

## Papers

### How the papers were obtained

<!-- Typically with [pubget](https://neuroquery.github.io/pubget/pubget.html).

We recommend invoking `pubget` with the `--query_file` option, and storing a copy of the query file in the project's directory, or including a copy in the `README.md`. -->

See the pubget `query.txt` file.

<!--
### Where the full papers are stored

Typically on [OSF](https://osf.io/).
Please also add a `documents/datasets.json` file containing the URL where the full `pubget` dataset can be downloaded, that looks like:
```
[
    {
    "url": "https://osf.io/download/<...>/"
    }
]
```

`<description>`
-->

## Annotations

### File(s) being annotated: 
- `/projects/<project_name>/documents/<documents_file1_name>.jsonl`
  - corresponding file in the pubget output: 
    - `<pubget_folder_name>/subset_allArticles_labelbuddyData/<documents_file1_name>.jsonl`
- `/projects/<project_name>/documents/<documents_file2_name>.jsonl`
  - corresponding file in the pubget output: 
    - `<pubget_folder_name>/subset_allArticles_labelbuddyData/<documents_file2_name>.jsonl`
  
### Annotation labels:

Generated from the [COBIDAS reproschema](https://github.com/ohbm/cobidas_schema):

Created with [`/tools/create_labelbuddy_labels.py`](https://github.com/ohbm/cobidas_schema/blob/master/tools/create_labelbuddy_labels.py) .

The labels contained here could be reused to label MRI, PET or eyetracking studies. 

The labels for each subsection of the schema are stored in a separate file prefixed with a number:
for example `cobidas/5_preprocessing_labels.jsonl`.
But there is also a jsonl file that combines all labels from all sections.

<!--
### Labels found in other projects as well:
- `<label2>`

### Instructions for annotators
`<description>`
-->
