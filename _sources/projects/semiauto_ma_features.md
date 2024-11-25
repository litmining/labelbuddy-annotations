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
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">TaskName (14 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … on inter-individual variability in the normal population remains unknown. Considering some cognitive tasks that have been extensively described in the neuroimaging literature, we chose to include: a <mark class="annotated-text">mental calculation task</mark> to investigate superior fronto-parietal networks [ ] and a language comprehension task which focuses on the inferior frontal and superior temporal lobes [ ]. Using auditory and visual stimulation all…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ing some cognitive tasks that have been extensively described in the neuroimaging literature, we chose to include: a mental calculation task to investigate superior fronto-parietal networks [ ] and a <mark class="annotated-text">language comprehension task </mark>which focuses on the inferior frontal and superior temporal lobes [ ]. Using auditory and visual stimulation allows us to isolate cortical pathways associated with perceptual processing (superior temp…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … mixed together and presented successively in a fixed order, which appeared random to the subject (Figure  ), with the E-Prime software (Psychology Software Tool, Inc.): 1-passive viewing of flashing <mark class="annotated-text">horizontal checkerboards</mark> (10 trials), 2-passive viewing of flashing vertical checkerboards (10 trials), 3-pressing three times the left button with the left thumb button according to visual instructions (5 trials), 4-pressin…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ppeared random to the subject (Figure  ), with the E-Prime software (Psychology Software Tool, Inc.): 1-passive viewing of flashing horizontal checkerboards (10 trials), 2-passive viewing of flashing <mark class="annotated-text">vertical checkerboards</mark> (10 trials), 3-pressing three times the left button with the left thumb button according to visual instructions (5 trials), 4-pressing three times the right button according to visual instruction (5 …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … according to more than one contrast. Eight contrasts of interest were selected: right vs. left hand action, vertical vs. horizontal checkerboards, auditory stimuli vs. rest, visual stimuli vs. rest, <mark class="annotated-text">auditory calculations</mark> vs. auditory non-numerical stimuli, visual calculations vs. visual non-numerical stimuli, auditory stimuli vs. visual stimuli and visual stimuli vs. checkerboards. 


### Data acquisition and process…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nterest were selected: right vs. left hand action, vertical vs. horizontal checkerboards, auditory stimuli vs. rest, visual stimuli vs. rest, auditory calculations vs. auditory non-numerical stimuli, <mark class="annotated-text">visual calculations</mark> vs. visual non-numerical stimuli, auditory stimuli vs. visual stimuli and visual stimuli vs. checkerboards. 


### Data acquisition and processing 
  
