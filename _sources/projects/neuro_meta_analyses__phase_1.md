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

# neuro_meta_analyses.phase_1

See also this project's [folder on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/neuro_meta_analyses.phase_1/).



## Labels in this project

```{code-cell}
:tags: [remove-input]

from labelrepo import displays
text = """
<div class="detailed-label-set">
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">fmri (91 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Costafreda, Sergi G.
Front Neuroinformatics, 2009

# Title

Pooling <mark class="annotated-text">fMRI</mark> Data: Meta-Analysis, Mega-Analysis and Multi-Center Studies

# Keywords

fMRI
meta-analysis
mega-analysis
multi-center studies
power
false positive results
random effects analysis
study design


# Ab…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2759345/"
                                       >PMC2759345</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …gmo and Long, Xiangyu and Neumann, Jane and Maeda, Yumi and Nierhaus, Till and Liang, Fanrong and Witt, Claudia M.
PLoS One, 2012

# Title

Characterizing Acupuncture Stimuli Using Brain Imaging with <mark class="annotated-text">fMRI</mark> - A Systematic Review and Meta-Analysis of the Literature

# Keywords



# Abstract
 
## Background 
  
The mechanisms of action underlying acupuncture, including acupuncture point specificity, are n…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3322129/"
                                       >PMC3322129</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Hattingh, Coenraad J. and Ipser, J. and Tromp, S. A. and Syal, S. and Lochner, C. and Brooks, S. J. and Stein, D. J.
Front Hum Neurosci, 2012

# Title

<mark class="annotated-text">Functional magnetic resonance imaging </mark>during emotion recognition in social anxiety disorder: an activation likelihood meta-analysis

# Keywords

ALE
social anxiety
generalized social phobia
SAD
meta-analysis
fMRI


# Abstract
 
 Backgroun…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3547329/"
                                       >PMC3547329</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … Helgi B.
PLoS One, 2013

# Title

Increased Prefrontal and Parahippocampal Activation with Reduced Dorsolateral Prefrontal and Insular Cortex Activation to Food Images in Obesity: A Meta-Analysis of <mark class="annotated-text">fMRI</mark> Studies

# Keywords



# Abstract
 
## Background and Objectives 
  
Obesity is emerging as the most significant health concern of the twenty-first century. A wealth of neuroimaging data suggest that…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3622693/"
                                       >PMC3622693</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Jamadar, Sharna D. and Fielding, Joanne and Egan, Gary F.
Front Psychol, 2013

# Title

Quantitative meta-analysis of <mark class="annotated-text">fMRI</mark> and PET studies reveals consistent activation in fronto-striatal-parietal regions and cerebellum during antisaccades and prosaccades

# Keywords

antisaccade
oculomotor
functional magnetic resonance …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3797465/"
                                       >PMC3797465</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e, Charlotte L. and Hughes, Laura E. and Weaver, Chelan and Anderson, Michael C. and Rowe, James B.
Neuroimage, 2014

# Title

Selection and stopping in voluntary action: A meta-analysis and combined <mark class="annotated-text">fMRI</mark> study☆

# Keywords

FDRc, false discovery rate cluster corrected
fMRI, functional magnetic resonance imaging
preSMA, pre-supplementary motor area
RT, reaction time
SSRT, stop signal reaction time
Act…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3898966/"
                                       >PMC3898966</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Wagner, Stefanie and Sebastian, Alexandra and Lieb, Klaus and Tüscher, Oliver and Tadić, André
BMC Neurosci, 2014

# Title

A coordinate-based ALE <mark class="annotated-text">functional MRI</mark> meta-analysis of brain activation during verbal fluency tasks in healthy control subjects

# Keywords

fMRI
Coordinate-based activation likelihood estimation (ALE)
Meta-analysis
Verbal fluency
Health…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3903437/"
                                       >PMC3903437</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …. and Hoffstaedter, Felix and Clos, Mareike and Goya-Maldonado, Roberto and Gruber, Oliver and Eickhoff, Simon B.
PLoS One, 2014

# Title

Meta-Analytically Informed Network Analysis of Resting State <mark class="annotated-text">fMRI</mark> Reveals Hyperconnectivity in an Introspective Socio-Affective Network in Depression

# Keywords



# Abstract
 
Alterations of social cognition and dysfunctional interpersonal expectations are though…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3997658/"
                                       >PMC3997658</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Boccia, Maddalena and Nemmi, Federico and Guariglia, Cecilia
Neuropsychol Rev, 2014

# Title

Neuropsychology of Environmental Navigation in Humans: Review and Meta-Analysis of <mark class="annotated-text">fMRI</mark> Studies in Healthy Participants

# Keywords

fMRI
Human navigation
Meta-analysis
Frame of reference
Experimental paradigm


# Abstract
 
In the past 20 years, many studies in the cognitive neuroscien…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4010721/"
                                       >PMC4010721</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Max C. and Müller-Axt, Christa and Langner, Robert and Eickhoff, Simon B. and Forstmann, Birte U. and Neumann, Jane
Front Hum Neurosci, 2014

# Title

Brain networks of perceptual decision-making: an <mark class="annotated-text">fMRI</mark> ALE meta-analysis

# Keywords

decision-making
meta-analysis
fronto-parietal-basal ganglia


# Abstract
 
In the recent perceptual decision-making literature, a fronto-parietal network is typically r…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4063192/"
                                       >PMC4063192</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #dbdb8d;">
        <summary class="label-display">mri (63 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …nk and Lee, Yi-Chung and Tsushima, Yoshito and Alphs, Hannah and Ladd, Susanne C and Warlow, Charles and Wardlaw, Joanna M and Al-Shahi Salman, Rustam
BMJ, 2009

# Title

Incidental findings on brain <mark class="annotated-text">magnetic resonance imaging</mark>: systematic review and meta-analysis

# Keywords



# Abstract
 
 Objective   To quantify the prevalence of incidental findings on magnetic resonance imaging (MRI) of the brain. 

 Design   Systemati…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2728201/"
                                       >PMC2728201</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Debette, Stéphanie and Markus, H S
BMJ, 2010

# Title

The clinical importance of white matter hyperintensities on brain <mark class="annotated-text">magnetic resonance imaging</mark>: systematic review and meta-analysis

# Keywords



# Abstract
 
 Objectives   To review the evidence for an association of white matter hyperintensities with risk of stroke, cognitive decline, demen…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2910261/"
                                       >PMC2910261</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …us and Harbord, Roger M and Astin, Margaret and Burke, Margaret and Bessell, Alysson and Ben-Shlomo, Yoav and Hawkins, James and Hollingworth, William and Whiting, Penny
BMC Neurol, 2012

# Title

Is <mark class="annotated-text">MRI</mark> better than CT for detecting a vascular component to dementia? A systematic review and meta-analysis

# Keywords

Dementia
CT
MRI
Diagnosis
Systematic review


# Abstract
 
## Background 
  
Identifi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3403932/"
                                       >PMC3403932</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Vita, A and De Peri, L and Deste, G and Sacchetti, E
Transl Psychiatry, 2012

# Title

Progressive loss of cortical gray matter in schizophrenia: a meta-analysis and meta-regression of longitudinal <mark class="annotated-text">MRI</mark> studies

# Keywords

antipsychotics
brain morphology
longitudinal studies
magnetic resonance imaging
meta-analysis
schizophrenia


# Abstract
 
Cortical gray matter deficits have been found in patien…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3565772/"
                                       >PMC3565772</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …o and Borgwardt, Stefan and Busatto, Geraldo F
BMC Psychiatry, 2013

# Title

Structural brain changes associated with antipsychotic treatment in schizophrenia as revealed by voxel-based morphometric <mark class="annotated-text">MRI</mark>: an activation likelihood estimation meta-analysis

# Keywords

Schizophrenia
Antipsychotics
Voxel-based morphometry
Magnetic resonance imaging
Neuroimaging


# Abstract
 
## Background 
  
The resul…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3878502/"
                                       >PMC3878502</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …and Ho, B.C. and Andreasen, N.C. and Borgwardt, S.
Neurosci Biobehav Rev, 2013

# Title

Progressive brain changes in schizophrenia related to antipsychotic treatment? A meta-analysis of longitudinal <mark class="annotated-text">MRI</mark> studies

# Keywords

Psychosis
Schizophrenia
Antipsychotic
Neuroimaging
MRI
Structural
Dopamine


# Abstract
 
## Context 
  
Antipsychotic treatment is the first-line treatment option for schizophre…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3964856/"
                                       >PMC3964856</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Rao, S. M. and Martin, A. L. and Huelin, R. and Wissinger, E. and Khankhel, Z. and Kim, E. and Fahrbach, K.
Mult Scler Int, 2014

# Title

Correlations between <mark class="annotated-text">MRI</mark> and Information Processing Speed in MS: A Meta-Analysis

# Keywords



# Abstract
 
 Objectives  . To examine relationships between conventional MRI measures and the paced auditory serial addition te…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3984845/"
                                       >PMC3984845</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …oudse-Moens, Cornelieke S. H. and Leenders, Arnold G. E. and Mol, Ben Willem J. and de Haan, Timo R.
Syst Rev, 2015

# Title

Predicting developmental outcomes in premature infants by term equivalent <mark class="annotated-text">MRI</mark>: systematic review and meta-analysis

# Keywords

Premature
Preterm
Development
White matter
MRI


# Abstract
 
## Background 
  
This study aims to determine the prognostic accuracy of term MRI in v…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4438620/"
                                       >PMC4438620</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Gargiulo, Giuseppe and Sannino, Anna and Stabile, Eugenio and Perrino, Cinzia and Trimarco, Bruno and Esposito, Giovanni
PLoS One, 2015

# Title

New Cerebral Lesions at <mark class="annotated-text">Magnetic Resonance Imaging</mark> after Carotid Artery Stenting Versus Endarterectomy: An Updated Meta-Analysis

# Keywords



# Abstract
 
## Background 
  
Carotid endarterectomy (CEA) or stenting (CAS) are associated with a relati…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4446340/"
                                       >PMC4446340</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Boccia, Maddalena and Piccardi, Laura and Guariglia, Paola
Biomed Res Int, 2015

# Title

The Meditative Mind: A Comprehensive Meta-Analysis of <mark class="annotated-text">MRI</mark> Studies

# Keywords



# Abstract
 
Over the past decade mind and body practices, such as yoga and meditation, have raised interest in different scientific fields; in particular, the physiological me…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4471247/"
                                       >PMC4471247</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">exclude not brain (58 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Pan, LingLing and Han, Yuan and Sun, XiaoGuang and Liu, JianJun and Gang, Huang
J Cancer Res Clin Oncol, 2010

# Title

FDG-PET and other imaging modalities for the evaluation of <mark class="annotated-text">breast</mark> cancer recurrence and metastases: a meta-analysis

# Keywords

Recurrent and/or metastatic breast cancer
US
CT
MRI
SMM
PET
Meta-analysis


# Abstract
 
## Background and purpose 
  
Breast carcinoma …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2874488/"
                                       >PMC2874488</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Bohte, Anneloes E. and van Werven, Jochem R. and Bipat, Shandra and Stoker, Jaap
Eur Radiol, 2010

# Title

The diagnostic accuracy of US, CT, MRI and 1H-MRS for the evaluation of <mark class="annotated-text">hepatic</mark> steatosis compared with liver biopsy: a meta-analysis

# Keywords

Hepatic steatosis
Diagnostic accuracy
Magnetic resonance imaging
Magnetic resonance spectroscopy
Computed tomography
Ultrasonography…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2995875/"
                                       >PMC2995875</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …oes E. and van Werven, Jochem R. and Bipat, Shandra and Stoker, Jaap
Eur Radiol, 2010

# Title

The diagnostic accuracy of US, CT, MRI and 1H-MRS for the evaluation of hepatic steatosis compared with <mark class="annotated-text">liver</mark> biopsy: a meta-analysis

# Keywords

Hepatic steatosis
Diagnostic accuracy
Magnetic resonance imaging
Magnetic resonance spectroscopy
Computed tomography
Ultrasonography


# Abstract
 
## Objective 
…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2995875/"
                                       >PMC2995875</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …and Zhang, Yicheng and Xiong, Weining
Arch Med Sci, 2014

# Title

Positron emission tomography alone, positron emission tomography-computed tomography and computed tomography in diagnosing recurrent <mark class="annotated-text">cervical</mark> carcinoma: a systematic review and meta-analysis

# Keywords

recurrent cervical cancer
positron emission tomography
computed tomography
meta-analysis


# Abstract
 
## Introduction 
  
The aim of th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4042042/"
                                       >PMC4042042</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …iu, Jianjun and Huang, Gang and Song, Shaoli
Biomed Res Int, 2016

# Title

The Role of 18F-FDG PET/CT and MRI in Assessing Pathological Complete Response to Neoadjuvant Chemotherapy in Patients with <mark class="annotated-text">Breast Cancer</mark>: A Systematic Review and Meta-Analysis

# Keywords



# Abstract
 
 Purpose  . We performed this meta-analysis to determine the utilities of  F-FDG PET/CT and MRI in assessing the pathological comple…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4770138/"
                                       >PMC4770138</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Wang, Hong and Ma, Jingxu and Zhao, Liping and Wang, Yunling and Jia, Xiaowen
Med Sci Monit, 2016

# Title

Utility of MRI Diffusion Tensor Imaging in <mark class="annotated-text">Carpal Tunnel</mark> Syndrome: A Meta-Analysis

# Keywords

Carpal Tunnel Syndrome
Diagnosis
Diffusion Tensor Imaging
Magnetic Resonance Imaging
Peripheral Nervous System Diseases


# Abstract
 
## Background 
  
After s…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4784544/"
                                       >PMC4784544</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Chao and Zhu, Si Pin and Dai, Bing and Xiang, Guang Heng
Clinics (Sao Paulo), 2016

# Title

The value of preoperative magnetic resonance imaging in predicting postoperative recovery in patients with <mark class="annotated-text">cervical</mark> spondylosis myelopathy: a meta-analysis

# Keywords

Cervical Spondylosis Myelopathy
Magnetic Resonance Imaging
Signal Intensity Changes
Meta-Analysis


# Abstract
 
This meta-analysis was designed t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4785856/"
                                       >PMC4785856</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Shen, Guohua and Hu, Shuang and Liu, Bin and Kuang, Anren
PLoS One, 2016

# Title

Diagnostic Performance of <mark class="annotated-text">Whole-Body</mark> PET/MRI for Detecting Malignancies in Cancer Patients: A Meta-Analysis

# Keywords



# Abstract
 
## Background 
  
As an evolving imaging modality, PET/MRI is preliminarily applied in clinical prac…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4849712/"
                                       >PMC4849712</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Bennani-Baiti, Barbara and Bennani-Baiti, Nabila and Baltzer, Pascal A.
PLoS One, 2016

# Title

Diagnostic Performance of <mark class="annotated-text">Breast</mark> Magnetic Resonance Imaging in Non-Calcified Equivocal Breast Findings: Results from a Systematic Review and Meta-Analysis

# Keywords



# Abstract
 
## Objectives 
  
To evaluate the performance of …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4970763/"
                                       >PMC4970763</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Gao, Peng and Shi, Changzheng and Zhao, Lianping and Zhou, Quan and Luo, Liangping
Medicine (Baltimore), 2016

# Title

Differential diagnosis of <mark class="annotated-text">prostate</mark> cancer and noncancerous tissue in the peripheral zone and central gland using the quantitative parameters of DCE-MRI

# Keywords

dynamic contrast-enhanced
Kep
Ktrans
magnetic resonance imaging
meta-…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5207570/"
                                       >PMC5207570</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #9edae5;">
        <summary class="label-display">pet (32 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Jamadar, Sharna D. and Fielding, Joanne and Egan, Gary F.
Front Psychol, 2013

# Title

Quantitative meta-analysis of fMRI and <mark class="annotated-text">PET</mark> studies reveals consistent activation in fronto-striatal-parietal regions and cerebellum during antisaccades and prosaccades

# Keywords

antisaccade
oculomotor
functional magnetic resonance imaging
…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3797465/"
                                       >PMC3797465</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ebenthal, Einat and Desai, Rutvik H. and Humphries, Colin and Sabri, Merav and Desai, Anjali
Front Neurosci, 2014

# Title

The functional organization of the left STS: a large scale meta-analysis of <mark class="annotated-text">PET</mark> and fMRI studies of healthy adults

# Keywords

functional organization
superior temporal sulcus (STS)
left hemisphere
meta-analysis
functional magnetic resonance imaging (fMRI)
positron emission tom…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4160993/"
                                       >PMC4160993</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Paulesu, Eraldo and Danelli, Laura and Berlingeri, Manuela
Front Hum Neurosci, 2014

# Title

Reading the dyslexic brain: multiple dysfunctional routes revealed by a new meta-analysis of <mark class="annotated-text">PET</mark> and fMRI activation studies

# Keywords

developmental dyslexia
meta-analysis
fMRI
PET
ALE
hierarchical clustering


# Abstract
 
Developmental dyslexia has been the focus of much functional anatomic…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4227573/"
                                       >PMC4227573</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ang and Cai, Yiyun and Xu, Yifeng and Dutt, Anirban and Shi, Shenxun and Bramon, Elvira
BMC Psychiatry, 2014

# Title

Cerebral metabolism in major depressive disorder: a voxel-based meta-analysis of <mark class="annotated-text">positron emission tomography</mark> studies

# Keywords

Major depressive disorder
Positron emission tomography
Meta-analysis
Activation likelihood estimation


# Abstract
 
## Background 
  
Major depressive disorder (MDD) is a common…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4240898/"
                                       >PMC4240898</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s, Elizabeth and Chalkidou, Anastasia and Hammers, Alexander and Peacock, Janet and Summers, Jennifer and Keevil, Stephen
Eur J Nucl Med Mol Imaging, 2015

# Title

Diagnostic accuracy of 18F amyloid <mark class="annotated-text">PET</mark> tracers for the diagnosis of Alzheimer’s disease: a systematic review and meta-analysis

# Keywords

Florbetapir
Florbetaben
Flutemetamol
Amyloid
PET
Alzheimer’s disease


# Abstract
 
Imaging or tis…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4700091/"
                                       >PMC4700091</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Seo, Eun Hyun and Park, Woon Yeong and Choo, IL Han
Psychiatry Investig, 2017

# Title

Structural MRI and Amyloid <mark class="annotated-text">PET</mark> Imaging for Prediction of Conversion to Alzheimer's Disease in Patients with Mild Cognitive Impairment: A Meta-Analysis

# Keywords

Mild cognitive impairment
Alzheimer's disease
MRI
Meta-analysis


…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5355020/"
                                       >PMC5355020</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ng, Xiangqi and States, Lisa J. and Zhang, Zishu and Zhou, Jianhua and Farwell, Michael D. and Zhang, Paul and Xiao, Bo and Yang, Li
Medicine (Baltimore), 2017

# Title

Diagnostic accuracy of SPECT, <mark class="annotated-text">PET</mark>, and MRS for primary central nervous system lymphoma in HIV patients

# Keywords

HIV
MRS
PCNSL
PET
SPECT


# Abstract
 
Supplemental Digital Content is available in the text 
  
## Background: 
  
W…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5428578/"
                                       >PMC5428578</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Li, Ye and Jin, Guanqiao and Su, Danke
Oncotarget, 2017

# Title

Comparison of Gadolinium-enhanced MRI and 18FDG PET/<mark class="annotated-text">PET</mark>-CT for the diagnosis of brain metastases in lung cancer patients: A meta-analysis of 5 prospective studies

# Keywords

lung cancer
brain metastases
magnetic resonance imaging
positron emission tomog…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5482613/"
                                       >PMC5482613</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Zou, Yaru and Tong, Jianjing and Leng, Haiyan and Jiang, Jingwei and Pan, Meng and Chen, Zi
Oncotarget, 2017

# Title

Diagnostic value of using 18F-FDG <mark class="annotated-text">PET</mark> and PET/CT in immunocompetent patients with primary central nervous system lymphoma: A systematic review and meta-analysis

# Keywords

18F-fluorodeoxyglucose
positron emission tomography
positron em…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5522282/"
                                       >PMC5522282</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Zou, Yaru and Tong, Jianjing and Leng, Haiyan and Jiang, Jingwei and Pan, Meng and Chen, Zi
Oncotarget, 2017

# Title

Diagnostic value of using 18F-FDG PET and <mark class="annotated-text">PET</mark>/CT in immunocompetent patients with primary central nervous system lymphoma: A systematic review and meta-analysis

# Keywords

18F-fluorodeoxyglucose
positron emission tomography
positron emission t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5522282/"
                                       >PMC5522282</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #f7b6d2;">
        <summary class="label-display">CT (12 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …Roger M and Astin, Margaret and Burke, Margaret and Bessell, Alysson and Ben-Shlomo, Yoav and Hawkins, James and Hollingworth, William and Whiting, Penny
BMC Neurol, 2012

# Title

Is MRI better than <mark class="annotated-text">CT</mark> for detecting a vascular component to dementia? A systematic review and meta-analysis

# Keywords

Dementia
CT
MRI
Diagnosis
Systematic review


# Abstract
 
## Background 
  
Identification of cause…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3403932/"
                                       >PMC3403932</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Li, Ye and Jin, Guanqiao and Su, Danke
Oncotarget, 2017

# Title

Comparison of Gadolinium-enhanced MRI and 18FDG PET/PET-<mark class="annotated-text">CT</mark> for the diagnosis of brain metastases in lung cancer patients: A meta-analysis of 5 prospective studies

# Keywords

lung cancer
brain metastases
magnetic resonance imaging
positron emission tomograp…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5482613/"
                                       >PMC5482613</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Zou, Yaru and Tong, Jianjing and Leng, Haiyan and Jiang, Jingwei and Pan, Meng and Chen, Zi
Oncotarget, 2017

# Title

Diagnostic value of using 18F-FDG PET and PET/<mark class="annotated-text">CT</mark> in immunocompetent patients with primary central nervous system lymphoma: A systematic review and meta-analysis

# Keywords

18F-fluorodeoxyglucose
positron emission tomography
positron emission tomo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5522282/"
                                       >PMC5522282</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Yang, Yihan and He, Mike Z. and Li, Tao and Yang, Xuejun
Neurosurg Rev, 2017

# Title

MRI combined with PET-<mark class="annotated-text">CT</mark> of different tracers to improve the accuracy of glioma diagnosis: a systematic review and meta-analysis

# Keywords

Glioma
MRI
PET-CT
Diagnostic accuracy


# Abstract
 
Based on studies focusing on …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6503074/"
                                       >PMC6503074</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Zhang, Qing and Gao, Xian and Wei, Guohua and Qiu, Cheng and Qu, Hongyi and Zhou, Xin
J Cancer, 2019

# Title

Prognostic Value of MTV, SUVmax and the T/N Ratio of PET/<mark class="annotated-text">CT</mark> in Patients with Glioma: A Systematic Review and Meta-Analysis

# Keywords

PET/CT
MTV
SUVmax
T/N ratio
glioma
survival


# Abstract
 
 Background:   In the past decade, positron emission tomography/…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6548003/"
                                       >PMC6548003</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …and Muoio, Barbara and Nicod-Lalonde, Marie and Schaefer, Niklaus and Giovanella, Luca and Prior, John O. and Treglia, Giorgio
Diagnostics (Basel), 2019

# Title

Diagnostic Performance of PET or PET/<mark class="annotated-text">CT</mark> Using 18F-FDG Labeled White Blood Cells in Infectious Diseases: A Systematic Review and a Bivariate Meta-Analysis

# Keywords

PET
infection
18F-FDG
leukocytes
white blood cells
meta-analysis


# Abs…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6627172/"
                                       >PMC6627172</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Xiao, Jiarui and Jin, Yizi and Nie, Ji and Chen, Fukun and Ma, Xuelei
BMC Cancer, 2019

# Title

Diagnostic and grading accuracy of 18F-FDOPA PET and PET/<mark class="annotated-text">CT</mark> in patients with gliomas: a systematic review and meta-analysis

# Keywords

PET
18F-FDOPA
Glioma
Meta-analysis


# Abstract
 
## Background 
  
Positron emission tomography (PET) and PET/computed to…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6683403/"
                                       >PMC6683403</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … a foremost cause for disability and death worldwide. This study is conducted in order to compare the diagnostic values between transcranial Doppler ultrasound (ultrasonography), computed tomography (<mark class="annotated-text">CT</mark>), and magnetic resonance imaging (MRI) in patients suffering from ischemic stroke by performing a network meta-analysis. 


## Methods: 
  
We made use of Cochrane Library, PubMed, and Embase in orde…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6709059/"
                                       >PMC6709059</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ra and Trevisi, Gianluca and Mattoli, Maria Vittoria and Albano, Domenico and Bertagna, Francesco and Giovanella, Luca
Int J Mol Sci, 2019

# Title

Diagnostic Performance and Prognostic Value of PET/<mark class="annotated-text">CT</mark> with Different Tracers for Brain Tumors: A Systematic Review of Published Meta-Analyses

# Keywords

PET
positron emission tomography
brain tumors
glioma
brain metastases
diagnostic performance
progn…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6802483/"
                                       >PMC6802483</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Choi, Yangsean and Lee, Min Kyoung
Eur J Radiol, 2020

# Title

Neuroimaging findings of brain MRI and <mark class="annotated-text">CT</mark> in patients with COVID-19: A systematic review and meta-analysis

# Keywords

ADEM, acute disseminated encephalomyelitis
CI, confidence interval
COVID-19, coronavirus disease 2019
ICH, intracranial h…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7606068/"
                                       >PMC7606068</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">perfusion mri (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Wan, Bing and Wang, Siqi and Tu, Mengqi and Wu, Bo and Han, Ping and Xu, Haibo
Medicine (Baltimore), 2017

# Title

The diagnostic performance of <mark class="annotated-text">perfusion MRI</mark> for differentiating glioma recurrence from pseudoprogression

# Keywords

CBV
glioma recurrence
meta-analysis
perfusion MRI
pseudoprogression


# Abstract
 
## Background: 
  
The purpose of this met…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5369914/"
                                       >PMC5369914</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …anein, Sara M and Sanverdi, Eser and Golay, Xavier and Thust, Stefanie and Panovska‐Griffiths, Jasmina and Bisdas, Sotirios
Cancer Med, 2019

# Title

Diagnostic accuracy of dynamic contrast‐enhanced <mark class="annotated-text">perfusion MRI</mark> in stratifying gliomas: A systematic review and meta‐analysis

# Keywords

dynamic contrast‐enhanced MRI
gliomas
lymphoma
meta‐analysis
perfusion


# Abstract
 
## Background 
  
T1‐weighted dynamic …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6745862/"
                                       >PMC6745862</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Wang, Longlong and Wei, Lizhou and Wang, Jingjian and Li, Na and Gao, Yanzhong and Ma, Hongge and Qu, Xinran and Zhang, Ming
Medicine (Baltimore), 2020

# Title

Evaluation of <mark class="annotated-text">perfusion MRI</mark> value for tumor progression assessment after glioma radiotherapy

# Keywords

glioma
meta-analysis
perfusion magnetic resonance imaging
radiotherapy
tumor progression


# Abstract
 
## Objectives: 
 …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7769293/"
                                       >PMC7769293</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Fu, Rongwei and Szidonya, Laszlo and Barajas, Ramon F and Ambady, Prakash and Varallyay, Csanad and Neuwelt, Edward A
Neurooncol Adv, 2022

# Title

Diagnostic performance of DSC <mark class="annotated-text">perfusion MRI</mark> to distinguish tumor progression and treatment-related changes: a systematic review and meta-analysis

# Keywords

diagnostic performance
dynamic susceptibility contrast (DSC) MRI
high-grade glioma
m…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8982196/"
                                       >PMC8982196</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nd Meijer, Frederick and Smits, Marion and Henssen, Dylan
Insights Imaging, 2022

# Title

A systematic review and meta-analysis on the differentiation of glioma grade and mutational status by use of <mark class="annotated-text">perfusion-based magnetic resonance imaging</mark>

# Keywords

Dynamic contrast enhancement magnetic resonance perfusion imaging
Dynamic susceptibility contrast magnetic resonance perfusion imaging
Glioma
Molecular classification


# Abstract
 
## B…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9174367/"
                                       >PMC9174367</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Daqqaq, Tareef S. and Alhasan, Ayman S.
Neurosciences (Riyadh), 2022

# Title

Positron emission tomography and <mark class="annotated-text">perfusion weighted imaging</mark> in the detection of brain tumors recurrence

# Keywords



# Abstract
 
## Objectives: 
  
To assess and compare the diagnostic accuracy, sensitivity and specificity of perfusion-weighted imaging (PW…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9424982/"
                                       >PMC9424982</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Zhang, Jun and Wang, Yulin and Wang, Yan and Xiao, Huafeng and Chen, Xinjing and Lei, Yifei and Feng, Zhebin and Ma, Xiaodong and Ma, Lin
Quant Imaging Med Surg, 2022

# Title

<mark class="annotated-text">Perfusion magnetic resonance imaging</mark> in the differentiation between glioma recurrence and pseudoprogression: a systematic review, meta-analysis and meta-regression

# Keywords

Perfusion-weighted imaging (PWI)
glioma
tumor recurrence
ps…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9511424/"
                                       >PMC9511424</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">INTERESTING (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …Haller, Sven and Frangou, Sophia and Goodwin, Guy M. and McDonald, Colm and Kempton, Matthew J.
Neurosci Biobehav Rev, 2018

# Title

Meta-analysis of regional white matter volume in bipolar disorder <mark class="annotated-text">with replication</mark> in an independent sample using coordinates, T-maps, and individual MRI data

# Keywords

Bipolar disorder
Meta-analysis
VBM
MRI
White matter


# Abstract
  Highlights  
  
The meta-analysis revealed …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5771263/"
                                       >PMC5771263</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …schewski, Tobias and Barker, Gareth J. and Bokde, Arun L. W. and Martinot, Jean-Luc and Lemaitre, Herve and Paus, Tomáš and Millenet, Sabina and Moerkerke, Beatrijs
Front Neurosci, 2017

# Title

The <mark class="annotated-text">Influence of Study-Level Inference Models and Study Set Size</mark> on Coordinate-Based fMRI Meta-Analyses

# Keywords

coordinate-based meta-analysis
fMRI
group modeling
mixed effects models
random effects models
reliability


# Abstract
 
Given the increasing amoun…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5778144/"
                                       >PMC5778144</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ttoria and Albano, Domenico and Bertagna, Francesco and Giovanella, Luca
Int J Mol Sci, 2019

# Title

Diagnostic Performance and Prognostic Value of PET/CT with Different Tracers for Brain Tumors: A <mark class="annotated-text">Systematic Review of Published Meta-Analyses
</mark>
# Keywords

PET
positron emission tomography
brain tumors
glioma
brain metastases
diagnostic performance
prognosis
meta-analysis


# Abstract
 
Background: Several meta-analyses reporting data on the…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6802483/"
                                       >PMC6802483</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Clausen, Malene M. and Vogelius, Ivan R. and Kjær, Andreas and Bentzen, Søren M.
Diagnostics (Basel), 2020

# Title

<mark class="annotated-text">Multiple Testing, Cut-Point Optimization, and Signs of Publication Bias </mark>in Prognostic FDG–PET Imaging Studies of Head and Neck and Lung Cancer: A Review and Meta-Analysis

# Keywords

FDG–PET/CT
HNSCC
NSCLC
prognostication
publication bias


# Abstract
 
Positron emission…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7761090/"
                                       >PMC7761090</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Veronese, Mattia and Wang, Yuchuan and Cervenka, Simon
Biol Psychiatry, 2018

# Title

Positron Emission Tomography Studies of the Glial Cell Marker Translocator Protein in Patients With Psychosis: A <mark class="annotated-text">Meta-analysis Using Individual Participant Data</mark>

# Keywords

Immune activation
Meta-analysis
Microglia
Positron emission tomography
Psychosis
Schizophrenia
Translocator protein


# Abstract
 
## BACKGROUND: 
  
Accumulating evidence suggests that …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7893597/"
                                       >PMC7893597</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … M and Dimitriadis, Stavros I and Perry, Gavin and Zammit, Stan and O’Donovan, Michael C and Linden, David E
Schizophr Bull, 2021

# Title

Morphometric Analysis of Structural MRI Using Schizophrenia <mark class="annotated-text">Meta-analytic Priors Distinguish Patients from Controls</mark> in Two Independent Samples and in a Sample of Individuals With High Polygenic Risk

# Keywords

multivariate
MRI
normative modelling
schizophrenia
heterogeneity
polygenic


# Abstract
 
Schizophrenia…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8886591/"
                                       >PMC8886591</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … and Ma, Lin
Quant Imaging Med Surg, 2022

# Title

Perfusion magnetic resonance imaging in the differentiation between glioma recurrence and pseudoprogression: a systematic review, meta-analysis and <mark class="annotated-text">meta-regression
</mark>
# Keywords

Perfusion-weighted imaging (PWI)
glioma
tumor recurrence
pseudoprogression (PsP)
meta-analysis


# Abstract
 
## Background 
  
Tumor recurrence and pseudoprogression (PsP) have similar i…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9511424/"
                                       >PMC9511424</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">structural mri (6 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Seo, Eun Hyun and Park, Woon Yeong and Choo, IL Han
Psychiatry Investig, 2017

# Title

<mark class="annotated-text">Structural MRI</mark> and Amyloid PET Imaging for Prediction of Conversion to Alzheimer's Disease in Patients with Mild Cognitive Impairment: A Meta-Analysis

# Keywords

Mild cognitive impairment
Alzheimer's disease
MRI
…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5355020/"
                                       >PMC5355020</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … Jon S. and Rowe, James B. and O'Callaghan, Claire and Murray, Graham K. and Suckling, John
EClinicalMedicine, 2019

# Title

Meta-analytic Evidence for the Plurality of Mechanisms in Transdiagnostic <mark class="annotated-text">Structural MRI</mark> Studies of Hallucination Status

# Keywords

Hallucination
Structural MRI
Transdiagnostic
Meta-analysis
Systematic review
Psychiatric
Neurodegenerative


# Abstract
 
## Background 
  
Hallucinations…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6537703/"
                                       >PMC6537703</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …. and Eddy, Kamryn T. and Thomas, Jennifer J. and Holsen, Laura M. and Lawson, Elizabeth A. and Misra, Madhusmita and Lyall, Amanda E. and Breithaupt, Lauren
Syst Rev, 2021

# Title

Meta-analysis of <mark class="annotated-text">structural MRI </mark>studies in anorexia nervosa and the role of recovery: a systematic review protocol

# Keywords

Anorexia nervosa
Structural MRI
Meta-analysis
Seed-based d mapping
Recovery


# Abstract
 
## Background…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8438886/"
                                       >PMC8438886</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Zacková, Mgr. Lenka and Jáni, Mgr. Martin and Brázdil, Milan and Nikolova, Yuliya S. and Marečková, Klára
Neuroimage Clin, 2021

# Title

Cognitive impairment and depression: Meta-analysis of <mark class="annotated-text">structural magnetic resonance imaging</mark> studies

# Keywords

Meta-analysis
structural magnetic resonance imaging (MRI)
voxel-based morphometry (VBM)
Major depressive disorder
Mild cognitive impairment
Shared volumetric reductions


# Abstr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8473769/"
                                       >PMC8473769</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Lancaster, Thomas M and Dimitriadis, Stavros I and Perry, Gavin and Zammit, Stan and O’Donovan, Michael C and Linden, David E
Schizophr Bull, 2021

# Title

Morphometric Analysis of <mark class="annotated-text">Structural MRI</mark> Using Schizophrenia Meta-analytic Priors Distinguish Patients from Controls in Two Independent Samples and in a Sample of Individuals With High Polygenic Risk

# Keywords

multivariate
MRI
normative …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8886591/"
                                       >PMC8886591</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …
Neuropsychopharmacology, 2022

# Title

Common and specific large-scale brain changes in major depressive disorder, anxiety disorders, and chronic pain: a transdiagnostic multimodal meta-analysis of <mark class="annotated-text">structural</mark> and functional MRI studies

# Keywords

Psychiatric disorders
Diseases of the nervous system


# Abstract
 
Major depressive disorder (MDD), anxiety disorders (ANX), and chronic pain (CP) are closely…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8938548/"
                                       >PMC8938548</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">dmrid (6 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Bajaj, Sweta and Krismer, Florian and Palma, Jose-Alberto and Wenning, Gregor K. and Kaufmann, Horacio and Poewe, Werner and Seppi, Klaus
PLoS One, 2017

# Title

<mark class="annotated-text">Diffusion-weighted MRI</mark> distinguishes Parkinson disease from the parkinsonian variant of multiple system atrophy: A systematic review and meta-analysis

# Keywords



# Abstract
 
## Background 
  
Putaminal diffusivity in …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5747439/"
                                       >PMC5747439</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Yu, Yang and Ma, Yue and Sun, Mengyao and Jiang, Wenyan and Yuan, Tingting and Tong, Dan
Medicine (Baltimore), 2020

# Title

Meta-analysis of the diagnostic performance of <mark class="annotated-text">diffusion magnetic resonance imaging</mark> with apparent diffusion coefficient measurements for differentiating glioma recurrence from pseudoprogression

# Keywords

apparent diffusion coefficient
diffusion magnetic resonance imaging
glioma r…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7306328/"
                                       >PMC7306328</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Lv, Bin and Jing, Feng and Tian, Cheng-lin and Liu, Jian-chao and Wang, Jun and Cao, Xiang-yu and Liu, Xin-feng and Yu, Sheng-yuan
J Korean Neurosurg Soc, 2021

# Title

<mark class="annotated-text">Diffusion-Weighted Magnetic Resonance Imaging</mark> in the Diagnosis of Cerebral Venous Thrombosis : A Meta-Analysis

# Keywords

Thrombosis, Cerebral venous
Magnetic resonance imaging, Diffusion weighted
Diagnosis
Specificity
Sensitivity


# Abstract…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8128531/"
                                       >PMC8128531</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Santos, Francisco de Souza and Verma, Nupur and Watte, Guilherme and Marchiori, Edson and Mohammed, Tan-Lucien H. and Medeiros, Tássia Machado and Hochhegger, Bruno
Radiol Bras, 2021

# Title

<mark class="annotated-text">Diffusion-weighted magnetic resonance imaging</mark> for differentiating between benign and malignant thoracic lymph nodes: a meta-analysis

# Keywords

Diffusion magnetic resonance imaging
Lymphadenopathy
Lymph nodes/diagnostic imaging
Thoracic neopla…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8354191/"
                                       >PMC8354191</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Lim, Su Jin and Kim, Minjae and Suh, Chong Hyun and Kim, Sang Yeong and Shim, Woo Hyun and Kim, Sang Joon
Korean J Radiol, 2021

# Title

Diagnostic Yield of <mark class="annotated-text">Diffusion-Weighted Brain Magnetic Resonance Imaging</mark> in Patients with Transient Global Amnesia: A Systematic Review and Meta-Analysis

# Keywords

Transient global amnesia
Magnetic resonance imaging
Diffusion-weighted imaging
Systematic review and meta…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8484159/"
                                       >PMC8484159</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Carreira Figueiredo, Inês and Borgan, Faith and Pasternak, Ofer and Turkheimer, Federico E. and Howes, Oliver D.
Neuropsychopharmacology, 2022

# Title

White-matter free-water <mark class="annotated-text">diffusion MRI</mark> in schizophrenia: a systematic review and meta-analysis

# Keywords

Schizophrenia
Psychosis


# Abstract
 
White-matter abnormalities, including increases in extracellular free-water, are implicated…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9117206/"
                                       >PMC9117206</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">SPECT (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … and Tang, Xiangqi and States, Lisa J. and Zhang, Zishu and Zhou, Jianhua and Farwell, Michael D. and Zhang, Paul and Xiao, Bo and Yang, Li
Medicine (Baltimore), 2017

# Title

Diagnostic accuracy of <mark class="annotated-text">SPECT</mark>, PET, and MRS for primary central nervous system lymphoma in HIV patients

# Keywords

HIV
MRS
PCNSL
PET
SPECT


# Abstract
 
Supplemental Digital Content is available in the text 
  
## Background: …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5428578/"
                                       >PMC5428578</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …or and Stamenkovic, Mara and Kasper, Siegfried and Lanzenberger, Rupert
Transl Psychiatry, 2018

# Title

Striatal dopaminergic alterations in Tourette’s syndrome: a meta-analysis based on 16 PET and <mark class="annotated-text">SPECT</mark> neuroimaging studies

# Keywords



# Abstract
 
Despite intense research, the underlying mechanisms and the etiology of Tourette’s syndrome (TS) remain unknown. Data from molecular imaging studies t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6072751/"
                                       >PMC6072751</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … and Tamburin, Stefano
Front Neurol, 2018

# Title

Dopaminergic Neurotransmission in Patients With Parkinson's Disease and Impulse Control Disorders: A Systematic Review and Meta-Analysis of PET and <mark class="annotated-text">SPECT</mark> Studies

# Keywords

Parkinson's disease
impulse control disorder
dopamine
PET
SPECT
transporter
receptors
meta-analysis


# Abstract
 
 Background:   Around 30% Parkinson's disease (PD) patients dev…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6290338/"
                                       >PMC6290338</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">arterial spin labelling mri (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …Huang, Li and Zhang, Yusi and Li, Zuanfang and Liang, Shengxiang
Front Aging Neurosci, 2022

# Title

Aberrant pattern of regional cerebral blood flow in mild cognitive impairment: A meta-analysis of <mark class="annotated-text">arterial spin labeling magnetic resonance imaging</mark>

# Keywords

mild cognitive impairment
cerebral blood flow
arterial spin labeling
meta-analysis
activation likelihood estimation


# Abstract
 
In mild cognitive impairment (MCI), cognitive decline i…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9475306/"
                                       >PMC9475306</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Kapasouri, Efthymia Maria and Ioannidis, Diomidis C. and Cameron, Donnie and Vassiliou, Vassilios S. and Hornberger, Michael
Diagnostics (Basel), 2022

# Title

The Utility of <mark class="annotated-text">Arterial Spin Labeling MRI</mark> in Medial Temporal Lobe as a Vascular Biomarker in Alzheimer’s Disease Spectrum: A Systematic Review and Meta-Analysis

# Keywords

arterial spin labeling
cerebral blood flow
medial temporal lobe
dem…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9776573/"
                                       >PMC9776573</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">exclude not meta analysis (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ttoria and Albano, Domenico and Bertagna, Francesco and Giovanella, Luca
Int J Mol Sci, 2019

# Title

Diagnostic Performance and Prognostic Value of PET/CT with Different Tracers for Brain Tumors: A <mark class="annotated-text">Systematic Review</mark> of Published Meta-Analyses

# Keywords

PET
positron emission tomography
brain tumors
glioma
brain metastases
diagnostic performance
prognosis
meta-analysis


# Abstract
 
Background: Several meta-an…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6802483/"
                                       >PMC6802483</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … M and Dimitriadis, Stavros I and Perry, Gavin and Zammit, Stan and O’Donovan, Michael C and Linden, David E
Schizophr Bull, 2021

# Title

Morphometric Analysis of Structural MRI Using Schizophrenia <mark class="annotated-text">Meta-analytic Priors</mark> Distinguish Patients from Controls in Two Independent Samples and in a Sample of Individuals With High Polygenic Risk

# Keywords

multivariate
MRI
normative modelling
schizophrenia
heterogeneity
pol…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8886591/"
                                       >PMC8886591</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">vessel wall MRI (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Lee, Han Na and Ryu, Chang-Woo and Yun, Seong Jong
Front Neurol, 2018

# Title

<mark class="annotated-text">Vessel-Wall Magnetic Resonance Imaging</mark> of Intracranial Atherosclerotic Plaque and Ischemic Stroke: A Systematic Review and Meta-Analysis

# Keywords

magnetic resonance imaging
intracranial arteriosclerosis
plaque
brain ischemia–diagnosis…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6287366/"
                                       >PMC6287366</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …sa-Basha, Mahmud and Zhu, Chengcheng
Front Cardiovasc Med, 2021

# Title

Assessment of Therapeutic Response to Statin Therapy in Patients With Intracranial or Extracranial Carotid Atherosclerosis by <mark class="annotated-text">Vessel Wall MRI</mark>: A Systematic Review and Updated Meta-Analysis

# Keywords

vessel wall imaging
intracranial
carotid
atherosclerosis
plaque
statin


# Abstract
 
 Background and Aims:   Statin therapy is an essentia…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8578267/"
                                       >PMC8578267</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">exclude not humans (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … Pascal and Granberg, Tobias and Absinta, Martina and Lee, Nathanael J. and Lefeuvre, Jennifer A. and Reich, Daniel S.
Neuroimage Clin, 2020

# Title

Magnetic resonance imaging in multiple sclerosis <mark class="annotated-text">animal</mark> models: A systematic review, meta-analysis, and white paper

# Keywords

Systematic review
Meta-analysis
Multiple sclerosis (MS)
Magnetic resonance imaging (MRI)
Animal models
Guidelines


# Abstract…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7451445/"
                                       >PMC7451445</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">exclude incomplete (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Keuken, Max C. and Müller-Axt, Christa and Langner, Robert and Eickhoff, Simon B. and Forstmann, Birte U. and Neumann, Jane
Front Hum Neurosci, 2017

# Title

<mark class="annotated-text">Corrigendum</mark>: Brain networks of perceptual decision-making: an fMRI ALE meta-analysis

# Keywords

decision-making
meta-analysis
fronto-parietal-basal ganglia
corrigendum
GingerALE


# Abstract


# Body
 
## Intr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5360986/"
                                       >PMC5360986</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #f7b6d2;">
        <summary class="label-display">MRS (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …qi and States, Lisa J. and Zhang, Zishu and Zhou, Jianhua and Farwell, Michael D. and Zhang, Paul and Xiao, Bo and Yang, Li
Medicine (Baltimore), 2017

# Title

Diagnostic accuracy of SPECT, PET, and <mark class="annotated-text">MRS</mark> for primary central nervous system lymphoma in HIV patients

# Keywords

HIV
MRS
PCNSL
PET
SPECT


# Abstract
 
Supplemental Digital Content is available in the text 
  
## Background: 
  
We perform…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5428578/"
                                       >PMC5428578</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #dbdb8d;">
        <summary class="label-display">TMS (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Zhong, Siqian and Hu, Yiru and Fu, Yu and Cao, Liping and Zhang, Bin
BMJ Open, 2020

# Title

Functional MRI in the effect of <mark class="annotated-text">transcranial magnetic stimulation</mark> therapy for patients with schizophrenia: a meta-analysis protocol

# Keywords

neuroradiology
schizophrenia & psychotic disorders
magnetic resonance imaging


# Abstract
 
## Introduction 
  
Schizop…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7713205/"
                                       >PMC7713205</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #9edae5;">
        <summary class="label-display">ultrasound (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …d and objective: 
  
Ischemic stroke is a foremost cause for disability and death worldwide. This study is conducted in order to compare the diagnostic values between transcranial Doppler ultrasound (<mark class="annotated-text">ultrasonography</mark>), computed tomography (CT), and magnetic resonance imaging (MRI) in patients suffering from ischemic stroke by performing a network meta-analysis. 


## Methods: 
  
We made use of Cochrane Library, …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6709059/"
                                       >PMC6709059</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```