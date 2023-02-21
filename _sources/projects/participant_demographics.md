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




## How to annotate

```{code-cell}
:tags: [remove-input]

from labelrepo import displays
from labelrepo.projects import participant_demographics

def show_pmcid(pmcid):
  annotations = participant_demographics.select_participants_annotations("Jerome_Dockes", "participant_demographics", pmcid)
  html = participant_demographics.get_annotation_stacks_display(annotations)
  return displays.HTMLDisplay(html)
```

The participant group structure.

![](../assets/annotate_participants.png)

### Patients and healthy controls

To annotate information about a participant group, we start by identifying the group: we select "healthy" or "patients", and if it applies, "male" or "female".
Then, we select the label corresponding to the type of information we are annotating; for example "count".
Finally, if necessary we specify any additional information in the "extra data" input field.
For example, if the count is provided as text (eg "twenty"), we must enter the numerical value (eg "20").

Below is an example where only the count is provided, for the patients and for the healthy controls.
Note that "diagnosis" implicitly refers to patients, so we can omit the group label here (but would not be an error to add it).

```{code-cell}
:tags: [remove-input]

show_pmcid(3447931)
```

### Subgroups

When there are several subgroups among the patients or the healthy controls, we use the "extra data" input field to distinguish them.
For example, in the following article there are 2 subgroups of patients: schizophrenia and Autism Spectrum Disorder.
To annotate information about the schizophrenia group, we first select "patients", then, we use the "extra data" of that annotation to enter the subgroup.
We can choose any name we want to identify that subgroup (in this case we chose "schizophrenia").
Later, when we need to refer to that subgroup again, the subgroup name will appear in the completion suggestions for the "extra data" field.

So for annotating information about a specific subgroup, the steps are:
- select the group ("patients" or "healthy")
- enter the subgroup identifier in the "extra data" field
- if it applies select "females" or "males"
- select the label that indicates the type of information ("count", "age minimum", etc.)
- if necessary add any complementary information in the "extra data" field

```{code-cell}
:tags: [remove-input]

show_pmcid(8883821)
```

## Participant demographics summaries

Here we show the information about participants that has been extracted from all the annotated documents.

```{code-cell}
:tags: [remove-input]

html = participant_demographics.get_report_for_repo(remove_failed_docs=True)
displays.HTMLDisplay(html)
```

