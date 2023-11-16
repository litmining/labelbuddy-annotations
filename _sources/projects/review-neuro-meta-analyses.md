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


# review-neuro-meta-analyses

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/review-neuro-meta-analyses/).

## Review of neuroimaging meta-analyses: Topics, authors, and methods

In this project, we review neuroimaging meta-analyses. 
The manual annotation part of the project focuses on methods. 

## Papers

### How the papers were obtained [to be updated]
There are two groups of papers:
1. full-text open-access papers that were obtained from PMC via pubget, and
2. abstracts from closed-access papers that were obtained from PubMed via a tweaked version of pubget (the out-of-the-box version can only access PMC).


Typically with [pubget](https://neuroquery.github.io/pubget/pubget.html).
We recommend invoking `pubget` with the `--query_file` option, and storing a copy of the query file in the project's directory, or including a copy in the `README.md`.

`<description>`

### Where the full papers are stored [to be updated]

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
1. full texts from open-access papers from PMC:
   - `/projects/review-neuro-meta-analayses/documents/documents_00001-ma-in-title.jsonl`
   - `/projects/review-neuro-meta-analayses/documents/documents_00002-ma-in-title.jsonl`
   - `/projects/review-neuro-meta-analayses/documents/documents_00003-ma-in-title.jsonl`
2. abstracts from closed-access papers from pubmed:
   - `projects/review-neuro-meta-analyses/documents/closed_documents_00000.jsonl`
  
### Annotation labels:
The label list is quite long, so I'm not including it here. But the labels group into these categories
- Reasons to come back to the paper
- info on the number of studies/contrasts found/included
- meta-analysis number (many papers have multiple)
- algorithm
- software
- large-scale meta-analysis method
- exclusion criteria
- has prisma chart

### Labels found in other projects as well:
- `<label2>`

### Instructions for annotators

At this point, I have finished annotating the open-access full-text papers. I'd love help annotating the closed-access abstracts. To do this, follow these steps:
- 



## Labels in this project



```{code-cell}
:tags: [remove-input]

from labelrepo import displays
text = """
<div class="detailed-label-set">
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">N studies included (421 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Fouragnan</mark>, Elsa and Retzler, Chris and Philiastides, Marios G
Human brain mapping, 2019

# Title

Separate neural representations of prediction error valence and surprise: Evidence from an fMRI meta-analysis.
…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">66</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Huang</mark>, Xiao and Tang, Shi and Lyu, Xiaojun and Yang, Changqiang and Chen, Xiaoping
Sleep medicine, 2020

# Title

Structural and functional brain alterations in obstructive sleep apnea: a multimodal meta-a…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">13</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Wu</mark>, Xin and Yang, Wenjing and Tong, Dandan and Sun, Jiangzhou and Chen, Qunlin and Wei, Dongtao and Zhang, Qinglin and Zhang, Meng and Qiu, Jiang
Human brain mapping, 2016

# Title

A meta-analysis of n…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">17</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Poeppl</mark>, Timm B and Langguth, Berthold and Rupprecht, Rainer and Safron, Adam and Bzdok, Danilo and Laird, Angela R and Eickhoff, Simon B
Frontiers in neuroendocrinology, 2017

# Title

The neural basis of s…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">19</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Keuken</mark>, Max C and Müller-Axt, Christa and Langner, Robert and Eickhoff, Simon B and Forstmann, Birte U and Neumann, Jane
Frontiers in human neuroscience, 2014

# Title

Brain networks of perceptual decision…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">18</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Yeung</mark>, Andy W K
Journal of sleep research, 2020

# Title

Morphometric and functional connectivity changes in the brain of patients with obstructive sleep apnea: A meta-analysis.

# Keywords

brain mapping…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">19</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Pan</mark>, Nanfang and Wang, Song and Qin, Kun and Li, Lei and Chen, Ying and Zhang, Xun and Lai, Han and Suo, Xueling and Long, Yajing and Yu, Yifan and Ji, Shiyu and Radua, Joaquim and Sweeney, John A and Go…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">124</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Gilat</mark>, Moran and Dijkstra, Bauke W and D&#39;Cruz, Nicholas and Nieuwboer, Alice and Lewis, Simon J G
Current neurology and neuroscience reports, 2020

# Title

Functional MRI to Study Gait Impairment in Parki…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">16</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Perdue</mark>, Meaghan V and Mahaffy, Kelly and Vlahcevic, Katherine and Wolfman, Emma and Erbeli, Florina and Richlan, Fabio and Landi, Nicole
Neuroscience and biobehavioral reviews, 2022

# Title

Reading interv…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">8</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Kim</mark>, Tae-Hyung and Woo, Sungmin and Han, Sangwon and Suh, Chong Hyun and Vargas, Hebert Alberto
AJR. American journal of roentgenology, 2020

# Title

The Diagnostic Performance of MRI for Detection of E…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">14</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">algorithm-ALE (417 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Yeung</mark>, Andy Wai Kan
Public health nutrition, 2021

# Title

Brain responses to watching food commercials compared with nonfood commercials: a meta-analysis on neuroimaging studies.

# Keywords

Child obesi…
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
                    <mark class="annotated-text">Fusar</mark>-Poli, Paolo and Howes, Oliver and Bechdolf, Andreas and Borgwardt, Stefan
Journal of psychiatry &amp; neuroscience : JPN, 2012

# Title

Mapping vulnerability to bipolar disorder: a systematic review and…
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
                    <mark class="annotated-text">Sacheli</mark>, Lucia Maria and Tomasetig, Giulia and Musco, Margherita Adelaide and Pizzi, Stefano and Bottini, Gabriella and Pizzamiglio, Luigi and Paulesu, Eraldo
Neuroscience and biobehavioral reviews, 2022

# …
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
Biological psychology, 2019

# Title

Neural correlates of explicit and implicit memory at encoding and retrieval: A unified framework and meta-analysis of functional neuroimaging studies.
…
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
Neuropsychologia, 2011

# Title

Reprint of: fMRI studies of successful emotional memory encoding: a quantitative meta-analysis.…
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
                    <mark class="annotated-text">Fischer</mark>, Manda and Moscovitch, Morris and Alain, Claude
Wiley interdisciplinary reviews. Cognitive science, 2021

# Title

A systematic review and meta-analysis of memory-guided attention: Frontal and pariet…
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
                    <mark class="annotated-text">Derrfuss</mark>, Jan and Brass, Marcel and Neumann, Jane and von Cramon, D Yves
Human brain mapping, 2005

# Title

Involvement of the inferior frontal junction in cognitive control: meta-analyses of switching and S…
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
                    <mark class="annotated-text">Miola</mark>, Alessandro and Meda, Nicola and Perini, Giulia and Sambataro, Fabio
Psychiatry and clinical neurosciences, 2023

# Title

Structural and functional features of treatment-resistant depression: A syst…
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
                    <mark class="annotated-text">Simmons</mark>, Alan N and Matthews, Scott C
Neuropharmacology, 2012

# Title

Neural circuitry of PTSD with or without mild traumatic brain injury: a meta-analysis.

# Keywords



# Abstract

Posttraumatic Stress …
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
                    <mark class="annotated-text">Morriss</mark>, Jayne and Gell, Martin and van Reekum, Carien M
Neuroscience and biobehavioral reviews, 2019

# Title

The uncertain brain: A co-ordinate based meta-analysis of the neural signatures supporting unce…
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
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">software-gingerale (221 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Ji</mark>, Shanling and Zhang, Yinghui and Chen, Nan and Liu, Xia and Li, Yongchao and Shao, Xuexiao and Yang, Zhengwu and Yao, Zhijun and Hu, Bin
Brain imaging and behavior, 2022

# Title

Shared increased en…
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
                    <mark class="annotated-text">Costa</mark>, Cristiano and Cristea, Ioana Alina and Dal Bò, Elisa and Melloni, Caterina and Gentili, Claudio
Journal of child psychology and psychiatry, and allied disciplines, 2021

# Title

Brain activity duri…
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
                    <mark class="annotated-text">Hétu</mark>, Sébastien and Grégoire, Mathieu and Saimpont, Arnaud and Coll, Michel-Pierre and Eugène, Fanny and Michon, Pierre-Emmanuel and Jackson, Philip L
Neuroscience and biobehavioral reviews, 2014

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
                    <mark class="annotated-text">Horn</mark>, Mathilde and Jardri, Renaud and D&#39;Hondt, Fabien and Vaiva, Guillaume and Thomas, Pierre and Pins, Delphine
Cognitive, affective &amp; behavioral neuroscience, 2016

# Title

The multiple neural networks…
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
                    <mark class="annotated-text">Eres</mark>, Robert and Louis, Winnifred R and Molenberghs, Pascal
Social neuroscience, 2018

# Title

Common and distinct neural networks involved in fMRI studies investigating morality: an ALE meta-analysis.

…
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
                    <mark class="annotated-text">Ferraro</mark>, Stefania and Klugah-Brown, Benjamin and Tench, Christopher R and Bazinet, Vincent and Bore, Mercy Chepngetich and Nigri, Anna and Demichelis, Greta and Bruzzone, Maria Grazia and Palermo, Sara and Z…
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
                    <mark class="annotated-text">Yang</mark>, Jie and Andric, Michael and Mathew, Mili M
Neuroscience and biobehavioral reviews, 2016

# Title

The neural basis of hand gesture comprehension: A meta-analysis of functional magnetic resonance ima…
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
                    <mark class="annotated-text">King</mark>, M and Rauch, H G and Stein, D J and Brooks, S J
NeuroImage, 2015

# Title

The handyman&#39;s brain: a neuroimaging meta-analysis describing the similarities and differences between grip type and patter…
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
                    <mark class="annotated-text">Stefaniak</mark>, James D and Alyahya, Reem S W and Lambon Ralph, Matthew A
NeuroImage, 2021

# Title

Language networks in aphasia and health: A 1000 participant activation likelihood estimation meta-analysis.

# Ke…
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
                    <mark class="annotated-text">Cona</mark>, Giorgia and Scarpazza, Cristina
Human brain mapping, 2020

# Title

Where is the &#34;where&#34; in the brain? A meta-analysis of neuroimaging studies on spatial cognition.

# Keywords

activation likelihoo…
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
    
    <details style="--label-color: #eeeeec;">
        <summary class="label-display">DONE (184 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Fusar</mark>-Poli, Paolo and Perez, Jorge and Broome, Matthew and Borgwardt, Stefan and Placentino, Anna and Caverzasi, Eduardo and Cortesi, Mariachiara and Veggiotti, Pierangelo and Politi, Peirluigi and Barale,…
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
                    <mark class="annotated-text">Samartsidis</mark>, Pantelis and Eickhoff, Claudia R and Eickhoff, Simon B and Wager, Tor D and Barrett, Lisa Feldman and Atzil, Shir and Johnson, Timothy D and Nichols, Thomas E
Journal of the Royal Statistical Societ…
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
                    <mark class="annotated-text">Andrews</mark>-Hanna, Jessica R and Saxe, Rebecca and Yarkoni, Tal
NeuroImage, 2014

# Title

Contributions of episodic retrieval and mentalizing to autobiographical thought: evidence from functional neuroimaging, …
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
                    Ramsey, J D and Spirtes, P and Glymour, C
NeuroImage, 2011

# Title

<mark class="annotated-text">On meta-analyses of imaging data and the mixture of records.
</mark>
# Keywords



# Abstract

Neumann et al. (2010) aim to find directed graphical representations of the independence and dependence relations among activities in brain regions by applying a search proc…
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
                    Peiffer, <mark class="annotated-text">Ann</mark> M. and Maldjian, Joseph A. and Laurienti, Paul J.
Int J Biomed Imaging, 2007

# Title

Resurrecting Brinley Plots for a Novel Use: Meta-Analyses of Functional Brain Imaging Data in Older Adults

# Ke…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2233772/"
                                       >PMC2233772</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Costafreda</mark>, Sergi G.
Front Neuroinformatics, 2009

# Title

Pooling fMRI Data: Meta-Analysis, Mega-Analysis and Multi-Center Studies

# Keywords

fMRI
meta-analysis
mega-analysis
multi-center studies
power
fals…
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
                    <mark class="annotated-text">Sugranyes</mark>, Gisela and Kyriakopoulos, Marinos and Corrigall, Richard and Taylor, Eric and Frangou, Sophia
PLoS One, 2011

# Title

Autism Spectrum Disorders and Schizophrenia: Meta-Analysis of the Neural Correl…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Huang</mark>, Wenjing and Pach, Daniel and Napadow, Vitaly and Park, Kyungmo and Long, Xiangyu and Neumann, Jane and Maeda, Yumi and Nierhaus, Till and Liang, Fanrong and Witt, Claudia M.
PLoS One, 2012

# Title
…
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
                    <mark class="annotated-text">Hayes</mark>, Jasmeet P and Hayes, Scott M and Mikedis, Amanda M
Biol Mood Anxiety Disord, 2012

# Title

Quantitative meta-analysis of neural activity in posttraumatic stress disorder

# Keywords

Activation lik…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3430553/"
                                       >PMC3430553</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Hattingh</mark>, Coenraad J. and Ipser, J. and Tromp, S. A. and Syal, S. and Lochner, C. and Brooks, S. J. and Stein, D. J.
Front Hum Neurosci, 2012

# Title

Functional magnetic resonance imaging during emotion rec…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3547329/"
                                       >PMC3547329</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA1 (148 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …s process effort-related costs and integrate them with rewards. We conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (<mark class="annotated-text">23</mark> studies, 15 maps, 549 participants) and net value (15 studies, 11 maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedi…
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
                    …fort-related costs and integrate them with rewards. We conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (23 studies, <mark class="annotated-text">15</mark> maps, 549 participants) and net value (15 studies, 11 maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedial prefronta…
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
                    …ray matter volume (GMV) and fMRI abnormalities during cognitive control were compared in the overall sample and in age-, sex- and IQ-matched subgroups with seed-based d mapping meta-analytic methods. <mark class="annotated-text">Eighty-six </mark>independent VBM (1533 ADHD and 1295 controls; 1445 ASD and 1477 controls) and 60 fMRI datasets (1001 ADHD and 1004 controls; 335 ASD and 353 controls) were identified. The VBM meta-analyses revealed A…
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
                    … fulfilled the inclusion criteria and were included in the meta-analysis. Details are shown in   and  . 

### Facial emotion recognition 
  
We identified 16 FER studies in ASD and 33 in SZ, of which <mark class="annotated-text">5</mark> and 12 respectively were used in the ALE analysis. The total sample comprised 55 ASD and 203 SZ patients and 253 healthy controls (HC) ( ). Demographic details for all participants and clinical infor…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …
   Studies included in the ALE meta-analyses.        
The meta-analysis for verum acupuncture stimuli on greater activation of verum acupuncture points compared to baseline (1a, verum&gt;rest) included <mark class="annotated-text">36</mark> experiments, 377 subjects and 470 foci. The result showed significant convergence in the supramarginal gyrus, secondary somatosensory cortex (SII), pre-supplementary motor area (pre-SMA), middle cigu…
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
                    …thods 
  
We conducted a literature search for PET and fMRI studies of PTSD that were published before February 2011. The article search resulted in 79 functional neuroimaging PTSD studies. Data from <mark class="annotated-text">26</mark> PTSD peer-reviewed neuroimaging articles reporting results from 342 adult patients and 342 adult controls were included. Peak activation coordinates from selected articles were used to generate activ…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3430553/"
                                       >PMC3430553</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …socially emotive cues in SAD was undertaken. ALE meta-analysis, a voxel-based meta-analytic technique, was used to estimate the most significant activations during emotional recognition.   Results:   <mark class="annotated-text">Seven</mark> studies were eligible for inclusion in the meta-analysis, constituting a total of 91 subjects with SAD, and 93 healthy controls. The most significant areas of activation during emotional vs. neutral …
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
                    …were used, we would find evidence of face-sensitive ATL activations that extend into the ventral ATL. 


## Methods 
  
### Meta-analysis 
  
A total of 25 articles were included in the ALE analysis. <mark class="annotated-text">Seven</mark> of these studies were used in the personally familiar condition with a total of 136 subjects (70 male, 66 female; mean age = 28.9 years). The famous face condition was comprised of 18 studies and had…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3561664/"
                                       >PMC3561664</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … imaging,” “motor sequence learning AND imaging,” and “working memory AND imaging.” Additionally, the searches used the limits “Humans,” “English,” and “Adult 19-44 years.” These searches resulted in <mark class="annotated-text">45</mark>, 149, and 1997 papers, respectively. We also consulted a recent review of motor learning and included related work on sensorimotor adaptation not found in our PubMed search (Seidler,  ). We followed …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3566602/"
                                       >PMC3566602</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ng (Bo and Seidler,  ; Bo et al.,  ,  ,  ; Anguera et al.,  ,  ). Thus, we excluded studies with emotional, auditory, and visual manipulations. After excluding studies that did not meet our criteria, <mark class="annotated-text">5</mark> studies of visuomotor adaptation, 18 studies of sequence learning, and 44 studies of working memory remained (9 of spatial working memory, and 35 of verbal working memory). Finally, for our analyses …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3566602/"
                                       >PMC3566602</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA2 (102 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … rewards. We conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (23 studies, 15 maps, 549 participants) and net value (<mark class="annotated-text">15</mark> studies, 11 maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedial prefrontal cortex (vmPFC) showed the opposite effec…
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
                    … conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (23 studies, 15 maps, 549 participants) and net value (15 studies, <mark class="annotated-text">11</mark> maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedial prefrontal cortex (vmPFC) showed the opposite effect. Moreover,…
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
                    …the overall sample and in age-, sex- and IQ-matched subgroups with seed-based d mapping meta-analytic methods. Eighty-six independent VBM (1533 ADHD and 1295 controls; 1445 ASD and 1477 controls) and <mark class="annotated-text">60</mark> fMRI datasets (1001 ADHD and 1004 controls; 335 ASD and 353 controls) were identified. The VBM meta-analyses revealed ADHD-differentiating decreased ventromedial orbitofrontal (z = 2.22, p &lt; 0.0001) …
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
                    …lled the inclusion criteria and were included in the meta-analysis. Details are shown in   and  . 

### Facial emotion recognition 
  
We identified 16 FER studies in ASD and 33 in SZ, of which 5 and <mark class="annotated-text">12</mark> respectively were used in the ALE analysis. The total sample comprised 55 ASD and 203 SZ patients and 253 healthy controls (HC) ( ). Demographic details for all participants and clinical information …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tor area (pre-SMA), middle cigulate gyrus, insula, thalamus and precentral gyrus. The meta-analysis for greater deactivation of verum acupuncture points compared to baseline (1b, rest&gt;verum) included <mark class="annotated-text">22</mark> experiments, 219 subjects and 265 foci and the result revealed significant convergence in the subgenual anterior cingulate, subgenual cortex, amygdala/hippocampal formation, ventromedial prefrontal c…
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
                    …ined to examine the neural regions involved across tasks and then were analyzed separately to examine differences between the two design types. A replicate set of analyses was performed that included <mark class="annotated-text">ROI-based studies</mark>. Differences in the whole-brain voxel-wise results with the inclusion of ROIs, when present, are noted in the tables and results. 

For each analysis reported, peak activation coordinates were smooth…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3430553/"
                                       >PMC3430553</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …LE analysis. Seven of these studies were used in the personally familiar condition with a total of 136 subjects (70 male, 66 female; mean age = 28.9 years). The famous face condition was comprised of <mark class="annotated-text">18</mark> studies and had 247 subjects (125 male, 122 female; mean age = 28.74 years). A total of 202 foci were used in the personally familiar face condition and 340 foci were used in the famous face conditio…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3561664/"
                                       >PMC3561664</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ging,” “motor sequence learning AND imaging,” and “working memory AND imaging.” Additionally, the searches used the limits “Humans,” “English,” and “Adult 19-44 years.” These searches resulted in 45, <mark class="annotated-text">149</mark>, and 1997 papers, respectively. We also consulted a recent review of motor learning and included related work on sensorimotor adaptation not found in our PubMed search (Seidler,  ). We followed the s…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3566602/"
                                       >PMC3566602</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …  ,  ; Anguera et al.,  ,  ). Thus, we excluded studies with emotional, auditory, and visual manipulations. After excluding studies that did not meet our criteria, 5 studies of visuomotor adaptation, <mark class="annotated-text">18</mark> studies of sequence learning, and 44 studies of working memory remained (9 of spatial working memory, and 35 of verbal working memory). Finally, for our analyses of sequence learning, we divided our …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3566602/"
                                       >PMC3566602</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …E, Family Wise Error correction for multiple comparisons; FDR, False Discovery Rate correction for multiple comparisons. 
  
We considered peaks emerging from simple effects of nouns vs. baseline and <mark class="annotated-text">verbs vs. baseline</mark>, and peaks corresponding to direct comparisons of verbs-minus-nouns and nouns-minus-verbs; activation coordinates that emerged in conjunction analyses or main effects (e.g., the main effect of task i…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3695563/"
                                       >PMC3695563</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">N studies found (90 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …y variables which displayed group differences were subjected to voxel-wise meta-regression analyses in order to examine their effect on the ALE results. 



## Results 
  
The initial search returned <mark class="annotated-text">415</mark> citations. Of these, 337 studies were discarded after reviewing the abstracts while the full text of the remaining 76 citations was examined in more detail. Thirty three studies fulfilled the inclusi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …er 2009, without any language restrictions. We included all studies using fMRI to investigate the effect of acupuncture on the human brain (at least one group that received needle-based acupuncture). <mark class="annotated-text">779</mark> papers were identified, 149 met the inclusion criteria for the descriptive analysis, and 34 were eligible for the meta-analyses. From a descriptive perspective, multiple studies reported that acupunc…
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
                    …derstanding of the neurocircuitry of PTSD. 


## Methods 
  
We conducted a literature search for PET and fMRI studies of PTSD that were published before February 2011. The article search resulted in <mark class="annotated-text">79</mark> functional neuroimaging PTSD studies. Data from 26 PTSD peer-reviewed neuroimaging articles reporting results from 342 adult patients and 342 adult controls were included. Peak activation coordinates…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3430553/"
                                       >PMC3430553</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … all remaining articles was then assessed using with a data extraction template, constructed for the purpose of organizing and extracting information from included articles. Following this procedure, <mark class="annotated-text">244</mark> initial publications were found, which were reduced to 44 after examining the title and abstract. A total of 7 out of 44 studies fulfilled all inclusion criteria, resulting in a combined sample of 91…
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
                    … imaging,” “motor sequence learning AND imaging,” and “working memory AND imaging.” Additionally, the searches used the limits “Humans,” “English,” and “Adult 19-44 years.” These searches resulted in <mark class="annotated-text">45</mark>, 149, and 1997 papers, respectively. We also consulted a recent review of motor learning and included related work on sensorimotor adaptation not found in our PubMed search (Seidler,  ). We followed …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3566602/"
                                       >PMC3566602</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ging,” “motor sequence learning AND imaging,” and “working memory AND imaging.” Additionally, the searches used the limits “Humans,” “English,” and “Adult 19-44 years.” These searches resulted in 45, <mark class="annotated-text">149</mark>, and 1997 papers, respectively. We also consulted a recent review of motor learning and included related work on sensorimotor adaptation not found in our PubMed search (Seidler,  ). We followed the s…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3566602/"
                                       >PMC3566602</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …otor sequence learning AND imaging,” and “working memory AND imaging.” Additionally, the searches used the limits “Humans,” “English,” and “Adult 19-44 years.” These searches resulted in 45, 149, and <mark class="annotated-text">1997</mark> papers, respectively. We also consulted a recent review of motor learning and included related work on sensorimotor adaptation not found in our PubMed search (Seidler,  ). We followed the same exclus…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3566602/"
                                       >PMC3566602</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nouns or verbs, we ran other four queries through the same database searching for “noun AND fMRI,” “nouns AND PET,” “verbs AND fMRI,” and “verbs AND PET.” After removing duplicates, we were left with <mark class="annotated-text">164</mark> records, which were then screened to exclude those studies that clearly did not satisfy the inclusion criteria as revealed by the title, keywords, or abstract. For example, several studies did includ…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3695563/"
                                       >PMC3695563</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ds]) AND (“teaching”[MeSH Terms] OR “teaching”[All Fields] OR “instruction”[All Fields]))). The   Web of Science   search yielded 75 articles. The   PubMed   search yielded 49 articles. The resulting <mark class="annotated-text">124</mark> articles were examined and those that did not meet criteria were systematically eliminated ( )  . Next, using references from studies that met inclusion criteria, additional studies were considered. …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3888398/"
                                       >PMC3888398</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …uded studies, specifically in the analysis of the semantic verbal fluency map, must be kept in mind when interpreting the results of our subtraction analysis. 



## Results 
  
The search identified <mark class="annotated-text">254</mark> studies which were screened by title and abstract. 196 of these studies had to be excluded because they did not fulfill the inclusion criteria. The full text of the remaining 58 studies was scrutiniz…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3903437/"
                                       >PMC3903437</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">algorithm-SDM (80 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Zeng</mark>, Jianguang and You, Lantao and Yang, Fan and Luo, Ya and Yu, Shuxian and Yan, Jiangnan and Liu, Mengqi and Yang, Xun
Human brain mapping, 2023

# Title

A meta-analysis of the neural substrates of mo…
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
                    <mark class="annotated-text">Lopez</mark>-Gamundi, Paula and Yao, Yuan-Wei and Chong, Trevor T-J and Heekeren, Hauke R and Mas-Herrero, Ernest and Marco-Pallarés, Josep
Neuroscience and biobehavioral reviews, 2022

# Title

The neural basis …
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
                    <mark class="annotated-text">Schulze</mark>, Lars and Schulze, Andreas and Renneberg, Babette and Schmahl, Christian and Niedtfeld, Inga
Biological psychiatry. Cognitive neuroscience and neuroimaging, 2020

# Title

Neural Correlates of Affect…
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
                    <mark class="annotated-text">Fullana</mark>, Miquel A and Albajes-Eizagirre, Anton and Soriano-Mas, Carles and Vervliet, Bram and Cardoner, Narcís and Benet, Olívia and Radua, Joaquim and Harrison, Ben J
Neuroscience and biobehavioral reviews,…
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
                    <mark class="annotated-text">Han</mark>, Jung Eun and Boachie, Nadia and Garcia-Garcia, Isabel and Michaud, Andréanne and Dagher, Alain
Physiology &amp; behavior, 2019

# Title

Neural correlates of dietary self-control in healthy adults: A me…
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
                    <mark class="annotated-text">Picó</mark>-Pérez, Maria and Radua, Joaquim and Steward, Trevor and Menchón, José M and Soriano-Mas, Carles
Progress in neuro-psychopharmacology &amp; biological psychiatry, 2018

# Title

Emotion regulation in mood…
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
                    <mark class="annotated-text">Picó</mark>-Pérez, Maria and Vieira, Rita and Fernández-Rodríguez, Marcos and De Barros, Maria Antónia Pereira and Radua, Joaquim and Morgado, Pedro
Psychological medicine, 2022

# Title

Multimodal meta-analysi…
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
                    <mark class="annotated-text">Leroy</mark>, Arnaud and Amad, Ali and D&#39;Hondt, Fabien and Pins, Delphine and Jaafari, Nematollah and Thomas, Pierre and Jardri, Renaud
Schizophrenia research, 2021

# Title

Reward anticipation in schizophrenia:…
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
                    <mark class="annotated-text">Luna</mark>, Licia P and Radua, Joaquim and Fortea, Lydia and Sugranyes, Gisela and Fortea, Adriana and Fusar-Poli, Paolo and Smith, Lee and Firth, Joseph and Shin, Jae Il and Brunoni, Andre R and Husain, Muhamm…
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
                    <mark class="annotated-text">Lisofsky</mark>, Nina and Kazzer, Philipp and Heekeren, Hauke R and Prehn, Kristin
Neuropsychologia, 2015

# Title

Investigating socio-cognitive processes in deception: a quantitative meta-analysis of neuroimaging …
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
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA3 (63 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … fulfilled the inclusion criteria and were included in the meta-analysis. Details are shown in   and  . 

### Facial emotion recognition 
  
We identified 16 FER studies in ASD and 33 in SZ, of which <mark class="annotated-text">5 and 12</mark> respectively were used in the ALE analysis. The total sample comprised 55 ASD and 203 SZ patients and 253 healthy controls (HC) ( ). Demographic details for all participants and clinical information …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …the direct contrast of verum and sham acupuncture on greater activation from verum than sham acupuncture or greater deactivation for sham acupuncture (2a, verum&gt;sham) we included in the meta-analysis <mark class="annotated-text">17</mark> experiments, 156 subjects and 171 foci, resulting in significant convergence in fusiform gyrus, cerebellum, SI and middle cingulate gyrus. Whereas, on greater deactivation from verum than sham acupun…
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
                    …P   &lt; 0.05 and a less conservative cluster-extent of 40 mm  (i.e., 5 contiguous voxels) was used. 



##  Results  
  
Separate meta-analyses were run to examine the neural activity across and within <mark class="annotated-text">symptom provocation</mark> and cognitive-emotional tasks in PTSD. Because of the variability in naming conventions of medial prefrontal cortex regions across different studies, activated regions are listed in the text and tabl…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3430553/"
                                       >PMC3430553</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …otor sequence learning AND imaging,” and “working memory AND imaging.” Additionally, the searches used the limits “Humans,” “English,” and “Adult 19-44 years.” These searches resulted in 45, 149, and <mark class="annotated-text">1997</mark> papers, respectively. We also consulted a recent review of motor learning and included related work on sensorimotor adaptation not found in our PubMed search (Seidler,  ). We followed the same exclus…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3566602/"
                                       >PMC3566602</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e excluded studies with emotional, auditory, and visual manipulations. After excluding studies that did not meet our criteria, 5 studies of visuomotor adaptation, 18 studies of sequence learning, and <mark class="annotated-text">44</mark> studies of working memory remained (9 of spatial working memory, and 35 of verbal working memory). Finally, for our analyses of sequence learning, we divided our studies into those investigating impl…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3566602/"
                                       >PMC3566602</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … considerable overlap between the two contrasts, the spatial extent of activation tended to be greater in antisaccade &gt; fixation compared to prosaccade &gt; fixation. 


### Antisaccade &gt; prosaccade 
  
<mark class="annotated-text">Thirteen</mark> manuscripts reported foci for antisaccade greater than prosaccade, yielding 192 total foci. Antisaccade vs. prosaccade trials (Table  , Figure  ) consistently activated 13 regions, including frontal …
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
                    …ency tasks was performed. The phonemic fluency data set included 17 experiments reporting 193 foci (N = 196), the semantic data set 13 experiments reporting 117 foci (N = 298) and the pooled data set <mark class="annotated-text">30</mark> experiments yielding 310 foci (N = 494). The subtraction of the phonemic versus semantic verbal fluency map revealed no significant differences in the ALE maps. 



## Discussion 
  
In this study, w…
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
                    …orted in 66 experiments including 1023 participants. 

We also performed four separate ALE analyses on four categories of studies in relation to the type of familiarity paradigm (recently learned vs. <mark class="annotated-text">familiar environment)</mark> and spatial strategies (egocentric vs. allocentric strategies) used in the experiment. 

Regarding the categorization of studies according to degree of familiarity, we separated experiments according…
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
                    … for example, their home town (Maguire et al.  ; Nemmi et al.  ), college campus (Epstein and Ward  ) or a specific district (Hirshhorn et al.  ). We categorized 40 experiments as RL environments and <mark class="annotated-text">26</mark> as F environments. 

Regarding spatial strategies, the allocentric strategy category included studies that required participants to access a cognitive map of the environment or tasks that forced them…
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
                    …nces were identified. In case of greater activation in the PBD group relative to HR, the analysis was also not performed due to a small sample size and few experiments showing significant results. 


<mark class="annotated-text">### PBD and TD: Recognizing the illness from wellness 
</mark>  
Patients with PBD demonstrated greater activation in the subcortical regions of the right amygdala, the parahippocampal gyrus, the subgenual ACC, and the medial PFC, and in the left ventral striatu…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4217331/"
                                       >PMC4217331</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">N contrasts included (61 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …r differences amongst morality tasks are the cause for such heterogeneous findings. Therefore, in the present study, a series of activation likelihood estimation (ALE) meta-analyses were conducted on <mark class="annotated-text">123</mark> datasets (inclusive of 1963 participants) to address this question. The ALE meta-analyses revealed a series of common brain areas associated with all moral tasks, including medial prefrontal cortex, …
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
                    …rch to collect resting-state functional magnetic resonance imaging (rs-fMRI) studies in patients with psychiatric disorders. This work identified 9 eligible rs-fMRI studies, which included a total of <mark class="annotated-text">14</mark> experiments, 67 activation foci, and 1383 subjects. We tested the convergence across their findings by using the activation likelihood estimation method. P-value maps were corrected by using cluster-…
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
   Studies included in the ALE meta-analyses.        
The meta-analysis for verum acupuncture stimuli on greater activation of verum acupuncture points compared to baseline (1a, verum&gt;rest) included <mark class="annotated-text">36</mark> experiments, 377 subjects and 470 foci. The result showed significant convergence in the supramarginal gyrus, secondary somatosensory cortex (SII), pre-supplementary motor area (pre-SMA), middle cigu…
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
                    …tor area (pre-SMA), middle cigulate gyrus, insula, thalamus and precentral gyrus. The meta-analysis for greater deactivation of verum acupuncture points compared to baseline (1b, rest&gt;verum) included <mark class="annotated-text">22</mark> experiments, 219 subjects and 265 foci and the result revealed significant convergence in the subgenual anterior cingulate, subgenual cortex, amygdala/hippocampal formation, ventromedial prefrontal c…
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
                    …the direct contrast of verum and sham acupuncture on greater activation from verum than sham acupuncture or greater deactivation for sham acupuncture (2a, verum&gt;sham) we included in the meta-analysis <mark class="annotated-text">17</mark> experiments, 156 subjects and 171 foci, resulting in significant convergence in fusiform gyrus, cerebellum, SI and middle cingulate gyrus. Whereas, on greater deactivation from verum than sham acupun…
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
                    …onvergence in fusiform gyrus, cerebellum, SI and middle cingulate gyrus. Whereas, on greater deactivation from verum than sham acupuncture or greater activation for sham (2b, sham&gt;verum, 21 subjects, <mark class="annotated-text">3</mark> experiments and 27 foci) the result showed significant convergence in supramarginal gyrus, superior temporal gyrus and cuneus ( ,  ). 
   Clusters showing significant convergence for verum versus sha…
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
                    … 3a–d for the pre-post contrast on verum or sham acupuncture compared to baseline ( ,  ). The analysis of greater activation of verum acupuncture than baseline (3a, verum&gt;rest) included 234 subjects, <mark class="annotated-text">20</mark> experiments and 305 foci and revealed significant convergence in middle cingulate gyrus, pre-SMA, superior temporal gyrus, supramarginal gyrus, SII, thalamus and insula. The analysis of greater deact…
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
                    …e gyrus, pre-SMA, superior temporal gyrus, supramarginal gyrus, SII, thalamus and insula. The analysis of greater deactivation of verum acupuncture compared to baseline (3b, rest&gt;verum, 172 subjects, <mark class="annotated-text">15</mark> experiments and 222 foci) came to the following significant convergence: subgenual anterior cingulate, amygdala/hippocampal formation, vmPFC and PCC. Comparing results on greater activation of sham a…
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
                    …gence: subgenual anterior cingulate, amygdala/hippocampal formation, vmPFC and PCC. Comparing results on greater activation of sham acupuncture points than baseline (3c, sham&gt;rest) from 164 subjects, <mark class="annotated-text">15</mark> experiments and 200 foci, showed significant convergence in cerebellum, supramarginal gyrus, superior temporal gyrus and thalamus. Including data on greater deactivation of sham acupuncture points co…
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
                    …ence in cerebellum, supramarginal gyrus, superior temporal gyrus and thalamus. Including data on greater deactivation of sham acupuncture points compared to baseline (3d, rest&gt;sham) from 50 subjects, <mark class="annotated-text">5</mark> experiments and 52 foci, resulted in significant convergence in pregenual anterior cingulate, subgenual cortex and parahippocampal gyrus. 

Finally, in the contrast (subtraction) comparing the betwee…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3322129/"
                                       >PMC3322129</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">exclude (56 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Fusar</mark>-Poli, Paolo and Perez, Jorge and Broome, Matthew and Borgwardt, Stefan and Placentino, Anna and Caverzasi, Eduardo and Cortesi, Mariachiara and Veggiotti, Pierangelo and Politi, Peirluigi and Barale,…
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
                    Yuan, <mark class="annotated-text">Rui</mark> and Biswal, Bharat B and Zaborszky, Laszlo
Cerebral cortex (New York, N.Y. : 1991), 2020

# Title

Functional Subdivisions of Magnocellular Cell Groups in Human Basal Forebrain: Test-Retest Resting-S…
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
                    Lange, N
Human brain mapping, 2010

# Title

<mark class="annotated-text">Empirical and substantive models, the Bayesian paradigm, and meta-analysis in functional brain imaging.
</mark>
# Keywords



# Abstract

Functional neuroimaging research is currently rediscovering and adapting established statistical methods for its use, including design of experiments, the general linear mod…
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
Neuroscience and biobehavioral reviews, 2022

# Title

<mark class="annotated-text">Attention- versus significance-driven memory formation: Taxonomy, neural substrates, and meta-analyses.
</mark>
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

Functional neuroimaging dat…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">discusses MAs, not a MA</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Ramsey, J D and Spirtes, P and Glymour, C
NeuroImage, 2011

# Title

<mark class="annotated-text">On meta-analyses of imaging data and the mixture of records.
</mark>
# Keywords



# Abstract

Neumann et al. (2010) aim to find directed graphical representations of the independence and dependence relations among activities in brain regions by applying a search proc…
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
                    Jennings, Robin G and Van Horn, John D
Neuroinformatics, 2012

# Title

<mark class="annotated-text">Publication bias in neuroimaging research: implications for meta-analyses.
</mark>
# Keywords



# Abstract

Neuroimaging and the neurosciences have made notable advances in sharing activation results through detailed databases, making meta-analysis of the published research faster…
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
                    Smith, David V and Delgado, Mauricio R
Human brain mapping, 2018

# Title

<mark class="annotated-text">Meta-analysis of psychophysiological interactions: Revisiting cluster-level thresholding and sample sizes.
</mark>
# Keywords

CBMA 
PPI 
fMRI 
meta-analysis 
open science 
psychophysiological interaction 


# Abstract

Within the neuroimaging community, coordinate based meta-analyses (CBMAs) are essential for ag…
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
                    Eickhoff, S B and Nickl-Jockschat, T and Kurth, F
Der Nervenarzt, 2010

# Title

<mark class="annotated-text">[Meta-analyses in clinical brain research].
</mark>
# Keywords



# Abstract

Positron emission tomography (PET) and functional magnetic resonance imaging (fMRI) have brought about an immense increase in findings on the localization of motor, cognitiv…
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
                    Shin, Minho and Jeon, Hyeon-Ae
Cerebral cortex (New York, N.Y. : 1991), 2022

# Title

<mark class="annotated-text">A Cortical Surface-Based Meta-Analysis of Human Reasoning.
</mark>
# Keywords

Bayesian meta-analysis of the cortical surface (BMACS) 
functional magnetic resonance imaging 
inductive and deductive reasoning 
integrated nested Laplace approximation (INLA) 
log-Gauss…
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
                    Goutte, C and Hansen, L K and Liptrot, M G and Rostrup, E
Human brain mapping, 2001

# Title

<mark class="annotated-text">Feature-space clustering for fMRI meta-analysis.
</mark>
# Keywords



# Abstract

Clustering functional magnetic resonance imaging (fMRI) time series has emerged in recent years as a possible alternative to parametric modeling approaches. Most of the work…
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
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">thresholding (47 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …rs-fMRI studies, which included a total of 14 experiments, 67 activation foci, and 1383 subjects. We tested the convergence across their findings by using the activation likelihood estimation method. <mark class="annotated-text">P-value maps were corrected by using cluster-level family-wise error p &lt; 0.05 and permuting 2000 times. </mark>Results showed that patients with different psychiatric disorders shared commonly increased entropy of brain signals in the left inferior and middle frontal gyri, and the right fusiform gyrus, cuneus,…
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
                    …n a voxel-by-voxel basis to test for convergent (random-effects) rather than study specific foci (fixed-effects). All ALE data processing was performed using the BrainMap Search and View software ( ).<mark class="annotated-text"> The threshold of statistical significance was set at p&lt;0.05, with False Discovery Rate (FDR) correction for multiple comparisons and a minimum cluster size of 80 mm .</mark> Each ALE map was imported into Mango ( ) and overlaid on an anatomical Template ( ) for representation purposes. Significant clusters were manually localized and Brodmann areas (BA) were identified u…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …. ALE statistics calculated the probability that at least one of the foci lay within each voxel and, therefore, the likelihood that each voxel was activated across all studies included in the analysis<mark class="annotated-text">. The ALE statistic maps were compared with a null-distribution of random spatial associations between experiments (random-effects model) to assess for above chance clustering between experiments using a threshold at false discovery rate (FDR) corrected   P   &lt; 0.05 and a cluster-extent of 100 mm . 
</mark>
To explore the hypothesis that activity in the ventromedial prefrontal cortex and the amygdala was inversely related, we first identified whole-brain studies that reported increased ventromedial pref…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3430553/"
                                       >PMC3430553</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …els via measurement error, which bypasses reliance on publication-specific anatomical labeling (Laird et al.,  ). 

For this ALE, the latest version of the ALE software (Eickhoff et al.,  ) was used, <mark class="annotated-text">with correction using False Discovery Rate (FDR) at   p   = 0.05 and a minimum cluster threshold of 160 mm .</mark> Previous versions of GingerALE calculated the probability of voxel activation in the brain on the basis of all foci reported in studies, as if these 3D coordinates were independent of each other. Thi…
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
                    ….,  ; Turkeltaub et al.,  ). 


### Statistical analysis 
  
In order to guarantee sufficient statistical power to the analyses and to exclude clusters that were not clear sign of converging evidence,<mark class="annotated-text"> only those clusters that contained 10 or more activation peaks, coming from at least five different studies were considered further. </mark>Because it was impossible to determine   a priori   the exact cluster size that granted the statistical analysis the desired reliability, the 10-peaks and 5-studies thresholds were set   a posteriori …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3695563/"
                                       >PMC3695563</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …arate meta-analyses of selection and stopping, any studies reporting Talairach coordinates instead of MNI were converted to MNI space using the Talairach to MNI transform as implemented in GingerALE. <mark class="annotated-text">In the GingerALE analysis, we then applied the following options in addition to the default settings: non-additive ALE method ( ); output cluster minimum volume, 100 mm ; and FDR   p   &lt; 0.05. </mark>The resulting thresholded ALE map was viewed in MRIcroN ( ) and the anatomical labelling of foci facilitated by the Anatomy toolbox ( ) in SPM8 ( ). 

To perform a GingerALE conjunction (action select…
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
                    …iously generated selection and stopping ALE maps as inputs. The same options used in the previous selection and stopping ALEs were applied and permutations testing carried out with 10,000 iterations. <mark class="annotated-text">A threshold of FDR   p   &lt; 0.05 was applied to the conjunction image. </mark>


### Combined selection and stopping fMRI study 
  
#### Subjects and task 
  
21 healthy right-handed subjects were recruited from the MRC Cognition and Brain Sciences Unit volunteer panel. Four su…
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
                    …ta-analysis used Ginger ALE ( ). All fMRI coordinates were converted into Talairach space. We used the default Ginger ALE parameters ( ), and additionally added the number of subjects per experiment. <mark class="annotated-text">We chose a false discovery rate threshold level of 0.05.</mark> We used all available fMRI publications of mTBI, most of which used working memory tasks, but the tasks also included resting state fMRI, an auditory odd-ball task, and a spatial navigation task ( ).…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4107372/"
                                       >PMC4107372</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …matically converted into MNI coordinates by GingerALE), according to   procedure. The Full-Width Half-Maximum (FWHM) value was automatically computed, as this parameter is empirically determined ( ). <mark class="annotated-text">The thresholded ALE map was corrected for multiple comparisons using False Discovery Rate (FDR), at a 0.05 level of significance. Moreover, a minimum cluster size of 200 mm  was chosen. </mark>The ALE results were registered on an MNI-normalized template using MRICRO. Hereafter the link to access MRICRO 


### Tasks and Contrasts Taken into Account 
  
Regarding the musical domain, particip…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4531218/"
                                       >PMC4531218</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …and a disagreement was ruled by a third party after discussions. The full width at half maximum (FWHM) was set at 20 mm, which had excellent control for false positives according to previous studies; <mark class="annotated-text">and the statistical threshold was set to be a   P  -value &lt;0.005 without correction for false discovery rate (FDR), which was found to be able to optimize the balance between sensitivity and specificity ( ).</mark> Mean analysis and Jackknife sensitivity analysis were carried out. The last analysis was a meta-regression of voxel values across the studies by the ALSFRS-R scores of the patients’ samples. 



## R…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4656846/"
                                       >PMC4656846</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">largescale-MACM (45 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Yuan</mark>, Rui and Biswal, Bharat B and Zaborszky, Laszlo
Cerebral cortex (New York, N.Y. : 1991), 2020

# Title

Functional Subdivisions of Magnocellular Cell Groups in Human Basal Forebrain: Test-Retest Rest…
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
                    Yeung, Andy W <mark class="annotated-text">K</mark>
Journal of sleep research, 2020

# Title

Morphometric and functional connectivity changes in the brain of patients with obstructive sleep apnea: A meta-analysis.

# Keywords

brain mapping 
magnetic…
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
                    Ran, Guangming and Cao, Xiaojun and Chen, Xu
Consciousness and cognition, 2019

# Title

Emotional prediction: An ALE meta-analysis and <mark class="annotated-text">MACM</mark> analysis.

# Keywords

ALE 
Dorsolateral prefrontal cortex 
Emotional prediction 
MACM 
Orbitofrontal cortex 
Ventrolateral prefrontal cortex 


# Abstract

The prediction of emotion has been explore…
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
                    Zald, David H and McHugo, Maureen and Ray, Kimberly L and Glahn, David C and Eickhoff, Simon B and Laird, Angela R
Cerebral cortex (New York, N.Y. : 1991), 2014

# Title

<mark class="annotated-text">Meta-analytic connectivity modeling</mark> reveals differential functional connectivity of the medial and lateral orbitofrontal cortex.

# Keywords

fMRI 
network 
orbital frontal 
ventrolateral prefrontal 
ventromedial prefrontal 


# Abstra…
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
                    Kohn, N and Eickhoff, S B and Scheller, M and Laird, A R and Fox, P T and Habel, U
NeuroImage, 2014

# Title

Neural network of cognitive emotion regulation--an ALE meta-analysis and <mark class="annotated-text">MACM</mark> analysis.

# Keywords

ALE 
Angular gyrus 
DLPFC 
Emotion regulation 
MACM 
SMA 
STG 
VLPFC 
aMCC 


# Abstract

Cognitive regulation of emotions is a fundamental prerequisite for intact social funct…
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
                    …anos, F Xavier and Eickhoff, Claudia R and D&#39;Acunto, Giulia and Masi, Gabriele and Fox, Peter T and Laird, Angela R and Eickhoff, Simon B
Biological psychiatry, 2017

# Title

Functional Decoding and <mark class="annotated-text">Meta-analytic Connectivity Modeling</mark> in Adult Attention-Deficit/Hyperactivity Disorder.

# Keywords

Adults 
Attention-deficit/hyperactivity disorder 
Functional decoding 
Meta-analysis 
Meta-analytic connectivity modeling 
fMRI 


# Ab…
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
                    …preng, R Nathan
NeuroImage, 2021

# Title

Social exclusion reliably engages the default network: A meta-analysis of Cyberball.

# Keywords

Cyberball 
Default network 
Functional MRI 
Meta-analysis 
<mark class="annotated-text">Meta-analytic connectivity modeling 
</mark>Social exclusion 


# Abstract

Social exclusion refers to the experience of being disregarded or rejected by others and has wide-ranging negative consequences for well-being and cognition. Cyberball,…
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
                    …g and Northoff, Georg
NeuroImage, 2022

# Title

Spatial-topographic nestedness of interoceptive regions within the networks of decision making and emotion regulation: Combining ALE meta-analysis and <mark class="annotated-text">MACM</mark> analysis.

# Keywords

Interoception 
decision making 
emotion regulation 
insula 
meta-analysis 
salience network 


# Abstract

Prominent theories propose that interoception modulates our behaviora…
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
                    … and Wang, Chun and Zhang, Ning and Li, Chiang-Shan R and Liu, Na
Journal of psychiatric research, 2022

# Title

Symptom provocation in obsessive-compulsive disorder: A voxel-based meta-analysis and <mark class="annotated-text">meta-analytic connectivity modeling</mark>.

# Keywords

Magnetic resonance imaging 
Meta-analysis 
Meta-analytic connectivity modeling 
Neural circuit 
Obsessive–compulsive disorder 
Symptom provocation 


# Abstract

Obsessive-compulsive di…
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
                    …brain mapping, 2015

# Title

Bridging the gap between functional and anatomical features of cortico-cerebellar circuits using meta-analytic connectivity modeling.

# Keywords

cerebellum 
cognition 
<mark class="annotated-text">meta-analytic connectivity modeling 
</mark>

# Abstract

Theories positing that the cerebellum contributes to cognitive as well as motor control are driven by two sources of information: (1) studies highlighting connections between the cerebel…
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
    
    <details style="--label-color: #4e9a06;">
        <summary class="label-display">has prisma chart (42 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …d in the attribution of salience to biological social cues (e.g. facial affect). 


## Materials and Methods 
  
### Data sources and inclusion criteria 
  
The study design and report adhered to the <mark class="annotated-text">PRISMA</mark> Statement guidelines (supporting information   and  ). The search method and inclusion criteria were specified in advance, informed by existing meta-analyses  ,  ,  . All identified articles were rev…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s, as recommended [ ]. The Egger’s regression test is used to quantify the bias captured in the funnel plot, and uses the values of the effect sizes and their precision [ ]. 



## 3. Results 
  
The <mark class="annotated-text">Flow Diagram</mark> displayed in   reflects the selection process. Our review of the literature using search items as described above identified 316 potential target articles [34 were identified via the PUBMED database,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5127572/"
                                       >PMC5127572</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … monographs, theses, or reference lists in identified studies were also regarded as potential sources to be included in the meta-analysis. 


### Inclusion and exclusion criteria 
  
According to the <mark class="annotated-text">Preferred Reporting Items for Systematic Reviews and Meta-Analyses guidelines</mark>,  the following criteria were used for inclusion in the meta-analysis: 1) whole-brain analysis was used in task-free rs-fMRI studies; 2) studies included a comparison of the localized connectivity be…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5317331/"
                                       >PMC5317331</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …lusion. We contacted all corresponding authors for the 108 articles of whom 70 responded. Brain maps corresponding to 36 articles were received. Of these, 21 were excluded for reasons detailed in the <mark class="annotated-text">Prisma flow diagram</mark> (Fig.  ).   
PRISMA flow diagram 
  

In total 15 sets of whole brain group maps were included in the meta-analysis of anticipation (Supplementary Table 1). Thirty-three articles were included in the…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6327084/"
                                       >PMC6327084</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … included. 
  
Note: n/r: not reported. Age is reported either in mean and standard deviation or in range. * derived by whole-brain contrast, positive correlation with punishment frequency. 
    
The <mark class="annotated-text">PRISMA</mark> flowchart for the search and eligibility of the articles . 
  


## ALE map 
  
Two clusters were detected during the analysis (see Fig.  , Table  ; the coordinates are in Talairach space). One with …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6728376/"
                                       >PMC6728376</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ame original data set as a previous published paper were removed. In sum, a total of 94 studies met the inclusion and exclusion criteria. See   for a full overview of the study selection process. 
  
<mark class="annotated-text">Diagram outlining the study selection </mark>process.   n  , number of studies or experiments;   n   [f], number of foci;   n   [p], number of participants. 
  
Among those, fMRI coordinates were extracted from only 84 studies. Ten studies met t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6847411/"
                                       >PMC6847411</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …y (Cochrane Library), Scopus, and Informit (Health Collection). The searches were confined to full-text research manuscripts published in English and indexed from January 1990 to October 16, 2019.   
<mark class="annotated-text">Preferred reporting items of systematic reviews and meta-analyses flow diagram.</mark> BOLD, blood oxygenation level dependent; mTBI, mild traumatic brain injury; ROI, region of interest; fMRI, functional magnetic resonance imaging. 
  Fig. 1   

Detailed electronic search strategies a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6939096/"
                                       >PMC6939096</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …r including the same experiments (i.e., contrasts) using same participants in different publications ( ,  ). These controls resulted in 32 acceptable articles testing children 14 years or younger.   
<mark class="annotated-text">PRISMA</mark> flowchart for identification and eligibility of articles (template by  ). n = number of papers. 
  Fig. 1   

Contrast coordinates were selected based on whether the experimental paradigm was related…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6969084/"
                                       >PMC6969084</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nd functional changes in TN/TNP patients in order to contribute to the elucidation of central pathophysiological mechanisms involved in TN/TNP. 


## Materials and methods 
  
### Search strategy 
  
<mark class="annotated-text">Literature was searched for until August 2018. PRISMA and MOOSE guidelines were followed during the conduction of this systematic review ( ;  ). </mark>Pubmed, MEDLINE, Embase, The Cochrane Library and Google Scholar were systematically searched in order to find eligible articles regarding structural and functional changes in TN patients as measured …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6978224/"
                                       >PMC6978224</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …r analyses would uncover novel information about disease-specific dysconnectivity in the regional pattern of the DMN. 


## Method 
  
### Literature search and article eligibility 
  
We applied the <mark class="annotated-text">Preferred Reporting Items for Systematic Reviews and Meta-analyses</mark> criteria ( ) (Figure S1) to identify rsfMRI whole-brain studies published between January 1, 2005 and January 31, 2019 that reported significant differences in DMN intra-network connectivity between …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7355168/"
                                       >PMC7355168</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA4 (37 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …rison of schizophrenia and autism spectrum disorders.        


### Theory of mind 
  
Our search identified 10 studies exploring ToM related processes in ASD subjects and 17 in SZ patients, of which <mark class="annotated-text">7</mark> and 9 respectively fulfilled inclusion criteria ( ). The total analysis encompassed 91 ASD and 133 SZ patients, and 239 HC subjects. Demographic details for all participants and clinical information …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …onvergence in fusiform gyrus, cerebellum, SI and middle cingulate gyrus. Whereas, on greater deactivation from verum than sham acupuncture or greater activation for sham (2b, sham&gt;verum, 21 subjects, <mark class="annotated-text">3</mark> experiments and 27 foci) the result showed significant convergence in supramarginal gyrus, superior temporal gyrus and cuneus ( ,  ). 
   Clusters showing significant convergence for verum versus sha…
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
                    …nservative cluster-extent of 40 mm  (i.e., 5 contiguous voxels) was used. 



##  Results  
  
Separate meta-analyses were run to examine the neural activity across and within symptom provocation and <mark class="annotated-text">cognitive-emotional tasks</mark> in PTSD. Because of the variability in naming conventions of medial prefrontal cortex regions across different studies, activated regions are listed in the text and tables both by their structure spe…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3430553/"
                                       >PMC3430553</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …pants. 

We also performed four separate ALE analyses on four categories of studies in relation to the type of familiarity paradigm (recently learned vs. familiar environment) and spatial strategies (<mark class="annotated-text">egocentric</mark> vs. allocentric strategies) used in the experiment. 

Regarding the categorization of studies according to degree of familiarity, we separated experiments according to whether the environment used in…
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
                    … were included in the general analysis and in the individual ALE analysis of the paradigm (RL vs. F environment) but not in the analysis of the neural substrate of navigational strategies. A total of <mark class="annotated-text">30</mark> experiments were defined as allocentric and 34 as egocentric (see Tables   and   for more details). 

After carrying out separate ALE analyses on the categories of studies [  paradigm   (recently lea…
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
                    …yses were performed on (1) 13 studies assessing musical creativity (219 participants, 197 activation foci), (2) 24 studies assessing verbal creativity (575 participants, 207 activation foci), and (3) <mark class="annotated-text">six</mark> studies assessing visuo-spatial creativity (164 participants, 52 activation foci). 

The ALE meta-analysis was performed using GingerALE  2.3.1 with MNI coordinates (Talairach coordinates were automa…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4531218/"
                                       >PMC4531218</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …n healthy control group (HC) and transdiagnostic patient group (mixed MDD and SZ) for reward consummatory, reward anticipation, and emotional processing 
  


#### Patients (mixed MDD and SZ) 
  
For <mark class="annotated-text">reward consummatory </mark>(11 studies and 68 foci), ALE analysis found seven statistically significant activation clusters, including left GPe, right caudate head, left red nucleus, right insula, left anterior cingulate gyrus …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …up (HC) and transdiagnostic patient group (mixed MDD and SZ) for reward consummatory, reward anticipation, and emotional processing 
  


#### Patients (mixed MDD and SZ) 
  
For reward consummatory (<mark class="annotated-text">11</mark> studies and 68 foci), ALE analysis found seven statistically significant activation clusters, including left GPe, right caudate head, left red nucleus, right insula, left anterior cingulate gyrus (AC…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … frontal gyrus including the frontal eye field (BA8), the left junction of the postcentral gyrus and inferior parietal (BA3/40), and left cingulate gyrus (BA31). 

When restricted to visuospatial WM, <mark class="annotated-text">five</mark> experiments of 110 subjects identified 17 foci. Only one region exceeded the minimum cluster size; the right inferior parietal lobe (BA40). No cluster for verbal WM exceeded the minimum volume. See  …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5153561/"
                                       >PMC5153561</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … on common executive (shared activation across tasks tapping inhibition, switching, and updating executive processes; Figure  ) and each specific putative executive process (inhibition, updating, and <mark class="annotated-text">switching</mark>) were conducted. First-level analyses describe clusters that pass the applied threshold for significant conjunctive activation across these groups of studies. These analyses were computed for both th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5383671/"
                                       >PMC5383671</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - traditional ma (34 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Fusar</mark>-Poli, Paolo and Perez, Jorge and Broome, Matthew and Borgwardt, Stefan and Placentino, Anna and Caverzasi, Eduardo and Cortesi, Mariachiara and Veggiotti, Pierangelo and Politi, Peirluigi and Barale,…
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
                    <mark class="annotated-text">Milani</mark>, Ana Carolina C and Hoffmann, Elis V and Fossaluza, Victor and Jackowski, Andrea P and Mello, Marcelo F
Psychiatry and clinical neurosciences, 2017

# Title

Does pediatric post-traumatic stress diso…
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
                    <mark class="annotated-text">Luna</mark>, Licia P and Sherbaf, Farzaneh Ghazi and Sair, Haris I and Mukherjee, Debraj and Oliveira, Isabella Bezerra and Köhler, Cristiano André
Radiology, 2021

# Title

Can Preoperative Mapping with Functio…
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
                    <mark class="annotated-text">Müller</mark>, Felix and Brändle, Raphael and Liechti, Matthias E and Borgwardt, Stefan
Neuroscience and biobehavioral reviews, 2019

# Title

Neuroimaging of chronic MDMA (&#34;ecstasy&#34;) effects: A meta-analysis.

# …
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
                    Xiao, Jian and Wu, Jun
Current medical imaging, 2023

# Title

<mark class="annotated-text">Effectiveness of the Neuroimaging Techniques in the Recognition of Psychiatric Disorders: A Systematic Review and Meta-analysis of RCTs.
</mark>
# Keywords

Anxiety. 
Attention deficit hyperactive disorders (ADHD) 
Autism spectrum disorder (ASD) 
Functional magnetic resonance imaging (fMRI) 
Neuroimaging 
Obsessive-compulsive disorder (OCD) 
…
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
                    Kwee, Robert M and Kwee, Thomas C
European radiology, 2022

# Title

<mark class="annotated-text">Diagnostic performance of MRI in detecting locally recurrent soft tissue sarcoma: systematic review and meta-analysis.
</mark>
# Keywords

Magnetic resonance imaging 
Meta-analysis 
Recurrence 
Sarcoma 
Systematic review 


# Abstract

To systematically review the diagnostic criteria and performance of MRI in detecting local…
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
                    Ferreira, Sónia and Pêgo, José Miguel and Morgado, Pedro
Psychiatry research, 2019

# Title

<mark class="annotated-text">The efficacy of biofeedback approaches for obsessive-compulsive and related disorders: A systematic review and meta-analysis.
</mark>
# Keywords

Electroencephalography 
Functional magnetic resonance imaging 
Human 
Neurofeedback 
Obsessive-compulsive disorder 
Self-regulation 
Treatment outcome 


# Abstract

Biofeedback is applie…
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
                    Bliksted, Vibeke and Ubukata, Shiho and Koelkebeck, Katja
Schizophrenia research, 2016

# Title

<mark class="annotated-text">Discriminating autism spectrum disorders from schizophrenia by investigation of mental state attribution on an on-line mentalizing task: A review and meta-analysis.
</mark>
# Keywords

ASD 
Autism 
Differential diagnosis 
Schizophrenia 
Theory of mind 
fMRI 


# Abstract

In recent years, theories of how humans form a &#34;theory of mind&#34; of others (&#34;mentalizing&#34;) have incr…
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
                    Hall, MacGregor and Kidgell, Dawson and Perraton, Luke and Morrissey, Jack and Jaberzadeh, Shapour
Pain medicine (Malden, Mass.), 2021

# Title

<mark class="annotated-text">Pain Induced Changes in Brain Oxyhemoglobin: A Systematic Review and Meta-Analysis of Functional NIRS Studies.
</mark>
# Keywords

Brain 
Cortical 
HbO 
Hemodynamics 
Near-infrared Spectroscopy 
Noxious 
Oxyhemoglobin 
Pain 
fNIRS 


# Abstract

Neuroimaging studies show that nociceptive stimuli elicit responses in a…
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
                    Kim, Tae-Hyung and Woo, Sungmin and Han, Sangwon and Suh, Chong Hyun and Vargas, Hebert Alberto
AJR. American journal of roentgenology, 2020

# Title

<mark class="annotated-text">The Diagnostic Performance of MRI for Detection of Extramural Venous Invasion in Colorectal Cancer: A Systematic Review and Meta-Analysis of the Literature.
</mark>
# Keywords

MRI 
colorectal cancer 
extramural venous invasion 
meta-analysis 
systematic review 


# Abstract



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
    
    <details style="--label-color: #babdb6;">
        <summary class="label-display">DONE (but did not look into full paper) (29 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Lukow</mark>, P B and Kiemes, A and Kempton, M J and Turkheimer, F E and McGuire, P and Modinos, G
Neuroscience and biobehavioral reviews, 2021

# Title

Neural correlates of emotional processing in psychosis ris…
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
                    <mark class="annotated-text">Pievani</mark>, Michela and Pini, Lorenzo and Ferrari, Clarissa and Pizzini, Francesca B and Boscolo Galazzo, Ilaria and Cobelli, Chiara and Cotelli, Maria and Manenti, Rosa and Frisoni, Giovanni B
Journal of Alzhe…
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
                    <mark class="annotated-text">Jiang</mark>, Sisi and Li, Hechun and Liu, Linli and Yao, Dezhong and Luo, Cheng
Current neuropharmacology, 2022

# Title

Voxel-wise Functional Connectivity of the Default Mode Network in Epilepsies: A Systemati…
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
                    <mark class="annotated-text">Yeung</mark>, Andy Wai Kan
Brain imaging and behavior, 2021

# Title

Structural and functional changes in the brain of patients with Crohn&#39;s disease: an activation likelihood estimation meta-analysis.

# Keyword…
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
                    <mark class="annotated-text">Del</mark> Casale, A and Rapinesi, C and Kotzalidis, G D and Ferracuti, S and Padovano, A and Grassi, C and Sani, G and Girardi, P and Pompili, M
Archives italiennes de biologie, 2018

# Title

Neural functiona…
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
                    <mark class="annotated-text">Yuan</mark>, Yixuan and Jiang, Xi and Zhu, Dajiang and Chen, Hanbo and Li, Kaiming and Lv, Peili and Yu, Xiang and Li, Xiaojin and Zhang, Shu and Zhang, Tuo and Hu, Xintao and Han, Junwei and Guo, Lei and Liu, T…
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
                    <mark class="annotated-text">Feng</mark>, Chunliang and Thompson, Wesley K and Paulus, Martin P
Depression and anxiety, 2022

# Title

Effect sizes of associations between neuroimaging measures and affective symptoms: A meta-analysis.

# Ke…
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
                    <mark class="annotated-text">Zhou</mark>, Hui-Xia and Chen, Xiao and Shen, Yang-Qian and Li, Le and Chen, Ning-Xuan and Zhu, Zhi-Chen and Castellanos, Francisco Xavier and Yan, Chao-Gan
NeuroImage, 2020

# Title

Rumination and the default …
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
                    <mark class="annotated-text">Brandl</mark>, Felix and Le Houcq Corbi, Zarah and Mulej Bratec, Satja and Sorg, Christian
NeuroImage, 2020

# Title

Cognitive reward control recruits medial and lateral frontal cortices, which are also involved …
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
                    <mark class="annotated-text">Lukito</mark>, Steve and Norman, Luke and Carlisi, Christina and Radua, Joaquim and Hart, Heledd and Simonoff, Emily and Rubia, Katya
Psychological medicine, 2021

# Title

Comparative meta-analyses of brain struc…
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
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">NO N studies found (29 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Santos</mark>, Sara and Almeida, Inês and Oliveiros, Bárbara and Castelo-Branco, Miguel
PLoS One, 2016

# Title

The Role of the Amygdala in Facial Trustworthiness Processing: A Systematic Review and Meta-Analyses…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">273</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5127572/"
                                       >PMC5127572</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Xia</mark>, Wenqing and Chen, Yu-Chen and Ma, Jianhua
Front Aging Neurosci, 2017

# Title

Resting-State Brain Anomalies in Type 2 Diabetes: A Meta-Analysis

# Keywords

type 2 diabetes
resting-state fMRI
meta-…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">45</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5281680/"
                                       >PMC5281680</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Xiao</mark>, Bo and Wang, Shuai and Liu, Jianbo and Meng, Tiantian and He, Yuqiong and Luo, Xuerong
Neuropsychiatr Dis Treat, 2017

# Title

Abnormalities of localized connectivity in schizophrenia patients and …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">27</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5317331/"
                                       >PMC5317331</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Bottenhorn</mark>, Katherine L. and Flannery, Jessica S. and Boeving, Emily R. and Riedel, Michael C. and Eickhoff, Simon B. and Sutherland, Matthew T. and Laird, Angela R.
Netw Neurosci, 2018

# Title

Cooperating ye…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">754</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6326731/"
                                       >PMC6326731</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Berlingeri</mark>, Manuela and Magnani, Francesca Giulia and Salvato, Gerardo and Rosanova, Mario and Bottini, Gabriella
J Clin Med, 2019

# Title

Neuroimaging Studies on Disorders of Consciousness: A Meta-Analytic E…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">1522</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6517954/"
                                       >PMC6517954</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Emch</mark>, Mónica and von Bastian, Claudia C. and Koch, Kathrin
Front Hum Neurosci, 2019

# Title

Neural Correlates of Verbal Working Memory: An fMRI Meta-Analysis

# Keywords

verbal working memory
meta-anal…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">589</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6581736/"
                                       >PMC6581736</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Zinchenko</mark>, Oksana
Sci Rep, 2019

# Title

Brain responses to social punishment: a meta-analysis

# Keywords

Decision
Cooperation


# Abstract
 
Many studies suggest that social punishment is beneficial for co…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">132</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6728376/"
                                       >PMC6728376</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Cook</mark>, Michael J. and Gardner, Andrew J. and Wojtowicz, Magdalena and Williams, W. Huw and Iverson, Grant L. and Stanwell, Peter
Neuroimage Clin, 2019

# Title

Task-related functional magnetic resonance i…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">8219</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6939096/"
                                       >PMC6939096</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Arsalidou</mark>, Marie and Pawliw-Levac, Matthew and Sadeghi, Mahsa and Pascual-Leone, Juan
Dev Cogn Neurosci, 2017

# Title

Brain areas associated with numbers and calculations in children: Meta-analyses of fMRI s…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">151</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6969084/"
                                       >PMC6969084</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Lin</mark>, Xiao and Deng, Jiahui and Shi, Le and Wang, Qiandong and Li, Peng and Li, Hui and Liu, Jiajia and Que, Jianyu and Chang, Suhua and Bao, Yanping and Shi, Jie and Weinberger, Daniel R. and Wu, Ping an…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">4398</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7078287/"
                                       >PMC7078287</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">algorithm-MKDA (27 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Buhle</mark>, Jason T and Silvers, Jennifer A and Wager, Tor D and Lopez, Richard and Onyemekwu, Chukwudi and Kober, Hedy and Weber, Jochen and Ochsner, Kevin N
Cerebral cortex (New York, N.Y. : 1991), 2015

# Ti…
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
                    <mark class="annotated-text">Satpute</mark>, Ajay B and Kang, Jian and Bickart, Kevin C and Yardley, Helena and Wager, Tor D and Barrett, Lisa F
Frontiers in psychology, 2015

# Title

Involvement of Sensory Regions in Affective Experience: A …
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
                    <mark class="annotated-text">Brandl</mark>, Felix and Avram, Mihai and Weise, Benedikt and Shang, Jing and Simões, Beatriz and Bertram, Teresa and Hoffmann Ayala, Daniel and Penzel, Nora and Gürsel, Deniz A and Bäuml, Josef and Wohlschläger, …
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
                    Rigo, <mark class="annotated-text">Paola</mark> and Kim, Pilyoung and Esposito, Gianluca and Putnick, Diane L and Venuti, Paola and Bornstein, Marc H
Developmental review : DR, 2020

# Title

Specific maternal brain responses to their own child&#39;s …
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
                    Chrastil, <mark class="annotated-text">Elizabeth</mark> R and Tobyne, Sean M and Nauer, Rachel K and Chang, Allen E and Stern, Chantal E
Behavioral neuroscience, 2018

# Title

Converging meta-analytic and connectomic evidence for functional subregions wi…
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
                    Qin, Pengmin <mark class="annotated-text">and</mark> Liu, Yijun and Shi, Jinfu and Wang, Yuzhi and Duncan, Niall and Gong, Qiyong and Weng, Xuchu and Northoff, Georg
Human brain mapping, 2012

# Title

Dissociation between anterior and posterior cortic…
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
                    Fede, Samantha J and Kiehl, Kent A
Brain imaging and behavior, 2021

# Title

Meta-analysis of the moral brain: patterns of neural engagement assessed using <mark class="annotated-text">multilevel kernel density analysis</mark>.

# Keywords

MKDA 
Machine learning 
Meta-analysis 
Moral 
fMRI 


# Abstract

The neuroimaging literature in moral cognition has rapidly developed in the last decade with more than 200 publications…
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
                    …n, Benjamin and Roecher, Erik and Biswal, Bharat and Zweerings, Jana and Mathiak, Klaus
Addiction biology, 2022

# Title

Shared network-level functional alterations across substance use disorders: A <mark class="annotated-text">multi-level kernel density meta-analysis</mark> of resting-state functional connectivity studies.

# Keywords

functional magnetic resonance imaging 
inhibitory control 
meta-analysis 
multi-level kernel density analysis 
resting-state functional …
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
                    …identified a series of different brain regions as being involved in empathy, it remains unclear concerning the activation consistence of these brain regions and their specific functional roles. Using <mark class="annotated-text">MKDA</mark>, a whole-brain based quantitative meta-analysis of recent fMRI studies of empathy was performed. This analysis identified the dACC-aMCC-SMA and bilateral anterior insula as being consistently activat…
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
                    …ivated. In this study, we aimed to determine whether there is a distinct age-related activation pattern in these two subcomponents. A total of 278 fMRI articles were included in the current analysis. <mark class="annotated-text">Multilevel kernel density analysis</mark> was used to provide data on brain activation under each subcomponent of IC. Contrast analyses were conducted to capture the distinct activated brain regions for the two subcomponents, whereas meta-re…
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
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">algorithm-AES-SDM (27 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ion of underling pathophysiological mechanisms of the clinical triad including motor, cognitive and psychiatric impairment in Huntington&#39;s Disease (HD). We performed a voxel-based meta-analysis using <mark class="annotated-text">anisotropic effect size-signed differential mapping</mark> (AES-SDM) method. 6 studies (78 symptomatic HD, 102 premanifest HD and 131 healthy controls) were included in total. Altered resting-state brain activity was primarily detected in the bilateral media…
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
                    … to functional neural changes in prefrontal control areas and fear-related limbic regions. Thus, discovering such therapy-associated neural changes might point to relevant mechanisms of action. Using <mark class="annotated-text">AES-SDM</mark>, we conducted a coordinate-based meta-analysis of 22 whole-brain datasets (n = 419 anxiety patients) from 18 studies identified by our systematic literature search following PRISMA criteria (preregis…
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
                    …der (rMDD) and MDD present common or distinct neuropathological mechanisms remains unclear. We performed a meta-analysis of task-related whole-brain functional magnetic resonance imaging (fMRI) using <mark class="annotated-text">anisotropic effect-size signed differential mapping</mark> software to compare brain activation between rMDD/MDD patients and healthy controls (HCs). We included 18 rMDD studies (458 patients and 476 HCs) and 120 MDD studies (3746 patients and 3863 HCs). The…
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
                    …e been linked with several neuropsychiatric disorders. However, questions still remain about the exact neural substrates implicated in social reward and punishment processing. Here, we conducted four <mark class="annotated-text">Anisotropic Effect Size Signed Differential Mapping</mark> voxel-based meta-analyses of fMRI studies investigating the neural correlates of the anticipation and receipt of social rewards and punishments using the Social Incentive Delay task. We found that th…
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
                    … of regional alterations. A meta-analysis has been employed to examine the common pattern of abnormal regional spontaneous brain activity in poststroke aphasia in the current study. Specifically, the <mark class="annotated-text">Anisotropic effect-size version of seed-based d mapping </mark>was utilized, and 237 poststroke aphasia patients and 242 healthy controls (HCs) from 12 resting-state functional magnetic resonance imaging studies using amplitude of low-frequency fluctuations (ALFF…
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
                    …rasting GAD and HC that included structure (connectivity and local indices such as volume, etc.), FC, or task-based magnetic resonance imaging data. Meta-analyses were conducted, as applicable, using <mark class="annotated-text">AES-SDM</mark> software. The literature search produced 4,645 total records, of which 85 met the inclusion criteria for the systematic review. Records included structural (n = 35), FC (n = 33), and task-based (n = …
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
                    …s-fMRI with amplitude of low frequency fluctuation (ALFF) and/or fractional ALFF (fALFF) on MDD patients and further explored the effect of antidepressants on the intrinsic activity of the brain. The <mark class="annotated-text">anisotropic effect size version of signed differential mapping </mark>(AES-SDM) was applied to investigate changes in ALFF/fALFF in depression. We performed a subgroup analysis and group comparison on medicated and drug naïve patients to detect drug effect on MDD patien…
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
                    …ole-brain functional magnetic resonance imaging (fMRI) or voxel-based morphometry (VBM). A CBMA of 30 fMRI (754 FRs; 959 controls) and 11 VBM (885 FRs; 775 controls) datasets were conducted using the <mark class="annotated-text">anisotropic effect-size version of signed differential mapping</mark>. Further, we conducted separate meta-analyses about functional alterations in different cognitive tasks: social cognition, executive functioning, working memory, and inhibitory control. FRs showed hi…
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
                    … and affective significance; and in a subgroup of youths with additional psychopathic traits. The authors performed a meta-analysis of voxel-based group differences in functional activation using the <mark class="annotated-text">anisotropic effect-size version of seed-based d mapping.</mark> Across 24 studies, 338 youths with disruptive behavior disorder or conduct problems relative to 298 typically developing youths had consistent underactivation in the rostral and dorsal anterior cingu…
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
                    …ency fluctuations (ALFF), fractional ALFF (fALFF), or regional homogeneity (ReHo) methods. Then, we performed a voxel-wise meta-analysis to identify consistent abnormal neural activity in migraine by <mark class="annotated-text">anisotropic effect size seed-based d mapping </mark>(AES-SDM). To confirm the AES-SDM meta-analysis results, we conducted two meta-analyses: activation likelihood estimation (ALE) and multi-level kernel density analysis (MKDA). We found that migraine s…
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
    
    <details style="--label-color: #eeeeec;">
        <summary class="label-display">read later (26 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Lange, N
Human brain mapping, 2010

# Title

<mark class="annotated-text">Empirical and substantive models, the Bayesian paradigm, and meta-analysis in functional brain imaging.
</mark>
# Keywords



# Abstract

Functional neuroimaging research is currently rediscovering and adapting established statistical methods for its use, including design of experiments, the general linear mod…
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
                    Jennings, Robin G and Van Horn, John D
Neuroinformatics, 2012

# Title

<mark class="annotated-text">Publication bias in neuroimaging research: implications for meta-analyses.
</mark>
# Keywords



# Abstract

Neuroimaging and the neurosciences have made notable advances in sharing activation results through detailed databases, making meta-analysis of the published research faster…
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
                    Phan, K Luan and Wager, Tor and Taylor, Stephan F and Liberzon, Israel
NeuroImage, <mark class="annotated-text">2002</mark>

# Title

Functional neuroanatomy of emotion: a meta-analysis of emotion activation studies in PET and fMRI.

# Keywords



# Abstract

Neuroimagingstudies with positron emission tomography (PET) and…
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
                    Shin, Minho and Jeon, Hyeon-Ae
Cerebral cortex (New York, N.Y. : 1991), 2022

# Title

<mark class="annotated-text">A Cortical Surface-Based Meta-Analysis of Human Reasoning.
</mark>
# Keywords

Bayesian meta-analysis of the cortical surface (BMACS) 
functional magnetic resonance imaging 
inductive and deductive reasoning 
integrated nested Laplace approximation (INLA) 
log-Gauss…
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
                    Robinson, Jennifer L and Salibi, Nouha and Deshpande, Gopikrishna
NeuroImage, 2018

# Title

<mark class="annotated-text">Functional connectivity of the left and right hippocampi: Evidence for functional lateralization along the long-axis using meta-analytic approaches and ultra-high field functional neuroimaging.
</mark>
# Keywords

7T 
BrainMap 
DTI 
Long-axis 
MACM 
fMRI 


# Abstract

Theories regarding the functional specialization of the hippocampus date back to over a century ago. Two main theories have dominat…
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
                    Niu, Zhendong and Nie, Yaoxin and Zhou, Qian and Zhu, Linlin and Wei, Jieyao
BMC neuroscience, 2017

# Title

<mark class="annotated-text">A brain-region-based meta-analysis method utilizing the Apriori algorithm.
</mark>
# Keywords

Apriori algorithm 
Brain network connectivity 
Co-activation relationship 
Meta-analysis 
Word reading 
fMRI 


# Abstract

Brain network connectivity modeling is a crucial method for stu…
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
                    Tench, C R and Tanasescu, Radu and Constantinescu, C S and Cottam, W J and Auer, D P
NeuroImage, 2020

# Title

<mark class="annotated-text">Coordinate based meta-analysis of networks in neuroimaging studies.
</mark>
# Keywords

Functional MRI 
Graphs 
Meta-analysis 
Networks 
Neuroimaging 
Voxel-based morphometry 


# Abstract

Meta-analysis of summary results from published neuroimaging studies independently te…
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
                    Fox, Peter T and Lancaster, Jack L and Laird, Angela R and Eickhoff, Simon B
Annual review of neuroscience, 2015

# Title

<mark class="annotated-text">Meta-analysis in human neuroimaging: computational modeling of large-scale databases.
</mark>
# Keywords

ALE 
MRI 
activation likelihood estimation 
fMRI 
human brain mapping 
magnetic resonance imaging 


# Abstract

Spatial normalization--applying standardized coordinates as anatomical add…
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
                    Montagna, Silvia and Wager, Tor and Barrett, Lisa Feldman and Johnson, Timothy D and Nichols, Thomas E
Biometrics, 2019

# Title

<mark class="annotated-text">Spatial Bayesian latent factor regression modeling of coordinate-based meta-analysis data.
</mark>
# Keywords

Bayesian modeling 
Factor analysis 
Functional principal component analysis 
Meta-analysis 
Reverse inference 
Spatial point pattern data 


# Abstract

Now over 20 years old, functional …
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
                    Tench, C R and Tanasescu, R and Constantinescu, C S and Auer, D P and Cottam, W J
Journal of neuroscience methods, 2022

# Title

<mark class="annotated-text">Easy to interpret coordinate based meta-analysis of neuroimaging studies: Analysis of brain coordinates (ABC).
</mark>
# Keywords

Functional MRI 
Meta-analysis 
Neuroimaging 
Voxel-based morphometry 


# Abstract

Functional MRI and voxel-based morphometry are important in neuroscience. They are technically challeng…
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
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA5 (23 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …of schizophrenia and autism spectrum disorders.        


### Theory of mind 
  
Our search identified 10 studies exploring ToM related processes in ASD subjects and 17 in SZ patients, of which 7 and <mark class="annotated-text">9</mark> respectively fulfilled inclusion criteria ( ). The total analysis encompassed 91 ASD and 133 SZ patients, and 239 HC subjects. Demographic details for all participants and clinical information corres…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … 3a–d for the pre-post contrast on verum or sham acupuncture compared to baseline ( ,  ). The analysis of greater activation of verum acupuncture than baseline (3a, verum&gt;rest) included 234 subjects, <mark class="annotated-text">20</mark> experiments and 305 foci and revealed significant convergence in middle cingulate gyrus, pre-SMA, superior temporal gyrus, supramarginal gyrus, SII, thalamus and insula. The analysis of greater deact…
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
                    …o performed four separate ALE analyses on four categories of studies in relation to the type of familiarity paradigm (recently learned vs. familiar environment) and spatial strategies (egocentric vs. <mark class="annotated-text">allocentric</mark> strategies) used in the experiment. 

Regarding the categorization of studies according to degree of familiarity, we separated experiments according to whether the environment used in the study was u…
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
                    …he individual ALE analysis of the paradigm (RL vs. F environment) but not in the analysis of the neural substrate of navigational strategies. A total of 30 experiments were defined as allocentric and <mark class="annotated-text">34</mark> as egocentric (see Tables   and   for more details). 

After carrying out separate ALE analyses on the categories of studies [  paradigm   (recently learned vs. familiar environment) and   spatial st…
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
                    …, ALE analysis found seven statistically significant activation clusters, including left GPe, right caudate head, left red nucleus, right insula, left anterior cingulate gyrus (ACC), IFG and amydala. <mark class="annotated-text">Reward anticipation</mark> (14 studies and 63 foci) was related to the significant activation of putamen, superior frontal gyrus (SFG) and IFG. As to the emotional processing (7 studies and 83 foci), increased likelihood of ac…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …seven statistically significant activation clusters, including left GPe, right caudate head, left red nucleus, right insula, left anterior cingulate gyrus (ACC), IFG and amydala. Reward anticipation (<mark class="annotated-text">14</mark> studies and 63 foci) was related to the significant activation of putamen, superior frontal gyrus (SFG) and IFG. As to the emotional processing (7 studies and 83 foci), increased likelihood of activa…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …,177 participants with a mean sample age more than 6 years and &lt;18 years (Table  ). The whole sample dataset incorporated 573 activation foci, and the child group incorporated 549 participants across <mark class="annotated-text">29</mark> experiments, containing 317 activation foci. The cut-off for the child group was based on previous research indicating that executive processes tend to be relatively mature by the age of 12, yet not …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5383671/"
                                       >PMC5383671</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s by false discovery rate (FDR; Laird et al.,  ) and a cluster threshold of 100 mm  (Hill et al.,  ) was employed in the first-level analyses. 


#### First-level analyses 
  
First-level analyses on <mark class="annotated-text">common executive</mark> (shared activation across tasks tapping inhibition, switching, and updating executive processes; Figure  ) and each specific putative executive process (inhibition, updating, and switching) were cond…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5383671/"
                                       >PMC5383671</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …. 

#### Is functional reorganisation in CP limited to neuropathic pain? 
  
CP studies were sub-grouped by etiology (neuropathic (NEUR ;  ), nociceptive musculo-skeletal (MSK ;  ), and fibromyalgia (<mark class="annotated-text">FM</mark> ;  ). There are distinct neurophysiological differences between neuropathic and musculo-skeletal pain disorders with controversies regarding the classification of FM  ( ,  ,  ). Thus, there may be di…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5554296/"
                                       >PMC5554296</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ipheral neuropathy n = 3; headache, n = 3; vulvar vestibulitis syndrome, n = 1); primary nociceptive musculo-skeletal disorders (low back pain, n = 6; osteoarthritis, n = 2) and fibromyalgia (FM, n = <mark class="annotated-text">8</mark>). We additionally subdivided CP studies according to the site of the nociceptive stimulation: at the most painful clinically affected site (CS ;  ), or at another body site (OS ;  ). 

### Experiment…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5554296/"
                                       >PMC5554296</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">algorithm-SDM-PSI (18 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … However, how music listening engages brain functional networks remains elusive due to inconsistent results from previous findings. A meta-analysis of functional magnetic resonance imaging data using <mark class="annotated-text">seed-based d mapping (SDM) with permutation of subject images</mark> was performed. Studies that presented music listening paradigms to healthy individuals were included. Subgroup analyses were performed to investigate the effects of music genres on brain activation. …
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
                    …, analyses on regions-of-interest). We aimed to conduct a meta-analysis of whole-brain fMRI studies on antisocial individuals based on distinct neurocognitive domains. A voxel-based meta-analysis via <mark class="annotated-text">permutation of subject images (SDM-PSI) </mark>was performed on studies using fMRI tasks in the domains of acute threat response, cognitive control, social cognition, punishment and reward processing. Overall, 83 studies were retrieved. Using a li…
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
                    … until June 15, 2019 and updated on March 20, 2020. This protocol will follow the Preferred Reporting Items for Systematic review and Meta-Analysis Protocols (PRISMA-P). The Seed-based d Mapping with <mark class="annotated-text">Permutation of Subject Images (SDM-PSI)</mark> software will be used for this voxel-wise meta-analysis. This meta-analysis will identify the most consistent ReHo alterations in CP. To our knowledge, this will be the first voxel-wise meta-analysis…
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
                    …ch strategy was applied to select pertinent studies up to December 2022 in PubMed, Web of Science, and Embase databases. Voxel-wise meta-analysis was conducted via the latest meta-analytic algorithm, <mark class="annotated-text">seed-based d mapping with permutation of subject images</mark> software. Meta-regression analyses were also conducted to explore the potential effect of clinical variables on resting-state neural activity. Eleven studies comprising 304 patients with ESRD and 296…
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
                    … We included randomized controlled trials where resting-state fMRI was used to observe the effect of NIBS in patients with MCI or AD. RevMan software was used to analyze the continuous variables, and <mark class="annotated-text">SDM-PSI</mark> software was used to perform an fMRI data analysis. A total of 17 studies comprising 258 patients in the treatment group and 256 in the control group were included. After NIBS, MCI patients in the tr…
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
                    …hreshold-free cluster enhancement family-wise multiple comparison correction (p &lt; .05), likely owing to the small number of studies identified. Using uncorrected statistical thresholds recommended by <mark class="annotated-text">Signed Differential Mapping with Permutation of Subject Images</mark>, the meta-analysis of reality-monitoring studies (k = 9 studies including 172 healthy subjects) revealed clusters in the lobule VI of the cerebellum, the right anterior medial prefrontal cortex and a…
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
                    …I to observe the effect of acupuncture on stroke patients with motor dysfunction. R software was used to analyze the continuous variables, and Seed-based d Mapping with Permutation of Subject Images (<mark class="annotated-text">SDM-PSI</mark>) was used to perform an analysis of fMRI data.   Findings  . A total of 7 studies comprising 143 patients in the treatment group and 138 in the control group were included in the meta-analysis. The r…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8192216/"
                                       >PMC8192216</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …taneous neural activity abnormalities in patients with T2DM. 

 Methods:   A systematic search was conducted to identify voxel-based rs-fMRI studies comparing T2DM patients with healthy controls. The <mark class="annotated-text">permutation of subject images seed-based   d   mapping (SDM)</mark> was used to quantitatively estimate the regional spontaneous neural activity abnormalities in patients with T2DM. Metaregression was conducted to examine the associations between clinical characteris…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8245688/"
                                       >PMC8245688</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …was incomplete were excluded. 


## Data sources 
  
Ovid, Medline and PsycInfo, from 2000 to 2020, plus checking of review articles and meta-analyses. 


## Data synthesis 
  
Data were pooled using <mark class="annotated-text">Seed-based d Mapping with Permutation of Subject Images</mark> (SDM-PSI). Heterogeneity among studies was examined using the   I   statistic. Publication bias was examined using funnel plots and statistical examination of asymmetries. Moderator variables includi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8341642/"
                                       >PMC8341642</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …es (Table  ). Finally, as MKDA meta-analysis cannot deal with studies reporting no significant results (Table   lists these studies), we used “Seed-based d-Mapping with Permutation of Subject Images (<mark class="annotated-text">SDM-PSI</mark>)” to test whether excluding these studies biased results ( ) [ ]. 



## Results 
  
### Included studies 
  
Concerning GMV, 63 MDD-studies (2934 patients/3284 controls), 41 ANX-studies (1021/1130),…
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
        <summary class="label-display">MA6 (16 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …rison of schizophrenia and autism spectrum disorders.        


### Theory of mind 
  
Our search identified 10 studies exploring ToM related processes in ASD subjects and 17 in SZ patients, of which <mark class="annotated-text">7 and 9</mark> respectively fulfilled inclusion criteria ( ). The total analysis encompassed 91 ASD and 133 SZ patients, and 239 HC subjects. Demographic details for all participants and clinical information corres…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e gyrus, pre-SMA, superior temporal gyrus, supramarginal gyrus, SII, thalamus and insula. The analysis of greater deactivation of verum acupuncture compared to baseline (3b, rest&gt;verum, 172 subjects, <mark class="annotated-text">15</mark> experiments and 222 foci) came to the following significant convergence: subgenual anterior cingulate, amygdala/hippocampal formation, vmPFC and PCC. Comparing results on greater activation of sham a…
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
                    …ilarly distribution and activation pattern (details see Table   and Fig.  ). 



### Between-group ALE analysis in a transdiagnostic approach across MDD and SZ 
  
#### Consummatory anhedonia 
  
For <mark class="annotated-text">consummatory anhedonia</mark> (29 studies and 151 foci), ALE analysis revealed five statistically significant clusters with decreased likelihood of activation in patients compared to controls (Fig.   and Table  ), including bilat…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …activation pattern (details see Table   and Fig.  ). 



### Between-group ALE analysis in a transdiagnostic approach across MDD and SZ 
  
#### Consummatory anhedonia 
  
For consummatory anhedonia (<mark class="annotated-text">29</mark> studies and 151 foci), ALE analysis revealed five statistically significant clusters with decreased likelihood of activation in patients compared to controls (Fig.   and Table  ), including bilateral…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s 
  
First-level analyses on common executive (shared activation across tasks tapping inhibition, switching, and updating executive processes; Figure  ) and each specific putative executive process (<mark class="annotated-text">inhibition</mark>, updating, and switching) were conducted. First-level analyses describe clusters that pass the applied threshold for significant conjunctive activation across these groups of studies. These analyses …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5383671/"
                                       >PMC5383671</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …n specific to experimental hyperalgesia in healthy controls as a model of pain sensitisation. To this end we studied the pattern of pain processing in HC after experimental induction of hyperalgesia (<mark class="annotated-text">HYPER</mark>  subgroup;  ) in comparison with normalgesia by CBMA of the hyperalgesia group, and by CMA and MAC between hyperalgesia and normalgesia. The frequency of reporting brain structures activated in each …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5554296/"
                                       >PMC5554296</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …  P   &lt;     0.05; 41 ‘OT &gt; PL’ contrasts, 250 activation coordinates;  ) and decreased neural activity in right amygdala (FWE   P   &lt;     0.05; 36 ‘OT &lt; PL’ contrasts, 228 activation coordinates;  ). <mark class="annotated-text">Twenty-one</mark> contrasts examined the effects of IN-OT in clinical population. ALE analysis from FWE correction revealed that IN-OT increased neural activity in the dorsal anterior cingulate cortex (dACC) (FWE   P …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5647800/"
                                       >PMC5647800</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …en different task domains, contrast analyses ( ) were conducted between each pair of the Think/No-Think, Stop-signal and Go/No-Go Tasks (i.e., Think/No-Think &amp; Stop-signal; Think/No-Think &amp; Go/No-Go; <mark class="annotated-text">Stop-signal &amp; Go/No-Go</mark>). For analysing each pair of the tasks, the thresholded activation maps from the individual analyses, as well as the pooled results from both tasks were used as inputs. The outputs were conjunction a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5759998/"
                                       >PMC5759998</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ity in the bilateral IPL and SPL, right PI, IFG, claustrum, MFG, PreCG and MOG, and left AI, PreCG, ITG, aMCC/ACC and putamen (see   and   for peak coordinates and ALE values). The ALE single map for <mark class="annotated-text">3PP</mark> yielded consistent activations in the bilateral PosCG and left AI, ACC, MOG and IPL (see   and   for peak coordinates and ALE values). Conjunction analysis for both perspectives revealed bilateral ac…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6847411/"
                                       >PMC6847411</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ncluded in the analysis, yielding a total of 258 subjects, and 23 foci of brain activations. No significant clusters emerged from this analysis. 

In the contrast focus on emotions   vs   acceptance, <mark class="annotated-text">6</mark> experiments reported significant results, yielding a total of 258 subjects, and 94 foci of brain activations. One significant clusters of decreased brain activity in acceptance relative to focus on e…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7943364/"
                                       >PMC7943364</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">largescale-neurosynth decoding (15 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    de la Vega, Alejandro and Chang, Luke J and Banich, Marie T and Wager, Tor D and Yarkoni, Tal
The Journal of neuroscience : the official journal of the Society for Neuroscience, 2017

# Title

<mark class="annotated-text">Large-Scale Meta-Analysis of Human Medial Frontal Cortex Reveals Tripartite Functional Organization.
</mark>
# Keywords

cognitive control 
medial frontal cortex 
meta-analysis 
pain 


# Abstract

The functional organization of human medial frontal cortex (MFC) is a subject of intense study. Using fMRI, th…
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
                    …ponent regions each exhibit distinct, but partially overlapping functional profiles. To date, there has been minimal effort to disentangle the functions of these regions. In the present study, we use <mark class="annotated-text">Neurosynth ( http://neurosynth.org ) to conduct an unbiased meta-analysis of the PMC based on fMRI coactivation and semantic information extracted from 11,406 studies. </mark>Our analyses revealed six PMC clusters with distinct functional profiles: superior and inferior dorsal PCC, anterior and posterior PrC, ventral PCC, and RSC. We discuss these findings in the context o…
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
                    …corporating observations from 3401 adult patients and 3238 healthy participants was performed by seed-based d mapping. Brain maps were subjected to meta-analytic connectivity modeling and data-driven <mark class="annotated-text">functional decoding </mark>analyses to identify associated neural circuit alterations and relations to behavioral dimensions. Both groups exhibited hypoactivated abnormalities in the left inferior parietal lobule, and altered c…
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
                    …tion during episodic encoding and retrieval, semantic retrieval, working memory, spatial navigation, simulation/scene construction, transitive inference, and social cognition tasks. The second was to <mark class="annotated-text">use a large meta-analytic database (neurosynth) to find text terms and coactivation maps associated with the anterior and posterior hippocampal regions identified in the literature search</mark>. The third approach was to contrast the resting-state functional connectivity of the anterior and posterior hippocampal regions using a publicly available database that includes a large sample of adu…
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
                    …termine which mental state activation patterns are most strongly associated with a given gene expression map. This chapter provides a step-by-step guide on how to use the AHBA in conjunction with the <mark class="annotated-text">NeuroSynth fMRI meta-analysis tool to identify the mental state correlates of specific gene expression patterns, using genes from oxytocin signaling pathway as an example.</mark> We also demonstrate how to perform an out-of-sample validation and assess the specificity of results for genes of interest. 

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
                    …al posterior cingulate cortex and superior frontal gyrus (key components of the default mode network) and in the bilateral paracentral lobule (a part of the sensorimotor network). We also performed a <mark class="annotated-text">functional association analysis of the identified areas</mark>, whose dysfunction is clinically consistent with the well-known deficits affecting individuals with ASD. Importantly, we did not find relevant clusters of local hyper-connectivity, which is contrary …
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
                    …fine dACC, fewer than 15% of studies reported peak coordinates in dACC. Meta-analytic connectivity mapping suggests patterns of co-activation are consistent with the topography of the default network.<mark class="annotated-text"> Reverse inference for cognition associated with reliable Cyberball activity computed in Neurosynth revealed social exclusion to be associated with cognitive terms Social, Autobiographical, Mental States, and Theory of Mind. </mark>Taken together, these findings highlight the role of the default network in social exclusion and warns against interpretations of the dACC as a key region involved in the experience of social exclusio…
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
                    …ons across a constellation of regions comprising the bilateral inferior frontal junction, intraparietal sulcus, dorsal anterior cingulate, angular gyrus, temporo-occipital cortex and anterior insula. <mark class="annotated-text">Neurosynth reverse inference revealed conscious visual processing to be intertwined with cognitive terms related to attention, cognitive control and working memory.</mark> Results of the meta-analysis on unconscious percepts revealed consistent activations in the lateral occipital complex, intraparietal sulcus and precuneus. These findings highlight the notion that con…
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
                    …h represented plausible network constructs. These included PCNs such as “self” and “empathy” as well as BCNs such as “occipito-temporal” and “temporal-parietal”. For each term pairing, we performed a <mark class="annotated-text">reverse inference meta-analysis</mark> (FDR corrected at p &lt; 0.01) identifying fMRI spatial activation profiles stored in Neurosynth. Each pair-wise comparison between search queries   i   and   j   was conditional, ensuring that no artic…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5347156/"
                                       >PMC5347156</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e not included in standard neuroimaging paradigm ontologies such as BrainMap (Fox et al.,  ) or CogPO (Turner &amp; Laird,  ). 
  
Manual functional decoding results across meta-analytic groupings 
    

<mark class="annotated-text">#### Automated Neurosynth annotations. 
</mark>  
To complement the manual annotation analysis, we used Neurosynth’s automated annotations, which describes experiments that engage each MAG based on published neuroimaging data, allowing comparison …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6326731/"
                                       >PMC6326731</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">algorithm-ES-SDM (13 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …n and Li, Tao
Addiction biology, 2016

# Title

The prefrontal dysfunction in individuals with Internet gaming disorder: a meta-analysis of functional magnetic resonance imaging studies.

# Keywords

<mark class="annotated-text">Effect size signed differential mapping (ES-SDM) 
</mark>Internet gaming disorder (IGD) 
functional magnetic resonance imaging (fMRI) 
impulsivity 
reward system 
the prefrontal lobe 


# Abstract

With the advancement in high-resolution magnetic resonance …
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
                    …o and Lam, Chaw and Lin, Xia
Behavioural brain research, 2015

# Title

Reward pathway dysfunction in gambling disorder: A meta-analysis of functional magnetic resonance imaging studies.

# Keywords

<mark class="annotated-text">Effect size signed differential mapping (ES-SDM) 
</mark>Functional magnetic resonance imaging (FMRI) 
Gambling disorder (GD) 
The frontostriatal cortical pathway 


# Abstract

Recent emerging functional magnetic resonance imaging (fMRI) studies have ident…
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
                    …, Lena
Neuroscience and biobehavioral reviews, 2015

# Title

Localized connectivity in depression: a meta-analysis of resting state functional imaging studies.

# Keywords

Connectivity 
Depression 
<mark class="annotated-text">Effect size – signed differential mapping </mark>
Regional homogeneity 
Resting-state fMRI 


# Abstract

Resting-state fMRI studies investigating the pathophysiology of depression have identified prominent abnormalities in large-scale brain network…
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
                    …s accept an offer. We present the first quantitative summary of neuroimaging studies in social decision-making with a meta-analysis of 11 fMRI studies of the UG, including data from 282 participants. <mark class="annotated-text">Effect-Size Signed Differential Mapping</mark> was used to estimate effect sizes from statistical parametric maps and reported peak information before meta-analysing them. Consistent activations were seen in the anterior insula, anterior cingulat…
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
                    … meta-analysis included 48 functional magnetic resonance imaging studies that reported pragmatic versus literal language contrasts. The pragmatic forms were speech acts, metaphors, idioms, and irony. <mark class="annotated-text">Effect Size-Signed Differential Mapping</mark> software was used to calculate the mean for all contrasts as well as for each pragmatic form, and make comparisons among all forms. Due to variations in pragmatic content configuration such as natura…
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
                    …ordinate-based, quantitative meta-analysis. We compiled functional magnetic resonance imaging studies that examined neural correlates of priming tasks using perceptual, conceptual and lexical primes. <mark class="annotated-text">Effect-size signed differential mapping</mark> was used to perform a neuroimaging meta-analysis on the negative priming effect. Results from fourteen studies (245 participants; 85 foci) show concordance across studies in the right middle frontal …
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
                    …using emotional tasks), published between 2003 and 2013. These studies included 467 healthy relatives of patients with schizophrenia and 768 controls. To conduct the statistical analysis, we used the <mark class="annotated-text">effect-size signed differential mapping</mark> software, a voxel-based meta-analytic approach. In healthy relatives of patients with schizophrenia, we observed a general pattern of overactivation across the 21 fMRI studies in right-sided frontal,…
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
                    …red with a control group. A voxel-wise meta-analysis with the effect-size version of Signed Differential Mapping (ES-SDM) identified regional abnormalities of functional brain response. Similarly, an <mark class="annotated-text">ES-SDM</mark> meta-analysis was conducted on VBM studies. A multi-modal imaging meta-analysis was used to highlight brain regions with both structural and functional abnormalities. Nineteen studies met the inclusi…
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
                    …psies Methods: A systematic review was conducted on 22 published articles before October 2020, indexed in PubMed and Web of Science. A meta-analysis with a random-effect model was performed using the <mark class="annotated-text">effect-size signed differential mapping</mark> approach. Subgroup analyses were performed in three groups: Idiopathic Generalized Epilepsy (IGE), mixed Temporal Lobe Epilepsy (TLE), and mixed Focal Epilepsy (FE) with different foci. The meta-anal…
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
                    … to the AM network have not been explored recently and have never been analyzed with consideration to the different processes of AM, them being retrieval and re-experiencing. We conducted a series of <mark class="annotated-text">effect-size signed differential mapping </mark>meta-analyses across twenty-eight studies investigating the neural correlates of trauma-related AMs in participants with PTSD as compared with controls. Studies included either trauma-related scripts …
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
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">algorithm-other ma method (13 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Bartra</mark>, Oscar and McGuire, Joseph T and Kable, Joseph W
NeuroImage, 2014

# Title

The valuation system: a coordinate-based meta-analysis of BOLD fMRI experiments examining neural correlates of subjective v…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">custom method, similar to MKDA</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Tench</mark>, C R and Tanasescu, Radu and Constantinescu, C S and Cottam, W J and Auer, D P
NeuroImage, 2020

# Title

Coordinate based meta-analysis of networks in neuroimaging studies.

# Keywords

Functional M…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">CBMAN</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Etkin</mark>, Amit and Wager, Tor D
The American journal of psychiatry, 2007

# Title

Functional neuroimaging of anxiety: a meta-analysis of emotional processing in PTSD, social anxiety disorder, and specific ph…
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
                    Zunhammer, Matthias and Bingel, Ulrike and Wager, Tor D
JAMA neurology, 2019

# Title

Placebo Effects on the Neurologic Pain Signature: A <mark class="annotated-text">Meta-analysis of Individual Participant Functional Magnetic Resonance Imaging Data.</mark>

# Keywords



# Abstract

Placebo effects reduce pain and contribute to clinical analgesia, but after decades of research, it remains unclear whether placebo treatments mainly affect nociceptive pro…
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
                    …rtin M
Neuroscience and biobehavioral reviews, 2023

# Title

Imaging the spin: Disentangling the core processes underlying mental rotation by network mapping of data from meta-analysis.

# Keywords

<mark class="annotated-text">Coordinate based network mapping </mark>
Functional magnetic resonance imaging 
Mental rotation 


# Abstract

Research on the mental rotation task has sparked debate regarding the specific processes that underly the capability of humans to…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">coordinate-based network mapping</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …is, we conducted a meta-analysis investigating cue-reactivity functional MRI studies for different addictions. We explored 8 different addiction-related brain regions in 27 studies (29 samples) using <mark class="annotated-text">homogeneity tests of effect sizes</mark>. An initial qualitative review failed to identify consistent activations in any brain region. We subsequently explored possible moderators related to either the addiction, participants, or study desi…
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
                    …ses were performed to examine consistent hypo-activated and/or hyper-activated regions for all tasks combined, and for social and non-social tasks separately; meta-analytic connectivity modelling and <mark class="annotated-text">behavioral/paradigm analyses</mark> were performed to examine co-activated regions and associated behaviors. One hundred studies (mean age range = 18-41 years) were included. For all tasks combined, the ASD group showed significant (p …
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
                    …rdly integrated in order to construct a model of the underlying neural correlates of neuroticism. The aim of the current meta-analysis was to provide a quantitative summary of the literature, using a <mark class="annotated-text">parametric coordinate-based meta-analysis</mark> (PCM) approach. Data were pooled for emotion processing tasks investigating the contrasts (negative&gt;neutral) and (positive&gt;neutral) to identify brain regions that are consistently associated with neu…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">parametric coordinate-based meta-analysis</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rly 2011. Data from 34 case-control comparisons (n=1165) and 6 treatment studies (n=105) were analysed separately with two meta-analytic methods for imaging data: Activation Likelihood Estimation and <mark class="annotated-text">Gaussian-Process Regression.</mark> There was broad support for limbic-cortical and cortico-striatal models in the case-control data. Evidence for the role of the default mode network was weaker. Treatment-sensitive regions were primar…
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
                    …ts&#39; BOLD signal in several 
brain regions; however, within the
clusters identified as significantly deviant 
from one, R-squared values were
lower and ranged between 0.1–0.46. 


## 4. DISCUSSION 
  
<mark class="annotated-text">Here we report the preliminary use of a 
novel meta-analysis technique </mark>in studies on
aging, which localizes one factor of general 
cognitive slowing to the
sensorimotor transfer. These findings lend support to 
existing data from
event-related potential work indicating t…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">new technique</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2233772/"
                                       >PMC2233772</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">software-none-or-unclear (12 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Klugah</mark>-Brown, Benjamin and Zhou, Xinqi and Pradhan, Basant K and Zweerings, Jana and Mathiak, Klaus and Biswal, Bharat and Becker, Benjamin
Addiction biology, 2021

# Title

Common neurofunctional dysregula…
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
                    <mark class="annotated-text">Fusar</mark>-Poli, Paolo and Placentino, Anna and Carletti, Francesco and Landi, Paola and Allen, Paul and Surguladze, Simon and Benedetti, Francesco and Abbamonte, Marta and Gasparotti, Roberto and Barale, Franc…
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
                    <mark class="annotated-text">Silva</mark>, P H R and Spedo, C T and Barreira, A A and Leoni, R F
Multiple sclerosis and related disorders, 2018

# Title

Symbol Digit Modalities Test adaptation for Magnetic Resonance Imaging environment: A s…
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
                    Fan, <mark class="annotated-text">Yan</mark> and Duncan, Niall W and de Greck, Moritz and Northoff, Georg
Neuroscience and biobehavioral reviews, 2011

# Title

Is there a core neural network in empathy? An fMRI based quantitative meta-analysis…
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
                    Yuan, <mark class="annotated-text">Rui</mark> and Biswal, Bharat B and Zaborszky, Laszlo
Cerebral cortex (New York, N.Y. : 1991), 2020

# Title

Functional Subdivisions of Magnocellular Cell Groups in Human Basal Forebrain: Test-Retest Resting-S…
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
                    Wager, <mark class="annotated-text">Tor</mark> D and Jonides, John and Reading, Susan
NeuroImage, 2004

# Title

Neuroimaging studies of shifting attention: a meta-analysis.

# Keywords



# Abstract

This paper reports a meta-analysis of neuroim…
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
                    Servaas, <mark class="annotated-text">Michelle</mark> N and van der Velde, Jorien and Costafreda, Sergi G and Horton, Paul and Ormel, Johan and Riese, Harriëtte and Aleman, André
Neuroscience and biobehavioral reviews, 2014

# Title

Neuroticism and the…
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
                    Satpute, <mark class="annotated-text">Ajay</mark> B and Kang, Jian and Bickart, Kevin C and Yardley, Helena and Wager, Tor D and Barrett, Lisa F
Frontiers in psychology, 2015

# Title

Involvement of Sensory Regions in Affective Experience: A Meta-A…
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
                    Wu, Xin and <mark class="annotated-text">Yang</mark>, Wenjing and Tong, Dandan and Sun, Jiangzhou and Chen, Qunlin and Wei, Dongtao and Zhang, Qinglin and Zhang, Meng and Qiu, Jiang
Human brain mapping, 2016

# Title

A meta-analysis of neuroimaging st…
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
                    Poeppl, Timm B <mark class="annotated-text">and</mark> Langguth, Berthold and Rupprecht, Rainer and Safron, Adam and Bzdok, Danilo and Laird, Angela R and Eickhoff, Simon B
Frontiers in neuroendocrinology, 2017

# Title

The neural basis of sex differenc…
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
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA7 (9 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …gence: subgenual anterior cingulate, amygdala/hippocampal formation, vmPFC and PCC. Comparing results on greater activation of sham acupuncture points than baseline (3c, sham&gt;rest) from 164 subjects, <mark class="annotated-text">15</mark> experiments and 200 foci, showed significant convergence in cerebellum, supramarginal gyrus, superior temporal gyrus and thalamus. Including data on greater deactivation of sham acupuncture points co…
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
                    … respectively 
    
ALE results in a transdiagnostic approach across MDD and SZ 
  
 p &lt;   0.01, FDR corrected, cluster size &gt;400 mm ;   BA   = Brodmann area 
  


#### Anticipatory anhedonia 
  
For <mark class="annotated-text">anticipatory anhedonia </mark>(30 studies and 119 foci), prefrontal cortex and striatal areas showed significantly different activity (Fig.   and Table  ). Decreased likelihood of activation was observed in bilateral caudate head,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …results in a transdiagnostic approach across MDD and SZ 
  
 p &lt;   0.01, FDR corrected, cluster size &gt;400 mm ;   BA   = Brodmann area 
  


#### Anticipatory anhedonia 
  
For anticipatory anhedonia (<mark class="annotated-text">30</mark> studies and 119 foci), prefrontal cortex and striatal areas showed significantly different activity (Fig.   and Table  ). Decreased likelihood of activation was observed in bilateral caudate head, le…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …level analyses on common executive (shared activation across tasks tapping inhibition, switching, and updating executive processes; Figure  ) and each specific putative executive process (inhibition, <mark class="annotated-text">updating</mark>, and switching) were conducted. First-level analyses describe clusters that pass the applied threshold for significant conjunctive activation across these groups of studies. These analyses were compu…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5383671/"
                                       >PMC5383671</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …complete study reporting, we were unable to perform CMA between normal and low mood. Instead, we performed MAC of studies comparing painful stimulation with or without concomitant low mood condition (<mark class="annotated-text">LM</mark>  subgroup;  ). We expected to detect increase in activation intensity during the low mood condition in emotional circuits and structures contributing to central pain augmentation and chronification. …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5554296/"
                                       >PMC5554296</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …y Material for included studies and  ). Coordinates from experimental hyperalgesia in HC and CP (11 studies, 116 subjects; 3 studies, 26 subjects) and pain studies in HC involving low mood induction (<mark class="annotated-text">5</mark> studies, 114 subjects) were also extracted.   
Flowchart of fMRI papers included in the analysis. 
  Fig. 1   

The studies were divided into modality and condition-specific sub datasets ( ). Relevan…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5554296/"
                                       >PMC5554296</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …mined the effects of IN-OT in clinical population. ALE analysis from FWE correction revealed that IN-OT increased neural activity in the dorsal anterior cingulate cortex (dACC) (FWE   P   &lt;     0.05; <mark class="annotated-text">14</mark> ‘OT &gt; PL’ contrasts, 114 activation coordinates;  ) and decreased the left amygdala activity (FWE   P   &lt;     0.05; 7 ‘OT &gt; PL’ contrasts, 33 activation coordinates;  ).
   
The effects of IN-OT on b…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5647800/"
                                       >PMC5647800</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …for peak coordinates and ALE values). The ALE single map for 3PP yielded consistent activations in the bilateral PosCG and left AI, ACC, MOG and IPL (see   and   for peak coordinates and ALE values). <mark class="annotated-text">Conjunction</mark> analysis for both perspectives revealed bilateral activity in the PosCG, left AI, ACC and IPL ( ). Subtraction analysis revealed no specific clusters for the 1PP (1PP &gt; 3PP) or 3PP (3PP &gt; 1PP; see   …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6847411/"
                                       >PMC6847411</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Gao, <mark class="annotated-text">Xinyu</mark> and Zhang, Mengzhe and Yang, Zhengui and Wen, Mengmeng and Huang, Huiyu and Zheng, Ruiping and Wang, Weijian and Wei, Yarui and Cheng, Jingliang and Han, Shaoqiang and Zhang, Yong
Front Psychiatry, 2…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8281314/"
                                       >PMC8281314</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ital gyrus and the right middle temporal gyrus. Relative to the pooled analysis, in the pediatric group (22 datasets), no significant hypoactivation was found in the right superior temporal gyrus and <mark class="annotated-text">the</mark> right postcentral gyrus. On the contrary, overactivation of the right fusiform gyrus was found. The rest was largely consistent with the pooled analysis (see  ,  ;  ). 
  
Results of subgroup analysi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9853532/"
                                       >PMC9853532</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">largescale-neurosynth encoding (9 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Chrastil</mark>, Elizabeth R and Tobyne, Sean M and Nauer, Rachel K and Chang, Allen E and Stern, Chantal E
Behavioral neuroscience, 2018

# Title

Converging meta-analytic and connectomic evidence for functional su…
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
                    <mark class="annotated-text">Zhang</mark>, Binlong and Liu, Jiao and Bao, Tuya and Wilson, Georgia and Park, Joel and Zhao, Bingcong and Kong, Jian
The Australian and New Zealand journal of psychiatry, 2021

# Title

Locations for noninvasiv…
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
                    …Direct comparison of aversive anticipation studies using tactile versus visual stimuli identified additional regions involved in sensory specific aversive anticipation across these sensory modalities.<mark class="annotated-text"> Results from complementary multi-study voxel-wise and NeuroSynth analyses generally provide converging evidence for a core circuit involved in aversive anticipation. </mark>The multi-study voxel-wise analyses also implicate a more widespread preparatory response across sensory, motor, and cognitive control regions during more prolonged periods of aversive anticipation. T…
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
                    …wo commonly employed tasks of episodic retrieval and mentalizing. In a subset of participants, relationships among task-evoked regions were examined at rest, in the absence of an overt task. Finally, <mark class="annotated-text">large-scale fMRI meta-analyses</mark> were conducted to identify brain regions that most strongly predicted the presence of episodic retrieval and mentalizing, and these results were compared to meta-analyses of autobiographical tasks. A…
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
                    …ain regions are evoked by the mere presence of social information using an automated meta-analysis and confirmatory data from an independent study of simple appraisal of social vs. non-social images. <mark class="annotated-text">Results of 1,000 published fMRI studies containing the keyword of “social” were subject to an automated meta-analysis</mark> ( ). To confirm that significant brain regions in the meta-analysis were driven by a social effect, these brain regions were used as regions of interest (ROIs) to extract and compare BOLD fMRI signal…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5933734/"
                                       >PMC5933734</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …-attentional network and the MCS map, while UWS patients, being unresponsive to external stimuli, by definition, should not activate this network. To explicitly test this assumption, we extracted the <mark class="annotated-text">dorsal-attentional uniformity map from the neurosynth toolbox ( ) by searching the term “dorsal-attentional”.</mark> The UWS and MCS ALE maps were binarised into VOIs using the software MRIcron [ ]. We then applied a standard intersection analysis to identify the regions of anatomical overlap between each category …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6517954/"
                                       >PMC6517954</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …at are used as general words in neuroscience literature, such as ‘focus’ and ‘strength.’ Thus, we selected the 121 cognitive terms shown in   as the targets to be considered in this study. 

Then, we <mark class="annotated-text">reconstructed the binary activation map</mark> on the 2-mm-resolution MNI 152 brain for each article registered in Neurosynth data by the following steps. First, we transformed the coordinates reported in the Talairach brain into the MNI brain us…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6965330/"
                                       >PMC6965330</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e using finite impulse response models (time window from 1 to 12 s). Regions of interest (ROIs) located in the SM cortex were defined as the overlap between anatomical and a priori functional masks . <mark class="annotated-text">Functional masks were obtained using the Neurosynth platform for an automatic meta-analysis ( ). We used a uniformity test with a default false discovery rate (FDR) corrected p &lt; 0.01 threshold for the “motor” term (2565 studies). </mark>To obtain anatomical masks, we used voxels with the maximum probability for “precentral gyrus” and “precentral gyrus” labels according to the probabilistic Harvard–Oxford atlas . ROI analysis was perf…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9203582/"
                                       >PMC9203582</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …, executive functioning (EF), and visuospatial abilities (VS) across ~1.5–2 years of follow-up, which matches follow-up periods of several recent phase 2b&amp;3 clinical trials (e.g., EMERGE/ENGAGE) [ ]. <mark class="annotated-text">To assess the association between tau-PET and cognitive-domain-specific decline, we obtained meta-analytical maps of task-fMRI studies from Neurosynth [ ,  ] to determine brain regions that are consistently associated with MEM/LAN/EF/VS across ~1900 task-fMRI studies. </mark>We then mapped patient-specific tau-PET to cognitive-domain-specific brain activation maps and tested whether determining baseline tau-PET in regions involved in a given cognitive domain improves the …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9639286/"
                                       >PMC9639286</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - protocol (8 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Lyu, Diyang and Li, Taoran and Lyu, Xuanxin
BMJ open, 2021

# Title

Resting-state functional reorganisation in Alzheimer&#39;s disease and amnestic mild cognitive impairment: <mark class="annotated-text">protocol</mark> for a systematic review and meta-analysis.

# Keywords

Dementia 
Diagnostic radiology 
NEUROLOGY 
dementia 
diagnostic radiology 
neurology 


# Abstract

The incidence of Alzheimer&#39;s disease (AD) i…
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
                    …d Li, Danyang and Me, Yutong and Fan, Hongyu and Wu, Hao and Zhang, Gaofeng
BMJ open, 2022

# Title

Effect of repetitive transcranial magnetic stimulation on patients with severe depression: a study <mark class="annotated-text">protocol</mark> for systematic review and meta-analysis of randomised clinical trials.

# Keywords

complementary medicine 
depression &amp; mood disorders 
radiology &amp; imaging 
radiotherapy 


# Abstract

Depression is…
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
                    … and Outhred, Tim and Westlye, Lars T. and Malhi, Gin S. and Andreassen, Ole A.
Syst Rev, 2016

# Title

The impact of oxytocin administration on brain activity: a systematic review and meta-analysis <mark class="annotated-text">protocol</mark>

# Keywords

Oxytocin
Brain imaging
Systematic review
Meta-analysis
Protocol


# Abstract
 
## Background 
  
Converging evidence demonstrates the important role of the neuropeptide hormone oxytocin …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5129649/"
                                       >PMC5129649</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … Hu, Yiru and Fu, Yu and Cao, Liping and Zhang, Bin
BMJ Open, 2020

# Title

Functional MRI in the effect of transcranial magnetic stimulation therapy for patients with schizophrenia: a meta-analysis <mark class="annotated-text">protocol</mark>

# Keywords

neuroradiology
schizophrenia &amp; psychotic disorders
magnetic resonance imaging


# Abstract
 
## Introduction 
  
Schizophrenia is a psychiatric illness associated with brain function alt…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7713205/"
                                       >PMC7713205</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … Horácio
Trends Psychiatry Psychother, 2021

# Title

Attention-deficit/hyperactivity disorder and brain metabolites from proton magnetic resonance spectroscopy: a systematic review and meta-analysis <mark class="annotated-text">protocol</mark>

# Keywords

MRS
spectroscopy
ADHD
meta-analysis
protocol


# Abstract
 
Despite major advances in the study of the brain, investigations on neurochemistry in vivo still lack the solid ground of more…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7932040/"
                                       >PMC7932040</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Ubalde, Leonard and Liang, Jing-Nong
Brain Sci, 2021

# Title

Neurophysiological Assessments of Brain and Spinal Cord Associated with Lower Limb Functions in Children with Cerebral Palsy: A <mark class="annotated-text">Protocol</mark> for Systematic Review and Meta-Analysis

# Keywords

cerebral palsy
walking
neuroplasticity
neurophysiology
systematic review


# Abstract
 
Background: Task-dependent neurophysiological adaptations …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8153104/"
                                       >PMC8153104</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …, Haizhu and Cao, Jiazhen and Wang, Guan and Liu, Yanze and Wang, Hongfeng
BMJ Open, 2021

# Title

Study on acupuncture in the treatment of painful diabetic peripheral neuropathy based on rs-fMRI: a <mark class="annotated-text">protocol</mark> for systematic review and meta-analysis

# Keywords

complementary medicine
diabetic neuropathy
magnetic resonance imaging
diabetes &amp; endocrinology
neurology


# Abstract
 
## Introduction 
  
Studie…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8388266/"
                                       >PMC8388266</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nd Wang, Ying and Ma, Shiqi and Lu, Qi and Wang, Hongfeng
Medicine (Baltimore), 2022

# Title

Study on acupuncture improving sleep deprivation comorbid with cognitive dysfunction based on rs-fMRI: A <mark class="annotated-text">protocol</mark> for systematic review and meta-analysis

# Keywords

acupuncture
cognitive dysfunction
meta-analysis
protocol
rs-fMRI
systematic review


# Abstract
  Background:  
Sleep deprivation often lead to ch…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10082247/"
                                       >PMC10082247</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - about ma&#39;s (8 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Ramsey, J D and Spirtes, P and Glymour, C
NeuroImage, 2011

# Title

<mark class="annotated-text">On meta-analyses of imaging data and the mixture of records.
</mark>
# Keywords



# Abstract

Neumann et al. (2010) aim to find directed graphical representations of the independence and dependence relations among activities in brain regions by applying a search proc…
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
                    … Simon B and Wager, Tor D and Barrett, Lisa Feldman and Atzil, Shir and Johnson, Timothy D and Nichols, Thomas E
Journal of the Royal Statistical Society. Series C, Applied statistics, 2021

# Title

<mark class="annotated-text">Bayesian log-Gaussian Cox process regression: with applications to meta-analysis of neuroimaging working memory studies.
</mark>
# Keywords

functional magnetic resonance imaging 
meta-regression 
random effects meta-analysis 
working memory 


# Abstract

Working memory (WM) was one of the first cognitive processes studied wi…
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
                    Peiffer, Ann M. and Maldjian, Joseph A. and Laurienti, Paul J.
Int J Biomed Imaging, 2007

# Title

<mark class="annotated-text">Resurrecting Brinley Plots for a Novel Use: Meta-Analyses of Functional Brain Imaging Data in Older Adults
</mark>
# Keywords



# Abstract
 
By plotting response times of young and older adults across a variety of tasks, Brinley spurred investigation and debate into the theory of general cognitive slowing. Thoug…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2233772/"
                                       >PMC2233772</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Costafreda, Sergi G.
Front Neuroinformatics, 2009

# Title

<mark class="annotated-text">Pooling fMRI Data: Meta-Analysis, Mega-Analysis and Multi-Center Studies
</mark>
# Keywords

fMRI
meta-analysis
mega-analysis
multi-center studies
power
false positive results
random effects analysis
study design


# Abstract
 
The quantitative analysis of pooled data from relate…
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
                    Tench, Christopher R. and Tanasescu, Radu and Auer, Dorothee P. and Constantinescu, Cris S.
PLoS One, 2013

# Title

<mark class="annotated-text">Coordinate Based Meta-Analysis of Functional Neuroimaging Data; False Discovery Control and Diagnostics
</mark>
# Keywords



# Abstract
 
Coordinate based meta-analysis (CBMA) is widely used to find regions of consistent activation across fMRI studies that have been selected for their functional relevance to …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3726528/"
                                       >PMC3726528</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Tench, Christopher R. and Tanasescu, Radu and Auer, Dorothee P. and Cottam, William J. and Constantinescu, Cris S.
PLoS One, 2014

# Title

<mark class="annotated-text">Coordinate Based Meta-Analysis of Functional Neuroimaging Data Using Activation Likelihood Estimation; Full Width Half Max and Group Comparisons
</mark>
# Keywords



# Abstract
 
Coordinate based meta-analysis (CBMA) is used to find regions of consistent activation across fMRI and PET studies selected for their functional relevance to a hypothesis. …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4165754/"
                                       >PMC4165754</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Acar, Freya and Seurinck, Ruth and Eickhoff, Simon B. and Moerkerke, Beatrijs
PLoS One, 2018

# Title

<mark class="annotated-text">Assessing robustness against potential publication bias in Activation Likelihood Estimation (ALE) meta-analyses for fMRI
</mark>
# Keywords



# Abstract
 
The importance of integrating research findings is incontrovertible and procedures for coordinate-based meta-analysis (CBMA) such as Activation Likelihood Estimation (ALE) …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6267999/"
                                       >PMC6267999</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ibene, Aurora and Corchs, Silvia E. and Clemente, Lucia and Danelli, Laura and Gallucci, Marcello and Borgoni, Riccardo and Borghese, Nunzio Alberto and Paulesu, Eraldo
Front Neurosci, 2019

# Title

<mark class="annotated-text">Clustering the Brain With “CluB”: A New Toolbox for Quantitative Meta-Analysis of Neuroimaging Data
</mark>
# Keywords

coordinate-based meta-analysis
clustering
non-parametric statistics
cognitive dimensions
anatomical segregation
clusters composition


# Abstract
 
In this paper we describe and validate …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6817507/"
                                       >PMC6817507</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #eeeeec;">
        <summary class="label-display">ask about this one (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Peiffer</mark>, Ann M. and Maldjian, Joseph A. and Laurienti, Paul J.
Int J Biomed Imaging, 2007

# Title

Resurrecting Brinley Plots for a Novel Use: Meta-Analyses of Functional Brain Imaging Data in Older Adults
…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">I don&#39;t get this study</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2233772/"
                                       >PMC2233772</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …in each cluster. Clusters were further considered if they contained a number of coordinates greater than the median of the distribution for each analysis and, in any event, with no &lt;3 coordinates. 


<mark class="annotated-text">### Activation likelihood analyses 
</mark>  
To assess to what extent the functional segregations identified by the HC analyses could be replicated on a much larger dataset of studies on action, we interrogated the BrainMap.org database to ge…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">did they do mcam? how many ma&#39;s did they do? 3?</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5434171/"
                                       >PMC5434171</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Burles</mark>, Ford and Umiltá, Alberto and McFarlane, Liam H. and Potocki, Kendra and Iaria, Giuseppe
Front Hum Neurosci, 2018

# Title

Ventral—Dorsal Functional Contribution of the Posterior Cingulate Cortex in…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">did they do macm?</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5951926/"
                                       >PMC5951926</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ons of different stimuli were interpreted to provide insight into how information processing is functionally segregated across cooperating neural systems during naturalistic tasks. 



## RESULTS 
  
<mark class="annotated-text">The literature search yielded a combined set of 110 studies that reported coordinates of brain activation from naturalistic fMRI tasks among healthy adults ( ; PubMed IDs available in Supporting Information Table S1, Bottenhorn, Flannery, Boeving, Riedel, Eickhoff, Sutherland, &amp; Laird,  ). The final dataset included activation foci from 376 experimental contrasts (  N   = 1,817 subjects) derived from tasks using a variety of stimulus types and sensory modalities. </mark>Across our corpus of naturalistic fMRI experiments, approximately 55% assessed a single stimulus modality, including 40% visual stimuli, 13% auditory, and 1% tactile. 

Conversely, 45% of experiments …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">They clustered maps into 6 groups then performed 6 meta-analyses, but I can&#39;t find the number of studies in each analysis.</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6326731/"
                                       >PMC6326731</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Jauniaux</mark>, Josiane and Khatibi, Ali and Rainville, Pierre and Jackson, Philip L
Soc Cogn Affect Neurosci, 2019

# Title

A meta-analysis of neuroimaging studies on pain empathy: investigating the role of visua…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">how to code individual analyses</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6847411/"
                                       >PMC6847411</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Sinha</mark>, Preeti and Joshi, Himanshu and Ithal, Dhruva
Front Hum Neurosci, 2020

# Title

Resting State Functional Connectivity of Brain With Electroconvulsive Therapy in Depression: Meta-Analysis to Understa…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">seems like they resorted to desperate measures to find more experiments to include.</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7859100/"
                                       >PMC7859100</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Zunhammer</mark>, Matthias and Spisák, Tamás and Wager, Tor D. and Bingel, Ulrike and nan, nan
Nat Commun, 2021

# Title

Meta-analysis of neural systems underlying placebo analgesia from individual participant fMRI …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">is this a meta-analysis? they analyzed participant-level maps</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7925520/"
                                       >PMC7925520</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #eeeeec;">
        <summary class="label-display">candidate for replication (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Kirby<mark class="annotated-text">,</mark> Lauren A J and Robinson, Jennifer L
Brain and cognition, 2018

# Title

Affective mapping: An activation likelihood estimation (ALE) meta-analysis.

# Keywords

Activation likelihood estimation 
Affe…
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
                    Hétu, <mark class="annotated-text">Sébastien</mark> and Grégoire, Mathieu and Saimpont, Arnaud and Coll, Michel-Pierre and Eugène, Fanny and Michon, Pierre-Emmanuel and Jackson, Philip L
Neuroscience and biobehavioral reviews, 2014

# Title

The neura…
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
                    Xu, Min and <mark class="annotated-text">Xu</mark>, Guiping and Yang, Yang
Frontiers in behavioral neuroscience, 2020

# Title

Neural Systems Underlying Emotional and Non-emotional Interference Processing: An ALE Meta-Analysis of Functional Neuroima…
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
                    Satpute, Ajay B <mark class="annotated-text">and</mark> Kang, Jian and Bickart, Kevin C and Yardley, Helena and Wager, Tor D and Barrett, Lisa F
Frontiers in psychology, 2015

# Title

Involvement of Sensory Regions in Affective Experience: A Meta-Analysi…
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
                    Gan, Xianyang and <mark class="annotated-text">Zhou</mark>, Xinqi and Li, Jialin and Jiao, Guojuan and Jiang, Xi and Biswal, Bharat and Yao, Shuxia and Klugah-Brown, Benjamin and Becker, Benjamin
Neuroscience and biobehavioral reviews, 2022

# Title

Common …
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
                    Picó-Pérez, Maria and Vieira, <mark class="annotated-text">Rita</mark> and Fernández-Rodríguez, Marcos and De Barros, Maria Antónia Pereira and Radua, Joaquim and Morgado, Pedro
Psychological medicine, 2022

# Title

Multimodal meta-analysis of structural gray matter, n…
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
                    <mark class="annotated-text">Yu</mark>, Miaomiao and Gao, Xinyu and Niu, Xiaoyu and Zhang, Mengzhe and Yang, Zhengui and Han, Shaoqiang and Cheng, Jingliang and Zhang, Yong
Front Psychiatry, 2022

# Title

Meta-analysis of structural and …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9853532/"
                                       >PMC9853532</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA8 (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ence in cerebellum, supramarginal gyrus, superior temporal gyrus and thalamus. Including data on greater deactivation of sham acupuncture points compared to baseline (3d, rest&gt;sham) from 50 subjects, <mark class="annotated-text">5</mark> experiments and 52 foci, resulted in significant convergence in pregenual anterior cingulate, subgenual cortex and parahippocampal gyrus. 

Finally, in the contrast (subtraction) comparing the betwee…
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
                    …hippocampus, ACC, mPFC and MFG (  p   &lt; 0.01, FDR corrected, cluster size &gt; 400 mm ). Increased likelihood of activation was observed in the left IFG and MFG. 


#### Emotional processing 
  
For the <mark class="annotated-text">emotional experience task</mark> (31 studies and 163 foci), decreased likelihood of activation was observed in a number of brain areas from the cortical-subcortical network (Fig.   and Table  ), including right GPe, right putamen, r…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …MFG (  p   &lt; 0.01, FDR corrected, cluster size &gt; 400 mm ). Increased likelihood of activation was observed in the left IFG and MFG. 


#### Emotional processing 
  
For the emotional experience task (<mark class="annotated-text">31</mark> studies and 163 foci), decreased likelihood of activation was observed in a number of brain areas from the cortical-subcortical network (Fig.   and Table  ), including right GPe, right putamen, right…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … on common executive (shared activation across tasks tapping inhibition, switching, and updating executive processes; Figure  ) and each specific putative executive process (inhibition, updating, and <mark class="annotated-text">switching</mark>) were conducted. First-level analyses describe clusters that pass the applied threshold for significant conjunctive activation across these groups of studies. These analyses were computed for both th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5383671/"
                                       >PMC5383671</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tion coordinates;  ).
   
The effects of IN-OT on brain activity in healthy volunteers and patients (threshold: FWE   P   &lt;     0.05, 1000 permutations,   k   &gt; 15 mm ) 
    


### Comparison between <mark class="annotated-text">patients and healthy volunteers </mark>
  
Given that the majority of IN-OT fMRI studies examined neural substrates mediating OT effects in healthy population, a key issue for OT clinical translation was to reveal the common and differenti…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5647800/"
                                       >PMC5647800</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …the pain visual cue factor 
  
Higher ALE values or   Z   scores are associated with greater probability of activation across experiments. 
  

### Self/other cognitive perspective taking 
  
For the <mark class="annotated-text">SEO</mark> condition, the single ALE map showed consistent activation in the left IFG, IPL, ACC, aMCC, AI, PreCG, MFG and claustrum, and right IPL and MOG (  and   for peak coordinates and ALE values). Several …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6847411/"
                                       >PMC6847411</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Gao, <mark class="annotated-text">Xinyu</mark> and Zhang, Mengzhe and Yang, Zhengui and Wen, Mengmeng and Huang, Huiyu and Zheng, Ruiping and Wang, Weijian and Wei, Yarui and Cheng, Jingliang and Han, Shaoqiang and Zhang, Yong
Front Psychiatry, 2…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8281314/"
                                       >PMC8281314</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …iform gyrus, and left middle temporal gyrus (Table  ). 


### Group differences for angry facial expressions 
  
The whole-brain meta-analysis of responses to angry facial expressions images included <mark class="annotated-text">five</mark> contrasts, one selected from each included study. No results survived FWER-correction. Uncorrected group differences in activation were observed in a cluster spanning left supplementary motor area an…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10063659/"
                                       >PMC10063659</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">software-MKDA toolbox (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Gong</mark>, Jiaying and Wang, Junjing and Chen, Pan and Qi, Zhangzhang and Luo, Zhenye and Wang, Jurong and Huang, Li and Wang, Ying
Journal of affective disorders, 2021

# Title

Large-scale network abnormalit…
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
                    <mark class="annotated-text">Nikolic</mark>, Maja and Pezzoli, Patrizia and Jaworska, Natalia and Seto, Michael C
Progress in neuro-psychopharmacology &amp; biological psychiatry, 2022

# Title

Brain responses in aggression-prone individuals: A s…
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
                    <mark class="annotated-text">Wang</mark>, Jing and Conder, Julie A and Blitzer, David N and Shinkareva, Svetlana V
Human brain mapping, 2011

# Title

Neural representation of abstract and concrete concepts: a meta-analysis of neuroimaging …
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
                    <mark class="annotated-text">Taebi</mark>, Arezoo and Becker, Benjamin and Klugah-Brown, Benjamin and Roecher, Erik and Biswal, Bharat and Zweerings, Jana and Mathiak, Klaus
Addiction biology, 2022

# Title

Shared network-level functional a…
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
                    Brandl, <mark class="annotated-text">Felix</mark> and Avram, Mihai and Weise, Benedikt and Shang, Jing and Simões, Beatriz and Bertram, Teresa and Hoffmann Ayala, Daniel and Penzel, Nora and Gürsel, Deniz A and Bäuml, Josef and Wohlschläger, Afra M …
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
                    Chrastil, Elizabeth <mark class="annotated-text">R</mark> and Tobyne, Sean M and Nauer, Rachel K and Chang, Allen E and Stern, Chantal E
Behavioral neuroscience, 2018

# Title

Converging meta-analytic and connectomic evidence for functional subregions with…
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
                    …we used a threshold of 15 studies. See Tables  –  for preliminary results from models that did not meet this threshold. 


### Multilevel kernel density analysis 
  
Analyses were conducted using the <mark class="annotated-text">MKDA toolbox</mark> in SPM12 . Foci in Talairach space were converted to MNI space . Binary indicator maps for each contrast were created by convolving peak foci using a 10-mm spherical kernel, with voxels related to ps…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7203015/"
                                       >PMC7203015</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">software-brainmap (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Zald</mark>, David H and McHugo, Maureen and Ray, Kimberly L and Glahn, David C and Eickhoff, Simon B and Laird, Angela R
Cerebral cortex (New York, N.Y. : 1991), 2014

# Title

Meta-analytic connectivity modeli…
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
                    <mark class="annotated-text">Wong</mark>, Ting Yat and Sid, Azah and Wensing, Tobias and Eickhoff, Simon B and Habel, Ute and Gur, Ruben C and Nickl-Jockschat, Thomas
Brain structure &amp; function, 2019

# Title

Neural networks of aggression:…
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
                    Yeung, <mark class="annotated-text">Andy</mark> Wai Kan
Public health nutrition, 2021

# Title

Brain responses to watching food commercials compared with nonfood commercials: a meta-analysis on neuroimaging studies.

# Keywords

Child obesity 
Fo…
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
                    Rotge, <mark class="annotated-text">Jean</mark>-Yves and Guehl, Dominique and Dilharreguy, Bixente and Cuny, Emmanuel and Tignol, Jean and Bioulac, Bernard and Allard, Michele and Burbaud, Pierre and Aouizerate, Bruno
Journal of psychiatry &amp; neuro…
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
                    Daniel, Thomas A and Katz, Jeffrey S and Robinson, Jennifer L
Biological psychology, 2017

# Title

Delayed match-to-sample in working memory: A <mark class="annotated-text">BrainMap</mark> meta-analysis.

# Keywords

ALE 
Activation likelihood estimation 
Functional neuroimaging 
Neural networks 
fMRI 


# Abstract

Working memory (WM), or the ability to temporarily store and manipulat…
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
                    Hill, Ashley C and Laird, Angela R and Robinson, Jennifer L
Biological psychology, 2015

# Title

Gender differences in working memory networks: a <mark class="annotated-text">BrainMap</mark> meta-analysis.

# Keywords

BrainMap 
Gender differences 
Sex differences 
Working memory 
fMRI 


# Abstract

Gender differences in psychological processes have been of great interest in a variety o…
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
                    … of psychopathy, we conducted a functional characterization of the regions that were found in our meta-analysis. Hereby, psychological terms were related to the respective region as registered in the <mark class="annotated-text">BrainMap</mark> database, i.e., on basis of functional experiments in healthy subjects ( ;  ). 

The right lateral prefrontal cortex was significantly associated with action execution and at the more liberal thresho…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6344321/"
                                       >PMC6344321</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">software-other (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Phan</mark>, K Luan and Wager, Tor and Taylor, Stephan F and Liberzon, Israel
NeuroImage, 2002

# Title

Functional neuroanatomy of emotion: a meta-analysis of emotion activation studies in PET and fMRI.

# Keyw…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">SPM-96</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Cortese</mark>, Samuele and Castellanos, F Xavier and Eickhoff, Claudia R and D&#39;Acunto, Giulia and Masi, Gabriele and Fox, Peter T and Laird, Angela R and Eickhoff, Simon B
Biological psychiatry, 2017

# Title

Fun…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">in-house MATLAB scripts implementing ALE</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Gilat, <mark class="annotated-text">Moran</mark> and Dijkstra, Bauke W and D&#39;Cruz, Nicholas and Nieuwboer, Alice and Lewis, Simon J G
Current neurology and neuroscience reports, 2020

# Title

Functional MRI to Study Gait Impairment in Parkinson&#39;s …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">sjView</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Derrfuss, <mark class="annotated-text">Jan</mark> and Brass, Marcel and Neumann, Jane and von Cramon, D Yves
Human brain mapping, 2005

# Title

Involvement of the inferior frontal junction in cognitive control: meta-analyses of switching and Stroop…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">from CSL lab</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Bliksted, <mark class="annotated-text">Vibeke</mark> and Ubukata, Shiho and Koelkebeck, Katja
Schizophrenia research, 2016

# Title

Discriminating autism spectrum disorders from schizophrenia by investigation of mental state attribution on an on-line …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">StataIC</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Rottschy, C <mark class="annotated-text">and</mark> Langner, R and Dogan, I and Reetz, K and Laird, A R and Schulz, J B and Fox, P T and Eickhoff, S B
NeuroImage, 2012

# Title

Modelling neural correlates of working memory: a coordinate-based meta-an…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">in-house MATLAB scripts</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …



### Data and code availability 
  
All data used in this project (coded foci of activation differences) are available in the  . The MKDA code used to perform meta-analyses is freely available via <mark class="annotated-text">CANLAB</mark> ( ). 



## Results 
  
### Included Studies. 
  
See   for flow diagram and detailed information on study selection. The initial database search yielded a total of 2213 articles. Of these, 76 met in…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7992390/"
                                       >PMC7992390</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">largescale-brainmap decoding (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … language comprehension in human children. Our analysis included 27 independent experiments involving n ​= ​625 children (49% girls) with a mean age of 8.9 years. Activation likelihood estimation and <mark class="annotated-text">seed-based effect size mapping</mark> revealed activation peaks in the pars triangularis of the left inferior frontal gyrus and bilateral superior and middle temporal gyri. In contrast to this distribution of activation in children, prev…
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
                    …distinct aspects of emotion processing, we applied an emergent meta-analytic clustering approach to the extensive body of affective neuroimaging results archived in the BrainMap database. Specifically<mark class="annotated-text">, we performed hierarchical clustering on the modeled activation maps from 1,747 experiments in the affective processing domain, </mark>resulting in five meta-analytic groupings of experiments demonstrating whole-brain recruitment. Behavioral inference analyses conducted for each of these groupings suggested dissociable networks suppo…
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
                    …e fMRI datasets and the functional roles of other DICCCOLs are unknown yet. This work aims to take the advantage of existing literature fMRI studies (1110 publications) reported and aggregated in the <mark class="annotated-text">BrainMap</mark> database to examine the possible functional roles of 358 DICCCOLs via meta-analysis. Our experimental results demonstrate that a majority of 358 DICCCOLs can be functionally annotated by the BrainMap…
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
                    …ation meta-analysis of 24 task-based fMRI studies in adults with ADHD. Each ADHD-related dysfunctional region resulting from the activation likelihood estimation meta-analysis was then analyzed using <mark class="annotated-text">functional decoding based on ~7500 fMRI experiments in the BrainMap database</mark>. This approach allows mapping brain regions to functions not necessarily tested in individual studies, thus suggesting possible novel functions for those regions. Additionally, ADHD-related dysfuncti…
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
                    …nt analysis approach tested for convergence by experiments (random effects) rather than foci (fixed effects) ( ); for further details and a summary of the ALE method please refer to ( ,  ,  ). 


### <mark class="annotated-text">Functional decoding using the BrainMap</mark> database 
  
To assess the functional roles of the abnormal brain regions in OSA, behavioral decoding using the BrainMap database was consequently performed. More specifically, we tested which types …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5103027/"
                                       >PMC5103027</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ant activity associated with psychopathy and thus provide a link to the psychopathology of psychopathy, we conducted a functional characterization of the regions that were found in our meta-analysis. <mark class="annotated-text">Hereby, psychological terms were related to the respective region as registered in the BrainMap database, i.e., on basis of functional experiments in healthy subjects ( ;  ). 
</mark>
The right lateral prefrontal cortex was significantly associated with action execution and at the more liberal threshold also with pain perception. In contrast, the left lateral prefrontal cluster wa…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6344321/"
                                       >PMC6344321</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s plugin tool is implemented in Mango software (version 4.1;  ). This plugin tool enables the analysis of behaviors and cognitive functions regarding the set ROI. This tool was developed based on the <mark class="annotated-text">BrainMap</mark> database. Foci corresponding with five behavioral domains (“Action”, “Cognition”, “Emotion”, “Interoception”, and “Perception”) are organized in the BrainMap database. Moreover, these behavioral doma…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9207674/"
                                       >PMC9207674</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">software-spm (6 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Giehl</mark>, Kathrin and Tahmasian, Masoud and Eickhoff, Simon B and van Eimeren, Thilo
Parkinsonism &amp; related disorders, 2020

# Title

Imaging executive functions in Parkinson&#39;s disease: An activation likeliho…
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
                    Etkin, <mark class="annotated-text">Amit</mark> and Wager, Tor D
The American journal of psychiatry, 2007

# Title

Functional neuroimaging of anxiety: a meta-analysis of emotional processing in PTSD, social anxiety disorder, and specific phobia.
…
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
                    Schumer, <mark class="annotated-text">Maya</mark> C and Chase, Henry W and Rozovsky, Renata and Eickhoff, Simon B and Phillips, Mary L
Molecular psychiatry, 2023

# Title

Prefrontal, parietal, and limbic condition-dependent differences in bipolar d…
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
                    Rigo, Paola <mark class="annotated-text">and</mark> Kim, Pilyoung and Esposito, Gianluca and Putnick, Diane L and Venuti, Paola and Bornstein, Marc H
Developmental review : DR, 2020

# Title

Specific maternal brain responses to their own child&#39;s face…
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
                    Qin, Pengmin and <mark class="annotated-text">Liu</mark>, Yijun and Shi, Jinfu and Wang, Yuzhi and Duncan, Niall and Gong, Qiyong and Weng, Xuchu and Northoff, Georg
Human brain mapping, 2012

# Title

Dissociation between anterior and posterior cortical r…
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
                    Adolfi, Federico and <mark class="annotated-text">Couto</mark>, Blas and Richter, Fabian and Decety, Jean and Lopez, Jessica and Sigman, Mariano and Manes, Facundo and Ibáñez, Agustín
Cortex; a journal devoted to the study of the nervous system and behavior, 201…
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
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - not a full report (6 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Alústiza, Irene and Garcés, María Sol and Ortuño, Marta and Molero, Patricio and Ortuño, Felipe
Schizophr Bull, 2018

# Title

<mark class="annotated-text">S71</mark>. ABERRANT TIMING AND SALIENCE NETWORK IN SCHIZOPHRENIA: FINDINGS FROM A META-ANALYSIS

# Keywords



# Abstract
 
## Background 
  
Schizophrenia (SZ) affects several domains of cognitive function. A…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5887562/"
                                       >PMC5887562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Lattanzi, Guido Maria and Scarpazza, Cristina and Di Fabio, Fabio and McGuire, Philip and Sartori, Giuseppe and Eickhoff, Simon B and Tognin, Stefania
Schizophr Bull, 2018

# Title

<mark class="annotated-text">S176</mark>. SYSTEMATIC REVIEW AND META-ANALYSIS OF MAGNETIC RESONANCE IMAGING FINDINGS IN 22Q11.2 DELETION SYNDROME

# Keywords



# Abstract
 
## Background 
  
Since the 22q11.2 Deletion Syndrome (22q11.2 DS)…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5887962/"
                                       >PMC5887962</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Rapp, Alexander and Purr, Franziska and Felsenheimer, Anne
Schizophr Bull, 2018

# Title

<mark class="annotated-text">T58</mark>. SARCASM COMPREHENSION AS A SOCIAL COGNITION MEASURE IN SCHIZOPHRENIA – A SYSTEMATIC LITERATURE SEARCH AND META-ANALYSIS ON THE USE OF THE TASIT

# Keywords



# Abstract
 
## Background 
  
Social c…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5888645/"
                                       >PMC5888645</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Lukow, Paulina and Kempton, Matthew and Turkheimer, Federico and Modinos, Gemma
Schizophr Bull, 2020

# Title

<mark class="annotated-text">T133. </mark>NEURAL CORRELATES OF EMOTIONAL PROCESSING IN PSYCHOSIS RISK AND ONSET – A SYSTEMATIC REVIEW AND META-ANALYSIS OF FMRI STUDIES

# Keywords



# Abstract
 
## Background 
  
Behavioural findings suggest…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7234314/"
                                       >PMC7234314</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Del Fabro, Lorenzo and Schmidt, André and Delvecchio, Giuseppe and D’Agostino, Armando and Borgwardt, Stefan and Brambilla, Paolo
Schizophr Bull, 2020

# Title

<mark class="annotated-text">T156.</mark> FUNCTIONAL CONNECTIVITY AND RISK OF PSYCHOSIS: AN ACTIVATION LIKELIHOOD ESTIMATION (ALE) META-ANALYSIS OF FUNCTIONAL MAGNETIC RESONANCE IMAGING STUDIES

# Keywords



# Abstract
 
## Background 
  
D…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7234455/"
                                       >PMC7234455</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Del Fabro, Lorenzo and Schmidt, André and Delvecchio, Giuseppe and D’Agostino, Armando and Borgwardt, Stefan and Brambilla, Paolo
Schizophr Bull, 2020

# Title

<mark class="annotated-text">T156</mark>. FUNCTIONAL CONNECTIVITY AND RISK OF PSYCHOSIS: AN ACTIVATION LIKELIHOOD ESTIMATION (ALE) META-ANALYSIS OF FUNCTIONAL MAGNETIC RESONANCE IMAGING STUDIES

# Keywords



# Abstract
 
## Background 
  
…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7234455/"
                                       >PMC7234455</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Torres</mark>, M. and Manghera, P. and Miller, C.
Eur Psychiatry, 2022

# Title

Prediction of Treatment Response in Patients with Major Depressive Disorder: A Meta-Analysis of Functional Magnetic Resonance Imagin…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9567359/"
                                       >PMC9567359</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA9 (5 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …d parahippocampal gyrus. 

Finally, in the contrast (subtraction) comparing the between-group differences for verum and sham acupuncture, significant differences between “verum&gt;rest” and “sham&gt;rest” (<mark class="annotated-text">3e</mark>) as well as between “rest&gt;verum” and “rest&gt;sham” (3f) were identified. The subtraction analysis for “verum&gt;rest” - “sham&gt;rest” showed convergent activations in pre-SMA, middle cingulate gyrus, claust…
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
                    …d, cluster size &gt; 400 mm ). Increased likelihood of activation was observed in the left middle occipital gyrus and fusiform gyrus. 



### Between-group ALE analysis in MDD or SZ 
  
#### MDD 
  
For <mark class="annotated-text">consummatory anhedonia in MDD</mark> (21 studies and 107 foci), decreased likelihood of activation was observed in the left GPe, right caudate body, left putamen, right insula and left ACC (  p   &lt; 0.01, FDR corrected, cluster size &gt; 40…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …reased likelihood of activation was observed in the left middle occipital gyrus and fusiform gyrus. 



### Between-group ALE analysis in MDD or SZ 
  
#### MDD 
  
For consummatory anhedonia in MDD (<mark class="annotated-text">21</mark> studies and 107 foci), decreased likelihood of activation was observed in the left GPe, right caudate body, left putamen, right insula and left ACC (  p   &lt; 0.01, FDR corrected, cluster size &gt; 400 mm…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ted number of IN-OT fMRI studies on patients). During negative social and affective processes, IN-OT increased parahippocampus activity (26.8/1.2/−13.1,   k   = 56 mm , FWE   P   &lt;     0.05; based on <mark class="annotated-text">16</mark> ‘OT &gt; PL’ contrasts, 72 activation coordinates), whereas decreased right amygdala (18.1/−5/−8,   k   = 256 mm , FWE   P   &lt;     0.05; ALE analysis on 21 ‘OT &lt; PL’ contrasts, 136 activation coordinate…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5647800/"
                                       >PMC5647800</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ndition when studies using an EC paradigm were added, namely, the bilateral IPL and claustrum, and left AI, IFG, PreCG, aMCC, ACC and MFG. Refer to   in   for peak coordinates and ALE values. For the <mark class="annotated-text">OTO</mark> condition, the single ALE map revealed consistent activation in the bilateral AI, IFG, MFG and fusiform gyrus; left PI, IPL, caudate head, ACC, claustrum and IOG; and right SPL, aMCC, culmen and PosC…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6847411/"
                                       >PMC6847411</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … conducted due to a lack of sufficient available studies (  n   = 1). 


### Group differences for empathic pain images 
  
The whole-brain meta-analysis of responses to empathic pain images included <mark class="annotated-text">3</mark> contrasts (Table  ). Three regions survived FWER-correction, including a region that spanned right temporal pole and included areas of middle and inferior temporal gyrus in which youths with conduct …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10063659/"
                                       >PMC10063659</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA10 (4 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …subtraction) comparing the between-group differences for verum and sham acupuncture, significant differences between “verum&gt;rest” and “sham&gt;rest” (3e) as well as between “rest&gt;verum” and “rest&gt;sham” (<mark class="annotated-text">3f</mark>) were identified. The subtraction analysis for “verum&gt;rest” - “sham&gt;rest” showed convergent activations in pre-SMA, middle cingulate gyrus, claustrum, insula, supramarginal gyrus, SII and dorsolatera…
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
                    …ith significant different activation between SZ patients and healthy controls. ALE clusters are projected on a standard anatomical template in axial orientation, referring to Talairach space 
  

For <mark class="annotated-text">anticipatory anhedonia in MDD </mark>(17 studies and 89 foci), decreased likelihood of activation was observed in bilateral caudate head and left MFG, and increased activation was observed in left IFG and right MFG. 

For emotional proce…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ation between SZ patients and healthy controls. ALE clusters are projected on a standard anatomical template in axial orientation, referring to Talairach space 
  

For anticipatory anhedonia in MDD (<mark class="annotated-text">17</mark> studies and 89 foci), decreased likelihood of activation was observed in bilateral caudate head and left MFG, and increased activation was observed in left IFG and right MFG. 

For emotional processi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ation coordinates). During the positive social and affective processes, we found that IN-OT increased activity in the caudate head (−7.2/3.2/2.8,   k   = 56 mm , FWE   P   &lt;     0.05; ALE analysis on <mark class="annotated-text">17</mark> ‘OT &gt; PL’ contrasts, 102 activation coordinates), whereas no brain activity decreased by IN-OT was significant (FWE   P   &lt;     0.05; ALE analysis on 13 ‘OT &lt; PL’ contrasts, 48 activation coordinates…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5647800/"
                                       >PMC5647800</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ion in the bilateral AI, IFG, MFG and fusiform gyrus; left PI, IPL, caudate head, ACC, claustrum and IOG; and right SPL, aMCC, culmen and PosCG (see   and   for peak coordinates and ALE values). When <mark class="annotated-text">adding studies using an EC paradigm</mark>, the analysis revealed a similar pattern, but with more regions of activation. Specifically, in this analysis, the bilateral AI, IFG, SPL, SFG and IPL, left ACC, claustrum, and fusiform gyrus and rig…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6847411/"
                                       >PMC6847411</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">IMBA (4 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …erefore, the aim here was to perform a meta-analysis of the existing literature using unthresholded statistical maps from previous studies. A voxelwise seed-based d mapping meta-analysis was performed<mark class="annotated-text"> using t-maps from studies</mark> comparing patients with OCD and healthy control subjects (HCs) during error processing and inhibitory control. For the error processing analysis, 239 patients with OCD (120 male; 79 medicated) and 22…
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
                    …ine consistency of network topography within and across these labels. We hypothesized finding considerable overlap in the spatial topography among the neural networks associated with these labels. An <mark class="annotated-text">image-based meta-analysis</mark> was performed on 158 group-level statistical maps (SPMs) received from authors of 69 papers listed on PubMed. Our results indicated that there was very little consistency in the SPMs labeled with a g…
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
                    …ordance with the Meta-analysis of Observational Studies in Epidemiology guidelines. Using Seed-based d Mapping software, meta-analyses were performed using random-effect nonparametric statistics with <mark class="annotated-text">group whole brain T-maps</mark> from individual studies as input. Analyses were performed across all addictions and for substance and gambling addictions separately. Group differences (individuals with addiction vs control individu…
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
                    …redictive methods of individual placebo analgesia from neuroimaging data, which would be of crucial importance both from a clinical and drug development point of view. Here, we conducted a systematic <mark class="annotated-text">participant-level meta-analysis of 20 independent neuroimaging studies</mark> on experimental placebo analgesia. Based on whole-brain activation patterns in a total of   N   = 603 healthy participants, we mapped the effects of placebo treatment on pain-related brain activity a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7925520/"
                                       >PMC7925520</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">label-based review/MA (4 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Phan, K <mark class="annotated-text">Luan</mark> and Wager, Tor and Taylor, Stephan F and Liberzon, Israel
NeuroImage, 2002

# Title

Functional neuroanatomy of emotion: a meta-analysis of emotion activation studies in PET and fMRI.

# Keywords



…
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
                    … the superior parietal lobule, inferior parietal lobule, and the dorsal premotor cortex but not the inferior frontal gyrus, are all commonly involved in imitation. An additional meta-analysis using a <mark class="annotated-text">label-based review</mark> confirmed that in the frontal lobe, the premotor cortex rather than the inferior frontal gyrus is consistently active in studies investigating imitation. In the parietal region the superior and infer…
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
                    …h study. Thus, the current work is aimed at identifying whether there are spatially consistent structural and functional brain abnormalities in individuals with 22q11.2 DS through (i) a comprehensive <mark class="annotated-text">label-based systematic review</mark> and (ii) a coordinate-based meta-analysis of magnetic resonance imaging studies. The systematic review identified the frontal middle gyri, posterior cingulum, right cuneus and bilateral precuneus as …
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
                    … the ALE map.   shows a flow chat that illustrated the process of this ALE meta-analysis. 
  
Flow chart that illustrates the process of activation likelihood estimation (ALE) meta-analysis. 
  

### <mark class="annotated-text">Label-based meta-analysis</mark> 
  
In addition, a “label-based meta-analysis” [method based on ( )] was performed to tabulate/summarize the activated brain regions commonly reported across the studies. The extracted activation foc…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9808082/"
                                       >PMC9808082</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA11 (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …hedonia in MDD (17 studies and 89 foci), decreased likelihood of activation was observed in bilateral caudate head and left MFG, and increased activation was observed in left IFG and right MFG. 

For <mark class="annotated-text">emotional processing in MDD</mark> (25 studies and 124 foci), decreased likelihood of activation was observed in right GPe and putamen, bilateral amygdala and anterior lobe, right IFG and left ACC, and increased activation was observe…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …d 89 foci), decreased likelihood of activation was observed in bilateral caudate head and left MFG, and increased activation was observed in left IFG and right MFG. 

For emotional processing in MDD (<mark class="annotated-text">25</mark> studies and 124 foci), decreased likelihood of activation was observed in right GPe and putamen, bilateral amygdala and anterior lobe, right IFG and left ACC, and increased activation was observed in…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … 56 mm , FWE   P   &lt;     0.05; ALE analysis on 17 ‘OT &gt; PL’ contrasts, 102 activation coordinates), whereas no brain activity decreased by IN-OT was significant (FWE   P   &lt;     0.05; ALE analysis on <mark class="annotated-text">13</mark> ‘OT &lt; PL’ contrasts, 48 activation coordinates). 


### OT effects in healthy males and females 
  
Conjunction and subtraction analyses on ‘OT &gt; PL’ contrasts (male: 164 activation coordinates in 25…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5647800/"
                                       >PMC5647800</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …n, but with more regions of activation. Specifically, in this analysis, the bilateral AI, IFG, SPL, SFG and IPL, left ACC, claustrum, and fusiform gyrus and right MOG, were recruited (see  ). For the <mark class="annotated-text">STO</mark> condition, the single ALE map showed consistent activations in the bilateral IPL and additionally in the right PosCG and IOG, and left IFG, PreCG, ITG and fusiform (  and  ). When adding studies usin…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6847411/"
                                       >PMC6847411</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA12 (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …observed in right GPe and putamen, bilateral amygdala and anterior lobe, right IFG and left ACC, and increased activation was observed in middle occipital gyrus and fusiform gyrus. 


#### SZ 
  
For <mark class="annotated-text">consummatory anhedonia in SZ</mark> (8 studies and 44 foci), decreased likelihood of activation was observed in left putamen and caudate head, pulvinar and right red nucleus (  p   &lt; 0.01, FDR corrected, cluster size &gt; 400 mm3; Table  …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …men, bilateral amygdala and anterior lobe, right IFG and left ACC, and increased activation was observed in middle occipital gyrus and fusiform gyrus. 


#### SZ 
  
For consummatory anhedonia in SZ (<mark class="annotated-text">8</mark> studies and 44 foci), decreased likelihood of activation was observed in left putamen and caudate head, pulvinar and right red nucleus (  p   &lt; 0.01, FDR corrected, cluster size &gt; 400 mm3; Table   an…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … 


### OT effects in healthy males and females 
  
Conjunction and subtraction analyses on ‘OT &gt; PL’ contrasts (male: 164 activation coordinates in 25 contrasts; female: 84 activation coordinates in <mark class="annotated-text">14</mark> contrasts) were conducted to reveal significant similarities as well as differences in brain activity increased by IN-OT between healthy males and females (this analysis was also only performed on he…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5647800/"
                                       >PMC5647800</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …see  ). For the STO condition, the single ALE map showed consistent activations in the bilateral IPL and additionally in the right PosCG and IOG, and left IFG, PreCG, ITG and fusiform (  and  ). When <mark class="annotated-text">adding studies using an EC paradigm</mark>, several additional clusters were found, including in the bilateral IPL, left AI, ITG, IFG and claustrum, and right PosCG, IOG, fusiform gyrus and SFG (see   for peak coordinate and ALE values). 

Wh…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6847411/"
                                       >PMC6847411</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA13 (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …tamen and caudate head, pulvinar and right red nucleus (  p   &lt; 0.01, FDR corrected, cluster size &gt; 400 mm3; Table   and Fig.  ). No areas with increased likelihood of activation were observed. 

For <mark class="annotated-text">anticipatory anhedonia in SZ</mark> (13 studies and 30 foci) decreased likelihood of activation was observed in left putamen, ACC, and mPFC and right caudate head. No areas with increased likelihood of activation were observed. 

For e…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ar and right red nucleus (  p   &lt; 0.01, FDR corrected, cluster size &gt; 400 mm3; Table   and Fig.  ). No areas with increased likelihood of activation were observed. 

For anticipatory anhedonia in SZ (<mark class="annotated-text">13</mark> studies and 30 foci) decreased likelihood of activation was observed in left putamen, ACC, and mPFC and right caudate head. No areas with increased likelihood of activation were observed. 

For emoti…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ncreased right amygdala activity (23.7/−1.7/−11,   k   = 128 mm ) was overlapped in males and females. Conjunction and subtraction analyses on ‘OT &lt; PL’ contrasts (male: 187 activation coordinates in <mark class="annotated-text">22</mark> contrasts; female: 39 activation coordinates in 13 contrasts) showed that IN-OT decreased brain activity in the right amygdala (extending to medial GP; 17.3/−4.2/−9.1,   k   = 656 mm , FDR   P   &lt;   …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5647800/"
                                       >PMC5647800</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ional clusters were found, including in the bilateral IPL, left AI, ITG, IFG and claustrum, and right PosCG, IOG, fusiform gyrus and SFG (see   for peak coordinate and ALE values). 

When running the <mark class="annotated-text">conjunction</mark> and subtraction analyses, results showed common and distinct patterns of activation for certain conditions. Conjunction analyses showed consistent activities in the bilateral IPL, left PreCG and righ…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6847411/"
                                       >PMC6847411</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">software-neuroelf (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Buhle, <mark class="annotated-text">Jason</mark> T and Silvers, Jennifer A and Wager, Tor D and Lopez, Richard and Onyemekwu, Chukwudi and Kober, Hedy and Weber, Jochen and Ochsner, Kevin N
Cerebral cortex (New York, N.Y. : 1991), 2015

# Title

Co…
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
                    …; Wager et al.,  ). 


### Multilevel Kernel Density Analysis (MKDA) 
  
We first converted all peak coordinates reported in Talairach space to MNI space (Lancaster et al.,  ), and imported them into <mark class="annotated-text">NeuroElf</mark>  to perform an MKDA. The coordinates were then smoothed using a 12-mm Gaussian kernel and combined to form a single map for each classified contrast, ensuring that contrasts reporting more coordinate…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5951926/"
                                       >PMC5951926</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tus of the target and reference (i.e. in-group or out-group), and coordinates of peak activation. 



## Data analysis 
  
MKDA (see   for more information) was implemented through the Matlab toolbox <mark class="annotated-text">NeuroElf</mark> ( ). Consistent with MKDA and neuroimaging meta-analytic procedures ( ;  ;  ), contrast coordinates in Talairach space were first converted to MNI space and then convolved using a smoothing kernel of…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8421705/"
                                       >PMC8421705</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #eeeeec;">
        <summary class="label-display">no-access (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Spets</mark>, Dylan S and Slotnick, Scott D
Cognitive neuroscience, 2021

# Title

Are there sex differences in brain activity during long-term memory? A systematic review and fMRI activation likelihood estimatio…
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
                    <mark class="annotated-text">Scheliga</mark>, Sebastian and Kellermann, Thilo and Lampert, Angelika and Rolke, Roman and Spehr, Marc and Habel, Ute
Reviews in the neurosciences, 2023

# Title

Neural correlates of multisensory integration in th…
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
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">N group-level stat maps included (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …fort-related costs and integrate them with rewards. We conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (23 studies, <mark class="annotated-text">15</mark> maps, 549 participants) and net value (15 studies, 11 maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedial prefronta…
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
                    … conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (23 studies, 15 maps, 549 participants) and net value (15 studies, <mark class="annotated-text">11</mark> maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedial prefrontal cortex (vmPFC) showed the opposite effect. Moreover,…
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
                    …th 677 participants (366 males, mean age 25.4 years) using a delay differential cue-conditioning paradigm were obtained. All studies reported a CS +  &gt; CS−, 19 of them also the opposite contrast. For <mark class="annotated-text">13</mark> of them, original empirical 3D statistical images were available [ ]. The entire data of fear conditioning have been published before in [ ]. 


### Meta-analytic procedure 
  
Functional activation …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10025232/"
                                       >PMC10025232</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">software-CluB (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …r a more detailed contrast characterization see the  . Further, all the Talairach coordinates were converted to MNI space through the Talairach to MNI (SPM) transformation implemented in the software <mark class="annotated-text">CluB</mark> (Clustering the Brain, see below). 

The final dataset included 474 participants (mean age = 27.35 ± 4) and 34 contrasts. 


##### Cluster analysis and cluster composition analysis: motor intention a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6473038/"
                                       >PMC6473038</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … first performed a HC analysis using the unique-solution clustering algorithm developed by Cattinelli et al. . This method is implemented in a suite of MATLAB (2014a MathWorks) and C++ scripts called <mark class="annotated-text">CluB</mark> (Clustering the Brain ). The CluB toolbox permits both to extract a set of spatially coherent clusters of activations from a database of stereotactic coordinates, and to explore each single cluster o…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8776875/"
                                       >PMC8776875</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">software-canlab mkda (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Fede</mark>, Samantha J and Kiehl, Kent A
Brain imaging and behavior, 2021

# Title

Meta-analysis of the moral brain: patterns of neural engagement assessed using multilevel kernel density analysis.

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
                    …elow), and 5) used targeted voxelwise reporting (n = 8, see below). 



### Data and code availability 
  
All data used in this project (coded foci of activation differences) are available in the  . <mark class="annotated-text">The MKDA code used to perform meta-analyses is freely available via CANLAB ( ). </mark>



## Results 
  
### Included Studies. 
  
See   for flow diagram and detailed information on study selection. The initial database search yielded a total of 2213 articles. Of these, 76 met initial …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7992390/"
                                       >PMC7992390</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">software-nimare (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Witt</mark>, Suzanne T and van Ettinger-Veenstra, Helene and Salo, Taylor and Riedel, Michael C and Laird, Angela R
Brain topography, 2021

# Title

What Executive Function Network is that? An Image-Based Meta-A…
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
                    …med a series of coordinate-based meta-analyses using the activation likelihood estimate (ALE) method. Meta-analysis was performed on whole-brain coordinates reported from 864 fMRI contrasts using the <mark class="annotated-text">NiMARE</mark> Python package, revealing convergence in medial prefrontal cortex, anterior cingulate cortex, posterior cingulate cortex, temporoparietal junction, bilateral insula, amygdala, fusiform gyrus, precune…
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
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - review (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Peyron, R and Laurent, B and García-Larrea, L
Neurophysiologie clinique = Clinical neurophysiology, 2001

# Title

<mark class="annotated-text">Functional</mark> imaging of brain responses to pain. A review and meta-analysis (2000).

# Keywords



# Abstract

Brain responses to pain, assessed through positron emission tomography (PET) and functional magnetic …
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
                    van Montfort, S.J.T. and van Dellen, E. and Stam, C.J. and Ahmad, A.H. and Mentink, L.J. and Kraan, C.W. and Zalesky, A. and Slooter, A.J.C.
Neuroimage Clin, 2019

# Title

<mark class="annotated-text">Brain network disintegration as a final common pathway for delirium: a systematic review and qualitative meta-analysis
</mark>
# Keywords

Delirium
Brain
Networks
Connectome
Aging
Cognitive impairment


# Abstract
 
Delirium is an acute neuropsychiatric syndrome characterized by altered levels of attention and awareness with…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6461601/"
                                       >PMC6461601</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">NO N studies included (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Zhu</mark>, Tingting and Wang, Zixu and Zhou, Chao and Fang, Xinyu and Huang, Chengbing and Xie, Chunming and Ge, Honglin and Yan, Zheng and Zhang, Xiangrong and Chen, Jiu
Front Psychiatry, 2022

# Title

Meta-…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">21</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9552970/"
                                       >PMC9552970</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Zhu, <mark class="annotated-text">Tingting</mark> and Wang, Zixu and Zhou, Chao and Fang, Xinyu and Huang, Chengbing and Xie, Chunming and Ge, Honglin and Yan, Zheng and Zhang, Xiangrong and Chen, Jiu
Front Psychiatry, 2022

# Title

Meta-analysis o…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">4</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9552970/"
                                       >PMC9552970</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Zhu, Tingting <mark class="annotated-text">and</mark> Wang, Zixu and Zhou, Chao and Fang, Xinyu and Huang, Chengbing and Xie, Chunming and Ge, Honglin and Yan, Zheng and Zhang, Xiangrong and Chen, Jiu
Front Psychiatry, 2022

# Title

Meta-analysis of st…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">6</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9552970/"
                                       >PMC9552970</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Zhu, Tingting and <mark class="annotated-text">Wang</mark>, Zixu and Zhou, Chao and Fang, Xinyu and Huang, Chengbing and Xie, Chunming and Ge, Honglin and Yan, Zheng and Zhang, Xiangrong and Chen, Jiu
Front Psychiatry, 2022

# Title

Meta-analysis of structu…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">5</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9552970/"
                                       >PMC9552970</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Zhu, Tingting and Wang, <mark class="annotated-text">Zixu</mark> and Zhou, Chao and Fang, Xinyu and Huang, Chengbing and Xie, Chunming and Ge, Honglin and Yan, Zheng and Zhang, Xiangrong and Chen, Jiu
Front Psychiatry, 2022

# Title

Meta-analysis of structural an…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">22</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9552970/"
                                       >PMC9552970</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA14 (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …Z (13 studies and 30 foci) decreased likelihood of activation was observed in left putamen, ACC, and mPFC and right caudate head. No areas with increased likelihood of activation were observed. 

For <mark class="annotated-text">emotional processing in SZ </mark>(6 studies and 39 foci), decreased likelihood of activation was observed in the right ventral lateral nucleus. No areas with increased likelihood of activation were observed. 




## Discussion 
  
Th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ecreased likelihood of activation was observed in left putamen, ACC, and mPFC and right caudate head. No areas with increased likelihood of activation were observed. 

For emotional processing in SZ (<mark class="annotated-text">6</mark> studies and 39 foci), decreased likelihood of activation was observed in the right ventral lateral nucleus. No areas with increased likelihood of activation were observed. 




## Discussion 
  
This…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838562/"
                                       >PMC4838562</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">algorithm-ABC (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …avioral reviews, 2022

# Title

The central autonomic system revisited - Convergent evidence for a regulatory role of the insular and midcingulate cortex from neuroimaging meta-analyses.

# Keywords

<mark class="annotated-text">ABC</mark> 
ALE 
Arousal 
Central autonomic system 
Cingulate cortex 
Cognition 
Coordinate-based 
Emotion 
Functional magnetic resonance imaging 
Insula 
Meta-analysis 
Parasympathetic 
Sympathetic 
fMRI 


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
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">algorithm-KDA (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Wager</mark>, Tor D and Jonides, John and Reading, Susan
NeuroImage, 2004

# Title

Neuroimaging studies of shifting attention: a meta-analysis.

# Keywords



# Abstract

This paper reports a meta-analysis of ne…
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
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">software-abc (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …avioral reviews, 2022

# Title

The central autonomic system revisited - Convergent evidence for a regulatory role of the insular and midcingulate cortex from neuroimaging meta-analyses.

# Keywords

<mark class="annotated-text">ABC</mark> 
ALE 
Arousal 
Central autonomic system 
Cingulate cortex 
Cognition 
Coordinate-based 
Emotion 
Functional magnetic resonance imaging 
Insula 
Meta-analysis 
Parasympathetic 
Sympathetic 
fMRI 


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
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">largescale-neurosynth MACM (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Bezdicek</mark>, Ondrej and Ballarini, Tommaso and Růžička, Filip and Roth, Jan and Mueller, Karsten and Jech, Robert and Schroeter, Matthias L
Neuropsychologia, 2019

# Title

Mild cognitive impairment disrupts att…
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
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">largescale-neuroquery encoding (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Antal</mark>, Botond and McMahon, Liam P and Sultan, Syed Fahad and Lithen, Andrew and Wexler, Deborah J and Dickerson, Bradford and Ratai, Eva-Maria and Mujica-Parodi, Lilianne R
eLife, 2022

# Title

Type 2 dia…
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
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - previous ma for seed / roi (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Kim, M Justin and Knodt, Annchen R and Hariri, Ahmad R
Soc Cogn Affect Neurosci, 2022

# Title

<mark class="annotated-text">Meta-analytic activation maps</mark> can help identify affective processes captured by contrast-based task fMRI: the case of threat-related facial expressions

# Keywords

fMRI
meta-analysis map
emotion
fear
anger
facial expression


# …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9433847/"
                                       >PMC9433847</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - not about the brain (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    von Eyben, Finn Edler and Kiljunen, Timo and Kangasmaki, Aki and Kairemo, Kalevi and von Eyben, Rie and Joensuu, Timo
Clinical genitourinary cancer, 2017

# Title

<mark class="annotated-text">Radiotherapy Boost for the Dominant Intraprostatic Cancer Lesion-A Systematic Review and Meta-Analysis.
</mark>
# Keywords

Diagnostic accuracy 
Functional magnetic resonance imaging 
Prostatic neoplasms 
Radiation injuries 
Survival 


# Abstract

External beam radiotherapy (EBRT) for prostate cancer can be p…
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
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">NO N contrasts included (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">N MAs (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - cites ma as justification (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - cites ma as consistent with findings (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - non-human focus (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - preprint (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - not a ma, doesn&#39;t fit other exclusion (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - ma not in title (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```