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


# autism_mri

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/autism_mri/).

## query_6b2c09de69c29c29626f794757ea4c68
 
Repo to do LabelBuddy annotations of a corpus of Autism MRI literature

## PubGet
This process was initialized with a *pubget* call:

`​`​`bash
pubget run -q "Brain Volume MRI 2022 Autism" pubget/test --labelbuddy --n_jobs 4
`​`​`

The whole `pubget` output has been uploaded to OSF: https://osf.io/meya4

## LabelBuddy
We are currently annotating the following file:

`projects/autism_mri/documents/documents_00001.jsonl`

Which in the `pubget` output corresponds to:

`query_6b2c09de69c29c29626f794757ea4c68/subset_allArticles_labelbuddyData/documents_00001.jsonl`

And writing the annotation files found in:
`projects/autism_mri/annotations/`





## Labels in this project



```{code-cell}
:tags: [remove-input]

from labelrepo import displays
text = """
<div class="detailed-label-set">
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">FieldStrength (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …d. Parents gave written informed consent and eligible participants gave assent to take part in the study. 


### Image acquisition 
  
Imaging was performed at the Alberta Children's Hospital using a <mark class="annotated-text">3</mark> Tesla MRI scanner (GE MR750w, GE Healthcare, Waukesha, WI) with a 32‐channel head coil. All participants completed the standard research neuroplasticity protocol used at this site, which included a T…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …n Inventory (BDI), Tridimensional Personality Questionnaire, and Spielberger's State-Trait Anxiety Inventory (STAI) to further characterize subjects. 


### MRI Data 
  
All scans were performed on a <mark class="annotated-text">3.0</mark>-Tesla MR system (Discovery MR750, General Electric, Milwaukee, WI, USA). Tight but comfortable foam padding was used to minimize head motion, and earplugs were used to reduce scanner noise. Resting-s…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8828908/"
                                       >PMC8828908</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …oice) by clicking a computer mouse as quickly as possible without sacrificing accuracy. Each image was displayed until a choice was made. 


### Functional Imaging 
  
Imaging took place on a Siemens <mark class="annotated-text">3</mark>T TiM Trio scanner. Two-hundred-twenty T2*-weighted echo-planar images (EPIs) (  TR   = 2,000 ms;   TE   = 30 ms;   FA   = 90°; FOV = 240 mm; slice thickness = 2.8 mm) were acquired on each of 36 cont…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">Diagnosis (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …Keywords

accident & emergency medicine
neurological injury
neuroradiology
paediatric neurology
developmental neurology & neurodisability
magnetic resonance imaging


# Abstract
 
## Introduction 
  
<mark class="annotated-text">Mild traumatic brain injury (mTBI)</mark> is highly prevalent, especially in children under 6 years. However, little research focuses on the consequences of mTBI early in development. The objective of the Kids’ Outcomes And Long-term Abiliti…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7574946/"
                                       >PMC7574946</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …d subcortical components of the early visual pathways. Social cognitive deficits, including face emotion recognition (FER) deficits, are characteristic of several neuropsychiatric disorders including <mark class="annotated-text">schizophrenia</mark> (Sz) and autism spectrum disorders (ASD). Here, we investigated potential visual sensory contributions to FER deficits in Sz (  n   = 28, 8/20 female/male; age 21–54 years) and adult ASD (  n   = 20,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s of the early visual pathways. Social cognitive deficits, including face emotion recognition (FER) deficits, are characteristic of several neuropsychiatric disorders including schizophrenia (Sz) and <mark class="annotated-text">autism spectrum disorders</mark> (ASD). Here, we investigated potential visual sensory contributions to FER deficits in Sz (  n   = 28, 8/20 female/male; age 21–54 years) and adult ASD (  n   = 20, 4/16 female/male; age 19–43 years)…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #dbdb8d;">
        <summary class="label-display">N_Patients (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …s (ADHD‐5 rating scale) and executive functioning (Behavior Rating Inventory of Executive Function (BRIEF)) were explored. Eighty‐three children were recruited (arterial ischemic stroke [AIS]   n   = <mark class="annotated-text">26</mark>; periventricular venous infarction [PVI]   n   = 26; controls   n   = 31). WM metrics were altered for stroke groups compared to controls. Along‐tract analyses showed differences in WM metrics in are…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ehavior Rating Inventory of Executive Function (BRIEF)) were explored. Eighty‐three children were recruited (arterial ischemic stroke [AIS]   n   = 26; periventricular venous infarction [PVI]   n   = <mark class="annotated-text">26</mark>; controls   n   = 31). WM metrics were altered for stroke groups compared to controls. Along‐tract analyses showed differences in WM metrics in areas approximating the lesion as well as more remote d…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tic of several neuropsychiatric disorders including schizophrenia (Sz) and autism spectrum disorders (ASD). Here, we investigated potential visual sensory contributions to FER deficits in Sz (  n   = <mark class="annotated-text">28</mark>, 8/20 female/male; age 21–54 years) and adult ASD (  n   = 20, 4/16 female/male; age 19–43 years) participants compared to neurotypical (  n   = 30, 8/22 female/male; age 19–54 years) controls using …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nia (Sz) and autism spectrum disorders (ASD). Here, we investigated potential visual sensory contributions to FER deficits in Sz (  n   = 28, 8/20 female/male; age 21–54 years) and adult ASD (  n   = <mark class="annotated-text">20,</mark> 4/16 female/male; age 19–43 years) participants compared to neurotypical (  n   = 30, 8/22 female/male; age 19–54 years) controls using task-based fMRI during an implicit static/dynamic FER task. Com…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #9edae5;">
        <summary class="label-display">N_Controls (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ory of Executive Function (BRIEF)) were explored. Eighty‐three children were recruited (arterial ischemic stroke [AIS]   n   = 26; periventricular venous infarction [PVI]   n   = 26; controls   n   = <mark class="annotated-text">31</mark>). WM metrics were altered for stroke groups compared to controls. Along‐tract analyses showed differences in WM metrics in areas approximating the lesion as well as more remote differences at midline…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ensory contributions to FER deficits in Sz (  n   = 28, 8/20 female/male; age 21–54 years) and adult ASD (  n   = 20, 4/16 female/male; age 19–43 years) participants compared to neurotypical (  n   = <mark class="annotated-text">30</mark>, 8/22 female/male; age 19–54 years) controls using task-based fMRI during an implicit static/dynamic FER task. Compared to neurotypical controls, both Sz (  d   = 1.97) and ASD (  d   = 1.13) partici…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">Age_Min (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …irth (> 36 weeks) with no evidence of additional bilateral or diffuse injury as confirmed by a pediatric neurologist and (2) MRI scan with anatomical and diffusion sequences taken between the ages of <mark class="annotated-text">6</mark>–19 years. We excluded participants with extreme head motion during the MRI scan (causing “venetian blind” artifacts that disrupted processing) or neurological conditions not attributable to the strok…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …um disorders (ASD). Here, we investigated potential visual sensory contributions to FER deficits in Sz (  n   = 28, 8/20 female/male; age 21–54 years) and adult ASD (  n   = 20, 4/16 female/male; age <mark class="annotated-text">19</mark>–43 years) participants compared to neurotypical (  n   = 30, 8/22 female/male; age 19–54 years) controls using task-based fMRI during an implicit static/dynamic FER task. Compared to neurotypical con…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #f7b6d2;">
        <summary class="label-display">Age_Max (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …th (> 36 weeks) with no evidence of additional bilateral or diffuse injury as confirmed by a pediatric neurologist and (2) MRI scan with anatomical and diffusion sequences taken between the ages of 6–<mark class="annotated-text">19</mark> years. We excluded participants with extreme head motion during the MRI scan (causing “venetian blind” artifacts that disrupted processing) or neurological conditions not attributable to the stroke. …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …eficits in Sz (  n   = 28, 8/20 female/male; age 21–54 years) and adult ASD (  n   = 20, 4/16 female/male; age 19–43 years) participants compared to neurotypical (  n   = 30, 8/22 female/male; age 19–<mark class="annotated-text">54</mark> years) controls using task-based fMRI during an implicit static/dynamic FER task. Compared to neurotypical controls, both Sz (  d   = 1.97) and ASD (  d   = 1.13) participants had significantly lower…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #dbdb8d;">
        <summary class="label-display">Scanner (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …en informed consent and eligible participants gave assent to take part in the study. 


### Image acquisition 
  
Imaging was performed at the Alberta Children's Hospital using a 3 Tesla MRI scanner (<mark class="annotated-text">GE MR750w</mark>, GE Healthcare, Waukesha, WI) with a 32‐channel head coil. All participants completed the standard research neuroplasticity protocol used at this site, which included a T1‐weighted (T W) anatomical a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …orced choice) by clicking a computer mouse as quickly as possible without sacrificing accuracy. Each image was displayed until a choice was made. 


### Functional Imaging 
  
Imaging took place on a <mark class="annotated-text">Siemens 3T TiM Trio</mark> scanner. Two-hundred-twenty T2*-weighted echo-planar images (EPIs) (  TR   = 2,000 ms;   TE   = 30 ms;   FA   = 90°; FOV = 240 mm; slice thickness = 2.8 mm) were acquired on each of 36 contiguous sli…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #9edae5;">
        <summary class="label-display">AnalysisTool (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …= 69 ms; acquisition time = 6:45). 


### Image processing 
  
Anatomical T W scans underwent segmentation into cerebrospinal fluid (CSF), gray, and white matter using Statistical Parametric Mapping (<mark class="annotated-text">SPM12</mark>; Wellcome Centre for Human Neuroimaging, UCL London). An estimate of total intracranial volume was calculated by summing volumes of CSF, gray, and white matter. Segmentations were also used to genera…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …econstructed streamlines to only white matter, termed anatomically constrained tractography (Smith et al.,  ). Anatomical scans and masks were linearly transformed into diffusion space using FSL's “  <mark class="annotated-text">FLIRT</mark>”   followed by nonlinear transformation using   “FNIRT”   (Andersson et al.,  ; Jenkinson et al.,  ). 

The FSL FDT toolbox was used to correct eddy current and small head motion for the dMRI scan (J…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …natomically constrained tractography (Smith et al.,  ). Anatomical scans and masks were linearly transformed into diffusion space using FSL's “  FLIRT”   followed by nonlinear transformation using   “<mark class="annotated-text">FNIRT</mark>”   (Andersson et al.,  ; Jenkinson et al.,  ). 

The FSL FDT toolbox was used to correct eddy current and small head motion for the dMRI scan (Jenkinson et al.,  ). Color maps showing directionality …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …cal scans and masks were linearly transformed into diffusion space using FSL's “  FLIRT”   followed by nonlinear transformation using   “FNIRT”   (Andersson et al.,  ; Jenkinson et al.,  ). 

The FSL <mark class="annotated-text">FDT</mark> toolbox was used to correct eddy current and small head motion for the dMRI scan (Jenkinson et al.,  ). Color maps showing directionality of diffusion was calculated using MRtrix3's “  dwi2tensor”   …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …n et al.,  ). 

The FSL FDT toolbox was used to correct eddy current and small head motion for the dMRI scan (Jenkinson et al.,  ). Color maps showing directionality of diffusion was calculated using <mark class="annotated-text">MRtrix3</mark>'s “  dwi2tensor”   command followed by   “tensor2metric”   (Tournier et al.,  ). Quality assurance was performed before and after color maps were generated, assessed by two researchers slice‐by‐slice…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ng through them. This streamline threshold was chosen given previous findings of reliable white matter metrics using this degree of sampling (Reid et al.,  ). Resulting tracts were binarized using   “<mark class="annotated-text">tckmap</mark>”   and then overlaid onto the tensor image where mean values of FA, MD, AD, and RD for the entire tract were extracted using   “tensor2metric”   and   “mrstats”   (Tournier et al.,  ). 


### Intrara…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …pling (Reid et al.,  ). Resulting tracts were binarized using   “tckmap”   and then overlaid onto the tensor image where mean values of FA, MD, AD, and RD for the entire tract were extracted using   “<mark class="annotated-text">tensor2metric</mark>”   and   “mrstats”   (Tournier et al.,  ). 


### Intrarater reliability 
  
To assess the reliability of ROI placements and reconstruction of tracts, extraction of mean white matter metrics for the …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Resulting tracts were binarized using   “tckmap”   and then overlaid onto the tensor image where mean values of FA, MD, AD, and RD for the entire tract were extracted using   “tensor2metric”   and   “<mark class="annotated-text">mrstats</mark>”   (Tournier et al.,  ). 


### Intrarater reliability 
  
To assess the reliability of ROI placements and reconstruction of tracts, extraction of mean white matter metrics for the anterior forceps w…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … MPRAGE sequence (  TR   = 2500 ms;   TE   = 3.5 ms; FOV = 256 mm, slice thickness = 1.0 mm, 192 slices). 

Individual cortical surfaces were rendered from the high-resolution anatomical images using <mark class="annotated-text">Freesurfer</mark> and registered to the std 0.141 fsaverage mesh ( ) with SUMA.  The pulvinar and amygdala were derived individually using a Bayesian atlas-based automated segmentation methods ( ;  ;  ) incorporated i…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …vidually using a Bayesian atlas-based automated segmentation methods ( ;  ;  ) incorporated in Freesurfer. Functional data were preprocessed and analyzed using the Analysis of Functional NeuroImages (<mark class="annotated-text">AFNI</mark>) software ( ;  ). Preprocessing consisted of concatenating data from two runs, removal of signal deviation >2.5 SDs from the mean (AFNI’s 3dDespike), temporal alignment, identification of motion outl…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">N_Total (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …structure. Associations between WM metrics and parent ratings of ADHD symptoms (ADHD‐5 rating scale) and executive functioning (Behavior Rating Inventory of Executive Function (BRIEF)) were explored. <mark class="annotated-text">Eighty‐three</mark> children were recruited (arterial ischemic stroke [AIS]   n   = 26; periventricular venous infarction [PVI]   n   = 26; controls   n   = 31). WM metrics were altered for stroke groups compared to con…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">N_Controls_Male (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … contributions to FER deficits in Sz (  n   = 28, 8/20 female/male; age 21–54 years) and adult ASD (  n   = 20, 4/16 female/male; age 19–43 years) participants compared to neurotypical (  n   = 30, 8/<mark class="annotated-text">22</mark> female/male; age 19–54 years) controls using task-based fMRI during an implicit static/dynamic FER task. Compared to neurotypical controls, both Sz (  d   = 1.97) and ASD (  d   = 1.13) participants …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">N_Controls_Female (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ry contributions to FER deficits in Sz (  n   = 28, 8/20 female/male; age 21–54 years) and adult ASD (  n   = 20, 4/16 female/male; age 19–43 years) participants compared to neurotypical (  n   = 30, <mark class="annotated-text">8</mark>/22 female/male; age 19–54 years) controls using task-based fMRI during an implicit static/dynamic FER task. Compared to neurotypical controls, both Sz (  d   = 1.97) and ASD (  d   = 1.13) participan…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">N_Patients_Male (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … several neuropsychiatric disorders including schizophrenia (Sz) and autism spectrum disorders (ASD). Here, we investigated potential visual sensory contributions to FER deficits in Sz (  n   = 28, 8/<mark class="annotated-text">20</mark> female/male; age 21–54 years) and adult ASD (  n   = 20, 4/16 female/male; age 19–43 years) participants compared to neurotypical (  n   = 30, 8/22 female/male; age 19–54 years) controls using task-b…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …z) and autism spectrum disorders (ASD). Here, we investigated potential visual sensory contributions to FER deficits in Sz (  n   = 28, 8/20 female/male; age 21–54 years) and adult ASD (  n   = 20, 4/<mark class="annotated-text">16</mark> female/male; age 19–43 years) participants compared to neurotypical (  n   = 30, 8/22 female/male; age 19–54 years) controls using task-based fMRI during an implicit static/dynamic FER task. Compared…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">N_Patients_Female (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …of several neuropsychiatric disorders including schizophrenia (Sz) and autism spectrum disorders (ASD). Here, we investigated potential visual sensory contributions to FER deficits in Sz (  n   = 28, <mark class="annotated-text">8</mark>/20 female/male; age 21–54 years) and adult ASD (  n   = 20, 4/16 female/male; age 19–43 years) participants compared to neurotypical (  n   = 30, 8/22 female/male; age 19–54 years) controls using tas…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …(Sz) and autism spectrum disorders (ASD). Here, we investigated potential visual sensory contributions to FER deficits in Sz (  n   = 28, 8/20 female/male; age 21–54 years) and adult ASD (  n   = 20, <mark class="annotated-text">4</mark>/16 female/male; age 19–43 years) participants compared to neurotypical (  n   = 30, 8/22 female/male; age 19–54 years) controls using task-based fMRI during an implicit static/dynamic FER task. Compa…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883821/"
                                       >PMC8883821</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">MRI_Modality (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …nd concomitant cognitive impairments are common but poorly understood. Rates of Attention Deficit/Hyperactivity Disorder (ADHD) are increased 5–10× and executive dysfunction can be disabling. We used <mark class="annotated-text">diffusion</mark> imaging to investigate whether stroke‐related differences in frontal white matter (WM) relate to cognitive impairments. Anterior forceps were isolated using tractography and sampled along the tract. …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8785614/"
                                       >PMC8785614</a></div>
                    <div class="annotator-name">David_Kennedy</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">discard_this_document (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">A</mark>lfahel, Leenor and Argueti-Ostrovsky, Shirel and Barel, Shir and Ali Saleh, Mahmood and Kahn, Joy and Azoulay-Ginsburg, Salome and Rothstein, Ayelet and Ebbinghaus, Simon and Gruzman, Arie and Israels…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">not about autism</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9409193/"
                                       >PMC9409193</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">N_Total_Male (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">N_Total_Female (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">Age_Mean (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```
