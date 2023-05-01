# cluster_inference

Repo to do LabelBuddy annotations of a corpus of fMRI literature.
This corpus consists of the open-access portion of NeuroQuery papers that conatain fMRI in the title or abstract.

## Papers
### How the papers were obtained
We rand a script with this code:
```bash
#!/bin/bash

pubget run --pmcids_file pmcids_for_open_fmri_papers.txt \
    --fit_neuroquery                                          \
    --labelbuddy                                              \
    --nimare                                              \
    ~/data/pubget_data
```

The `pmcids_for_open_fmri_papers.txt` file is found in the current directory.
It contains the pmcids for all the papers in the `neuroquery` dataset that could be found on PubMed Central (i.e., that were open access).


### Where the full papers are stored
The full pubget output is stored on OSF: [https://osf.io/gukw2](https://osf.io/gukw2).


## Annotations
### File(s) being annotated: 
- `/projects/cluster_inference/documents/documents.jsonl`
  - corresponding file in the pubget output: 
    - `cluster_inference/pmcidList_a84871e6b29a46f53d30d0463f66407f/subset_allArticles_labelbuddyData/documents00001.jsonl`
  
### Annotation labels:
- smoothing_snippet
- cluster_thresh_used
- cluster_thresh_in_voxels
- cluster_thresh_in_mm
- nonparametric_cluster_thresh
- info_removed_in_name_extract
- is_annotated
- annotation_in_progress
- discard_this_paper 

### Labels found in other projects as well:
- `<label2>`

### Instructions for annotators
`<description>`


