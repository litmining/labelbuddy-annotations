# neuro_meta_analyses.phase_1

Phase 1 of a review of neuroimaging meta-analyses. In this phase, we selected relevant papers and labelled their imaging modality. 

## Papers

### How the papers were obtained
We ran the following bash script:
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
- `/projects/neuro_meta_analyses.phase_1/documents/documents_00001.jsonl`
  - corresponding file in the pubget output: 
    - `review_neuro_meta_analyses__meta_analyses/query_7f23003d269ec31139a1b8ead2b5f74f/subset_allArticles_labelbuddyData/documents_00001.jsonl`
- `/projects/neuro_meta_analyses.phase_1/documents/documents_00002.jsonl`
  - corresponding file in the pubget output: 
    - `review_neuro_meta_analyses__meta_analyses/query_7f23003d269ec31139a1b8ead2b5f74f/subset_allArticles_labelbuddyData/documents_00002.jsonl`
  
### Annotation labels:
-  exclude not brain
-  arterial spin labelling mri
-  fmri
-  structural mri
-  perfusion mri
-  dmrid
-  CT
-  mri
-  pet
-  SPECT
-  exclude not humans
-  INTERESTING
-  exclude not meta analysis
-  vessel wall MRI
-  exclude incomplete
-  MRS
-  TMS
-  ultrasound

### Labels found in other projects as well:
- `<label2>`

### Instructions for annotators
`<description>`
