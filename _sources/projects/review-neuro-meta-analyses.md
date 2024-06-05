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
        <summary class="label-display">N studies included (479 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
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
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Rotge</mark>, Jean-Yves and Guehl, Dominique and Dilharreguy, Bixente and Cuny, Emmanuel and Tignol, Jean and Bioulac, Bernard and Allard, Michele and Burbaud, Pierre and Aouizerate, Bruno
Journal of psychiatry &amp;…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">8</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">algorithm-ALE (418 docs)</summary>
        
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
        <summary class="label-display">DONE (192 docs)</summary>
        
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
                    <mark class="annotated-text">Fusar</mark>-Poli, Paolo and Perez, Jorge and Broome, Matthew and Borgwardt, Stefan and Placentino, Anna and Caverzasi, Eduardo and Cortesi, Mariachiara and Veggiotti, Pierangelo and Politi, Peirluigi and Barale,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Fusar</mark>-Poli, Paolo and Perez, Jorge and Broome, Matthew and Borgwardt, Stefan and Placentino, Anna and Caverzasi, Eduardo and Cortesi, Mariachiara and Veggiotti, Pierangelo and Politi, Peirluigi and Barale,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Fusar</mark>-Poli, Paolo and Perez, Jorge and Broome, Matthew and Borgwardt, Stefan and Placentino, Anna and Caverzasi, Eduardo and Cortesi, Mariachiara and Veggiotti, Pierangelo and Politi, Peirluigi and Barale,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Niusha_Mirhakimi</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA1 (158 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …f working memory: a meta-analysis.

# Keywords



# Abstract

We performed meta-analyses on 60 neuroimaging (PET and fMRI) studies of working memory (WM), considering three types of storage material (<mark class="annotated-text">spatial</mark>, verbal, and object), three types of executive function (continuous updating of WM, memory for temporal order, and manipulation of information in WM), and interactions between material and executive …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s, several neuroimaging studies have investigated the neural correlates of guilt, but no meta-analyses have yet identified the most robust activation patterns. A systematic review of literature found <mark class="annotated-text">16</mark> functional magnetic resonance imaging studies with whole-brain analyses meeting the inclusion criteria, for a total of 325 participants and 135 foci of activation. A meta-analysis was then conducted …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … aim of our study was to perform a meta-analysis of whole-brain functional magnetic resonance imaging (fMRI) studies that compared adult healthy relatives of patients with schizophrenia and controls. <mark class="annotated-text">Twenty-one</mark> whole-brain fMRI studies were included (17 using cognitive tasks and four using emotional tasks), published between 2003 and 2013. These studies included 467 healthy relatives of patients with schizo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … vocal signals and task demands. The present meta-analysis was designed to disentangle this diversity of results by summarizing neuroimaging data in the vocal emotion perception literature. Data from <mark class="annotated-text">44</mark> experiments contrasting emotional and neutral voices was analyzed to assess brain areas involved in vocal affect perception in general, as well as depending on the type of voice signal (speech prosod…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …f results by summarizing neuroimaging data in the vocal emotion perception literature. Data from 44 experiments contrasting emotional and neutral voices was analyzed to assess brain areas involved in <mark class="annotated-text">vocal affect perception in general</mark>, as well as depending on the type of voice signal (speech prosody or vocalizations), the task demands (implicit or explicit attention to emotions), and the specific emotion perceived. Results reasses…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …bolic number processing, arithmetic, and mental rotation. We used Activation Likelihood Estimation (ALE) to construct quantitative meta-analytic maps synthesizing results from 83 neuroimaging papers (<mark class="annotated-text">24</mark>-31 studies/cognitive process). All three cognitive processes were found to activate bilateral parietal regions in and around the intraparietal sulcus (IPS); a finding consistent with shared processin…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    …s process effort-related costs and integrate them with rewards. We conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (<mark class="annotated-text">23</mark> studies, 15 maps, 549 participants) and net value (15 studies, 11 maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s process effort-related costs and integrate them with rewards. We conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (<mark class="annotated-text">23</mark> studies, 15 maps, 549 participants) and net value (15 studies, 11 maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s process effort-related costs and integrate them with rewards. We conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (<mark class="annotated-text">23</mark> studies, 15 maps, 549 participants) and net value (15 studies, 11 maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Niusha_Mirhakimi</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #babdb6;">
        <summary class="label-display">DONE (but did not look into full paper) (131 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">de</mark> la Vega, Alejandro and Yarkoni, Tal and Wager, Tor D and Banich, Marie T
Cerebral cortex (New York, N.Y. : 1991), 2019

# Title

Large-scale Meta-analysis Suggests Low Regional Modularity in Lateral …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Kronbichler</mark>, Lisa and Tschernegg, Melanie and Martin, Anna Isabel and Schurz, Matthias and Kronbichler, Martin
Schizophrenia bulletin, 2018

# Title

Abnormal Brain Activation During Theory of Mind Tasks in Schi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Van</mark> Overwalle, Frank and Baetens, Kris
NeuroImage, 2009

# Title

Understanding others&#39; actions and goals by mirror and mentalizing systems: a meta-analysis.

# Keywords



# Abstract

This meta-analysis…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Ma</mark>, Y
Molecular psychiatry, 2016

# Title

Neuropsychological mechanism underlying antidepressant effect: a systematic meta-analysis.

# Keywords



# Abstract

Antidepressants are widely used in clinic…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Rotge</mark>, Jean-Yves and Lemogne, Cedric and Hinfray, Sophie and Huguet, Pascal and Grynszpan, Ouriel and Tartour, Eric and George, Nathalie and Fossati, Philippe
Social cognitive and affective neuroscience, 2…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Filgueiras</mark>, Alberto and Quintas Conde, Erick Francisco and Hall, Craig R
Brain imaging and behavior, 2019

# Title

The neural basis of kinesthetic and visual imagery in sports: an ALE meta - analysis.

# Keywo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Pierce</mark>, Zachary P and Johnson, Emily R and Kim, Isabelle A and Lear, Brianna E and Mast, A Michaela and Black, Jessica M
Frontiers in psychology, 2023

# Title

Therapeutic interventions impact brain functi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Ma</mark>, Ning and Dinges, David F and Basner, Mathias and Rao, Hengyi
Sleep, 2015

# Title

How acute total sleep loss affects the attending brain: a meta-analysis of neuroimaging studies.

# Keywords

atten…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Kim</mark>, Hongkeun
Human brain mapping, 2013

# Title

Differential neural activity in the recognition of old versus new events: an activation likelihood estimation meta-analysis.

# Keywords



# Abstract

T…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">van</mark> Dun, Kim and Brinkmann, Pia and Depestele, Siel and Verstraelen, Stefanie and Meesen, Raf
Cerebellum (London, England), 2022

# Title

Cerebellar Activation During Simple and Complex Bimanual Coordin…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA2 (114 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Costa, <mark class="annotated-text">Cristiano</mark> and Cristea, Ioana Alina and Dal Bò, Elisa and Melloni, Caterina and Gentili, Claudio
Journal of child psychology and psychiatry, and allied disciplines, 2021

# Title

Brain activity during facial p…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Horn, Mathilde and Jardri, Renaud and D&#39;Hondt, Fabien and Vaiva, Guillaume and Thomas, Pierre and Pins, Delphine
Cognitive, affective &amp; behavioral neuroscience, 2016

# Title

<mark class="annotated-text">The</mark> multiple neural networks of familiarity: A meta-analysis of functional imaging studies.

# Keywords

Familiarity 
Limbic system 
Meta-analysis 
Parietal cortex 
Prefrontal cortex 
fMRI 


# Abstract
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
                    … memory: a meta-analysis.

# Keywords



# Abstract

We performed meta-analyses on 60 neuroimaging (PET and fMRI) studies of working memory (WM), considering three types of storage material (spatial, <mark class="annotated-text">verbal</mark>, and object), three types of executive function (continuous updating of WM, memory for temporal order, and manipulation of information in WM), and interactions between material and executive function…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … whole-brain functional magnetic resonance imaging (fMRI) studies that compared adult healthy relatives of patients with schizophrenia and controls. Twenty-one whole-brain fMRI studies were included (<mark class="annotated-text">17</mark> using cognitive tasks and four using emotional tasks), published between 2003 and 2013. These studies included 467 healthy relatives of patients with schizophrenia and 768 controls. To conduct the st…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …perception literature. Data from 44 experiments contrasting emotional and neutral voices was analyzed to assess brain areas involved in vocal affect perception in general, as well as depending on the <mark class="annotated-text">type of voice signal</mark> (speech prosody or vocalizations), the task demands (implicit or explicit attention to emotions), and the specific emotion perceived. Results reassessed a consistent bilateral network of Emotional Vo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ic number processing, arithmetic, and mental rotation. We used Activation Likelihood Estimation (ALE) to construct quantitative meta-analytic maps synthesizing results from 83 neuroimaging papers (24-<mark class="annotated-text">31</mark> studies/cognitive process). All three cognitive processes were found to activate bilateral parietal regions in and around the intraparietal sulcus (IPS); a finding consistent with shared processing a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    … rewards. We conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (23 studies, 15 maps, 549 participants) and net value (<mark class="annotated-text">15</mark> studies, 11 maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedial prefrontal cortex (vmPFC) showed the opposite effec…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … rewards. We conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (23 studies, 15 maps, 549 participants) and net value (<mark class="annotated-text">15</mark> studies, 11 maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedial prefrontal cortex (vmPFC) showed the opposite effec…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … rewards. We conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (23 studies, 15 maps, 549 participants) and net value (<mark class="annotated-text">15</mark> studies, 11 maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedial prefrontal cortex (vmPFC) showed the opposite effec…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Niusha_Mirhakimi</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">N studies found (98 docs)</summary>
        
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
                    <div class="extra-data">4</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Schizophrenia: A Meta-Analysis.

# Keywords

fMRI 
mentalizing 
psychosis 


# Abstract

Social cognition abilities are severely impaired in schizophrenia (SZ). The current meta-analysis used foci of <mark class="annotated-text">21</mark> individual studies on functional abnormalities in the schizophrenic brain in order to identify regions that reveal convergent under- or over-activation during theory of mind (TOM) tasks. Studies were…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">21</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …only marginally involved in social cognition and emotionality, with a few meta-analyses pointing to an involvement of at most 54% of the individual studies. In this study, novel meta-analyses of over <mark class="annotated-text">350</mark> fMRI studies, dividing up the domain of social cognition in homogeneous subdomains, confirmed this low involvement of the cerebellum in conditions that trigger the mirror network (e.g., when familiar…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">not precise n</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …arge-scale efforts to map the full range of psychological states across the entirety of LFC. Here, we used a data-driven approach to generate a comprehensive functional-anatomical mapping of LFC from <mark class="annotated-text">11 406</mark> neuroimaging studies. We identified putatively separable LFC regions on the basis of whole-brain co-activation, revealing 14 clusters organized into 3 whole-brain networks. Next, we generated functio…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ming disorder (IGD), and to explore the underpinning neuroscience basis of IGD. Yet, no available literature has systemically reviewed the fMRI studies of IGD using meta-analyses. This study reviewed <mark class="annotated-text">61</mark> candidate articles and finally selected 10 qualified voxel-wise whole-brain analysis studies for performing a comprehensive series of meta-analyses employing effect size signed differential mapping a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …-traumatic growth for adult trauma survivors. We utilized the following databases to conduct our systematic search: Boston College Libraries, PubMed, MEDLINE, and PsycINFO. Our initial search yielded <mark class="annotated-text">834</mark> studies for initial screening. We implemented seven eligibility criteria to vet articles for full-text review. Twenty-nine studies remained for full-text review after our systematic review process wa…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">834</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ducted separate comprehensive PUBMED (1990-May 2008) searches to find all functional magnetic resonance imaging studies using a variant of the emotional faces paradigm in healthy subjects. Out of the <mark class="annotated-text">551</mark> originally identified studies, 105 studies met inclusion criteria. The overall database consisted of 1785 brain coordinates which yield an overall sample of 1600 healthy subjects. We found no support…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rence (MD) of Fugl-Meyer Assessment (FMA) scores were pooled and the random-effects model method was used to perform the meta-analysis. The PRISMA criteria were followed in current review. A total of <mark class="annotated-text">897</mark> records were identified, eight single-group studies and 11 controlled-trial studies were included in our review. The systematic analysis indicated that the BCI-robot systems had a significant improve…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
        <summary class="label-display">MA3 (72 docs)</summary>
        
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
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Ji, <mark class="annotated-text">Shanling</mark> and Zhang, Yinghui and Chen, Nan and Liu, Xia and Li, Yongchao and Shao, Xuexiao and Yang, Zhengwu and Yao, Zhijun and Hu, Bin
Brain imaging and behavior, 2022

# Title

Shared increased entropy of b…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Klugah-Brown, <mark class="annotated-text">Benjamin</mark> and Zhou, Xinqi and Pradhan, Basant K and Zweerings, Jana and Mathiak, Klaus and Biswal, Bharat and Becker, Benjamin
Addiction biology, 2021

# Title

Common neurofunctional dysregulations characteri…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …eta-analysis.

# Keywords



# Abstract

We performed meta-analyses on 60 neuroimaging (PET and fMRI) studies of working memory (WM), considering three types of storage material (spatial, verbal, and <mark class="annotated-text">object</mark>), three types of executive function (continuous updating of WM, memory for temporal order, and manipulation of information in WM), and interactions between material and executive function. Analyses o…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tic resonance imaging (fMRI) studies that compared adult healthy relatives of patients with schizophrenia and controls. Twenty-one whole-brain fMRI studies were included (17 using cognitive tasks and <mark class="annotated-text">four</mark> using emotional tasks), published between 2003 and 2013. These studies included 467 healthy relatives of patients with schizophrenia and 768 controls. To conduct the statistical analysis, we used the…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …number processing, arithmetic, and mental rotation. We used Activation Likelihood Estimation (ALE) to construct quantitative meta-analytic maps synthesizing results from 83 neuroimaging papers (24-31 <mark class="annotated-text">studies</mark>/cognitive process). All three cognitive processes were found to activate bilateral parietal regions in and around the intraparietal sulcus (IPS); a finding consistent with shared processing accounts.…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …emotional and neutral voices was analyzed to assess brain areas involved in vocal affect perception in general, as well as depending on the type of voice signal (speech prosody or vocalizations), the <mark class="annotated-text">task demands</mark> (implicit or explicit attention to emotions), and the specific emotion perceived. Results reassessed a consistent bilateral network of Emotional Voices Areas consisting of the superior temporal corte…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …identify overlapping brain regions. In total 303 articles were included: 53 for FTD (n = 1153 patients, 42.5% female; 1337 controls, 53.8% female), 28 for music perception (n = 540, 51.8% female) and <mark class="annotated-text">222</mark> for social cognition in controls (n = 5664, 50.2% female). We observed considerable overlap in atrophy patterns associated with FTD, and functional activation associated with music perception and soc…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …on differences. A whole-brain activation likelihood estimation based meta-analysis was conducted on fMRI studies that examined episodic memory in HOA (n = 200), MCI (n = 131), and AD populations (n = <mark class="annotated-text">89</mark>; total n = 409). Diffuse activation was exhibited in the HOA sample, while activation was more limited in the clinical populations. Additionally, the HOA sample showed more activation in the right hi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">N contrasts included (71 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …years, raising the need for an integrative understanding of the literature. The present study performed a quantitative meta-analysis of the data to fulfill that need. The meta-analysis focused on the <mark class="annotated-text">three</mark> most widely used types of activation contrast: Hit &gt; Miss, Intact &gt; Rearranged, and Memory &gt; Perception. The major results were as follows. First, the Hit &gt; Miss contrast mainly involved regions in t…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">3</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …gdala interact in emotion processing. However, no meta-analyses have focused on studies that reported concurrent vmPFC and amygdala activities. With activation likelihood estimation (ALE) we examined <mark class="annotated-text">100</mark> experiments that reported concurrent vmPFC and amygdala activities, and distinguished responses to positive vs. negative emotions and to passive exposure to vs. active regulation of emotions. We also…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … vocal signals and task demands. The present meta-analysis was designed to disentangle this diversity of results by summarizing neuroimaging data in the vocal emotion perception literature. Data from <mark class="annotated-text">44</mark> experiments contrasting emotional and neutral voices was analyzed to assess brain areas involved in vocal affect perception in general, as well as depending on the type of voice signal (speech prosod…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …and fear-related limbic regions. Thus, discovering such therapy-associated neural changes might point to relevant mechanisms of action. Using AES-SDM, we conducted a coordinate-based meta-analysis of <mark class="annotated-text">22</mark> whole-brain datasets (n = 419 anxiety patients) from 18 studies identified by our systematic literature search following PRISMA criteria (preregistration available at OSF: https://osf.io/dgc4p). In t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    …r differences amongst morality tasks are the cause for such heterogeneous findings. Therefore, in the present study, a series of activation likelihood estimation (ALE) meta-analyses were conducted on <mark class="annotated-text">123</mark> datasets (inclusive of 1963 participants) to address this question. The ALE meta-analyses revealed a series of common brain areas associated with all moral tasks, including medial prefrontal cortex, …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …r differences amongst morality tasks are the cause for such heterogeneous findings. Therefore, in the present study, a series of activation likelihood estimation (ALE) meta-analyses were conducted on <mark class="annotated-text">123</mark> datasets (inclusive of 1963 participants) to address this question. The ALE meta-analyses revealed a series of common brain areas associated with all moral tasks, including medial prefrontal cortex, …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …r differences amongst morality tasks are the cause for such heterogeneous findings. Therefore, in the present study, a series of activation likelihood estimation (ALE) meta-analyses were conducted on <mark class="annotated-text">123</mark> datasets (inclusive of 1963 participants) to address this question. The ALE meta-analyses revealed a series of common brain areas associated with all moral tasks, including medial prefrontal cortex, …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Niusha_Mirhakimi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …available fMRI data is now possible to extract the most relevant information. Using the Activation Likelihood Estimation method, we therefore conducted such a meta-analysis on 9 studies, representing <mark class="annotated-text">27</mark> neuroimaging contrasts and 131 participants. We identified a network composed of brain areas underlying the cognitive abilities required for driving: sensorimotor coordination, sensory and attentiona…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
            
        </div>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">exclude (62 docs)</summary>
        
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
                    <mark class="annotated-text">Fusar</mark>-Poli, Paolo and Perez, Jorge and Broome, Matthew and Borgwardt, Stefan and Placentino, Anna and Caverzasi, Eduardo and Cortesi, Mariachiara and Veggiotti, Pierangelo and Politi, Peirluigi and Barale,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Neumann</mark>, Jane and Turner, Robert and Fox, Peter T and Lohmann, Gabriele
NeuroImage, 2011

# Title

Exploring functional relations between brain regions from fMRI meta-analysis data: comments on Ramsey, Spirt…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Fusar</mark>-Poli, Paolo and Perez, Jorge and Broome, Matthew and Borgwardt, Stefan and Placentino, Anna and Caverzasi, Eduardo and Cortesi, Mariachiara and Veggiotti, Pierangelo and Politi, Peirluigi and Barale,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Fusar</mark>-Poli, Paolo and Perez, Jorge and Broome, Matthew and Borgwardt, Stefan and Placentino, Anna and Caverzasi, Eduardo and Cortesi, Mariachiara and Veggiotti, Pierangelo and Politi, Peirluigi and Barale,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    Yuan, <mark class="annotated-text">Rui</mark> and Biswal, Bharat B and Zaborszky, Laszlo
Cerebral cortex (New York, N.Y. : 1991), 2020

# Title

Functional Subdivisions of Magnocellular Cell Groups in Human Basal Forebrain: Test-Retest Resting-S…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Cañete-Massé, <mark class="annotated-text">Cristina</mark> and Carbó-Carreté, María and Peró-Cebollero, Maribel and Guàrdia-Olmos, Joan
Brain connectivity, 2021

# Title

Task-Related Brain Connectivity Activation Functional Magnetic Resonance Imaging in Int…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">thresholding (48 docs)</summary>
        
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
                    …rs-fMRI studies, which included a total of 14 experiments, 67 activation foci, and 1383 subjects. We tested the convergence across their findings by using the activation likelihood estimation method. <mark class="annotated-text">P-value maps were corrected by using cluster-level family-wise error p &lt; 0.05 and permuting 2000 times. </mark>Results showed that patients with different psychiatric disorders shared commonly increased entropy of brain signals in the left inferior and middle frontal gyri, and the right fusiform gyrus, cuneus,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rs-fMRI studies, which included a total of 14 experiments, 67 activation foci, and 1383 subjects. We tested the convergence across their findings by using the activation likelihood estimation method. <mark class="annotated-text">P-value maps were corrected by using cluster-level family-wise error p &lt; 0.05 and permuting 2000 times. </mark>Results showed that patients with different psychiatric disorders shared commonly increased entropy of brain signals in the left inferior and middle frontal gyri, and the right fusiform gyrus, cuneus,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rs-fMRI studies, which included a total of 14 experiments, 67 activation foci, and 1383 subjects. We tested the convergence across their findings by using the activation likelihood estimation method. <mark class="annotated-text">P-value maps were corrected by using cluster-level family-wise error p &lt; 0.05 and permuting 2000 times. </mark>Results showed that patients with different psychiatric disorders shared commonly increased entropy of brain signals in the left inferior and middle frontal gyri, and the right fusiform gyrus, cuneus,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <mark class="annotated-text">Yuan</mark>, Rui and Biswal, Bharat B and Zaborszky, Laszlo
Cerebral cortex (New York, N.Y. : 1991), 2020

# Title

Functional Subdivisions of Magnocellular Cell Groups in Human Basal Forebrain: Test-Retest Rest…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #4e9a06;">
        <summary class="label-display">has prisma chart (44 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … of action. Using AES-SDM, we conducted a coordinate-based meta-analysis of 22 whole-brain datasets (n = 419 anxiety patients) from 18 studies identified by our systematic literature search following <mark class="annotated-text">PRISMA</mark> criteria (preregistration available at OSF: https://osf.io/dgc4p). In these studies, fMRI data was collected in response to negative stimuli during cognitive-emotional tasks before and after psychoth…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … studies were included for the meta-analysis. The mean difference (MD) of Fugl-Meyer Assessment (FMA) scores were pooled and the random-effects model method was used to perform the meta-analysis. The <mark class="annotated-text">PRISMA</mark> criteria were followed in current review. A total of 897 records were identified, eight single-group studies and 11 controlled-trial studies were included in our review. The systematic analysis indic…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA4 (41 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Yeung, Andy Wai <mark class="annotated-text">Kan</mark>
Public health nutrition, 2021

# Title

Brain responses to watching food commercials compared with nonfood commercials: a meta-analysis on neuroimaging studies.

# Keywords

Child obesity 
Food comme…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …performed meta-analyses on 60 neuroimaging (PET and fMRI) studies of working memory (WM), considering three types of storage material (spatial, verbal, and object), three types of executive function (<mark class="annotated-text">continuous updating of WM</mark>, memory for temporal order, and manipulation of information in WM), and interactions between material and executive function. Analyses of material type showed the expected dorsal-ventral dissociation…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …olved in vocal affect perception in general, as well as depending on the type of voice signal (speech prosody or vocalizations), the task demands (implicit or explicit attention to emotions), and the <mark class="annotated-text">specific emotion perceived.</mark> Results reassessed a consistent bilateral network of Emotional Voices Areas consisting of the superior temporal cortex and primary auditory regions. Specific activations and lateralization of these r…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …in atrophy patterns associated with FTD, and functional activation associated with music perception and social cognition, mostly encompassing the ventral language network. We further observed overlap <mark class="annotated-text">across all three modalities</mark> in mesolimbic, basal forebrain and striatal regions. The results of our meta-analysis suggest that music perception and social cognition share neurobiological circuits that are affected in FTD. This …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <mark class="annotated-text">Fusar</mark>-Poli, Paolo and Perez, Jorge and Broome, Matthew and Borgwardt, Stefan and Placentino, Anna and Caverzasi, Eduardo and Cortesi, Mariachiara and Veggiotti, Pierangelo and Politi, Peirluigi and Barale,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Fusar</mark>-Poli, Paolo and Perez, Jorge and Broome, Matthew and Borgwardt, Stefan and Placentino, Anna and Caverzasi, Eduardo and Cortesi, Mariachiara and Veggiotti, Pierangelo and Politi, Peirluigi and Barale,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">NO N studies found (30 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">van</mark> Veluw, Susanne J and Chance, Steven A
Brain imaging and behavior, 2014

# Title

Differentiating between self and others: an ALE meta-analysis of fMRI studies of self-recognition and theory of mind.
…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
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
            
        </div>
        
    </details>
    
    <details style="--label-color: #eeeeec;">
        <summary class="label-display">read later (28 docs)</summary>
        
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #eeeeec;">
        <summary class="label-display">ask about this one (28 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Neumann</mark>, Jane and Turner, Robert and Fox, Peter T and Lohmann, Gabriele
NeuroImage, 2011

# Title

Exploring functional relations between brain regions from fMRI meta-analysis data: comments on Ramsey, Spirt…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Tench, C R and Tanasescu, Radu and Constantinescu, C S and Auer, D P and Cottam, W J
<mark class="annotated-text">NeuroImage</mark>, 2018

# Title

Coordinate based random effect size meta-analysis of neuroimaging studies.

# Keywords

Functional MRI 
Meta-analysis 
Neuroimaging 
Voxel based morphometry 


# Abstract

Low power i…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Kim, Hongkeun
Human brain mapping, 2018

# Title

Brain regions that show repetition suppression and enhancement: A meta-analysis of <mark class="annotated-text">137</mark> neuroimaging experiments.

# Keywords

fMRI 
memory 
meta-analysis 
neural networks 
repetition priming 


# Abstract

Repetition suppression and enhancement refer to the reduction and increase in th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Dugré, Jules R and Dumais, Alexandre and Bitar, Nathalie and Potvin, Stéphane
PeerJ, 2022

# Title

Loss anticipation and outcome during <mark class="annotated-text">the</mark> 

# Keywords

Loss avoidance 
Meta-analysis 
Monetary Incentive Delay Task 
Punishment 
fMRI 


# Abstract

Reward seeking and avoidance of punishment are key motivational processes. Brain-imaging st…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Wager, Tor D and Smith, Edward E
Cognitive, affective &amp; behavioral neuroscience, 2004

# Title

Neuroimaging studies of working memory: a meta-analysis.

# Keywords



# <mark class="annotated-text">Abstract</mark>

We performed meta-analyses on 60 neuroimaging (PET and fMRI) studies of working memory (WM), considering three types of storage material (spatial, verbal, and object), three types of executive funct…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …oscience, 2018

# Title

Is the voice an auditory face? An ALE meta-analysis comparing vocal and facial emotion processing.

# Keywords

PET 
affective 
auditory 
fMRI 
nonverbal 
social 
visual 


# <mark class="annotated-text">Abstract</mark>

This meta-analysis compares the brain structures and mechanisms involved in facial and vocal emotion recognition. Neuroimaging studies contrasting emotional with neutral (face: N = 76, voice: N = 34…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … &amp; behavioral neuroscience, 2023

# Title

Disentangling emotional signals in the brain: an ALE meta-analysis of vocal affect perception.

# Keywords

Brain 
Emotion 
Neuroimaging 
Prosody 
fMRI 


# <mark class="annotated-text">Abstract</mark>

Recent advances in neuroimaging research on vocal emotion perception have revealed voice-sensitive areas specialized in processing affect. Experimental data on this subject is varied, investigating …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Corrigendum: Brain networks of perceptual decision-making: an fMRI ALE meta-analysis.

# Keywords

GingerALE 
corrigendum 
decision-making 
fronto-parietal-basal ganglia 
meta-analysis 


# Abstract

<mark class="annotated-text">[This corrects the article on p. 445 in vol. 8, PMID: 24994979.]. </mark>

                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ng its neuroanatomy remain controversial. In this work, we used coordinate-based activation-likelihood estimations to merge available fMRI data on non-literal language. A literature search identified <mark class="annotated-text">38 fMRI studies on non-literal language (24 metaphor studies, 14 non-salient stimuli studies, 7 idiom studies, 8 irony studies, and 1 metonymy study)</mark>. Twenty-eight studies with direct comparisons of non-literal and literal studies were included in the main meta-analysis. Sub-analyses for metaphors, idioms, irony, salient metaphors, and non-salient…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …eta-analysis 
Open monitoring 


# Abstract

Meditation is a family of mental practices that encompasses a wide array of techniques employing distinctive mental strategies. We systematically reviewed <mark class="annotated-text">78</mark> functional neuroimaging (fMRI and PET) studies of meditation, and used activation likelihood estimation to meta-analyze 257 peak foci from 31 experiments involving 527 participants. We found reliably…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <mark class="annotated-text">Buhle</mark>, Jason T and Silvers, Jennifer A and Wager, Tor D and Lopez, Richard and Onyemekwu, Chukwudi and Kober, Hedy and Weber, Jochen and Ochsner, Kevin N
Cerebral cortex (New York, N.Y. : 1991), 2015

# Ti…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    …ion of underling pathophysiological mechanisms of the clinical triad including motor, cognitive and psychiatric impairment in Huntington&#39;s Disease (HD). We performed a voxel-based meta-analysis using <mark class="annotated-text">anisotropic effect size-signed differential mapping</mark> (AES-SDM) method. 6 studies (78 symptomatic HD, 102 premanifest HD and 131 healthy controls) were included in total. Altered resting-state brain activity was primarily detected in the bilateral media…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ion of underling pathophysiological mechanisms of the clinical triad including motor, cognitive and psychiatric impairment in Huntington&#39;s Disease (HD). We performed a voxel-based meta-analysis using <mark class="annotated-text">anisotropic effect size-signed differential mapping</mark> (AES-SDM) method. 6 studies (78 symptomatic HD, 102 premanifest HD and 131 healthy controls) were included in total. Altered resting-state brain activity was primarily detected in the bilateral media…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ion of underling pathophysiological mechanisms of the clinical triad including motor, cognitive and psychiatric impairment in Huntington&#39;s Disease (HD). We performed a voxel-based meta-analysis using <mark class="annotated-text">anisotropic effect size-signed differential mapping</mark> (AES-SDM) method. 6 studies (78 symptomatic HD, 102 premanifest HD and 131 healthy controls) were included in total. Altered resting-state brain activity was primarily detected in the bilateral media…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    … to functional neural changes in prefrontal control areas and fear-related limbic regions. Thus, discovering such therapy-associated neural changes might point to relevant mechanisms of action. Using <mark class="annotated-text">AES-SDM</mark>, we conducted a coordinate-based meta-analysis of 22 whole-brain datasets (n = 419 anxiety patients) from 18 studies identified by our systematic literature search following PRISMA criteria (preregis…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    …der (rMDD) and MDD present common or distinct neuropathological mechanisms remains unclear. We performed a meta-analysis of task-related whole-brain functional magnetic resonance imaging (fMRI) using <mark class="annotated-text">anisotropic effect-size signed differential mapping</mark> software to compare brain activation between rMDD/MDD patients and healthy controls (HCs). We included 18 rMDD studies (458 patients and 476 HCs) and 120 MDD studies (3746 patients and 3863 HCs). The…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA5 (24 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …60 neuroimaging (PET and fMRI) studies of working memory (WM), considering three types of storage material (spatial, verbal, and object), three types of executive function (continuous updating of WM, <mark class="annotated-text">memory for temporal order</mark>, and manipulation of information in WM), and interactions between material and executive function. Analyses of material type showed the expected dorsal-ventral dissociation between spatial and nonspa…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">software-none-or-unclear (21 docs)</summary>
        
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
                    <mark class="annotated-text">Klugah</mark>-Brown, Benjamin and Zhou, Xinqi and Pradhan, Basant K and Zweerings, Jana and Mathiak, Klaus and Biswal, Bharat and Becker, Benjamin
Addiction biology, 2021

# Title

Common neurofunctional dysregula…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">algorithm-other ma method (19 docs)</summary>
        
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    … However, how music listening engages brain functional networks remains elusive due to inconsistent results from previous findings. A meta-analysis of functional magnetic resonance imaging data using <mark class="annotated-text">seed-based d mapping (SDM) with permutation of subject images</mark> was performed. Studies that presented music listening paradigms to healthy individuals were included. Subgroup analyses were performed to investigate the effects of music genres on brain activation. …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … However, how music listening engages brain functional networks remains elusive due to inconsistent results from previous findings. A meta-analysis of functional magnetic resonance imaging data using <mark class="annotated-text">seed-based d mapping (SDM) with permutation of subject images</mark> was performed. Studies that presented music listening paradigms to healthy individuals were included. Subgroup analyses were performed to investigate the effects of music genres on brain activation. …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … However, how music listening engages brain functional networks remains elusive due to inconsistent results from previous findings. A meta-analysis of functional magnetic resonance imaging data using <mark class="annotated-text">seed-based d mapping (SDM) with permutation of subject images</mark> was performed. Studies that presented music listening paradigms to healthy individuals were included. Subgroup analyses were performed to investigate the effects of music genres on brain activation. …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    …, analyses on regions-of-interest). We aimed to conduct a meta-analysis of whole-brain fMRI studies on antisocial individuals based on distinct neurocognitive domains. A voxel-based meta-analysis via <mark class="annotated-text">permutation of subject images (SDM-PSI) </mark>was performed on studies using fMRI tasks in the domains of acute threat response, cognitive control, social cognition, punishment and reward processing. Overall, 83 studies were retrieved. Using a li…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    … until June 15, 2019 and updated on March 20, 2020. This protocol will follow the Preferred Reporting Items for Systematic review and Meta-Analysis Protocols (PRISMA-P). The Seed-based d Mapping with <mark class="annotated-text">Permutation of Subject Images (SDM-PSI)</mark> software will be used for this voxel-wise meta-analysis. This meta-analysis will identify the most consistent ReHo alterations in CP. To our knowledge, this will be the first voxel-wise meta-analysis…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA6 (17 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … studies of working memory (WM), considering three types of storage material (spatial, verbal, and object), three types of executive function (continuous updating of WM, memory for temporal order, and<mark class="annotated-text"> manipulation of information in WM</mark>), and interactions between material and executive function. Analyses of material type showed the expected dorsal-ventral dissociation between spatial and nonspatial storage in the posterior cortex, b…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    …ponent regions each exhibit distinct, but partially overlapping functional profiles. To date, there has been minimal effort to disentangle the functions of these regions. In the present study, we use <mark class="annotated-text">Neurosynth ( http://neurosynth.org ) to conduct an unbiased meta-analysis of the PMC based on fMRI coactivation and semantic information extracted from 11,406 studies. </mark>Our analyses revealed six PMC clusters with distinct functional profiles: superior and inferior dorsal PCC, anterior and posterior PrC, ventral PCC, and RSC. We discuss these findings in the context o…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    …corporating observations from 3401 adult patients and 3238 healthy participants was performed by seed-based d mapping. Brain maps were subjected to meta-analytic connectivity modeling and data-driven <mark class="annotated-text">functional decoding </mark>analyses to identify associated neural circuit alterations and relations to behavioral dimensions. Both groups exhibited hypoactivated abnormalities in the left inferior parietal lobule, and altered c…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">algorithm-ES-SDM (14 docs)</summary>
        
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">NO N studies included (10 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Zhou</mark>, Chendan and Zhuang, Yong and Lin, Xingjie and Michelson, Alan D and Zhang, Aijun
British journal of haematology, 2020

# Title

Changes in neurocognitive function and central nervous system structur…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Daigle</mark>, Katrina M and Pietrzykowski, Malvina O and Waters, Abigail B and Swenson, Lance P and Gansler, David A
The Journal of neuropsychiatry and clinical neurosciences, 2022

# Title

Central Executive Net…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Chase</mark>, Henry W and Clos, Mareike and Dibble, Sofia and Fox, Peter and Grace, Anthony A and Phillips, Mary L and Eickhoff, Simon B
NeuroImage, 2016

# Title

Evidence for an anterior-posterior differentiati…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Fernández</mark>-Alvarez, J and Grassi, M and Colombo, D and Botella, C and Cipresso, P and Perna, G and Riva, G
Psychological medicine, 2022

# Title

Efficacy of bio- and neurofeedback for depression: a meta-analys…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Amanzio</mark>, Martina and Benedetti, Fabrizio and Porro, Carlo A and Palermo, Sara and Cauda, Franco
Human brain mapping, 2013

# Title

Activation likelihood estimation meta-analysis of brain correlates of place…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …l connections between musical rhythm and linguistic syntax, suggesting that these abilities may be mediated by common neural resources. Here, we performed a quantitative meta-analysis of neuroimaging <mark class="annotated-text">studies</mark> using activation likelihood estimate (ALE) to localize the shared neural structures engaged in a representative set of musical rhythm (rhythm, beat, and meter) and linguistic syntax (merge movement, …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ere we aimed at studying how the brain activation patterns related to value of &#34;wanted&#34; stimuli differs from that of &#34;needed&#34; stimuli using activation likelihood estimation neuroimaging meta-analysis <mark class="annotated-text">approaches</mark>. We used the perception of a cue predicting a reward for &#34;wanting&#34; related value and the perception of food stimuli in a hungry state as a model for &#34;needing&#34; related value. We carried out separate, …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …te a differential role of the anterior and posterior cerebellum depending on the complexity of the coordination. An activation likelihood estimation (ALE) meta-analysis was used combining the data of <mark class="annotated-text">several</mark> functional MRI studies involving bimanual coordination tasks with varying complexities to unravel the involvement of the different areas of the cerebellum in simple and complex bimanual coordination.…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …shed meta-analytic technique and use ultra-high field, high-resolution functional and structural neuroimaging to examine hippocampal lateralization with consideration for a long-axis differentiation. <mark class="annotated-text">Data</mark> revealed strong support for an evolutionarily preserved hemispheric specialization. Specifically, we found intra- and interhemispheric differences with regard to anterior and posterior functional and…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
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
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA7 (10 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ly with demand for manipulation (including dual-task requirements or mental operations). BA 7, in the posterior parietal cortex, is involved in all types of executive function. Finally, we consider a <mark class="annotated-text">potential fourth executive function</mark>: selective attention to features of a stimulus to be stored in WM, which leads to increased probability of activating the medial prefrontal cortex (BA 32) in storage tasks. 

                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <mark class="annotated-text">Chrastil</mark>, Elizabeth R and Tobyne, Sean M and Nauer, Rachel K and Chang, Allen E and Stern, Chantal E
Behavioral neuroscience, 2018

# Title

Converging meta-analytic and connectomic evidence for functional su…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    …Direct comparison of aversive anticipation studies using tactile versus visual stimuli identified additional regions involved in sensory specific aversive anticipation across these sensory modalities.<mark class="annotated-text"> Results from complementary multi-study voxel-wise and NeuroSynth analyses generally provide converging evidence for a core circuit involved in aversive anticipation. </mark>The multi-study voxel-wise analyses also implicate a more widespread preparatory response across sensory, motor, and cognitive control regions during more prolonged periods of aversive anticipation. T…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">largescale-brainmap decoding (9 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Yeung, Andy <mark class="annotated-text">Wai</mark> Kan
Public health nutrition, 2021

# Title

Brain responses to watching food commercials compared with nonfood commercials: a meta-analysis on neuroimaging studies.

# Keywords

Child obesity 
Food c…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Cañete-Massé, <mark class="annotated-text">Cristina</mark> and Carbó-Carreté, María and Peró-Cebollero, Maribel and Guàrdia-Olmos, Joan
Brain connectivity, 2021

# Title

Task-Related Brain Connectivity Activation Functional Magnetic Resonance Imaging in Int…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
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
                    … language comprehension in human children. Our analysis included 27 independent experiments involving n ​= ​625 children (49% girls) with a mean age of 8.9 years. Activation likelihood estimation and <mark class="annotated-text">seed-based effect size mapping</mark> revealed activation peaks in the pars triangularis of the left inferior frontal gyrus and bilateral superior and middle temporal gyri. In contrast to this distribution of activation in children, prev…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … language comprehension in human children. Our analysis included 27 independent experiments involving n ​= ​625 children (49% girls) with a mean age of 8.9 years. Activation likelihood estimation and <mark class="annotated-text">seed-based effect size mapping</mark> revealed activation peaks in the pars triangularis of the left inferior frontal gyrus and bilateral superior and middle temporal gyri. In contrast to this distribution of activation in children, prev…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … language comprehension in human children. Our analysis included 27 independent experiments involving n ​= ​625 children (49% girls) with a mean age of 8.9 years. Activation likelihood estimation and <mark class="annotated-text">seed-based effect size mapping</mark> revealed activation peaks in the pars triangularis of the left inferior frontal gyrus and bilateral superior and middle temporal gyri. In contrast to this distribution of activation in children, prev…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    …distinct aspects of emotion processing, we applied an emergent meta-analytic clustering approach to the extensive body of affective neuroimaging results archived in the BrainMap database. Specifically<mark class="annotated-text">, we performed hierarchical clustering on the modeled activation maps from 1,747 experiments in the affective processing domain, </mark>resulting in five meta-analytic groupings of experiments demonstrating whole-brain recruitment. Behavioral inference analyses conducted for each of these groupings suggested dissociable networks suppo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - not a full report (9 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">Zang</mark>, Yu-Feng and Zuo, Xi-Nian and Milham, Michael and Hallett, Mark
BioMed research international, 2016

# Title

Toward a Meta-Analytic Synthesis of the Resting-State fMRI Literature for Clinical Popula…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Gao, Rong and <mark class="annotated-text">Wang</mark>, Ping and Zhou, Sheng and Yao, Hongyan
Asian journal of surgery, 2023

# Title

Resting-state fMRI study of vulnerable brain regions in patients with end-stage renal disease: An activation likelihood…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Cañete-Massé, Cristina and Carbó-Carreté, María and Peró-Cebollero, Maribel and Guàrdia-Olmos, Joan
Brain <mark class="annotated-text">connectivity</mark>, 2021

# Title

Task-Related Brain Connectivity Activation Functional Magnetic Resonance Imaging in Intellectual Disability Population: A Meta-Analytic Study.

# Keywords

cognitive task 
fMRI 
intel…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
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
        <summary class="label-display">MA8 (8 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ing three types of storage material (spatial, verbal, and object), three types of executive function (continuous updating of WM, memory for temporal order, and manipulation of information in WM), and <mark class="annotated-text">interactions between material and executive function.</mark> Analyses of material type showed the expected dorsal-ventral dissociation between spatial and nonspatial storage in the posterior cortex, but not in the frontal cortex. Some support was found for lef…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
        <summary class="label-display">software-brainmap (8 docs)</summary>
        
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
                    <mark class="annotated-text">Zald</mark>, David H and McHugo, Maureen and Ray, Kimberly L and Glahn, David C and Eickhoff, Simon B and Laird, Angela R
Cerebral cortex (New York, N.Y. : 1991), 2014

# Title

Meta-analytic connectivity modeli…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">software-other (8 docs)</summary>
        
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    Hétu, <mark class="annotated-text">Sébastien</mark> and Grégoire, Mathieu and Saimpont, Arnaud and Coll, Michel-Pierre and Eugène, Fanny and Michon, Pierre-Emmanuel and Jackson, Philip L
Neuroscience and biobehavioral reviews, 2014

# Title

The neura…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    Xu, Min and <mark class="annotated-text">Xu</mark>, Guiping and Yang, Yang
Frontiers in behavioral neuroscience, 2020

# Title

Neural Systems Underlying Emotional and Non-emotional Interference Processing: An ALE Meta-Analysis of Functional Neuroima…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <mark class="annotated-text">Gong</mark>, Jiaying and Wang, Junjing and Chen, Pan and Qi, Zhangzhang and Luo, Zhenye and Wang, Jurong and Huang, Li and Wang, Ying
Journal of affective disorders, 2021

# Title

Large-scale network abnormalit…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <mark class="annotated-text">Giehl</mark>, Kathrin and Tahmasian, Masoud and Eickhoff, Simon B and van Eimeren, Thilo
Parkinsonism &amp; related disorders, 2020

# Title

Imaging executive functions in Parkinson&#39;s disease: An activation likeliho…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    Schumer, <mark class="annotated-text">Maya</mark> C and Chase, Henry W and Rozovsky, Renata and Eickhoff, Simon B and Phillips, Mary L
Molecular psychiatry, 2023

# Title

Prefrontal, parietal, and limbic condition-dependent differences in bipolar d…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">IMBA (5 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … unclear. Here, we systematically reviewed functional magnetic resonance studies that used emotion processing task paradigms in FEP patients, and in people at clinical high-risk for psychosis (CHRp). <mark class="annotated-text">Image-based meta-analyses</mark> with Seed-based d Mapping on available studies (n = 6) were also performed. Compared to controls, FEP patients showed decreased neural responses to emotion, particularly in the amygdala and anterior …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
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
                    …erefore, the aim here was to perform a meta-analysis of the existing literature using unthresholded statistical maps from previous studies. A voxelwise seed-based d mapping meta-analysis was performed<mark class="annotated-text"> using t-maps from studies</mark> comparing patients with OCD and healthy control subjects (HCs) during error processing and inhibitory control. For the error processing analysis, 239 patients with OCD (120 male; 79 medicated) and 22…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …erefore, the aim here was to perform a meta-analysis of the existing literature using unthresholded statistical maps from previous studies. A voxelwise seed-based d mapping meta-analysis was performed<mark class="annotated-text"> using t-maps from studies</mark> comparing patients with OCD and healthy control subjects (HCs) during error processing and inhibitory control. For the error processing analysis, 239 patients with OCD (120 male; 79 medicated) and 22…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …erefore, the aim here was to perform a meta-analysis of the existing literature using unthresholded statistical maps from previous studies. A voxelwise seed-based d mapping meta-analysis was performed<mark class="annotated-text"> using t-maps from studies</mark> comparing patients with OCD and healthy control subjects (HCs) during error processing and inhibitory control. For the error processing analysis, 239 patients with OCD (120 male; 79 medicated) and 22…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    …ine consistency of network topography within and across these labels. We hypothesized finding considerable overlap in the spatial topography among the neural networks associated with these labels. An <mark class="annotated-text">image-based meta-analysis</mark> was performed on 158 group-level statistical maps (SPMs) received from authors of 69 papers listed on PubMed. Our results indicated that there was very little consistency in the SPMs labeled with a g…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">N group-level stat maps included (4 docs)</summary>
        
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
                    …fort-related costs and integrate them with rewards. We conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (23 studies, <mark class="annotated-text">15</mark> maps, 549 participants) and net value (15 studies, 11 maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedial prefronta…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …es that used emotion processing task paradigms in FEP patients, and in people at clinical high-risk for psychosis (CHRp). Image-based meta-analyses with Seed-based d Mapping on available studies (n = <mark class="annotated-text">6</mark>) were also performed. Compared to controls, FEP patients showed decreased neural responses to emotion, particularly in the amygdala and anterior cingulate cortex. There were no significant difference…
                </div>
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
                    … conducted two meta-analyses of functional magnetic resonance imaging data to examine consistent neural correlates of effort demands (23 studies, 15 maps, 549 participants) and net value (15 studies, <mark class="annotated-text">11</mark> maps, 428 participants). The pre-supplementary motor area (pre-SMA) scaled positively with pure effort demand, whereas the ventromedial prefrontal cortex (vmPFC) showed the opposite effect. Moreover,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …n and across these labels. We hypothesized finding considerable overlap in the spatial topography among the neural networks associated with these labels. An image-based meta-analysis was performed on <mark class="annotated-text">158 </mark>group-level statistical maps (SPMs) received from authors of 69 papers listed on PubMed. Our results indicated that there was very little consistency in the SPMs labeled with a given network name. We …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">MA12 (4 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Hétu, Sébastien <mark class="annotated-text">and</mark> Grégoire, Mathieu and Saimpont, Arnaud and Coll, Michel-Pierre and Eugène, Fanny and Michon, Pierre-Emmanuel and Jackson, Philip L
Neuroscience and biobehavioral reviews, 2014

# Title

The neural ne…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    … the superior parietal lobule, inferior parietal lobule, and the dorsal premotor cortex but not the inferior frontal gyrus, are all commonly involved in imitation. An additional meta-analysis using a <mark class="annotated-text">label-based review</mark> confirmed that in the frontal lobe, the premotor cortex rather than the inferior frontal gyrus is consistently active in studies investigating imitation. In the parietal region the superior and infer…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    …h study. Thus, the current work is aimed at identifying whether there are spatially consistent structural and functional brain abnormalities in individuals with 22q11.2 DS through (i) a comprehensive <mark class="annotated-text">label-based systematic review</mark> and (ii) a coordinate-based meta-analysis of magnetic resonance imaging studies. The systematic review identified the frontal middle gyri, posterior cingulum, right cuneus and bilateral precuneus as …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">N MAs (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …i have been linked with several neuropsychiatric disorders. However, questions still remain about the exact neural substrates implicated in social reward and punishment processing. Here, we conducted <mark class="annotated-text">four</mark> Anisotropic Effect Size Signed Differential Mapping voxel-based meta-analyses of fMRI studies investigating the neural correlates of the anticipation and receipt of social rewards and punishments usi…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">4</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ship between social and emotional semantic features, which might confound interpreting the degree of overlap vs. specificity of social and emotional conceptual processing. We addressed this issue via <mark class="annotated-text">two</mark> activation-likelihood-estimation meta-analyses of neuroimaging studies reporting brain structures associated with processing social or emotional concepts. Alongside a common involvement of the ventro…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">2</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ROIs). This approach can produce inflated findings when results are synthesized in meta-analyses. We conducted a systematic search of the fMRI literature of ownership of body parts and entire bodies. <mark class="annotated-text">Three</mark> activation likelihood estimation (ALE) meta-analyses were conducted, testing the impact of including ROI-based findings. When both whole-brain and ROI-based results were included, frontal and posteri…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">3</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    Buhle, <mark class="annotated-text">Jason</mark> T and Silvers, Jennifer A and Wager, Tor D and Lopez, Richard and Onyemekwu, Chukwudi and Kober, Hedy and Weber, Jochen and Ochsner, Kevin N
Cerebral cortex (New York, N.Y. : 1991), 2015

# Title

Co…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <mark class="annotated-text">Witt</mark>, Suzanne T and van Ettinger-Veenstra, Helene and Salo, Taylor and Riedel, Michael C and Laird, Angela R
Brain topography, 2021

# Title

What Executive Function Network is that? An Image-Based Meta-A…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
            
            <div class="annotation">
                <div class="context">
                    …med a series of coordinate-based meta-analyses using the activation likelihood estimate (ALE) method. Meta-analysis was performed on whole-brain coordinates reported from 864 fMRI contrasts using the <mark class="annotated-text">NiMARE</mark> Python package, revealing convergence in medial prefrontal cortex, anterior cingulate cortex, posterior cingulate cortex, temporoparietal junction, bilateral insula, amygdala, fusiform gyrus, precune…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Michelle_Wang</div>
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
                    <div class="annotator-name">Mohammad_Torabi</div>
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
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
                    <div class="annotator-name">Michelle_Wang</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Mohammad_Torabi</div>
                </div>
            </div>
            
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
                    <div class="annotator-name">Niusha_Mirhakimi</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - non-human focus (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …Resting fMRI 
Subiculum 
fMRI 


# Abstract

Previous studies, predominantly in experimental animals, have suggested the presence of a differentiation of function across the hippocampal formation. In <mark class="annotated-text">rodents</mark>, ventral regions are thought to be involved in emotional behavior while dorsal regions mediate cognitive or spatial processes. Using a combination of modeling the co-occurrence of significant activat…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …dence for a role for each subregion in mnemonic processing, as well as implication of the anterior subregion in emotional and visual processing and the right posterior subregion in reward processing. <mark class="annotated-text">These findings lend support to models which posit anterior-posterior differentiation of function within the human hippocampal formation and complement other early steps toward a comparative (cross-species) model of the region.</mark> 

                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMCNone/"
                                       >PMCNone</a></div>
                    <div class="annotator-name">Brent_McPherson</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">stopped here (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Huang, Xiao and <mark class="annotated-text">Tang</mark>, Shi and Lyu, Xiaojun and Yang, Changqiang and Chen, Xiaoping
Sleep medicine, 2020

# Title

Structural and functional brain alterations in obstructive sleep apnea: a multimodal meta-analysis.

# Key…
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
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - cites ma as justification (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">EXCLUDE - cites ma as consistent with findings (0 docs)</summary>
        
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