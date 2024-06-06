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


# semiauto_ma_features

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/semiauto_ma_features/).

## `Semi-automated fMRI Meta-Analysis features`

`Annotation of the tasks, conditions and contrasts used in an fMRI study, that would be useful to extract to help users perform a semi-automated meta-analysis in Neurosynth Compose`

## Papers

### How the papers were obtained
Papers annotated were the same as used in the participant_demographics project, in order to maximize re-usability of that dataset.

## Annotations

The goal is to annotate features useful for a semi-automated MA.
The schema of the features is inspied by NeuroVault upload schema for simplicity;

- `Modality`: imaging modality. For simplicity, this categorical variable is split onto into several labels for each level
- `TaskName`: explicit mention of a task name (e.g. Stroop). For resting-state fMRI, if no task given, highlight first char of doc and specify "rest" as task label name
- `TaskDescription`: a description of the task. Especially useful when no explicit name given
- `Condition`: a condition name (e.g. "Congruent")
- `ContrastDefinition`: a specific contrast specificaiton (e.g. "Congruent>Incongruent")

### Instructions for annotators
At least highlight all first occurances of each Condition and ContrastDefinition. If these exact phrases are repeated, you can search and highlight, or leave blank and will autofill later.
For now, skipping Discussion section, but pay attention to Table captions

To identify problem areas, all annotators will focus on the first batch at first, but then we will split across remaining batches to expediency. 




## Labels in this project



```{code-cell}
:tags: [remove-input]

from labelrepo import displays
text = """
<div class="detailed-label-set">
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">TaskName (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">TaskDescription (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">Condition (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">ContrastDefinition (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #dbdb8d;">
        <summary class="label-display">Modality-fMRI-BOLD (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">Modality-DiffusionMRI (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">Modality-StructuralMRI (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">Modality-PET (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```