Functional images were acquired on a 3T Brucker …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … with the AC-PC line, TE/TR = 31/333 ms, flip angle 30°, multiband factor 8, bandwith = 1776 Hz/Pixel) collecting 1200 volumes. Subsequently, the same EPI sequence was used during a commonly employed <mark class="annotated-text">matching task</mark>  designed to activate the amygdala. Subjects were shown triplets of geometric shapes (as neutral stimuli) and of threatening scenes as well as fearful faces (as emotional conditions) presented in alt…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4440210/"
                                       >PMC4440210</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …omparison purposes. This dataset was also acquired at Medical University of Vienna, and comprised anatomical images using the same MPRAGE sequence as above, as well as functional scans using the same <mark class="annotated-text">emotional matching task</mark> as above, but acquired with a 12 channel head coil and a standard (i.e., non-multiband) single-shot EPI sequence with a TR of 2 s, totalling 280 volumes (TE/TR = 42/2000 ms, 96 × 96 matrix, 210 mm sq…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4440210/"
                                       >PMC4440210</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …, participants were asked several debriefing questions. 


### Materials and Apparatus 
  
#### Composite Letter Task with Motivation Manipulation 
  
Participants completed a modified version of the <mark class="annotated-text">composite letter task</mark>, in which the ratio of global to local targets changes across blocks of trials [ ]. In this task, participants were presented with a large letter composed of several smaller letters (e.g. a T made of…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4441475/"
                                       >PMC4441475</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
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
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">Modality-fMRI-BOLD (12 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …y). First, a high-resolution anatomical image was acquired using MPRAGE with 1 × 1 × 1.1 mm  resolution, and 160 sagittal slices (TE/TR = 4.21/2300 ms, flip angle 90°, inversion time 900 ms). Second, <mark class="annotated-text">BOLD</mark> fluctuations at rest were measured with an advanced, low-TR multi-band EPI-sequence  using 1.7 × 1.7 × 2 mm  resolution, 2 mm slice gap (matrix size 128 × 128, 32 axial slices aligned with the AC-PC …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4440210/"
                                       >PMC4440210</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …t the University of Oregon’s Robert and Beverly Lewis Center for Neuroimaging. The task described here involved 4 functional runs of T2*-weighted blood oxygenation level dependent echo-planar images (<mark class="annotated-text">BOLD</mark>-EPI; TR = 2000 ms; TE = 30 ms; flip angle = 80°; matrix size = 64 x 64; 32 axial slices with interleaved acquisition; slice thickness = 4mm; field of view = 200 mm; in-plane resolution = 3.125 x 3.12…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4441475/"
                                       >PMC4441475</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
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
            
            <div class="annotation">
                <div class="context">
                    … (MAGNETOM Skyra, Siemens Healthcare, Erlangen, Germany) and a 32‐channel receiving head coil. Whole brain functional data were acquired with a T2*‐weighted echoplanar (EPI) sequence sensitive to the <mark class="annotated-text">BOLD</mark>‐contrast (TR 2000 ms, echo time (TE) 30 ms, flip angle 76°, field of view (FOV) 220 mm, 3.4‐mm slice thickness, 37 oblique slices acquired in ascending order covering the whole brain in plane resolut…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5607552/"
                                       >PMC5607552</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …r in computer vision. Visual dissimilarities between image stimuli were then calculated based on the selected image representation and were entered as covariates in the general linear models relating <mark class="annotated-text">BOLD</mark> pattern dissimilarities to dissimilarities between sets of personal semantic tags and vividness judgments (described later). 

All images were resized to 640 × 480. The color histogram and color corr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6175904/"
                                       >PMC6175904</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …(for a detailed description see section “    – Button Box Responses”). 


### fMRI Data Acquisition and Analysis 
  
#### Acquisition Parameter 
  
In Basel, whole-brain blood oxygen level-dependent (<mark class="annotated-text">BOLD</mark>) fMRI data and structural T1-weighted magnetization prepared rapid gradient echo imaging images were acquired on a Siemens 3T Prisma MRI system using a 20-channel phased-array radio frequency head co…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6200838/"
                                       >PMC6200838</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … were run independently (though at the same time) and not linked. For MR signal reception, system-provided receive-only 8-element surface coil head coils were used. Blood-oxygenation level-dependent (<mark class="annotated-text">BOLD</mark>) fMRI scans were obtained with a single-shot gradient-recalled EPI sequence with sensitivity encoding (SENSE). The following EPI parameters were used: FOV/slice/gap = 240/2.9/0 mm, 41 axial slices pe…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7018765/"
                                       >PMC7018765</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nel head coil. T1-weighted structural images were acquired using a 3D MPRAGE sequence: 1 × 1 × 1 mm resolution voxels; 176 sagittal slices, 256 × 224 matrix; TR = 2530 ms; TE = 3.34 ms; TI = 1100 ms. <mark class="annotated-text">BOLD</mark> T2 -weighted functional images were acquired using a gradient-echo EPI pulse sequence: 3 × 3 × 3 mm resolution voxels; 48 transverse slices, 64 × 74 matrix; TR = 3.36; TE = 30 ms; slice tilt = 0 degr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7377905/"
                                       >PMC7377905</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rain Research and Imaging Center (TUBRIC) using a 3.0 Tesla Siemens Prisma scanner equipped with a 20-channel phased array head coil. Functional images sensitive to blood-oxygenation-level-dependent (<mark class="annotated-text">BOLD</mark>) contrast were acquired using a single-shot T2*-weighted echo-planar imaging sequence with slices roughly parallel to the axial plane collected in descending order [repetition time (TR): 2.02 s; echo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9308012/"
                                       >PMC9308012</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">Unsure (11 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … on inter-individual variability in the normal population remains unknown. Considering some cognitive tasks that have been extensively described in the neuroimaging literature, we chose to include: a <mark class="annotated-text">mental calculation task</mark> to investigate superior fronto-parietal networks [ ] and a language comprehension task which focuses on the inferior frontal and superior temporal lobes [ ]. Using auditory and visual stimulation all…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ing some cognitive tasks that have been extensively described in the neuroimaging literature, we chose to include: a mental calculation task to investigate superior fronto-parietal networks [ ] and a <mark class="annotated-text">language comprehension task </mark>which focuses on the inferior frontal and superior temporal lobes [ ]. Using auditory and visual stimulation allows us to isolate cortical pathways associated with perceptual processing (superior temp…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … according to more than one contrast. Eight contrasts of interest were selected: right vs. left hand action, vertical vs. horizontal checkerboards, auditory stimuli vs. rest, visual stimuli vs. rest, <mark class="annotated-text">auditory calculations</mark> vs. auditory non-numerical stimuli, visual calculations vs. visual non-numerical stimuli, auditory stimuli vs. visual stimuli and visual stimuli vs. checkerboards. 


### Data acquisition and process…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nterest were selected: right vs. left hand action, vertical vs. horizontal checkerboards, auditory stimuli vs. rest, visual stimuli vs. rest, auditory calculations vs. auditory non-numerical stimuli, <mark class="annotated-text">visual calculations</mark> vs. visual non-numerical stimuli, auditory stimuli vs. visual stimuli and visual stimuli vs. checkerboards. 


### Data acquisition and processing 
  
Functional images were acquired on a 3T Brucker …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … with the AC-PC line, TE/TR = 31/333 ms, flip angle 30°, multiband factor 8, bandwith = 1776 Hz/Pixel) collecting 1200 volumes. Subsequently, the same EPI sequence was used during a commonly employed <mark class="annotated-text">matching task</mark>  designed to activate the amygdala. Subjects were shown triplets of geometric shapes (as neutral stimuli) and of threatening scenes as well as fearful faces (as emotional conditions) presented in alt…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4440210/"
                                       >PMC4440210</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …omparison purposes. This dataset was also acquired at Medical University of Vienna, and comprised anatomical images using the same MPRAGE sequence as above, as well as functional scans using the same <mark class="annotated-text">emotional matching task</mark> as above, but acquired with a 12 channel head coil and a standard (i.e., non-multiband) single-shot EPI sequence with a TR of 2 s, totalling 280 volumes (TE/TR = 42/2000 ms, 96 × 96 matrix, 210 mm sq…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4440210/"
                                       >PMC4440210</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …, participants were asked several debriefing questions. 


### Materials and Apparatus 
  
#### Composite Letter Task with Motivation Manipulation 
  
Participants completed a modified version of the <mark class="annotated-text">composite letter task</mark>, in which the ratio of global to local targets changes across blocks of trials [ ]. In this task, participants were presented with a large letter composed of several smaller letters (e.g. a T made of…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4441475/"
                                       >PMC4441475</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …cial Anxiety Scale for adolescents [ ], and the Brief Fear of Negative Evaluation-R scale [ ]. These results are not discussed in the present paper. 

Participants of the imaging sample performed the <mark class="annotated-text">story-reading phase</mark> of the SNPT-R in the MRI scanner, located at the Leiden University Medical Center (LUMC). Imaging data were collected during the story-reading phase using a Philips 3.0 T Achieva MRI scanner (Philips…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5404760/"
                                       >PMC5404760</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ants then relived their experiences in an fMRI scanner cued by images from their own lives. Representational Similarity Analysis revealed a broad network, including parts of the DMN, that represented <mark class="annotated-text">personal semantics</mark> during autobiographical reminiscence. Within this network, activity in the right precuneus reflected more detailed representations of subjective contents during vivid relative to non-vivid, recollect…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6175904/"
                                       >PMC6175904</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …periences in an fMRI scanner cued by images from their own lives. Representational Similarity Analysis revealed a broad network, including parts of the DMN, that represented personal semantics during <mark class="annotated-text">autobiographical reminiscence</mark>. Within this network, activity in the right precuneus reflected more detailed representations of subjective contents during vivid relative to non-vivid, recollection. Our results suggest a more speci…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6175904/"
                                       >PMC6175904</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">TaskDescription (9 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … ), with the E-Prime software (Psychology Software Tool, Inc.): 1-passive viewing of flashing horizontal checkerboards (10 trials), 2-passive viewing of flashing vertical checkerboards (10 trials), 3-<mark class="annotated-text">pressing three times the left button with the left thumb button according to visual instructions </mark>(5 trials), 4-pressing three times the right button according to visual instruction (5 trials), 5-pressing three times the left button according to auditory instruction (5 trials), 6-pressing three ti…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rboards (10 trials), 2-passive viewing of flashing vertical checkerboards (10 trials), 3-pressing three times the left button with the left thumb button according to visual instructions (5 trials), 4-<mark class="annotated-text">pressing three times the right button according to visual instruction (5 trials), 5-pressing three times the left button according to auditory instruction</mark> (5 trials), 6-pressing three times the right button according to auditory instruction (5 trials), 7-silently reading short visual sentences (10 trials), 8-listening to short sentences (10 trials), 9-…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ual instructions (5 trials), 4-pressing three times the right button according to visual instruction (5 trials), 5-pressing three times the left button according to auditory instruction (5 trials), 6-<mark class="annotated-text">pressing three times the right button according to auditory instruction</mark> (5 trials), 7-silently reading short visual sentences (10 trials), 8-listening to short sentences (10 trials), 9-solving silently visual subtraction problems (10 trials), 10-solving silently auditory…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …al instruction (5 trials), 5-pressing three times the left button according to auditory instruction (5 trials), 6-pressing three times the right button according to auditory instruction (5 trials), 7-<mark class="annotated-text">silently reading short visual sentences (10 trials), 8-listening to short sentences</mark> (10 trials), 9-solving silently visual subtraction problems (10 trials), 10-solving silently auditory subtraction problems (10 trials). 20 rest periods (black screen) were inserted in the sequence an…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2241626/"
                                       >PMC2241626</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e 30°, multiband factor 8, bandwith = 1776 Hz/Pixel) collecting 1200 volumes. Subsequently, the same EPI sequence was used during a commonly employed matching task  designed to activate the amygdala. <mark class="annotated-text">Subjects were shown triplets of geometric shapes (as neutral stimuli) and of threatening scenes as well as fearful faces (as emotional conditions) presented in alternating blocks of neutral and emotional stimuli.</mark> In this task-fMRI experiment, 1420 volumes were acquired. Finally, susceptibility weighted images (SWI) were acquired at 0.6 × 0.6 × 2.0 mm resolution (matrix size 384 384, 52 slices per slab, 1 slab…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4440210/"
                                       >PMC4440210</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Letter Task with Motivation Manipulation 
  
Participants completed a modified version of the composite letter task, in which the ratio of global to local targets changes across blocks of trials [ ]. <mark class="annotated-text">In this task, participants were presented with a large letter composed of several smaller letters (e.g. a T made of smaller Ls), and instructed to indicate with a button press whether the stimulus contained a T or an H. Each composite stimulus contained only one target letter (T or H), which was presented as either the large letter (global target) or the small letters (local target)</mark>. Each trial had an equal probability of having a T or H target (though the probability of a global or local target was varied systematically by block as described below). Non-target letters, which co…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4441475/"
                                       >PMC4441475</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
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
            
            <div class="annotation">
                <div class="context">
                    … refer to the subsequent presentations of the sentences in the distorted, intact and, again, in distorted form as a “D‐I‐D” stimulus set. 


### Experimental design 
  
#### Behavioral experiment 
  
<mark class="annotated-text">In the behavioral measurements, the subject was presented with 15 D‐I‐D stimulus sets. Each set comprised one block of seven distorted sentences, followed by a block of five intact sentences (a subset of the previous seven), which was followed by the same seven distorted sentences as in the first block. The presentation order of the sentences was the same in each case (notwithstanding sentence omissions in the second block). Two of the sentences were only presented in the distorted form to investigate the effect of repetition on the intelligibility of the distorted sentences. Following the presentation of each sentence, the subject used a keypad to type what he/she had heard.</mark> The experiment began with a presentation of an additional stimulus set during which the subject was familiarized with the experiment. The experiment was carried out in a soundproofed listening booth,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5607552/"
                                       >PMC5607552</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …pecified. Nine participants (all female) wore smartphone devices to record episodes from their daily lives for multiple weeks, each night indicating the personally-salient attributes of each episode. <mark class="annotated-text">Participants then relived their experiences in an fMRI scanner cued by images from their own lives.</mark> Representational Similarity Analysis revealed a broad network, including parts of the DMN, that represented personal semantics during autobiographical reminiscence. Within this network, activity in t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6175904/"
                                       >PMC6175904</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rue event-related design. Figure   summarizes the fMRI experimental design and representational similarity analysis.   
Depiction of the fMRI experiment and Representational Similarity Analysis (RSA).<mark class="annotated-text"> Participants are shown images from their own lives and are instructed to relive the associated experiences. </mark>The neural activity during this reminiscence period is analyzed using RSA to investigate whether distances between neural patterns (NeuralD ) corresponding to pairs of image cues (an example of such a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6175904/"
                                       >PMC6175904</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">Exclude-MetaAnalysis (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …Leonhard and Vogeley, Kai and Schneider, Karla and Laird, Angela R. and Langner, Robert and Eickhoff, Simon B.
Brain Struct Funct, 2012

# Title

Parsing the neural correlates of moral cognition: ALE <mark class="annotated-text">meta-analysis</mark> on morality, theory of mind, and empathy

# Keywords

Moral cognition
Theory of mind (ToM)
Empathy
Social cognition
Meta-analysis
ALE


# Abstract
 
Morally judicious behavior forms the fabric of hum…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3445793/"
                                       >PMC3445793</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
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
            
            <div class="annotation">
                <div class="context">
                    Sazhin, Daniel and Dachs, Abraham and Smith, David V.
bioRxiv, 2024

# Title

<mark class="annotated-text">Meta-Analysis</mark> Reveals That Explore-Exploit Decisions are Dissociable by Activation in the Dorsal Lateral Prefrontal Cortex, Anterior Insula, and the Anterior Cingulate Cortex

# Keywords

Exploration
Exploitation
…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10634720/"
                                       >PMC10634720</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #f7b6d2;">
        <summary class="label-display">Modality-StructuralMRI (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ing

# Keywords

brain aging
convolutional neural networks
deep learning
interpretability
neuroimaging


# Abstract
 
We present a Deep Learning framework for the prediction of chronological age from <mark class="annotated-text">structural</mark> magnetic resonance imaging scans. Previous findings associate increased brain age with neurodegenerative diseases and higher mortality rates. However, the importance of brain age prediction goes beyo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7426775/"
                                       >PMC7426775</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …. During this task we measured participants’ expectancies for social reward (anticipated feelings of social connection) or threat (anticipated feelings of rejection). On a separate day they underwent <mark class="annotated-text">structural MRI</mark>; voxel-based morphometry was used to explore the relation between social reward and threat expectancies and regional grey matter volumes (rGMV). Increased rGMV in key default-network regions involved…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7582181/"
                                       >PMC7582181</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e accomplished using independent-samples   t  -tests, and data are reported as mean ± standard deviation, unless indicated otherwise. 


### Magnetic Resonance Imaging and Voxel-Based Morphometry 
  
<mark class="annotated-text">Structural</mark> images were acquired on a 3 Tesla MR scanner using a 32-channel head coil (Skyra, Siemens Healthcare, Erlangen, Germany). All data were acquired on the identical scanner, and used one of two 3D-MPRag…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8564184/"
                                       >PMC8564184</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">DesignType-RestingState (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …Functional connectivity
Anterior temporal lobe
Inferior frontal gyrus
Visual word form area
Semantics
Verbal fluency


# Abstract
  Highlights  
  
Variations in semantic performance are reflected in <mark class="annotated-text">resting-state</mark> networks. 
  
Inferior frontal connectivity predicts verbal fluency performance. 
  
Connectivity between visual and anterior temporal areas predicts synonym judgement. 
  
  
Efficient semantic cogn…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5090046/"
                                       >PMC5090046</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ols were as follows: T1 MPRAGE (TR/TE/TI: 2000/3.62/845 ms, FoV: 256 mm, voxel size: 0.8 mm  × 0.8 mm  × 0.8 mm ), T2 SPACE (TR/TE: 3200/409 ms, FoV: 256 mm, voxel size: 0.8 mm  × 0.8 mm  × 0.8 mm ), <mark class="annotated-text">resting-state</mark> fMRI (TR/TE: 2000/30 ms, FoV: 240 mm, 180 measurements, voxel size: 3 mm  × 3 mm  × 3 mm ), diffusion MRI (TR/TE: 8000/92 ms, FoV: 220 mm, voxel size: 2 mm  × 2 mm  × 2 mm , b-value: 1,000 s/mm  in 6…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9202476/"
                                       >PMC9202476</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #dbdb8d;">
        <summary class="label-display">None (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …et included 40 (20 males, age range, 17–20 years, age, 19.10 ± 0.80 years, mean ± SD) right-handed participants. The multimodal MRI data of 40 healthy adults were acquired using a 3.0 T GE MR Scanner <mark class="annotated-text">(see   for a full description of the data sample and acquisition parameters)</mark>. 


### Initial Seed Masks Definition 
  
First, each subject&#39;s   T   image was parcellated into 34 cortical regions of interest (ROIs) per hemisphere and 14 subcortical ROIs based on the Desikan–Kil…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4961028/"
                                       >PMC4961028</a></div>
                    <div class="annotator-name">alice_chen</div>
                </div>
            </div>
            
        </div>
        
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
