# neuro_meta_analyses.phase_2

Phase 2 of a review of neuroimaging meta-analyses. In this phase, we labelled fMRI meta-analyses for their meta-analysis method 

## Papers
### How the papers were obtained
The phase 2 data consists of the phase 1 meta-analysis papers that were labelled as having meta-analyzed fMRI papers.

We ran the following bash script to get the phase 1 data:
```bash
#!/bin/bash

pubget run -f 0_pmc_search.txt \
    --fit_neuroquery                                          \
    --labelbuddy                                              \
    ~/data/pubget_data
```
The file `0_pmc_search.txt` is in the current directory. It contains the search query for PubMed Central.

### Where the full papers are stored

The full pubget output can be found on OSF: [https://osf.io/eu398](https://osf.io/eu398).  This includes the papers used in both phases 1 and 2. Phase 1 used all the papers; phase 2 used a subset that had been labelled as using fMRI

## Annotations
### File(s) being annotated: 
- `/projects/neuro_meta_analyses.phase_2/documents/documents_included_from_phase_1.jsonl`
  - corresponding to some (but not all) of the papers in these files in the pubget output: 
    - `review_neuro_meta_analyses__meta_analyses/query_7f23003d269ec31139a1b8ead2b5f74f/subset_allArticles_labelbuddyData/documents_00001.jsonl`
    - `review_neuro_meta_analyses__meta_analyses/query_7f23003d269ec31139a1b8ead2b5f74f/subset_allArticles_labelbuddyData/documents_00002.jsonl`
  
### Annotation labels:
-  literature query
-  literature sources
-  literature search date
-  original n
-  final n
-  exclusion criteria
-  meta-analysis method
-  inference
-  covariates
-  n individual participants
-  LOOK UP LATER
-  exclude?

### Labels found in other projects as well:
- `<label2>`

### Instructions for annotators
`<description>`
