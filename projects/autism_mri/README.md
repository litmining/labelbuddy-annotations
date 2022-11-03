# query_6b2c09de69c29c29626f794757ea4c68
 
Repo to do LabelBuddy annotations of a corpus of Autism MRI literature

## PubGet
This process was initialized with a *pubget* call:

```bash
pubget run -q "Brain Volume MRI 2022 Autism" pubget/test --labelbuddy --n_jobs 4
```

The whole `pubget` output has been uploaded to OSF: https://osf.io/meya4

## LabelBuddy
We are currently annotating the following file:

`projects/autism_mri/documents/documents_00001.jsonl`

Which in the `pubget` output corresponds to:

`query_6b2c09de69c29c29626f794757ea4c68/subset_allArticles_labelbuddyData/documents_00001.jsonl`

And writing the annotation files found in:
`projects/autism_mri/annotations/`

