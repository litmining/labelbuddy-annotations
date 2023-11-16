# Review of neuroimaging meta-analyses: Topics, authors, and methods

In this project, we review neuroimaging meta-analyses. 
The manual annotation part of the project focuses on methods. 

## Papers

### How the papers were obtained [to be updated]
There are two groups of papers:
1. full-text open-access papers that were obtained from PMC via pubget, and
2. abstracts from closed-access papers that were obtained from PubMed via a tweaked version of pubget (the out-of-the-box version can only access PMC).


Typically with [pubget](https://neuroquery.github.io/pubget/pubget.html).
We recommend invoking `pubget` with the `--query_file` option, and storing a copy of the query file in the project's directory, or including a copy in the `README.md`.

`<description>`

### Where the full papers are stored [to be updated]

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


## Annotations
### File(s) being annotated: 
1. full texts from open-access papers from PMC:
   - `/projects/review-neuro-meta-analayses/documents/documents_00001-ma-in-title.jsonl`
   - `/projects/review-neuro-meta-analayses/documents/documents_00002-ma-in-title.jsonl`
   - `/projects/review-neuro-meta-analayses/documents/documents_00003-ma-in-title.jsonl`
2. abstracts from closed-access papers from pubmed:
   - `projects/review-neuro-meta-analyses/documents/closed_documents_00000.jsonl`
  
### Annotation labels:
The label list is quite long, so I'm not including it here. But the labels group into these categories
- Reasons to come back to the paper
- info on the number of studies/contrasts found/included
- meta-analysis number (many papers have multiple)
- algorithm
- software
- large-scale meta-analysis method
- exclusion criteria
- has prisma chart

### Labels found in other projects as well:
- `<label2>`

### Instructions for annotators

At this point, I have finished annotating the open-access full-text papers. I'd love help annotating the closed-access abstracts. To do this, follow these steps:
- 