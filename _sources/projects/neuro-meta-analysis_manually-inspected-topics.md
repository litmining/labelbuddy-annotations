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


# neuro-meta-analysis_manually-inspected-topics

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/neuro-meta-analysis_manually-inspected-topics/).

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
        <summary class="label-display">modality - task fmri (37 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Bottenhorn, <mark class="annotated-text">Katherine</mark> L and Flannery, Jessica S and Boeving, Emily R and Riedel, Michael C and Eickhoff, Simon B and Sutherland, Matthew T and Laird, Angela R
Netw Neurosci, 2019

# Title

Cooperating yet distinct brain n…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Kim, Hongkeun
Neuroimage, 2011

# Title

Neural activity that predicts subsequent memory and forgetting: a meta-analysis of 74 <mark class="annotated-text">fMRI</mark> studies.

# Keywords



# Abstract
The present study performed a quantitative meta-analysis of functional MRI studies that used a subsequent memory approach. The meta-analysis considered both subsequ…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Yaple, Zachary A and Stevens, W Dale and Arsalidou, Marie
Neuroimage, 2019

# Title

Meta-analyses of the n-back working memory task: <mark class="annotated-text">fMRI</mark> evidence of age-related changes in prefrontal cortex involvement across the adult lifespan.

# Keywords



# Abstract
Working memory, a fundamental cognitive function that is highly dependent on the …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Terry, Douglas P and Sabatinelli, Dean and Puente, A Nicolas and Lazar, Nicole A and Miller, L Stephen
J Neuroimaging, 2015

# Title

A Meta-Analysis of <mark class="annotated-text">fMRI</mark> Activation Differences during Episodic Memory in Alzheimer&#39;s Disease and Mild Cognitive Impairment.

# Keywords

Alzheimer&#39;s disease
MCI
Memory
episodic memory
fMRI
meta-analysis
mild cognitive impai…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Li, Xuqian and O&#39;Sullivan, Michael J and Mattingley, Jason B
Neuroimage, 2022

# Title

Delay activity during visual working memory: A meta-analysis of 30 <mark class="annotated-text">fMRI</mark> experiments.

# Keywords

Activation likelihood estimation
Content-specific storage
Delay period
Meta-analysis
Seed-based d mapping
Visual working memory
fMRI

# Abstract
Visual working memory refers…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Kim, Hongkeun
Hum Brain Mapp, 2019

# Title

Neural activity during working memory encoding, maintenance, and retrieval: A network-based model and meta-analysis.

# Keywords

encoding
<mark class="annotated-text">fMRI</mark>
maintenance
meta-analysis
retrieval
working memory

# Abstract
It remains unclear whether and to what extent working memory (WM) temporal subprocesses (i.e., encoding, maintenance, and retrieval) inv…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    E, Keren-Happuch and Chen, Shen-Hsing Annabel and Ho, Moon-Ho Ringo and Desmond, John E
Hum Brain Mapp, 2014

# Title

A meta-analysis of cerebellar contributions to higher cognition from PET and <mark class="annotated-text">fMRI</mark> studies.

# Keywords

cerebellum
cognition
emotion
language
meta-analysis
music
neuroimaging
timing

# Abstract
A growing interest in cerebellar function and its involvement in higher cognition have …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …wilambwe-Tshilobo, Laetitia and Spreng, R Nathan
Neuroimage, 2021

# Title

Social exclusion reliably engages the default network: A meta-analysis of Cyberball.

# Keywords

Cyberball
Default network
<mark class="annotated-text">Functional MRI
</mark>Meta-analysis
Meta-analytic connectivity modeling
Social exclusion

# Abstract
Social exclusion refers to the experience of being disregarded or rejected by others and has wide-ranging negative conseq…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ra and Almeida, Inês and Oliveiros, Bárbara and Castelo-Branco, Miguel
PLoS One, 2016

# Title

The Role of the Amygdala in Facial Trustworthiness Processing: A Systematic Review and Meta-Analyses of <mark class="annotated-text">fMRI</mark> Studies.

# Keywords



# Abstract
Faces play a key role in signaling social cues such as signals of trustworthiness. Although several studies identify the amygdala as a core brain region in social c…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …t D
Cogn Neurosci, 2021

# Title

Are there sex differences in brain activity during long-term memory? A systematic review and fMRI activation likelihood estimation meta-analysis.

# Keywords

Debate
<mark class="annotated-text">fMRI</mark>
gender
meta-analysis
recall
recognition
review
sex

# Abstract
The degree to which sex differences exist in the brain is a current topic of debate. In the present discussion paper, we reviewed eight …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition (22 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Kronbichler</mark>, Lisa and Tschernegg, Melanie and Martin, Anna Isabel and Schurz, Matthias and Kronbichler, Martin
Schizophr Bull, 2017

# Title

Abnormal Brain Activation During Theory of Mind Tasks in Schizophreni…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Bottenhorn</mark>, Katherine L and Flannery, Jessica S and Boeving, Emily R and Riedel, Michael C and Eickhoff, Simon B and Sutherland, Matthew T and Laird, Angela R
Netw Neurosci, 2019

# Title

Cooperating yet disti…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Tso</mark>, Ivy F and Rutherford, Saige and Fang, Yu and Angstadt, Mike and Taylor, Stephan F
PLoS One, 2018

# Title

The &#34;social brain&#34; is highly sensitive to the mere presence of social information: An autom…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Santos</mark>, Sara and Almeida, Inês and Oliveiros, Bárbara and Castelo-Branco, Miguel
PLoS One, 2016

# Title

The Role of the Amygdala in Facial Trustworthiness Processing: A Systematic Review and Meta-Analyses…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Robinson</mark>, Jennifer L and Salibi, Nouha and Deshpande, Gopikrishna
Neuroimage, 2016

# Title

Functional connectivity of the left and right hippocampi: Evidence for functional lateralization along the long-axi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Makovac</mark>, Elena and Fagioli, Sabrina and Rae, Charlotte L and Critchley, Hugo D and Ottaviani, Cristina
Psychiatry Res Neuroimaging, 2020

# Title

Can&#39;t get it off my brain: Meta-analysis of neuroimaging stu…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Van</mark>&#39;t Hooft, Jochum J and Pijnenburg, Yolande A L and Sikkes, Sietske A M and Scheltens, Philip and Spikman, Jacoba M and Jaschke, Artur C and Warren, Jason D and Tijms, Betty M
Brain Cogn, 2021

# Title…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Sugranyes</mark>, Gisela and Kyriakopoulos, Marinos and Corrigall, Richard and Taylor, Eric and Frangou, Sophia
PLoS One, 2011

# Title

Autism spectrum disorders and schizophrenia: meta-analysis of the neural correl…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Diveica</mark>, Veronica and Koldewyn, Kami and Binney, Richard J
Neuroimage, 2021

# Title

Establishing a role of the semantic control network in social cognitive processing: A meta-analysis of functional neuroim…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Crepaldi</mark>, Davide and Berlingeri, Manuela and Cattinelli, Isabella and Borghese, Nunzio A and Luzzatti, Claudio and Paulesu, Eraldo
Front Hum Neurosci, 2013

# Title

Clustering the lexicon in the brain: a met…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">memory (22 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Yaple</mark>, Zachary A and Stevens, W Dale and Arsalidou, Marie
Neuroimage, 2019

# Title

Meta-analyses of the n-back working memory task: fMRI evidence of age-related changes in prefrontal cortex involvement a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Murty</mark>, Vishnu P and Ritchey, Maureen and Adcock, R Alison and LaBar, Kevin S
Neuropsychologia, 2010

# Title

fMRI studies of successful emotional memory encoding: A quantitative meta-analysis.

# Keywords…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Nellessen</mark>, Nils and Rottschy, Claudia and Eickhoff, Simon B and Ketteler, Simon T and Kuhn, Hanna and Shah, N Jon and Schulz, Jörg B and Reske, Martina and Reetz, Kathrin
Brain Struct Funct, 2015

# Title

Spe…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Zhang</mark>, Zheng and Peng, Peng and Eickhoff, Simon B and Lin, Xin and Zhang, Delong and Wang, Yingying
Dev Sci, 2021

# Title

Neural substrates of the executive function construct, age-related changes, and t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Von</mark> Der Heide, Rebecca J and Skipper, Laura M and Olson, Ingrid R
Front Hum Neurosci, 2013

# Title

Anterior temporal face patches: a meta-analysis and empirical study.

# Keywords

anterior temporal lo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Kim</mark>, Hongkeun
Neuroimage, 2011

# Title

Neural activity that predicts subsequent memory and forgetting: a meta-analysis of 74 fMRI studies.

# Keywords



# Abstract
The present study performed a quanti…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Daniel</mark>, Thomas A and Katz, Jeffrey S and Robinson, Jennifer L
Biol Psychol, 2016

# Title

Delayed match-to-sample in working memory: A BrainMap meta-analysis.

# Keywords

ALE
Activation likelihood estimat…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Dahlén</mark>, Amelia D and Schofield, Aphra and Schiöth, Helgi B and Brooks, Samantha J
Front Neurosci, 2022

# Title

Subliminal Emotional Faces Elicit Predominantly Right-Lateralized Amygdala Activation: A Syst…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Terry</mark>, Douglas P and Sabatinelli, Dean and Puente, A Nicolas and Lazar, Nicole A and Miller, L Stephen
J Neuroimaging, 2015

# Title

A Meta-Analysis of fMRI Activation Differences during Episodic Memory i…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Boccia</mark>, Maddalena and Teghil, Alice and Guariglia, Cecilia
Neurosci Biobehav Rev, 2019

# Title

Looking into recent and remote past: Meta-analytic evidence for cortical re-organization of episodic autobiog…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition task (19 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …a S and Boeving, Emily R and Riedel, Michael C and Eickhoff, Simon B and Sutherland, Matthew T and Laird, Angela R
Netw Neurosci, 2019

# Title

Cooperating yet distinct brain networks engaged during <mark class="annotated-text">naturalistic</mark> paradigms: A meta-analysis of functional MRI results.

# Keywords

Clustering analysis
Naturalistic paradigms
Neuroimaging meta-analysis
Neuroinformatics

# Abstract
Cognitive processes do not occur …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ity modeling
Social exclusion

# Abstract
Social exclusion refers to the experience of being disregarded or rejected by others and has wide-ranging negative consequences for well-being and cognition. <mark class="annotated-text">Cyberball</mark>, a game where a ball is virtually tossed between players, then leads to the exclusion of the research participant, is a common method used to examine the experience of social exclusion. The neural co…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …lesion approach.

# Keywords

Frontotemporal networks
Insula
Multi-level Kernel Density Analysis
Stroke

# Abstract
Guided by indirect evidence, recent approaches propose a tripartite crosstalk among <mark class="annotated-text">interoceptive signaling</mark>, emotional regulation, and low-level social cognition. Here we examined the neurocognitive convergence of such domains. First, we performed three meta-analyses of functional magnetic resonance imagin…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rds

Frontotemporal networks
Insula
Multi-level Kernel Density Analysis
Stroke

# Abstract
Guided by indirect evidence, recent approaches propose a tripartite crosstalk among interoceptive signaling, <mark class="annotated-text">emotional regulation</mark>, and low-level social cognition. Here we examined the neurocognitive convergence of such domains. First, we performed three meta-analyses of functional magnetic resonance imaging studies to identify …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ks
Insula
Multi-level Kernel Density Analysis
Stroke

# Abstract
Guided by indirect evidence, recent approaches propose a tripartite crosstalk among interoceptive signaling, emotional regulation, and <mark class="annotated-text">low-level social cognition</mark>. Here we examined the neurocognitive convergence of such domains. First, we performed three meta-analyses of functional magnetic resonance imaging studies to identify which areas are consistently coa…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … basis of over 200 fMRI studies, it tests alternative theoretical proposals that attempt to explain how several brain areas process information relevant for social cognition. The results suggest that <mark class="annotated-text">inferring temporary states</mark> such as goals, intentions, and desires of other people-even when they are false and unjust from our own perspective--strongly engages the temporo-parietal junction (TPJ). Inferring more enduring disp…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …he current meta-analysis used foci of 21 individual studies on functional abnormalities in the schizophrenic brain in order to identify regions that reveal convergent under- or over-activation during <mark class="annotated-text">theory of mind </mark>(TOM) tasks. Studies were included in the analyses when contrasting tasks that require the processing of mental states with tasks which did not. Only studies that investigated patients with an ICD or …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …re a ball is virtually tossed between players, then leads to the exclusion of the research participant, is a common method used to examine the experience of social exclusion. The neural correlates of <mark class="annotated-text">social exclusion</mark> remain a topic of debate, particularly with regards to the role of the dorsal anterior cingulate cortex (dACC) and the concept of social pain. Here we conducted a quantitative meta-analysis using act…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tigation of neuroimaging studies on divergent thinking. Based on the ALE results, the functional magnetic resonance imaging (fMRI) studies showed that distributed brain regions were more active under <mark class="annotated-text">divergent thinking</mark> tasks (DTTs) than those under control tasks, but a large portion of the brain regions were deactivated. The ALE results indicated that the brain networks of the creative idea generation in DTTs may b…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …t inferring temporary states such as goals, intentions, and desires of other people-even when they are false and unjust from our own perspective--strongly engages the temporo-parietal junction (TPJ). <mark class="annotated-text">Inferring more enduring dispositions</mark> of others and the self, or interpersonal norms and scripts, engages the medial prefrontal cortex (mPFC), although temporal states can also activate the mPFC. Other candidate tasks reflecting general-…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">memory task (17 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Maillet, David and Rajah, M Natasha
Neurosci Biobehav Rev, 2014

# Title

Age-related differences in brain activity in the <mark class="annotated-text">subsequent memory paradigm</mark>: a meta-analysis.

# Keywords

Aging
Encoding
Episodic memory
Spontaneous thoughts
Subsequent memory
Task-unrelated thoughts

# Abstract
Healthy aging is associated with declines in episodic memory. …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Yaple, Zachary and Arsalidou, Marie
Child Dev, 2018

# Title

N-back Working Memory Task: Meta-analysis of Normative fMRI Studies With Children.

# Keywords



# Abstract
The <mark class="annotated-text">n-back</mark> task is likely the most popular measure of working memory for functional magnetic resonance imaging (fMRI) studies. Despite accumulating neuroimaging studies with the n-back task and children, its ne…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …predicts subsequent memory and forgetting: a meta-analysis of 74 fMRI studies.

# Keywords



# Abstract
The present study performed a quantitative meta-analysis of functional MRI studies that used a <mark class="annotated-text">subsequent memory</mark> approach. The meta-analysis considered both subsequent memory (SM; remembered&gt;forgotten) and subsequent forgetting (SF; forgotten&gt;remembered) effects, restricting the data used to that concerning vis…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …meta-analysis.

# Keywords

encoding
fMRI
maintenance
meta-analysis
retrieval
working memory

# Abstract
It remains unclear whether and to what extent working memory (WM) temporal subprocesses (i.e., <mark class="annotated-text">encoding</mark>, maintenance, and retrieval) involve shared or distinct intrinsic networks. To address this issue, I constructed a model of intrinsic network contributions to different WM phases and then evaluated t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …sis.

# Keywords

encoding
fMRI
maintenance
meta-analysis
retrieval
working memory

# Abstract
It remains unclear whether and to what extent working memory (WM) temporal subprocesses (i.e., encoding, <mark class="annotated-text">maintenance</mark>, and retrieval) involve shared or distinct intrinsic networks. To address this issue, I constructed a model of intrinsic network contributions to different WM phases and then evaluated the validity o…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …
encoding
fMRI
maintenance
meta-analysis
retrieval
working memory

# Abstract
It remains unclear whether and to what extent working memory (WM) temporal subprocesses (i.e., encoding, maintenance, and <mark class="annotated-text">retrieval</mark>) involve shared or distinct intrinsic networks. To address this issue, I constructed a model of intrinsic network contributions to different WM phases and then evaluated the validity of the model by …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ory approach. The meta-analysis considered both subsequent memory (SM; remembered&gt;forgotten) and subsequent forgetting (SF; forgotten&gt;remembered) effects, restricting the data used to that concerning <mark class="annotated-text">visual information encoding</mark> in healthy young adults. The meta-analysis of SM effects indicated that they most consistently associated with five neural regions: left inferior frontal cortex (IFC), bilateral fusiform cortex, bila…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …on, it has become one of the leading explanations for how humans are able to operate on a cognitive level. The current study probed the neural networks underlying one of the most commonly used tasks, <mark class="annotated-text">delayed match-to-sample</mark> (DMTS), to study WM. An activation likelihood estimation (ALE) analysis of 42 functional neuroimaging studies (626 participants) was conducted to demonstrate neural network engagement during DMTS. Re…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …on 79 neuroimaging experiments, classified according to the remoteness of EAMs, and meta-analytic connectivity modeling. A wide brain network, spanning from occipital to frontal lobe, was involved in <mark class="annotated-text">recalling EAMs</mark>. However, remote and recent EAMs were processed by different nodes of this network: recent EAMs activated angular gyrus, dorsomedial prefrontal cortex and hippocampus/parahippocampal gyrus, that we f…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ateral fusiform cortex, bilateral hippocampal formation, bilateral premotor cortex (PMC), and bilateral posterior parietal cortex (PPC). Direct comparisons of the SM effects between the studies using <mark class="annotated-text">verbal</mark> versus pictorial material and item-memory versus associative-memory tasks yielded three main sets of findings. First, the left IFC exhibited greater SM effects during verbal material than pictorial m…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">verbal information encoding</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition - social (12 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Van Overwalle, Frank
Hum Brain Mapp, 2009

# Title

<mark class="annotated-text">Social cognition</mark> and the brain: a meta-analysis.

# Keywords



# Abstract
This meta-analysis explores the location and function of brain areas involved in social cognition, or the capacity to understand people&#39;s beh…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Mwilambwe-Tshilobo, Laetitia and Spreng, R Nathan
Neuroimage, 2021

# Title

<mark class="annotated-text">Social exclusion</mark> reliably engages the default network: A meta-analysis of Cyberball.

# Keywords

Cyberball
Default network
Functional MRI
Meta-analysis
Meta-analytic connectivity modeling
Social exclusion

# Abstrac…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Van Overwalle, Frank and Baetens, Kris and Mariën, Peter and Vandekerckhove, Marie
Neuroimage, 2014

# Title

<mark class="annotated-text">Social cognition</mark> and the cerebellum: a meta-analysis of over 350 fMRI studies.

# Keywords

Cerebellum
Functional neuroimaging
Meta-analysis
Review
Social cognition

# Abstract
This meta-analysis explores the role of…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Diveica, Veronica and Koldewyn, Kami and Binney, Richard J
Neuroimage, 2021

# Title

Establishing a role of the semantic control network in <mark class="annotated-text">social cognitive processing</mark>: A meta-analysis of functional neuroimaging studies.

# Keywords

Cognitive control
Empathy
Meta-analysis
Moral reasoning
Theory of mind
Trait inference

# Abstract
The contribution and neural basis …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Merritt, Carrington C and MacCormack, Jennifer K and Stein, Andrea G and Lindquist, Kristen A and Muscatell, Keely A
Soc Cogn Affect Neurosci, 2021

# Title

The neural underpinnings of intergroup <mark class="annotated-text">social cognition</mark>: an fMRI meta-analysis.

# Keywords

fMRI
intergroup bias
meta-analysis
race
social cognition

# Abstract
Roughly 20 years of functional magnetic resonance imaging (fMRI) studies have investigated th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …co and Couto, Blas and Richter, Fabian and Decety, Jean and Lopez, Jessica and Sigman, Mariano and Manes, Facundo and Ibáñez, Agustín
Cortex, 2017

# Title

Convergence of interoception, emotion, and <mark class="annotated-text">social cognition</mark>: A twofold fMRI meta-analysis and lesion approach.

# Keywords

Frontotemporal networks
Insula
Multi-level Kernel Density Analysis
Stroke

# Abstract
Guided by indirect evidence, recent approaches pr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … and Kyriakopoulos, Marinos and Corrigall, Richard and Taylor, Eric and Frangou, Sophia
PLoS One, 2011

# Title

Autism spectrum disorders and schizophrenia: meta-analysis of the neural correlates of <mark class="annotated-text">social cognition</mark>.

# Keywords



# Abstract
Impaired social cognition is a cardinal feature of Autism Spectrum Disorders (ASD) and Schizophrenia (SZ). However, the functional neuroanatomy of social cognition in eithe…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nd Sikkes, Sietske A M and Scheltens, Philip and Spikman, Jacoba M and Jaschke, Artur C and Warren, Jason D and Tijms, Betty M
Brain Cogn, 2021

# Title

Frontotemporal dementia, music perception and <mark class="annotated-text">social cognition</mark> share neurobiological circuits: A meta-analysis.

# Keywords

Frontotemporal dementia
Insula
Music perception
Social cognition
Ventral language pathway

# Abstract
Frontotemporal dementia (FTD) is a …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Ingrid R
Front Hum Neurosci, 2013

# Title

Anterior temporal face patches: a meta-analysis and empirical study.

# Keywords

anterior temporal lobe
fMRI
face processing
person memory
semantic memory
<mark class="annotated-text">social cognition
</mark>social networks
temporal pole

# Abstract
Evidence suggests the anterior temporal lobe (ATL) plays an important role in person identification and memory. In humans, neuroimaging studies of person memo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ias and Kronbichler, Martin
Schizophr Bull, 2017

# Title

Abnormal Brain Activation During Theory of Mind Tasks in Schizophrenia: A Meta-Analysis.

# Keywords

fMRI
mentalizing
psychosis

# Abstract
<mark class="annotated-text">Social cognition</mark> abilities are severely impaired in schizophrenia (SZ). The current meta-analysis used foci of 21 individual studies on functional abnormalities in the schizophrenic brain in order to identify regions…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">memory - working (11 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Yaple, Zachary and Arsalidou, Marie
Child Dev, 2018

# Title

N-back <mark class="annotated-text">Working Memory</mark> Task: Meta-analysis of Normative fMRI Studies With Children.

# Keywords



# Abstract
The n-back task is likely the most popular measure of working memory for functional magnetic resonance imaging (…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Andre, Julia and Picchioni, Marco and Zhang, Ruibin and Toulopoulou, Timothea
Neuroimage Clin, 2016

# Title

<mark class="annotated-text">Working memory </mark>circuit as a function of increasing age in healthy adolescence: A systematic review and meta-analyses.

# Keywords

Brain activation
Neurodevelopment
Neurodevelopmental disorders
Schizophrenia
Working…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Saldarini, Francesco and Gottlieb, Natalie and Stokes, Paul R A
J Affect Disord, 2022

# Title

Neural correlates of <mark class="annotated-text">working memory</mark> function in euthymic people with bipolar disorder compared to healthy controls: A systematic review and meta-analysis.

# Keywords

Bipolar disorder
Healthy controls
Meta-analysis
Systematic review
W…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Rottschy, C and Langner, R and Dogan, I and Reetz, K and Laird, A R and Schulz, J B and Fox, P T and Eickhoff, S B
Neuroimage, 2012

# Title

Modelling neural correlates of <mark class="annotated-text">working memory</mark>: a coordinate-based meta-analysis.

# Keywords



# Abstract
Working memory subsumes the capability to memorize, retrieve and utilize information for a limited period of time which is essential to ma…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Li, Ke and Huang, Xiaoyan and Han, Yingping and Zhang, Jun and Lai, Yuhan and Yuan, Li and Lu, Jiaojiao and Zeng, Dong
Front Hum Neurosci, 2015

# Title

Enhanced Neuroactivation during <mark class="annotated-text">Working Memory</mark> Task in Postmenopausal Women Receiving Hormone Therapy: A Coordinate-Based Meta-Analysis.

# Keywords

ALE meta-analysis
functional magnetic resonance imaging
hormone therapy
neural activation
postme…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …app, 2019

# Title

Neural activity during working memory encoding, maintenance, and retrieval: A network-based model and meta-analysis.

# Keywords

encoding
fMRI
maintenance
meta-analysis
retrieval
<mark class="annotated-text">working memory</mark>

# Abstract
It remains unclear whether and to what extent working memory (WM) temporal subprocesses (i.e., encoding, maintenance, and retrieval) involve shared or distinct intrinsic networks. To addr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …
Neuroimage, 2019

# Title

Meta-analyses of the n-back working memory task: fMRI evidence of age-related changes in prefrontal cortex involvement across the adult lifespan.

# Keywords



# Abstract
<mark class="annotated-text">Working memory</mark>, a fundamental cognitive function that is highly dependent on the integrity of the prefrontal cortex, is known to show age-related decline across the typical healthy adult lifespan. Moreover, we know…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Psychol, 2016

# Title

Delayed match-to-sample in working memory: A BrainMap meta-analysis.

# Keywords

ALE
Activation likelihood estimation
Functional neuroimaging
Neural networks
fMRI

# Abstract
<mark class="annotated-text">Working memory </mark>(WM), or the ability to temporarily store and manipulate information, is one of the most widely studied constructs in cognitive psychology. Since its inception, it has become one of the leading explan…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …a-analysis of 30 fMRI experiments.

# Keywords

Activation likelihood estimation
Content-specific storage
Delay period
Meta-analysis
Seed-based d mapping
Visual working memory
fMRI

# Abstract
Visual <mark class="annotated-text">working memory </mark>refers to the temporary maintenance and manipulation of task-related visual information. Recent debate on the underlying neural substrates of visual working memory has focused on the delay period of r…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ysis of 408 functional magnetic resonance imaging studies (9639 participants, 7587 activation foci, 518 experimental contrasts) covering three fundamental EF subcomponents: inhibition, switching, and <mark class="annotated-text">working memory</mark>. Our results found that activation common to all three EF subcomponents converged in the multiple-demand network across adolescence and adulthood. The function of EF with the multiple-demand network …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">modality - functional connectivity (6 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Diveica, Veronica and Koldewyn, Kami and Binney, Richard J
Neuroimage, 2021

# Title

Establishing a role of the semantic control <mark class="annotated-text">network</mark> in social cognitive processing: A meta-analysis of functional neuroimaging studies.

# Keywords

Cognitive control
Empathy
Meta-analysis
Moral reasoning
Theory of mind
Trait inference

# Abstract
The…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …22

# Title

Neural substrates of brand equity: applying a quantitative meta-analytical method for neuroimage studies.

# Keywords

ALE
Brand management
Consumer decision making
Consumer neuroscience
<mark class="annotated-text">DMN</mark>
Neuromarketing
fMRI

# Abstract
Although the concept of brand equity has been investigated using various approaches, a comprehensive neural basis for brand equity remains unclear. The default mode ne…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Brain Mapp, 2020

# Title

A meta-analysis of functional magnetic resonance imaging studies of divergent thinking using activation likelihood estimation.

# Keywords

ALE
divergent
fMRI
meta-analysis
<mark class="annotated-text">semantic control network
</mark>
# Abstract
There are conflicting findings regarding brain regions and networks underpinning creativity, with divergent thinking tasks commonly used to study this. A handful of meta-analyses have atte…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …gman, Mariano and Manes, Facundo and Ibáñez, Agustín
Cortex, 2017

# Title

Convergence of interoception, emotion, and social cognition: A twofold fMRI meta-analysis and lesion approach.

# Keywords

<mark class="annotated-text">Frontotemporal networks
</mark>Insula
Multi-level Kernel Density Analysis
Stroke

# Abstract
Guided by indirect evidence, recent approaches propose a tripartite crosstalk among interoceptive signaling, emotional regulation, and low…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ion (ALE) meta-analyses to 43 functional neuroimaging studies of perseverative cognition to elucidate the neurobiological substrates across individuals with and without psychopathological conditions. <mark class="annotated-text">Task-related and resting state functional connectivity studies</mark> were examined in separate meta-analyses. Across task-based studies, perseverative cognition engaged medial frontal gyrus, cingulate gyrus, insula, and posterior cingulate cortex. Resting state functi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …pecifically, we found intra- and interhemispheric differences with regard to anterior and posterior functional and structural connectivity, between the right and left hippocampi. For task-independent <mark class="annotated-text">functional connectivity</mark>, we found the right anterior hippocampus to have functional connectivity with a large, distributed network, whereas the left anterior hippocampus demonstrated primarily fronto-limbic connectivity. Th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">memory - episodic (6 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Terry, Douglas P and Sabatinelli, Dean and Puente, A Nicolas and Lazar, Nicole A and Miller, L Stephen
J Neuroimaging, 2015

# Title

A Meta-Analysis of fMRI Activation Differences during <mark class="annotated-text">Episodic Memory</mark> in Alzheimer&#39;s Disease and Mild Cognitive Impairment.

# Keywords

Alzheimer&#39;s disease
MCI
Memory
episodic memory
fMRI
meta-analysis
mild cognitive impairment

# Abstract
Functional MRI (fMRI) has th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Boccia, Maddalena and Teghil, Alice and Guariglia, Cecilia
Neurosci Biobehav Rev, 2019

# Title

Looking into recent and remote past: Meta-analytic evidence for cortical re-organization of <mark class="annotated-text">episodic</mark> autobiographical memories.

# Keywords

Declarative memory
Hippocampus
Memory
Time
fMRI

# Abstract
Episodic autobiographical memory (EAM) is pivotal for the development and maintenance of personal i…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ickhoff, Simon B and Ketteler, Simon T and Kuhn, Hanna and Shah, N Jon and Schulz, Jörg B and Reske, Martina and Reetz, Kathrin
Brain Struct Funct, 2015

# Title

Specific and disease stage-dependent <mark class="annotated-text">episodic memory</mark>-related brain activation patterns in Alzheimer&#39;s disease: a coordinate-based meta-analysis.

# Keywords



# Abstract
Episodic memory is typically affected during the course of Alzheimer&#39;s disease (A…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …elates of successful emotional episodic encoding and retrieval: An SDM meta-analysis of neuroimaging studies.

# Keywords

Amygdala
Emotion
Encoding
Episodic memory
Neuroimaging
Retrieval

# Abstract
<mark class="annotated-text">Episodic memory </mark>for emotional events is typically enhanced and engages additional brain mechanisms relative to episodic memory for neutral events. Many functional magnetic resonance imaging (fMRI) studies have probed…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …t memory paradigm: a meta-analysis.

# Keywords

Aging
Encoding
Episodic memory
Spontaneous thoughts
Subsequent memory
Task-unrelated thoughts

# Abstract
Healthy aging is associated with declines in <mark class="annotated-text">episodic memory</mark>. This reduction is thought to be due in part to age-related differences in encoding-related processes. In the current study, we performed an activation likelihood estimation meta-analysis of function…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …lyses.

# Keywords

Attention
Dorsal attention network
Emotion
Episodic memory encoding
Medial temporal lobe
Memory trace
Meta-analysis
Novelty
Reward
fMRI

# Abstract
Functional neuroimaging data on <mark class="annotated-text">episodic memory</mark> formation have expanded rapidly over the last 30 years, which raises the need for an integrative framework. This study proposes a taxonomy of episodic memory formation to address this need. At the br…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">modality - positron emission tomography (4 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    E, Keren-Happuch and Chen, Shen-Hsing Annabel and Ho, Moon-Ho Ringo and Desmond, John E
Hum Brain Mapp, 2014

# Title

A meta-analysis of cerebellar contributions to higher cognition from <mark class="annotated-text">PET</mark> and fMRI studies.

# Keywords

cerebellum
cognition
emotion
language
meta-analysis
music
neuroimaging
timing

# Abstract
A growing interest in cerebellar function and its involvement in higher cognit…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …studies to find the relationship between cognition in AD patients and normal elderlies. A systematic search was conducted to collect functional neuroimaging studies such as positron emission therapy (<mark class="annotated-text">PET</mark>) and functional magnetic resonance imaging (fMRI) in AD patients and healthy elderlies. The coordinates of regions related to cognition were meta-analyzed using the activation likelihood estimation (…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …sis of the neuroimaging evidence on noun and verb processing in order to address this dichotomy more effectively at the anatomical level. We used a hierarchical clustering algorithm that grouped fMRI/<mark class="annotated-text">PET</mark> activation peaks solely on the basis of spatial proximity. Cluster specificity for grammatical class was then tested on the basis of the noun-verb distribution of the activation peaks included in eac…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …neural activation commonly found in social functional neuroimaging studies extends to these &#39;semantic control&#39; regions. We conducted five coordinate-based meta-analyses to combine results of 499 fMRI/<mark class="annotated-text">PET</mark> experiments and identified the brain regions consistently involved in semantic control, as well as four social abilities: theory of mind, trait inference, empathy and moral reasoning. This allowed an…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">group - alzheimer&#39;s disease (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Sadigh-Eteghad, Saeed and Majdi, Alireza and Farhoudi, Mehdi and Talebi, Mahnaz and Mahmoudi, Javad
J Neurol Sci, 2014

# Title

Different patterns of brain activation in normal aging and <mark class="annotated-text">Alzheimer</mark>&#39;s disease from cognitional sight: meta analysis using activation likelihood estimation.

# Keywords

Activation likelihood estimation
Aging
Alzheimer disease
Cognition
Meta-analysis
Neuroimaging

# A…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Douglas P and Sabatinelli, Dean and Puente, A Nicolas and Lazar, Nicole A and Miller, L Stephen
J Neuroimaging, 2015

# Title

A Meta-Analysis of fMRI Activation Differences during Episodic Memory in <mark class="annotated-text">Alzheimer</mark>&#39;s Disease and Mild Cognitive Impairment.

# Keywords

Alzheimer&#39;s disease
MCI
Memory
episodic memory
fMRI
meta-analysis
mild cognitive impairment

# Abstract
Functional MRI (fMRI) has the potential t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …a and Shah, N Jon and Schulz, Jörg B and Reske, Martina and Reetz, Kathrin
Brain Struct Funct, 2015

# Title

Specific and disease stage-dependent episodic memory-related brain activation patterns in <mark class="annotated-text">Alzheimer</mark>&#39;s disease: a coordinate-based meta-analysis.

# Keywords



# Abstract
Episodic memory is typically affected during the course of Alzheimer&#39;s disease (AD). Due to the pronounced heterogeneity of func…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">group - older adults (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Sadigh-Eteghad, Saeed and Majdi, Alireza and Farhoudi, Mehdi and Talebi, Mahnaz and Mahmoudi, Javad
J Neurol Sci, 2014

# Title

Different patterns of brain activation in <mark class="annotated-text">normal aging </mark>and Alzheimer&#39;s disease from cognitional sight: meta analysis using activation likelihood estimation.

# Keywords

Activation likelihood estimation
Aging
Alzheimer disease
Cognition
Meta-analysis
Neur…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …gions including bilateral middle/superior frontal gyri, anterior medial frontal gyrus, precuneus and left inferior parietal lobe. We demonstrate that all of the regions consistently over-recruited by <mark class="annotated-text">older adults</mark> during successful encoding exhibit either direct overlap, or occur in close vicinity to regions consistently involved in unsuccessful encoding in young adults. We discuss the possibility that this ov…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ompile data from eligible fMRI articles that report stereotaxic coordinates of brain activity from healthy adults in three age-groups: young (23.57 ± 5.63 years), middle-aged (38.13 ± 5.63 years) and <mark class="annotated-text">older</mark> (66.86 ± 5.70 years) adults. Findings show that the three groups share concordance in the engagement of parietal and cingulate cortices, which have been consistently identified as core areas involved…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">group - schizophrenia (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Sugranyes, Gisela and Kyriakopoulos, Marinos and Corrigall, Richard and Taylor, Eric and Frangou, Sophia
PLoS One, 2011

# Title

Autism spectrum disorders and <mark class="annotated-text">schizophrenia</mark>: meta-analysis of the neural correlates of social cognition.

# Keywords



# Abstract
Impaired social cognition is a cardinal feature of Autism Spectrum Disorders (ASD) and Schizophrenia (SZ). Howev…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Title

Abnormal Brain Activation During Theory of Mind Tasks in Schizophrenia: A Meta-Analysis.

# Keywords

fMRI
mentalizing
psychosis

# Abstract
Social cognition abilities are severely impaired in <mark class="annotated-text">schizophrenia</mark> (SZ). The current meta-analysis used foci of 21 individual studies on functional abnormalities in the schizophrenic brain in order to identify regions that reveal convergent under- or over-activation…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">does not seem to belong in topic (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Robinson, <mark class="annotated-text">Jennifer</mark> L and Salibi, Nouha and Deshpande, Gopikrishna
Neuroimage, 2016

# Title

Functional connectivity of the left and right hippocampi: Evidence for functional lateralization along the long-axis using me…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …faces, and whether a right-hemispheric dominance persists in line with specific affective responses. We aim to review the neural responses systematically, quantitatively, and qualitatively underlying <mark class="annotated-text">subliminal face processing</mark>. PubMed was searched for Functional Magnetic Resonance Imaging (fMRI) publications assessing subliminal emotional face stimuli up to March 2022. Activation Likelihood Estimation (ALE) meta-analyses a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">modality - structural mri (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ents with profound changes in social cognition. Music might be a sensitive probe for social cognition abilities, but underlying neurobiological substrates are unclear. We performed a meta-analysis of <mark class="annotated-text">voxel-based morphometry </mark>studies in FTD patients and functional MRI studies for music perception and social cognition tasks in cognitively normal controls to identify robust patterns of atrophy (FTD) or activation (music perc…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …he semantic information related to the retrieval and buffering of the formed creative ideas, and several regions in the temporal cortex may be related to the stored long-term memory. In addition, the <mark class="annotated-text">ALE results of the structural studies</mark> showed that divergent thinking was related to the dopaminergic system (e.g., left caudate and claustrum). Based on the ALE results, both fMRI and structural MRI studies could uncover the neural basis…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">memory - emotional (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Murty, Vishnu P and Ritchey, Maureen and Adcock, R Alison and LaBar, Kevin S
Neuropsychologia, 2010

# Title

fMRI studies of successful <mark class="annotated-text">emotional memory</mark> encoding: A quantitative meta-analysis.

# Keywords



# Abstract
Over the past decade, fMRI techniques have been increasingly used to interrogate the neural correlates of successful emotional memory…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …elates of successful emotional episodic encoding and retrieval: An SDM meta-analysis of neuroimaging studies.

# Keywords

Amygdala
Emotion
Encoding
Episodic memory
Neuroimaging
Retrieval

# Abstract
<mark class="annotated-text">Episodic memory for emotional events</mark> is typically enhanced and engages additional brain mechanisms relative to episodic memory for neutral events. Many functional magnetic resonance imaging (fMRI) studies have probed the neural basis of…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">group - mild cognitive impairment (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …i, Dean and Puente, A Nicolas and Lazar, Nicole A and Miller, L Stephen
J Neuroimaging, 2015

# Title

A Meta-Analysis of fMRI Activation Differences during Episodic Memory in Alzheimer&#39;s Disease and <mark class="annotated-text">Mild Cognitive Impairment</mark>.

# Keywords

Alzheimer&#39;s disease
MCI
Memory
episodic memory
fMRI
meta-analysis
mild cognitive impairment

# Abstract
Functional MRI (fMRI) has the potential to be used as a tool to detect biomarkers…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s typically affected during the course of Alzheimer&#39;s disease (AD). Due to the pronounced heterogeneity of functional neuroimaging studies on episodic memory impairments in mild cognitive impairment (<mark class="annotated-text">MCI</mark>) and AD regarding their methodology and findings, we aimed to delineate consistent episodic memory-related brain activation patterns. We performed a systematic, quantitative, coordinate-based whole-b…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">group - adolescents (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … Peng and Eickhoff, Simon B and Lin, Xin and Zhang, Delong and Wang, Yingying
Dev Sci, 2021

# Title

Neural substrates of the executive function construct, age-related changes, and task materials in <mark class="annotated-text">adolescents</mark> and adults: ALE meta-analyses of 408 fMRI studies.

# Keywords

ALE meta-analysis
development
domain-general
domain-specific
executive function
integrative model

# Abstract
To explore the neural sub…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …development we conducted a systematic review and coordinate based meta-analyses of all the available primary functional magnetic resonance imaging studies (n = 382) that mapped WM function in healthy <mark class="annotated-text">adolescents</mark> (10-17 years) and young adults (18-30 years). Activation Likelihood Estimation analyses across all WM tasks revealed increased activation with increasing subject age in the middle frontal gyrus (BA6)…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">memory - subsequent (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Kim, Hongkeun
Neuroimage, 2011

# Title

Neural activity that predicts <mark class="annotated-text">subsequent memory and forgetting</mark>: a meta-analysis of 74 fMRI studies.

# Keywords



# Abstract
The present study performed a quantitative meta-analysis of functional MRI studies that used a subsequent memory approach. The meta-anal…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Maillet, David and Rajah, M Natasha
Neurosci Biobehav Rev, 2014

# Title

Age-related differences in brain activity in the <mark class="annotated-text">subsequent memory</mark> paradigm: a meta-analysis.

# Keywords

Aging
Encoding
Episodic memory
Spontaneous thoughts
Subsequent memory
Task-unrelated thoughts

# Abstract
Healthy aging is associated with declines in episodic…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition - naturalistic (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …dynamic, interactive tasks have allowed researchers to study cognition as it more naturally occurs. Collective analysis across such neuroimaging experiments may answer broader questions regarding how <mark class="annotated-text">naturalistic cognition</mark> is biologically distributed throughout the brain. We applied an unbiased, data-driven, meta-analytic approach that uses  
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition - perservative (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …uroimaging, 2020

# Title

Can&#39;t get it off my brain: Meta-analysis of neuroimaging studies on perseverative cognition.

# Keywords

Activation likelihood estimation
Rumination
Worry
fMRI

# Abstract
<mark class="annotated-text">Perseverative cognition</mark> (i.e. rumination and worry) describes intrusive, uncontrollable, repetitive thoughts. These negative affective experiences are accompanied by physiological arousal, as if the individual were facing a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">group - dementia (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … Hooft, Jochum J and Pijnenburg, Yolande A L and Sikkes, Sietske A M and Scheltens, Philip and Spikman, Jacoba M and Jaschke, Artur C and Warren, Jason D and Tijms, Betty M
Brain Cogn, 2021

# Title

<mark class="annotated-text">Frontotemporal dementia</mark>, music perception and social cognition share neurobiological circuits: A meta-analysis.

# Keywords

Frontotemporal dementia
Insula
Music perception
Social cognition
Ventral language pathway

# Abstr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">group - autism spectrum disorder (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Sugranyes, Gisela and Kyriakopoulos, Marinos and Corrigall, Richard and Taylor, Eric and Frangou, Sophia
PLoS One, 2011

# Title

<mark class="annotated-text">Autism spectrum disorders </mark>and schizophrenia: meta-analysis of the neural correlates of social cognition.

# Keywords



# Abstract
Impaired social cognition is a cardinal feature of Autism Spectrum Disorders (ASD) and Schizoph…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition - noun and verb processing (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …i, Isabella and Borghese, Nunzio A and Luzzatti, Claudio and Paulesu, Eraldo
Front Hum Neurosci, 2013

# Title

Clustering the lexicon in the brain: a meta-analysis of the neurofunctional evidence on <mark class="annotated-text">noun and verb processing</mark>.

# Keywords

clustering algorithm
left inferior frontal gyrus
meta-analysis
neuroimaging
noun-verb dissociation
task demand

# Abstract
Although it is widely accepted that nouns and verbs are functi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">group - obsessive compulsive disorder (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Rasgon, A and Lee, W H and Leibu, E and Laird, A and Glahn, D and Goodman, W and Frangou, S
Eur Psychiatry, 2017

# Title

Neural correlates of affective and non-affective cognition in <mark class="annotated-text">obsessive compulsive disorder</mark>: A meta-analysis of functional imaging studies.

# Keywords

Activation likelihood estimation
Basal ganglia
Functional imaging
Habit

# Abstract
Obsessive compulsive disorder (OCD) is characterized b…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition - affective versus non-affective (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Rasgon, A and Lee, W H and Leibu, E and Laird, A and Glahn, D and Goodman, W and Frangou, S
Eur Psychiatry, 2017

# Title

Neural correlates of <mark class="annotated-text">affective and non-affective</mark> cognition in obsessive compulsive disorder: A meta-analysis of functional imaging studies.

# Keywords

Activation likelihood estimation
Basal ganglia
Functional imaging
Habit

# Abstract
Obsessive c…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition - brand equity (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Watanuki, Shinya and Akama, Hiroyuki
Heliyon, 2022

# Title

Neural substrates of <mark class="annotated-text">brand equity</mark>: applying a quantitative meta-analytical method for neuroimage studies.

# Keywords

ALE
Brand management
Consumer decision making
Consumer neuroscience
DMN
Neuromarketing
fMRI

# Abstract
Although t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition - emotion (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …dolfi, Federico and Couto, Blas and Richter, Fabian and Decety, Jean and Lopez, Jessica and Sigman, Mariano and Manes, Facundo and Ibáñez, Agustín
Cortex, 2017

# Title

Convergence of interoception, <mark class="annotated-text">emotion</mark>, and social cognition: A twofold fMRI meta-analysis and lesion approach.

# Keywords

Frontotemporal networks
Insula
Multi-level Kernel Density Analysis
Stroke

# Abstract
Guided by indirect evidence…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition - interoception (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Adolfi, Federico and Couto, Blas and Richter, Fabian and Decety, Jean and Lopez, Jessica and Sigman, Mariano and Manes, Facundo and Ibáñez, Agustín
Cortex, 2017

# Title

Convergence of <mark class="annotated-text">interoception</mark>, emotion, and social cognition: A twofold fMRI meta-analysis and lesion approach.

# Keywords

Frontotemporal networks
Insula
Multi-level Kernel Density Analysis
Stroke

# Abstract
Guided by indirect…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">modality - lesions (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …Jean and Lopez, Jessica and Sigman, Mariano and Manes, Facundo and Ibáñez, Agustín
Cortex, 2017

# Title

Convergence of interoception, emotion, and social cognition: A twofold fMRI meta-analysis and <mark class="annotated-text">lesion</mark> approach.

# Keywords

Frontotemporal networks
Insula
Multi-level Kernel Density Analysis
Stroke

# Abstract
Guided by indirect evidence, recent approaches propose a tripartite crosstalk among intero…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">group - brain damage (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …r insular and frontotemporal regions (viz., the orbitofrontal and inferior frontal gyri, the amygdala, and mid temporal lobe/subcortical structures). Second, we explored such domains in patients with <mark class="annotated-text">fronto-insulo-temporal damage</mark>. Relative to controls, the patients showed behavioral impairments of interoception, emotional processing, and social cognition, with preservation of other cognitive functions. Convergent results from…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition - divergent thinking (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …m Brain Mapp, 2015

# Title

A meta-analysis of neuroimaging studies on divergent thinking using activation likelihood estimation.

# Keywords

MRI studies
activation likelihood estimation
creativity
<mark class="annotated-text">divergent thinking
</mark>
# Abstract
In this study, an activation likelihood estimation (ALE) meta-analysis was used to conduct a quantitative investigation of neuroimaging studies on divergent thinking. Based on the ALE resu…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition - dual process (thinking fast and slow) (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Gronchi, Giorgio and Gavazzi, Gioele and Viggiano, Maria Pia and Giovannelli, Fabio
Brain Sci, 2024

# Title

<mark class="annotated-text">Dual-Process Theory </mark>of Thought and Inhibitory Control: An ALE Meta-Analysis.

# Keywords

DMN
PARCS theory
dual process
insula
left inferior frontal gyrus
meta-analysis
pre-SMA

# Abstract
The dual-process theory of thou…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition - moral (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Fede, Samantha J and Kiehl, Kent A
Brain Imaging Behav, 2020

# Title

Meta-analysis of the <mark class="annotated-text">moral brain</mark>: patterns of neural engagement assessed using multilevel kernel density analysis.

# Keywords

MKDA
Machine learning
Meta-analysis
Moral
fMRI

# Abstract
The neuroimaging literature in moral cognitio…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">cognition - no specificity (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ate (FDR) of P&lt;0.05 thresholds and the clusters with a minimum size of 200 mm(3) were considered. Data were visualized with MANGO software. Forty-one articles that explored the areas activated during <mark class="annotated-text">cognition</mark> in normal elderly subjects and AD patients were found. According to the findings, left middle frontal gyrus and left precuneus are the most activated areas in cognitional tasks in healthy elderlies a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">memory - person (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …igating whether similar subregions in the dorsal, ventral, lateral, or polar aspects of the ATL are sensitive to personally familiar, famous, and novel faces. We present the results of two studies of <mark class="annotated-text">person memory</mark>: a meta-analysis of existing fMRI studies and an empirical fMRI study using optimized imaging parameters. Both studies showed left-lateralized ATL activations to familiar individuals while novel face…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">memory - episodic autobiographical (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ooking into recent and remote past: Meta-analytic evidence for cortical re-organization of episodic autobiographical memories.

# Keywords

Declarative memory
Hippocampus
Memory
Time
fMRI

# Abstract
<mark class="annotated-text">Episodic autobiographical memory</mark> (EAM) is pivotal for the development and maintenance of personal identity. However, a theoretical debate still exists about where EAMs are stored in our brain and about hippocampal unique contributio…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">memory - declarative (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …d Guariglia, Cecilia
Neurosci Biobehav Rev, 2019

# Title

Looking into recent and remote past: Meta-analytic evidence for cortical re-organization of episodic autobiographical memories.

# Keywords

<mark class="annotated-text">Declarative memory
</mark>Hippocampus
Memory
Time
fMRI

# Abstract
Episodic autobiographical memory (EAM) is pivotal for the development and maintenance of personal identity. However, a theoretical debate still exists about wh…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">group - postmenopausal women receiving hormonal therapy (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …d Huang, Xiaoyan and Han, Yingping and Zhang, Jun and Lai, Yuhan and Yuan, Li and Lu, Jiaojiao and Zeng, Dong
Front Hum Neurosci, 2015

# Title

Enhanced Neuroactivation during Working Memory Task in <mark class="annotated-text">Postmenopausal Women Receiving Hormone Therapy</mark>: A Coordinate-Based Meta-Analysis.

# Keywords

ALE meta-analysis
functional magnetic resonance imaging
hormone therapy
neural activation
postmenopause
working memory

# Abstract
Hormone therapy (HT)…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">group - eurhythmic people with bipolar disorder (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Saldarini, Francesco and Gottlieb, Natalie and Stokes, Paul R A
J Affect Disord, 2022

# Title

Neural correlates of working memory function in <mark class="annotated-text">euthymic people with bipolar disorder</mark> compared to healthy controls: A systematic review and meta-analysis.

# Keywords

Bipolar disorder
Healthy controls
Meta-analysis
Systematic review
Working memory
fMRI

# Abstract
Bipolar disorders (…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">memory - long-term (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Spets, Dylan S and Slotnick, Scott D
Cogn Neurosci, 2021

# Title

Are there sex differences in brain activity during <mark class="annotated-text">long-term</mark> memory? A systematic review and fMRI activation likelihood estimation meta-analysis.

# Keywords

Debate
fMRI
gender
meta-analysis
recall
recognition
review
sex

# Abstract
The degree to which sex di…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">group - male vs female (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Spets, Dylan S and Slotnick, Scott D
Cogn Neurosci, 2021

# Title

Are there <mark class="annotated-text">sex differences</mark> in brain activity during long-term memory? A systematic review and fMRI activation likelihood estimation meta-analysis.

# Keywords

Debate
fMRI
gender
meta-analysis
recall
recognition
review
sex

# …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">group - children (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …(fMRI) studies. Despite accumulating neuroimaging studies with the n-back task and children, its neural representation is still unclear. fMRI studies that used the n-back were compiled, and data from <mark class="annotated-text">children up to 15 years</mark> (n = 260) were analyzed using activation likelihood estimation. Results show concordance in frontoparietal regions recognized for their role in working memory as well as regions not typically highlig…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```
