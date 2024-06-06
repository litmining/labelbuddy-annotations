# `Semi-automated fMRI Meta-Analysis features`

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
