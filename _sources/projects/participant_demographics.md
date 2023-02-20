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


# participant_demographics

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/participant_demographics/).

Annotating information about participants (for now just the sample size) in articles that match the query `fMRI[Abstract]`.

The full pubget output can be found here: https://osf.io/kfmdp/




## Participant demographics summaries

Here we show the information about participants that has been extracted from all the annotated documents.

```{code-cell}
:tags: [remove-input]

from labelrepo import displays
from labelrepo.projects import participant_demographics
text = participant_demographics.get_report_for_repo(remove_failed_docs=True)
displays.HTMLDisplay(text)
```

