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


# cobidas

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/cobidas/).

## COBIDAS checklist

`<1-2 sentences describing the project>`

## Papers

### How the papers were obtained

<!-- Typically with [pubget](https://neuroquery.github.io/pubget/pubget.html).

We recommend invoking `pubget` with the `--query_file` option, and storing a copy of the query file in the project's directory, or including a copy in the `README.md`. -->

See the pubget `query.txt` file.

<!--
### Where the full papers are stored

Typically on [OSF](https://osf.io/).
Please also add a `documents/datasets.json` file containing the URL where the full `pubget` dataset can be downloaded, that looks like:
`​`​`
[
    {
    "url": "https://osf.io/download/<...>/"
    }
]
`​`​`

`<description>`
-->

<!-- 
## Annotations

### File(s) being annotated: 
- `/projects/<project_name>/documents/<documents_file1_name>.jsonl`
  - corresponding file in the pubget output: 
    - `<pubget_folder_name>/subset_allArticles_labelbuddyData/<documents_file1_name>.jsonl`
- `/projects/<project_name>/documents/<documents_file2_name>.jsonl`
  - corresponding file in the pubget output: 
    - `<pubget_folder_name>/subset_allArticles_labelbuddyData/<documents_file2_name>.jsonl`
-->

### Annotation labels:

Generated from the [COBIDAS reproschema](https://github.com/ohbm/cobidas_schema):

Created with [`/tools/create_labelbuddy_labels.py`](https://github.com/ohbm/cobidas_schema/blob/master/tools/create_labelbuddy_labels.py) .

The labels contained here could be reused to label MRI, PET or eyetracking studies. 

The labels for each subsection of the schema are stored in a separate file prefixed with a number:
for example `cobidas/5_preprocessing_labels.jsonl`.
But there is also a jsonl file that combines all labels from all sections.

<!--
### Labels found in other projects as well:
- `<label2>`

### Instructions for annotators
`<description>`
-->




## Labels in this project



```{code-cell}
:tags: [remove-input]

from labelrepo import displays
text = """
<div class="detailed-label-set">
    
    <details style="--label-color: #eeeeec;">
        <summary class="label-display">interesting (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #73fdff;">
        <summary class="label-display">PCC (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #73fdff;">
        <summary class="label-display">Alff or fAlff (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #73fdff;">
        <summary class="label-display">ReHo (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #73fdff;">
        <summary class="label-display">wavelet coherence (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #73fdff;">
        <summary class="label-display">ICs maps or networks (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #73fdff;">
        <summary class="label-display">Other (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #941100;">
        <summary class="label-display">whole-brain maps (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #941100;">
        <summary class="label-display">connectivity matrices (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #941100;">
        <summary class="label-display">network measurements (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #941100;">
        <summary class="label-display">ROI-maps (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #fffc79;">
        <summary class="label-display">AAL ROIs (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #fffc79;">
        <summary class="label-display">Atlas-based ROIs (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #fffc79;">
        <summary class="label-display">Litterature-based ROIs (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #fffc79;">
        <summary class="label-display">ICA-based ROIs (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #fffc79;">
        <summary class="label-display">Alff or ReHo based ROIs (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #fffc79;">
        <summary class="label-display">Structural connectivity-based ROIs (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #fffc79;">
        <summary class="label-display">Others (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #008f00;">
        <summary class="label-display">seed-based (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #008f00;">
        <summary class="label-display">roi-based (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #008f00;">
        <summary class="label-display">network-based (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #9437ff;">
        <summary class="label-display">supplementary file (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #9437ff;">
        <summary class="label-display">exclusions (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">toolbox (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">distortion correction (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">realignment (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">slice-timing correction (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">segmentation (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">coregistration (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">standardization (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">smoothing (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">band-pass filtering (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">nuisance regressors (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">other preprocessing (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">removed volumes (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">outliers (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">GCA (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```
