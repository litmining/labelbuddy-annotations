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
- `TaskName_Unsure`: Use this label if the task name is not in Cognitive Atlas, but the task is mentioned in the Methods section. 
- `TaskName_None`: If the task name is not mentioned, use this label on the closest term that resembles a task name in the Methods section. 
- `TaskDescription`: If the task is not mentioned or is `TaskName_Unsure`, use this label on the phrase(s) or sentence(s) that describe the task in the Methods section. 

### Type of study
- `Meta-analysis`: If the study is a meta-analysis, use this label on the first clue that the study is a meta-analysis.
- `RestingState`: If the study is a  resting-state study, use this label on the first clue that the study is a resting-state study.
- `Review`: If the study is a review paper, use this label on the first clue that the study is a review paper.


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
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">Modality-fMRI-BOLD (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ors) the results of a PubMed search for “fMRI” and “reward” conducted by Bartra et al. ( ), which was filtered based on a number of selection criteria. Sampling only English language papers that used <mark class="annotated-text">BOLD</mark> fMRI, the authors excluded studies that use physical pain as a negative outcome, or those that use psychoactive drugs as a positive outcome. Further, they required that the study results reported a d…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5243799/"
                                       >PMC5243799</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …5), Stage 2 = 21.53 (20.50), Stage 3 = 56 (33.79). Importantly, response times did not significantly differ between learning stage;   F  (3,42) = 1.125,   P   = .350. As such, it is unlikely that any <mark class="annotated-text">BOLD</mark> effects coincident with learning stage are a result of differential reaction times. Performance on the 12 generalization trials was taken as the proportion of correct responses. Although each subject…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5324609/"
                                       >PMC5324609</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">TaskName (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …‐based generalizations is poorly understood. Using fMRI in humans, we investigated the hippocampal role in gradually learning a set of spatial discriminations and subsequently generalizing them in an <mark class="annotated-text">acquired equivalence task</mark>. We found a highly significant correlation between individuals’ performance on a generalization test and hippocampal activity during the test, providing evidence that hippocampal processes support on…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5324609/"
                                       >PMC5324609</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">TaskDescription (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …rted here used data from 15 subjects (7 male) with a mean age of 23.8 years (SD = 4.14). The study was approved by the Brighton and Sussex Medical school&#39;s Research Governance and Ethics Committee. 

<mark class="annotated-text">During scanning participants learned a set of visual discriminations via trial‐and‐error (learning phase), and were subsequently tested on their ability to generalize what they had learned (generalization phase). Both learning and generalization occurred within a single scanning session and took place in the context of a first‐person virtual reality environment (see Fig.  ). </mark>On each trial, a scene was presented depicting two buildings positioned equidistantly from a start location. One building concealed a pile of gold (the “reward”). The location of this gold was determi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5324609/"
                                       >PMC5324609</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">Exclude-MetaAnalysis (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Acikalin, M. Yavuz and Gorgolewski, Krzysztof J. and Poldrack, Russell A.
Front Neurosci, 2017

# Title

A Coordinate-Based <mark class="annotated-text">Meta-Analysis</mark> of Overlaps in Regional Specialization and Functional Connectivity across Subjective Value and Default Mode Networks

# Keywords

fMRI BOLD
metaanalysis
decision making
subjective value
default mode …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5243799/"
                                       >PMC5243799</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">DesignType-RestingState (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">Unsure (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #f7b6d2;">
        <summary class="label-display">Modality-StructuralMRI (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #dbdb8d;">
        <summary class="label-display">None (0 docs)</summary>
        
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
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">Modality-DiffusionMRI (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">Modality-PET (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #bb83c6;">
        <summary class="label-display">Exclude-Review (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```
