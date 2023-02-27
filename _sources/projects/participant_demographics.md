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

Annotating information about participants: count, sex, age, and diagnosis.

The full pubget output can be found here: https://osf.io/kfmdp/




## How to annotate

```{code-cell}
:tags: [remove-input]

from labelrepo import displays
from labelrepo.projects import participant_demographics

def show_pmcid(pmcid):
  annotations = participant_demographics.select_participants_annotations("Jerome_Dockes", "participant_demographics", pmcid)
  html = participant_demographics.get_annotation_stacks_display(annotations, standalone=False)
  return displays.HTMLDisplay(html)
```

Annotating demographic information about the participants is more complex than other projects in this repository, because studies typically involve several groups of participants, with diverse structures, and there is some variation in how the relevant information is reported.
To annotate a piece of information about a group of participants, we stack several annotations on top of each other.
We add annotations that identify the group of participants (eg patients vs controls), then an annotation that contains the information of interest (eg count, min age, etc.).
To be easily linked these annotations should be at the exact same positions, which is easy to acheive in **labelbuddy** by clicking several labels in sequence (or by first selecting an existing annotation and then clicking a new label to add it on top).

We consider that most articles roughly conform to the participant group structure depicted in the tree shown in {numref}`participants-tree-fig`.
The root contains all the participants, which are then divided in patients and healthy controls, each of which may contain several subgroups, and finally each subgroup can contain females and males.
Note that for many articles, some of the nodes will be empty -- eg studies involving only healthy controls, only one sex, etc.

```{figure} ../assets/annotate_participants.png
---
name: participants-tree-fig
---
The participant group structure and corresponding annotations.
```

### Annotation example with subgroups

In {numref}`participants-tree-fig` we see the general way of annotating information about participants.
We start by describing the most complex case but for most annotations the situation will be simpler.

This video (without sound) illustrates the annotation process that is described below.


```{code-cell}
:tags: [remove-input]

html = """
<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/801946148?h=173137dc76&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="participants-annotations-2023-02-24.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>
"""
displays.HTMLDisplay(html)
```

Here we annotate the count (20) of a specific subgroup, constituted of:

- Patients
- Within patients, the schizophrenia subgroup (this article also has an autism spectrum disorder subgroup of patients)
- Within the schizophrenia subgroup, the males.

To annotate this information, we select the information we want to annotate and then apply labels, starting from the top of the participants tree (the actual order doesn't matter, this is just a suggestion). 
We first click the "patients" label.

Then, as there are several patients subgroups in this article, we need to differentiate the schizophrenia subgroup.
We don't want to add new *labels* for subgroups, as we would end up with a very long list of labels, most of which are used in few papers (eg "schizophrenia", "siblings", "experts", etc.)
Instead, we rely on the **extra data** input field in **labelbuddy**.
While the "patients" annotation is still selected, we write int its **extra data** field (on the bottom left of **labelbuddy**).
We enter in there whatever name we want to give to the schizophrenia subgroup, which will act as a local identifier within the current paper.
This name is arbitrary and only serves to link the different annotations about that subgroup, here we unoriginally chose "schizophrenia".
Referring it to it again for other annotations will be easy because **labelbuddy** will propose it in a completion list whenever we are entering **extra data** for the "patients" label. 

Next, we click on the "males" label to create a new annotation, indicating that within the "patients" / "schizophrenia" subgroup, we are looking at the males.
Finally, we click on the "count" label to create a new annotation, indicating the type of information contained in our selected text.
If needed, we can use the **extra data** here again -- for example if the count was indicated as "twenty" (in English), we would enter in the **extra data** "20" (the value in numbers), to make it easier to use the annotation later.

So to summarize, the steps are:

- Select the group ("patients" or "healthy")
- Enter the subgroup identifier in the "extra data" field (with the help of the completion list if we have seen that subgroup before)
- Select the sex ("females" or "males")
- Select the label that indicates the type of information ("count", "age mean", etc.)
- If necessary add any complementary information in the "extra data" field (eg "20" when the selected text is "twenty").

When we annotate information about nodes that are higher in the participant group tree, we simply omit the labels that do not apply.
For example, if we are annotating the total count of participants (healthy and patients), we simply apply the label "count", without indicating a group, subgroup or sex.
As we see below, when we select the diagnosis, we only indicate the group and subgroup, as the diagnosis applies to both males and females.

Here are all the annotations for article discussed above, **PMC8883821**:

```{code-cell}
:tags: [remove-input]

show_pmcid(8883821)
```

### A simpler example

When the participant structure of an article is simpler, we can omit any of the labels as long as it does not introduce an ambiguity.
For example, if there is only one group of patients, we do not need to indicate a subgroup.

Below is an example for the article **PMC3447931** where only the count is provided, for the patients and for the healthy controls.
Note that "diagnosis" implicitly refers to patients, so we can omit the group label here (but would not be an error to add it).

```{code-cell}
:tags: [remove-input]

show_pmcid(3447931)
```


## Participant demographics summaries

The repository contains utilities to extract summaries about the participant groups from an article's annotations.

- `scripts/participants_report.py` creates a report for all the articles in a `.labelbuddy` file, similar to the list shown below.
- `scripts/watch_participants.py` serves a live summary of the participant groups in the document we are currently annotating in **labelbuddy**.

Below we show the information about participants that has been extracted from all the annotated documents (all projects and annotators).

```{code-cell}
:tags: [remove-input]

html = participant_demographics.get_report_for_repo(remove_failed_docs=True)
displays.HTMLDisplay(html)
```

