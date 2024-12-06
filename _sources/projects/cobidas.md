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
    
    <details style="--label-color: #ff9300;">
        <summary class="label-display">toolbox (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …2 cm , number of averages = 1, data matrix = 64 × 64, voxel size = 3.4375 × 3.4375 × 4 mm , and 180 volumes lasting for 360 s. 


### 2.3. Data preprocessing 
  
Based on MATLAB (MathWorks) platform, <mark class="annotated-text">DPABI toolbox </mark> was used to preprocess rs-fMRI data. To allow magnetic saturation, the first five volumes of data were thrown away. Next, additional preprocessing was conducted with the following procedures: (1) sli…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9892902/"
                                       >PMC9892902</a></div>
                    <div class="annotator-name">annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ownloaded on the website of Automated Human Habenula Segmentation Program  according to a previously calculated functional magnetic resonance imaging study ( ). 


### 2.5. Static FC analyses 
  
The <mark class="annotated-text">Data Processing Assistant for Resting-State fMRI Advanced Edition (DPARSFA) software package in DPABI software </mark>is used for sFC analysis. The BOLD time series of the left and right habenula was extracted respectively, then the Pearson correlation coefficients with the whole brain’s time series were measured, an…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9892902/"
                                       >PMC9892902</a></div>
                    <div class="annotator-name">annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …on coefficients with the whole brain’s time series were measured, and finally the Fisher Z transformation values were used for subsequent statistical analysis. 


### 2.6. Dynamic FC analyses 
  
The <mark class="annotated-text">Temporary Dynamic Analysis software package in DPABI software</mark> is used for dFC analysis with the sliding window method ( ), which was employed to form dFC maps for each subject. According to the recommendations on dFC in previous researches ( ), in order to opti…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9892902/"
                                       >PMC9892902</a></div>
                    <div class="annotator-name">annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …uence with the following parameters: TR = 8.1 ms, TE = 3.2 ms, matrix size = 256 × 256, flip angle = 12°, FOV = 240 × 240 mm , 176 slices, and with 1.0 mm thickness (no gap). 

Data were processed in <mark class="annotated-text">Matlab 2018b</mark> platform (MathWorks, Natick, MA) using the DPABI toolbox.  For each subject, the first 10 functional images were discarded and were then corrected for differences in slice timing and head motion. The…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9907463/"
                                       >PMC9907463</a></div>
                    <div class="annotator-name">annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    ….2 ms, matrix size = 256 × 256, flip angle = 12°, FOV = 240 × 240 mm , 176 slices, and with 1.0 mm thickness (no gap). 

Data were processed in Matlab 2018b platform (MathWorks, Natick, MA) using the <mark class="annotated-text">DPABI toolbox.</mark>  For each subject, the first 10 functional images were discarded and were then corrected for differences in slice timing and head motion. The corrected images were coregistered to the T1-weighted ana…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9907463/"
                                       >PMC9907463</a></div>
                    <div class="annotator-name">annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …l, were regressed out. 


### 2.5. Static functional connectivity analysis 
  
Based on the previous study ( ), the left TPJ seed was defined as a 10 mm radius sphere surrounding a central voxel ( ). <mark class="annotated-text">Resting-State fMRI Data Analysis (REST) toolkit</mark> ( ) was used to calculate the seed-based resting-state SFC. The Pearson correlation coefficients between the time courses of the seed and the time series of each voxel of the whole brain were calcula…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9907463/"
                                       >PMC9907463</a></div>
                    <div class="annotator-name">annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …map with Fisher’s transformations to improve the normality of the data. 
  
Graphical representation of the prior defined region of interest (left temporoparietal junction area) was defined using the <mark class="annotated-text">Marsbar toolbox </mark>(MNI: −50.7, −41.4, 22.7). 
  

### 2.6. Dynamic functional connectivity analysis 
  
The DFC was computed by using a sliding window approach through the DynamicBC toolbox ( ). DFC calculates the corr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9907463/"
                                       >PMC9907463</a></div>
                    <div class="annotator-name">annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …n area) was defined using the Marsbar toolbox (MNI: −50.7, −41.4, 22.7). 
  

### 2.6. Dynamic functional connectivity analysis 
  
The DFC was computed by using a sliding window approach through the <mark class="annotated-text">DynamicBC toolbox </mark>( ). DFC calculates the correlation of time series according to a certain length of the sliding window. Based on the previous literature ( ,  ), the length of the sliding window was set a 50 TRs, and …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9907463/"
                                       >PMC9907463</a></div>
                    <div class="annotator-name">annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ments. Whole-brain mask images were manually inspected and cleaned to remove excess parenchymal tissue using MRIcron ( ) to create a final whole-brain mask. 

BOLD fMRI images were preprocessed using <mark class="annotated-text">SPM</mark>, FSL, and warping parameters from ANTs implemented in an automated pipeline run through Matlab (The MathWorks, Natick, MA, USA). The first 10 vol were dropped to allow for signal stabilization and th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10025420/"
                                       >PMC10025420</a></div>
                    <div class="annotator-name">annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …. Whole-brain mask images were manually inspected and cleaned to remove excess parenchymal tissue using MRIcron ( ) to create a final whole-brain mask. 

BOLD fMRI images were preprocessed using SPM, <mark class="annotated-text">FSL</mark>, and warping parameters from ANTs implemented in an automated pipeline run through Matlab (The MathWorks, Natick, MA, USA). The first 10 vol were dropped to allow for signal stabilization and the ‘to…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10025420/"
                                       >PMC10025420</a></div>
                    <div class="annotator-name">annotations</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #9437ff;">
        <summary class="label-display">exclusions (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …n area) was defined using the Marsbar toolbox (MNI: −50.7, −41.4, 22.7). 
  

### 2.6. Dynamic functional connectivity analysis 
  
The DFC was computed by using a sliding window approach through the <mark class="annotated-text">DynamicBC toolbox </mark>( ). DFC calculates the correlation of time series according to a certain length of the sliding window. Based on the previous literature ( ,  ), the length of the sliding window was set a 50 TRs, and …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9907463/"
                                       >PMC9907463</a></div>
                    <div class="annotator-name">annotations</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
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
