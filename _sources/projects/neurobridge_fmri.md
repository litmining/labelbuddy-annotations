---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

% !!!
%
% Don't edit this page directly!
% It has been automatically generated.
% Instead, edit the project's README.md file which gets inserted here,
% or the templates in /analysis/book_helpers/templates/
%
% !!!


# neurobridge_fmri

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/neurobridge_fmri/).

## fMRI tasks in NeuroBridge documents

This is a satellite project of the [NeuroBridge annotation project](https://github.com/NeuroBridge/Annotation-Project).
The goal is to annotate the tasks used by task-based fMRI acquisitions described in the **NeuroBridge** papers.

The documents were copied from [this directory](https://github.com/NeuroBridge/Annotation-Project/tree/main/Phase_1/INPUT_Papers_for_Annotation/All_Papers_For_Annotation_From_Phase_2) in the **NeuroBridge** repository, and converted from WebAnno3 format to [labelbuddy](https://jeromedockes.github.io/labelbuddy/labelbuddy/current/)'s format using [labelutils](https://github.com/jeromedockes/labelutils).

As the documents for this project do not come from a [pubget](https://neuroquery.github.io/pubget/pubget.html) download, they have less metadata and a different formatting (no headings or paragraph breaks) than documents in other projects in this repository.
Also, a **pubget** dataset is not available for download with `/scripts/download_datasets.py`.
But keeping the same version of the documents makes it possible to combine the annotations created here with those of the larger **NeuroBridge** project, down to the character positions, which trumps the other details.





## Labels in this project


(No labels have been added to this project yet)


```{code-cell}
:tags: [remove-input]

from labelrepo import displays
text = """
<div class="detailed-label-set">
    
</div>
"""
displays.HTMLDisplay(text)
```
