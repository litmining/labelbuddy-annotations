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


# parkinsons

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/parkinsons/).

## `<Project Name>`

`<1-2 sentences describing the project>`

## Papers

### How the papers were obtained
Typically with [pubget](https://neuroquery.github.io/pubget/pubget.html).
We recommend invoking `pubget` with the `--query_file` option, and storing a copy of the query file in the project's directory, or including a copy in the `README.md`.

`<description>`

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


## Annotations
### File(s) being annotated: 
- `/projects/<project_name>/documents/<documents_file1_name>.jsonl`
  - corresponding file in the pubget output: 
    - `<pubget_folder_name>/subset_allArticles_labelbuddyData/<documents_file1_name>.jsonl`
- `/projects/<project_name>/documents/<documents_file2_name>.jsonl`
  - corresponding file in the pubget output: 
    - `<pubget_folder_name>/subset_allArticles_labelbuddyData/<documents_file2_name>.jsonl`
  
### Annotation labels:
- `<label1>: <description of label1>`
- `<label2>: <description of label2>` 

### Labels found in other projects as well:
- `<label2>`

### Instructions for annotators
`<description>`




## Labels in this project



```{code-cell}
:tags: [remove-input]

from labelrepo import displays
text = """
<div class="detailed-label-set">
    
    <details >
        <summary class="label-display">_Discarded (47 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …structural MRI images obtained from subjects with Parkinson disease (PD), compared to age-matched controls. 


## Results 
  
No significant differences in volume were detected in the thalami between <mark class="annotated-text">eighteen normal subjects</mark> and eighteen PD subjects groups. However significant (p &lt; 0.03) shape differences were detected between the Left vs. Right thalami in PD, between the left thalami in PD and controls, and between the …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 18  subjects []&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2386499/"
                                       >PMC2386499</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …d from subjects with Parkinson disease (PD), compared to age-matched controls. 


## Results 
  
No significant differences in volume were detected in the thalami between eighteen normal subjects and <mark class="annotated-text">eighteen PD subjects</mark> groups. However significant (p &lt; 0.03) shape differences were detected between the Left vs. Right thalami in PD, between the left thalami in PD and controls, and between the right thalami in PD and c…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 18  subjects []&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2386499/"
                                       >PMC2386499</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …). In this study we evaluated the clinical efficacy of using putaminal atrophy in brain MRI to differentiate MSA and PD. 


## Methods 
  
We measured the putamen/caudate volume ratio on brain MRI in <mark class="annotated-text">24 patients</mark> with MSA and 21 patients with PD. Two clinicians who were blinded to the patients&#39; diagnoses and to each other&#39;s assessments measured the volume ratio using a computer program. 


## Results 
  
The …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 24  patients []&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2686861/"
                                       >PMC2686861</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ated the clinical efficacy of using putaminal atrophy in brain MRI to differentiate MSA and PD. 


## Methods 
  
We measured the putamen/caudate volume ratio on brain MRI in 24 patients with MSA and <mark class="annotated-text">21 patients</mark> with PD. Two clinicians who were blinded to the patients&#39; diagnoses and to each other&#39;s assessments measured the volume ratio using a computer program. 


## Results 
  
The measured volume ratios of…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 21  patients []&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2686861/"
                                       >PMC2686861</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …icacy of using putaminal atrophy in brain MRI to differentiate MSA and PD. 


## Methods 
  
We measured the putamen/caudate volume ratio on brain MRI in 24 patients with MSA and 21 patients with PD. <mark class="annotated-text">Two clinicians who were blinded to the patients</mark>&#39; diagnoses and to each other&#39;s assessments measured the volume ratio using a computer program. 


## Results 
  
The measured volume ratios of the two investigators were highly correlated (  r  =0.72…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 2  patients []&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2686861/"
                                       >PMC2686861</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …highly correlated (  r  =0.72,   p  &lt;0.0001). The volume ratio was significantly lower in MSA (1.29±0.28) than PD (1.91±0.29,   p  &lt;0.0001). Setting an arbitrary cutoff ratio of 1.6 resulted in about <mark class="annotated-text">90% of patients</mark> with MSA falling into the group with a lower ratio, whereas more than 80% of patients with PD belonged to the other group. 


## Conclusions 
  
The present results demonstrate that putaminal atrophy…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 90  patients []&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2686861/"
                                       >PMC2686861</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … in MSA (1.29±0.28) than PD (1.91±0.29,   p  &lt;0.0001). Setting an arbitrary cutoff ratio of 1.6 resulted in about 90% of patients with MSA falling into the group with a lower ratio, whereas more than <mark class="annotated-text">80% of patients</mark> with PD belonged to the other group. 


## Conclusions 
  
The present results demonstrate that putaminal atrophy in MSA as measured on brain MRI represents an effective tool for differentiating MSA …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 80  patients []&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2686861/"
                                       >PMC2686861</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …al alterations in the brains of individuals with mild-moderate PD we quantified neurochemical profiles of the pons, putamen and substantia nigra by 7 tesla (T) proton magnetic resonance spectroscopy. <mark class="annotated-text">Thirteen individuals</mark> with idiopathic PD (Hoehn &amp; Yahr stage 2) and 12 age- and gender-matched healthy volunteers participated in the study. γ-Aminobutyric acid (GABA) concentrations in the pons and putamen were significa…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 13  individuals []&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3266292/"
                                       >PMC3266292</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e quantified neurochemical profiles of the pons, putamen and substantia nigra by 7 tesla (T) proton magnetic resonance spectroscopy. Thirteen individuals with idiopathic PD (Hoehn &amp; Yahr stage 2) and <mark class="annotated-text">12 age- and gender-matched healthy volunteers</mark> participated in the study. γ-Aminobutyric acid (GABA) concentrations in the pons and putamen were significantly higher in patients (N = 11, off medications) than controls (N = 11, p&lt;0.001 for pons an…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 12 healthy volunteers []&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3266292/"
                                       >PMC3266292</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …cally to determine if alterations in neurotransmitter levels similar to those observed in animal models of PD would be detectable in patients with mild-moderate PD. 


## Methods 
  
### Subjects 
  
<mark class="annotated-text">Thirteen individuals</mark> with mild–moderate PD (6 women and 7 men, 56±10 years old, mean±SD) and 12 age-matched healthy volunteers (7 women and 5 men, 54±8 years old) participated in the study after giving written informed c…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 13  individuals [&lt;ParticipantsSubGroup: 6 women&gt;, &lt;ParticipantsSubGroup: 7 men&gt;, &lt;AgeMoments: 56.0 ± 10.0&gt;]&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3266292/"
                                       >PMC3266292</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">ParticipantsInfo (34 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">v</mark>an der Hoorn, Anouk and Renken, Remco J. and Leenders, Klaus L. and de Jong, Bauke M.
PLoS One, 2014

# Title

Parkinson-Related Changes of Activation in Visuomotor Brain Regions during Perceived Forw…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;22 participants: [&lt;22 patients (PATIENT) ()&gt;]&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3995937/"
                                       >PMC3995937</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">W</mark>elter, Marie-Laure and Schüpbach, Michael and Czernecki, Virginie and Karachi, Carine and Fernandez-Vidal, Sara and Golmard, Jean-Louis and Serra, Giulia and Navarro, Soledad and Welaratne, Arlette an…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;309 participants: [&lt;309 patients (PATIENT) ()&gt;]&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4001189/"
                                       >PMC4001189</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">C</mark>hung, Eun Joo and Kim, Eung Gyu and Bae, Jong Seok and Eun, Choong Ki and Lee, Kwang Sig and Oh, Minkyung and Kim, Sang Jin
J Mov Disord, 2009

# Title

Usefulness of Diffusion-Weighted MRI for Differ…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;12 participants: [&lt;12 patients (PATIENT) ()&gt;]&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4027714/"
                                       >PMC4027714</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Q</mark>uattrocchi, Carlo Cosimo and de Pandis, Maria Francesca and Piervincenzi, Claudia and Galli, Manuela and Melgari, Jean Marc and Salomone, Gaetano and Sale, Patrizio and Mallio, Carlo Augusto and Cardu…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;11 participants: [&lt;11 patients (PATIENT) (6 females, 5 males)&gt;]&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4607499/"
                                       >PMC4607499</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">A</mark>l-Hourani, Khalid and Frost, Chelsea and Mesfin, Addisu
Geriatr Orthop Surg Rehabil, 2015

# Title

Upper Cervical Epidural Abscess in a Patient With Parkinson Disease

# Keywords

upper cervical
oste…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;66 participants: [&lt;66 male ()&gt;]&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4647191/"
                                       >PMC4647191</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">L</mark>in, Wei-Che and Chen, Pei-Chin and Huang, Yung-Cheng and Tsai, Nai-Wen and Chen, Hsiu-Ling and Wang, Hung-Chen and Lin, Tsu-Kung and Chou, Kun-Hsien and Chen, Meng-Hsiang and Chen, Yi-Wen and Lu, Chen…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;34 participants: [&lt;34 patients (PATIENT) (21 females, 13 males, mean age = 62.18)&gt;]&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4748867/"
                                       >PMC4748867</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">N</mark>agae, Lidia M. and Honce, Justin M. and Tanabe, Jody and Shelton, Erika and Sillau, Stefan H. and Berman, Brian D.
Front Neuroanat, 2016

# Title

Microstructural Changes within the Basal Ganglia Diff…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;41 participants: [&lt;20 controls (HEALTHY) ()&gt;, &lt;21 patients (PATIENT) ()&gt;]&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4763054/"
                                       >PMC4763054</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">L</mark>u, Yan-Ting and Chang, Wen-Neng and Chang, Chiung-Chih and Lu, Cheng-Hsien and Chen, Nai-Ching and Huang, Chi-Wei and Lin, Wei-Che and Chang, Ya-Ting
Parkinsons Dis, 2016

# Title

Insula Volume and S…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;23 participants: [&lt;23 patients (PATIENT) ()&gt;]&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4779527/"
                                       >PMC4779527</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">M</mark>akovac, Elena and Cercignani, Mara and Serra, Laura and Torso, Mario and Spanò, Barbara and Petrucci, Simona and Ricciardi, Lucia and Ginevrino, Monia and Caltagirone, Carlo and Bentivoglio, Anna Rita…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;30 participants: [&lt;8 patients (PATIENT) (mean age = 51.4)&gt;, &lt;22 controls (HEALTHY) (mean age = 47.0)&gt;]&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5082970/"
                                       >PMC5082970</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">R</mark>ittman, Timothy and Rubinov, Mikail and Vértes, Petra E. and Patel, Ameera X. and Ginestet, Cedric E. and Ghosh, Boyd C.P. and Barker, Roger A. and Spillantini, Maria Grazia and Bullmore, Edward T. an…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;128 participants: [&lt;128 subjects ()&gt;]&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5096886/"
                                       >PMC5096886</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">ParticipantsGroupInfo (34 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … effects of optic flow on motor-related cerebral circuitry were explored with functional magnetic resonance imaging in healthy controls (HC) and patients with Parkinson’s disease (PD). Fifteen HC and <mark class="annotated-text">22 PD patients</mark>, of which 7 experienced freezing of gait (FOG), watched wide-field flow, interruptions by narrowing or deceleration and equivalent control conditions with static dots. Statistical parametric mapping …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;22 patients (PATIENT) ()&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3995937/"
                                       >PMC3995937</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …es, surgical procedure, and locations of stimulating contacts that might help us to define the best target for a given patient. 

## METHODS 
  
### Patients. 
  
Between February 1996 and July 2009, <mark class="annotated-text">309 patients</mark> with PD underwent DBS-STN at the Pitié-Salpêtrière Hospital (Paris, France). Patients were deemed suitable for surgery according to the following criteria : (1) age younger than 70 years (mean age: 5…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;309 patients (PATIENT) ()&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4001189/"
                                       >PMC4001189</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e usefulness of DWI by using the rADC for differential diagnosis between MSA-p and PD and investigated the correlation between the rADC value and clinical features of MSA-p and PD. 


## Methods: 
  
<mark class="annotated-text">Twelve patients</mark> with PD and 10 with MSA-p were studied. The rADC value was determined in different brain regions, including the dorsal putamen (DP) and middle cerebellar peduncles (MCP). 


## Results: 
  
The rADC …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;12 patients (PATIENT) ()&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4027714/"
                                       >PMC4027714</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …st whether measurable stimulus-specific functional connectivity changes exist after Automatic Mechanical Peripheral Stimulation (AMPS) in patients with idiopathic Parkinson Disease. 


## Methods 
  
<mark class="annotated-text">Eleven patients</mark> (6 women and 5 men) with idiopathic Parkinson Disease underwent brain fMRI immediately before and after sham or effective AMPS. Resting state Functional Connectivity (RSFC) was assessed using the see…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;11 patients (PATIENT) (6 females, 5 males)&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4607499/"
                                       >PMC4607499</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … in a patient with PD and to review upper cervical spine infection. We present the patient’s presentation, physical examination, imaging findings, and management as well a review of the literature. A <mark class="annotated-text">66-year-old male</mark> with PD presented to the emergency department (ED) following referral by a neurologist for a presumed C2 fracture. The preceding history was 1 week of severe neck pain requiring a magnetic resonance …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;66 male ()&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4647191/"
                                       >PMC4647191</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s reflected in a priori approval by the Chang Gung Memorial Hospital human research committee. All participants or their guardians provided written informed consent before participation in the study. <mark class="annotated-text">Thirty-four right-handed PD and PDD patients</mark> (13 men and 21 women, mean age: 62.18 ± 9.1 years) were prospectively enrolled in the Neurology Department of Kaohsiung Chang Gung Memorial Hospital. Patients were included if they had a definitive d…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;34 patients (PATIENT) (21 females, 13 males, mean age = 62.18)&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4748867/"
                                       >PMC4748867</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …verage of the left and right sides was used for the healthy control values when making comparisons between PD patients and healthy controls. 



## Results 
  
### Subject characteristics 
  
Healthy <mark class="annotated-text">controls (  N   = 20)</mark> and PD patients (  N   = 21) were closely matched in age (61.1 ± 9.0 vs. 61.1 ± 7.7,   p   =   0.97  ) and gender (11M:9F vs. 12M:9F,   p   = 0.89). Patient demographics broken down by motor subtype …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;20 controls (HEALTHY) ()&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4763054/"
                                       >PMC4763054</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …sides was used for the healthy control values when making comparisons between PD patients and healthy controls. 



## Results 
  
### Subject characteristics 
  
Healthy controls (  N   = 20) and PD <mark class="annotated-text">patients (  N   = 21)</mark> were closely matched in age (61.1 ± 9.0 vs. 61.1 ± 7.7,   p   =   0.97  ) and gender (11M:9F vs. 12M:9F,   p   = 0.89). Patient demographics broken down by motor subtype are shown in Table  . Disease…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;21 patients (PATIENT) ()&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4763054/"
                                       >PMC4763054</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …estigated structural brain change in subjects with a clinical diagnosis of Parkinson disease with mild cognitive impairment (PD-MCI) and examined its relationship with memory impairment.   Methods.   <mark class="annotated-text">Twenty-three PD-MCI patients</mark> were enrolled and underwent cognitive evaluation and 3-dimensional T1-weighted imaging. Voxel-based morphometry (VBM) was used to assess brain-behavior correlations and examine the relationship betwe…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;23 patients (PATIENT) ()&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4779527/"
                                       >PMC4779527</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …duals. Conversely, in HET individuals, we expected to identify preclinical FC modifications in the absence of obvious neuropsychological deficits. 


## Materials and Methods 
  
### Participants 
  
<mark class="annotated-text">Eight HOM patients</mark> (5   PINK1   and 3   Park2   mutation carriers; M/F = 6/3; mean age = 51.4, SD = 8.1 years), 12 HET relatives (10   PINK1   and 2   Park2   mutation carriers; M/F = 5/10; mean age = 40.2, SD = 14.7 y…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;8 patients (PATIENT) (mean age = 51.4)&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5082970/"
                                       >PMC5082970</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">_Mention (17 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …rmine the causes of variable outcome from deep brain stimulation of the subthalamic nucleus (DBS-STN) in patients with Parkinson disease (PD). 


## Methods: 
  
Data were obtained from our cohort of <mark class="annotated-text">309 patients</mark> with PD who underwent DBS-STN between 1996 and 2009. We examined the relationship between the 1-year motor, cognitive, and psychiatric outcomes and (1) preoperative PD clinical features, (2) MRI meas…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 309  patients []&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4001189/"
                                       >PMC4001189</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tly, we measured the correlation between clinical characteristics and rADC values in patients with both PD and MSA-p. 


## Subjects and Methods 
  
### Patients 
  
Twenty-two patients, comprised of <mark class="annotated-text">12 patients</mark> with PD and 10 patients with MSA-p, and 10 age-matched healthy controls participated in this study. Diagnosis of PD and MSA-p was performed by an experienced movement disorder specialist using establ…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 12  patients []&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4027714/"
                                       >PMC4027714</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rimental protocol of the pilot interventional study as approved by the local ethical committee.    

### Patients and clinical assessment 
  
From September 15th to October 30th 2013, we investigated <mark class="annotated-text">11 patients</mark> (6 women and 5 men) with a diagnosis of PD according to the clinical diagnostic criteria of the United Kingdom Parkinson’s disease Society Brain Bank. Inclusion criteria were: 1) age of 45 years or o…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 11  patients [&lt;ParticipantsSubGroup: 6 women&gt;, &lt;ParticipantsSubGroup: 5 men&gt;]&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4607499/"
                                       >PMC4607499</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ocol of the pilot interventional study as approved by the local ethical committee.    

### Patients and clinical assessment 
  
From September 15th to October 30th 2013, we investigated 11 patients (<mark class="annotated-text">6 women</mark> and 5 men) with a diagnosis of PD according to the clinical diagnostic criteria of the United Kingdom Parkinson’s disease Society Brain Bank. Inclusion criteria were: 1) age of 45 years or older; 2) …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;ParticipantsSubGroup: 6 women&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4607499/"
                                       >PMC4607499</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …pilot interventional study as approved by the local ethical committee.    

### Patients and clinical assessment 
  
From September 15th to October 30th 2013, we investigated 11 patients (6 women and <mark class="annotated-text">5 men</mark>) with a diagnosis of PD according to the clinical diagnostic criteria of the United Kingdom Parkinson’s disease Society Brain Bank. Inclusion criteria were: 1) age of 45 years or older; 2) a Hoehn &amp; …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;ParticipantsSubGroup: 5 men&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4607499/"
                                       >PMC4607499</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …inical scores before an after sham or effective AMPS were tested with the Wilcoxon-signed rank test for paired data by means of the SPSS software package 19.0. 



## Results 
  
### Patients 
  
The <mark class="annotated-text">11 patients</mark> enrolled in the study were randomly assigned to a sham or effective AMPS according to the cross-over design ( ). Patients showed a clinical akinesia/rigidity subtype in 72% (8/11) while a tremor subt…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 11  patients []&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4607499/"
                                       >PMC4607499</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …modifications in any of the clinical measures. ( ) 
   Demographic and clinical parameters of patients with Parkinson’s disease before and after effective AMPS and sham stimulation.        
Among the <mark class="annotated-text">11 patients</mark>, 7 (4 female, 3 men) were included for fMRI analyses of resting state functional connectivity. The exclusion of four participants was necessary because of the following reasons: one patient showed a …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 11  patients [&lt;ParticipantsSubGroup: 4 female&gt;, &lt;ParticipantsSubGroup: 3 men&gt;]&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4607499/"
                                       >PMC4607499</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … any of the clinical measures. ( ) 
   Demographic and clinical parameters of patients with Parkinson’s disease before and after effective AMPS and sham stimulation.        
Among the 11 patients, 7 (<mark class="annotated-text">4 female</mark>, 3 men) were included for fMRI analyses of resting state functional connectivity. The exclusion of four participants was necessary because of the following reasons: one patient showed a large arachno…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;ParticipantsSubGroup: 4 female&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4607499/"
                                       >PMC4607499</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e clinical measures. ( ) 
   Demographic and clinical parameters of patients with Parkinson’s disease before and after effective AMPS and sham stimulation.        
Among the 11 patients, 7 (4 female, <mark class="annotated-text">3 men</mark>) were included for fMRI analyses of resting state functional connectivity. The exclusion of four participants was necessary because of the following reasons: one patient showed a large arachnoid cyst…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;ParticipantsSubGroup: 3 men&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4607499/"
                                       >PMC4607499</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ability/gait difficulty (PIGD) subtypes. Fractional anisotropy, mean diffusivity, radial, and axial diffusivity were obtained from bilateral caudate, putamen, globus pallidus, and substantia nigra of <mark class="annotated-text">21 PD patients</mark> (12 TD and 9 PIGD) and 20 age-matched healthy controls.   T  -tests and ANOVA methods were used to compare PD patients, subtypes, and controls, and Spearman correlations tested for relationships betw…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;DetailedParticipantsGroup: 21  patients []&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4763054/"
                                       >PMC4763054</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">ParticipantsSubGroup (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …able stimulus-specific functional connectivity changes exist after Automatic Mechanical Peripheral Stimulation (AMPS) in patients with idiopathic Parkinson Disease. 


## Methods 
  
Eleven patients (<mark class="annotated-text">6 women</mark> and 5 men) with idiopathic Parkinson Disease underwent brain fMRI immediately before and after sham or effective AMPS. Resting state Functional Connectivity (RSFC) was assessed using the seed-ROI bas…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;ParticipantsSubGroup: 6 women&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4607499/"
                                       >PMC4607499</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s-specific functional connectivity changes exist after Automatic Mechanical Peripheral Stimulation (AMPS) in patients with idiopathic Parkinson Disease. 


## Methods 
  
Eleven patients (6 women and <mark class="annotated-text">5 men</mark>) with idiopathic Parkinson Disease underwent brain fMRI immediately before and after sham or effective AMPS. Resting state Functional Connectivity (RSFC) was assessed using the seed-ROI based analysi…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;ParticipantsSubGroup: 5 men&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4607499/"
                                       >PMC4607499</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Gung Memorial Hospital human research committee. All participants or their guardians provided written informed consent before participation in the study. Thirty-four right-handed PD and PDD patients (<mark class="annotated-text">13 men</mark> and 21 women, mean age: 62.18 ± 9.1 years) were prospectively enrolled in the Neurology Department of Kaohsiung Chang Gung Memorial Hospital. Patients were included if they had a definitive diagnosis…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;ParticipantsSubGroup: 13 men&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4748867/"
                                       >PMC4748867</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …al Hospital human research committee. All participants or their guardians provided written informed consent before participation in the study. Thirty-four right-handed PD and PDD patients (13 men and <mark class="annotated-text">21 women</mark>, mean age: 62.18 ± 9.1 years) were prospectively enrolled in the Neurology Department of Kaohsiung Chang Gung Memorial Hospital. Patients were included if they had a definitive diagnosis of idiopathi…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;ParticipantsSubGroup: 21 women&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4748867/"
                                       >PMC4748867</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …issue characteristics at the preexcited segment in adult WPW syndrome patients and their implicated findings. 


## Methods 
  
For this prospective study, we enrolled 22 adult WPW syndrome patients (<mark class="annotated-text">16 male</mark>, mean 45.4 ± 17.8 years) with echocardiographic findings of regional wall motion abnormality in our electrophysiology clinic. Of these patients, 14 underwent radiofrequency ablation before cardiac ma…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;ParticipantsSubGroup: 16 male&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5983519/"
                                       >PMC5983519</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">AgeMoments (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …search committee. All participants or their guardians provided written informed consent before participation in the study. Thirty-four right-handed PD and PDD patients (13 men and 21 women, mean age: <mark class="annotated-text">62.18 ± 9.1</mark> years) were prospectively enrolled in the Neurology Department of Kaohsiung Chang Gung Memorial Hospital. Patients were included if they had a definitive diagnosis of idiopathic PD  and had been foll…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;AgeMoments: 62.18 ± 9.1&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4748867/"
                                       >PMC4748867</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ns in the absence of obvious neuropsychological deficits. 


## Materials and Methods 
  
### Participants 
  
Eight HOM patients (5   PINK1   and 3   Park2   mutation carriers; M/F = 6/3; mean age = <mark class="annotated-text">51.4</mark>, SD = 8.1 years), 12 HET relatives (10   PINK1   and 2   Park2   mutation carriers; M/F = 5/10; mean age = 40.2, SD = 14.7 years) and 22 age- and gender-matched healthy controls (HC; M/F = 10/12; mea…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;AgeMoments: 51.4&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5082970/"
                                       >PMC5082970</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    ….1 years), 12 HET relatives (10   PINK1   and 2   Park2   mutation carriers; M/F = 5/10; mean age = 40.2, SD = 14.7 years) and 22 age- and gender-matched healthy controls (HC; M/F = 10/12; mean age = <mark class="annotated-text">47.0</mark>, SD = 12.3 years) took part in the study (see   for demographic, clinical and pharmacological characteristics). The diagnosis of clinically definite or probable PD was made according to the clinical …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;AgeMoments: 47.0&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5082970/"
                                       >PMC5082970</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ristics at the preexcited segment in adult WPW syndrome patients and their implicated findings. 


## Methods 
  
For this prospective study, we enrolled 22 adult WPW syndrome patients (16 male, mean <mark class="annotated-text">45.4 ± 17.8</mark> years) with echocardiographic findings of regional wall motion abnormality in our electrophysiology clinic. Of these patients, 14 underwent radiofrequency ablation before cardiac magnetic resonance i…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">&lt;AgeMoments: 45.4 ± 17.8&gt;</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5983519/"
                                       >PMC5983519</a></div>
                    <div class="annotator-name">pubextract_annotations</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```
