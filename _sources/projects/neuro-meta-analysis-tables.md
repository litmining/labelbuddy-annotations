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


# neuro-meta-analysis-tables

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/neuro-meta-analysis-tables/).

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
        <summary class="label-display">doi - included (67 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …     Reference  ...                                     Matching
0                          Autism Spectrum Disorders  ...                    Autism Spectrum Disorders
1                               <mark class="annotated-text">Hall</mark> et al, 2010 ???  ...                   Gender, age, non-verbal IQ
2                               Monk et al, 2010 ???  ...                  Gender, age, handedness, IQ
3                             …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1371/journal.pone.0010804</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …trum Disorders  ...                    Autism Spectrum Disorders
1                               Hall et al, 2010 ???  ...                   Gender, age, non-verbal IQ
2                               <mark class="annotated-text">Monk</mark> et al, 2010 ???  ...                  Gender, age, handedness, IQ
3                             Deeley et al, 2007 ???  ...                       Gender, age, verbal IQ
4                             …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1503/jpn.090085</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … et al, 2010 ???  ...                   Gender, age, non-verbal IQ
2                               Monk et al, 2010 ???  ...                  Gender, age, handedness, IQ
3                             <mark class="annotated-text">Deeley</mark> et al, 2007 ???  ...                       Gender, age, verbal IQ
4                             Ashwin et al, 2007 ???  ...                      Gender, age, handedness
5                          Cri…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1016/j.biopsych.2006.09.037</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … et al, 2010 ???  ...                  Gender, age, handedness, IQ
3                             Deeley et al, 2007 ???  ...                       Gender, age, verbal IQ
4                             <mark class="annotated-text">Ashwin</mark> et al, 2007 ???  ...                      Gender, age, handedness
5                          Critchley et al, 2000 ???  ...                              Gender, age, IQ
6                             …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1016/j.neuropsychologia.2006.04.014</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ley et al, 2007 ???  ...                       Gender, age, verbal IQ
4                             Ashwin et al, 2007 ???  ...                      Gender, age, handedness
5                          <mark class="annotated-text">Critchley</mark> et al, 2000 ???  ...                              Gender, age, IQ
6                                      Schizophrenia  ...                                Schizophrenia
7                             …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1093/brain/123.11.2203</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187762/"
                                       >PMC3187762</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …  ...         a) Comparison of Different Needling Depths 
1                                      Li et al. 2000  ...                                                NSD 
2                              <mark class="annotated-text">MacPherson et al. 2008</mark>  ...                                                NSD 
3                                   Zhang et al. 2007  ...                                                NSD 
4                              …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1016/j.neulet.2008.01.058</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3322129/"
                                       >PMC3322129</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …                                             NSD 
3                                   Zhang et al. 2007  ...                                                NSD 
4                                      <mark class="annotated-text">Wu</mark> et al. 1999  ...  1)MA (2 cm)&gt;MA (1 mm): Bil. Ant. CingC (rostra... 
5   b) Comparison of Electro-acupuncture vs. Manua...  ...  b) Comparison of Electro-acupuncture vs. Manua... 
6                  …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1148/radiology.212.1.r99jl04133</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3322129/"
                                       >PMC3322129</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … 1)MA (2 cm)&gt;MA (1 mm): Bil. Ant. CingC (rostra... 
5   b) Comparison of Electro-acupuncture vs. Manua...  ...  b) Comparison of Electro-acupuncture vs. Manua... 
6                                    <mark class="annotated-text">Kong</mark> et al. 2002  ...  1) MA&gt;EA: Con. STG and Put/IN, post. Cing, STG... 
7                                      Li et al. 2003  ...  MA&gt;2 EA groups: Bil. Cun(BA18), TTG (BA41), MF... 
8                  …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1089/107555302760253603</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3322129/"
                                       >PMC3322129</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …) Comparison of Electro-acupuncture vs. Manua... 
6                                    Kong et al. 2002  ...  1) MA&gt;EA: Con. STG and Put/IN, post. Cing, STG... 
7                                      <mark class="annotated-text">Li</mark> et al. 2003  ...  MA&gt;2 EA groups: Bil. Cun(BA18), TTG (BA41), MF... 
8                                 Napadow et al. 2005  ...                                 EA&gt;MA: septal area 
9   c) Comparison o…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data"> 10.1097/00001756-200304150-00002 </div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3322129/"
                                       >PMC3322129</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …..  1) MA&gt;EA: Con. STG and Put/IN, post. Cing, STG... 
7                                      Li et al. 2003  ...  MA&gt;2 EA groups: Bil. Cun(BA18), TTG (BA41), MF... 
8                                 <mark class="annotated-text">Napadow</mark> et al. 2005  ...                                 EA&gt;MA: septal area 
9   c) Comparison of Different Frequencies of Elec...  ...  c) Comparison of Different Frequencies of Elec... 
10                 …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1002/hbm.20081</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3322129/"
                                       >PMC3322129</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">no table with included papers (15 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                           ROI <mark class="annotated-text">abbrev</mark>.  ... Supporting publications (ALE coord. within 20 mm)???
0   mTBI &gt; Control  ...                                     mTBI &gt; Control  
1              CBT  ...                             Wi2010, Sl2…
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
                       <mark class="annotated-text">Unnamed</mark>: 0 Go/No-Go Other Chi Squared value P-value
0           A        A     A                 A       A
1        What       17    39               NaN     NaN
2         vs.      NaN   NaN              10.…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5434171/"
                                       >PMC5434171</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                                                                     Area  ...  Center-of-mass coordinate (x, y, z)
0                <mark class="annotated-text">Dorsomedial</mark> prefrontal cortex(dmPFC)  ...                     -1.6, 54.2, 27.6
1               Ventromedial prefrontal cortex(vmPFC)  ...                     1.9, 47.2, -14.9
2                   R occipito-tempo…
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
                                <mark class="annotated-text">MAG</mark> 1 MAG 1.1  ...              MAG 6 MAG 6.1
0         NS term   corr.  ...            NS term   corr.
1          Motion   0.555  ...             visual   0.431
2            Body   0.451  ...           …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6326731/"
                                       >PMC6326731</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                                   Brain <mark class="annotated-text">regions</mark> (BA)  ...  MNI coordinates.15
0              Unnamed: 0_level_1  ...    Right hemisphere
1              Unnamed: 0_level_2  ...  Standard deviation
2              Unnamed: 0_level_3  ...             …
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
                                    <mark class="annotated-text">Diagnostic</mark> coding  ... Healthy individuals.2
0               Diagnostic coding  ...          Male sex (%)
1                   Schizophrenia  ...               58 (14)
2       Major depressive disorder  ...     …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7355168/"
                                       >PMC7355168</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                                                    <mark class="annotated-text">Cluster</mark> no.  ...        No. of contributing experiments.1
0                        Unnamed: 0_level_1  ...                                        %
1   RS in perceptual priming tasks (n = 27)  ...  RS in per…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7530292/"
                                       >PMC7530292</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                                                            <mark class="annotated-text">Local</mark> maximum  ...                      Heterogeneity
0                                              Region  ...                      Heterogeneity
1                             MDD vs. HCs (MDD &gt; HCs)  ..…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7573621/"
                                       >PMC7573621</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                        <mark class="annotated-text">Cluster</mark> # Cluster size (mm3)  ...    y    z
0         2.0             13,216  ...   56   28
1         8.0              4,800  ...   28   40
2        10.0              2,432  ...    4   46
3         NaN      …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8410528/"
                                       >PMC8410528</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                                              <mark class="annotated-text">Region</mark>  Brodmann    x     y     z    k   Max  Mean
0   Overall in-group &gt; out-group       NaN  NaN   NaN   NaN  NaN   NaN   NaN
1   LH anterior insula (cluster)      13.0  −36  15.0  10.0  260  0.33  0.25
2…
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
    
    <details >
        <summary class="label-display">included studies not in reference list (9 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                        Study  ...       Sample.4
0  Author  ...  Age (years).1
1   <mark class="annotated-text">Blair</mark>  ...    29.7 (2.28)
2   Blair  ...    31.1 (6.37)
3   Evans  ...    27.9 (10.6)
4  Goldin  ...     32.1 (9.3)
5  Klumpp  ...     33.6 (9.6)
6    Phan  ...     26.6 (6.8)
7    Yoon  ...    26.9 (6.16)…
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
                             Task       <mark class="annotated-text">First</mark> author    Year  ... Stop cue N subjects  Foci
0   Selection             Beudel  2009.0  ...      NaN       16.0   5.0
1         NaN                NaN     NaN  ...      NaN       16.0  10.0
2        …
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
                    …   Study    N  ... Loss Outcome MIDT type
0                Adcock et al. (???)   12  ...            –         A
1               Balodis et al. (???)   14  ...            ✓         B
2                 <mark class="annotated-text">Beck</mark> et al. (2009)   19  ...            –         A
3                 Behan et al. (???)   20  ...            –         E
4                 Bjork et al. (???)   12  ...            –         A
5           …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6055646/"
                                       >PMC6055646</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                                   <mark class="annotated-text">Current</mark> Cannabis User Studies  ...  Tesla
0                     Abdullaev et al., 2010  ...     3T
1                                        NaN  ...     3T
2                         Smith et al., 2011  ...  …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6331661/"
                                       >PMC6331661</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                                    Author, year  ...  Foci
0          Baumgartner, 2012  ...     8
1             <mark class="annotated-text">Bellucci</mark>, 2016  ...     6
2            Buckholtz, 2008  ...    11
3   Corradi-dell’Acqua, 2013  ...     2
4                 Feng, 2016  ...    19
5                  Guo, 2013  ...    20
6                   Hu…
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
                                <mark class="annotated-text">Author</mark> (year)  ... Use of medication at the moment of brain scanning?
0    Gustin et al. (2011)  ...               Yes; CBZ; GBP; TCA; NSAID and/or PGB
1   DeSouza et al. (2013)  ...  Yes: CBZ; GBP; TCA; VP…
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
                            #  ... <mark class="annotated-text">Instructed</mark> or Natural Deception
0     1.0  ...                         Natural
1     NaN  ...                             NaN
2     NaN  ...                             NaN
3     NaN  ...                       …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8386837/"
                                       >PMC8386837</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                        No.               First author (year)  ... Controls (M)  Mean age (SD).1
0     1              <mark class="annotated-text">Aderjan</mark> et al (2010)  ...       15 (7)      28.8 (7.73)
1     2             Bogdanov et al (2019)  ...           24             31.3
2     3                 Chen et al (2015)  ...       20 (6)     28.10 (5.9…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9622585/"
                                       >PMC9622585</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                                            Article Sample  ...       fMRI.3     fMRI.4
0            First author, year      N  ...  Hemi-sphere  # of foci
1                   <mark class="annotated-text">Barch</mark>, 2016    105  ...         Both          7
2                    Birn, 2014     27  ...         Both          6
3               Buchweitz, 2019     40  ...         Both          1
4                  Ca…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10545708/"
                                       >PMC10545708</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">doi - excluded (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                        Year  ... Inclusion in the meta-analysis or reason for exclusion
0   <mark class="annotated-text">1999</mark>  ...                       Excluded—without coordinates    
1   2003  ...          Excluded—without the contrast of interest    
2   2006  ...          Excluded—without the contrast of interest    
3…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1016/S0304-3940(99)00372-9</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6183416/"
                                       >PMC6183416</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                        Year  ... Inclusion in the meta-analysis or reason for exclusion
0   1999  ...                       Excluded—without coordinates    
1   <mark class="annotated-text">2003</mark>  ...          Excluded—without the contrast of interest    
2   2006  ...          Excluded—without the contrast of interest    
3   2007  ...                                           Included    
4…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1016/S1053-8119(03)00300-8</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6183416/"
                                       >PMC6183416</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …..          Excluded—without the contrast of interest    
2   2006  ...          Excluded—without the contrast of interest    
3   2007  ...                                           Included    
4   <mark class="annotated-text">2008</mark>  ...                       Excluded—without coordinates    
5   2008  ...                                           Included    
6   2008  ...                                           Included    
7…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1007/s12264-008-0928-2</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6183416/"
                                       >PMC6183416</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …..                                           Included    
6   2008  ...                                           Included    
7   2009  ...                                           Included    
8   <mark class="annotated-text">2010</mark>  ...                       Excluded—without coordinates    
9   2009  ...                                           Included    
10  2010  ...                                           Included    
1…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1162/jocn.2009.21311</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6183416/"
                                       >PMC6183416</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …..                       Excluded—without coordinates    
9   2009  ...                                           Included    
10  2010  ...                                           Included    
11  <mark class="annotated-text">2010</mark>  ...          Excluded—without the contrast of interest    
12  2010  ...                                           Included    
13  2010  ...          Excluded—without the contrast of interest    
1…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1523/JNEUROSCI.2751-09.2010</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6183416/"
                                       >PMC6183416</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                                  References  ...             Reason for exclusion from ALE analysis
0     <mark class="annotated-text">Beall</mark> et al. (???)  ...  No other study has matching ROI to ROI in resu...
1    Perrin et al. (???)  ...  No other study used same measure of rsFC analysis
2       Wei et al. (???)  ...  No other study use…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1097/YCT.0b013e31825ebcc7</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7859100/"
                                       >PMC7859100</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                                  References  ...             Reason for exclusion from ALE analysis
0     Beall et al. (???)  ...  No other study has matching ROI to ROI in resu...
1    <mark class="annotated-text">Perrin</mark> et al. (???)  ...  No other study used same measure of rsFC analysis
2       Wei et al. (???)  ...  No other study used same measure of rsFC analysis
3      Cano et al. (???)  ...  No other study use…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1073/pnas.1117206109</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7859100/"
                                       >PMC7859100</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …r exclusion from ALE analysis
0     Beall et al. (???)  ...  No other study has matching ROI to ROI in resu...
1    Perrin et al. (???)  ...  No other study used same measure of rsFC analysis
2       <mark class="annotated-text">Wei</mark> et al. (???)  ...  No other study used same measure of rsFC analysis
3      Cano et al. (???)  ...  No other study used same seed for Seed-voxel r...
4    Leaver et al. (???)  ...   No other study ha…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1038/tp.2014.101</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7859100/"
                                       >PMC7859100</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … GTN is not analyzed with ALE
14       Qi et al. (???)  ...  Guidelines for combining different modality of...
15      Sun et al. (???)  ...  No other study has matching ROI to ROI in resu...
16      <mark class="annotated-text">Wei</mark> et al. (???)  ...                   No other study used similar mask
17      Wei et al. (???)  ...  No other study used same seed for Seed-voxel r...

[18 rows x 9 columns]
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1007/s11682-020-00290-x</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7859100/"
                                       >PMC7859100</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ning different modality of...
15      Sun et al. (???)  ...  No other study has matching ROI to ROI in resu...
16      Wei et al. (???)  ...                   No other study used similar mask
17      <mark class="annotated-text">Wei</mark> et al. (???)  ...  No other study used same seed for Seed-voxel r...

[18 rows x 9 columns]
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">10.1016/j.jad.2019.11.120 </div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7859100/"
                                       >PMC7859100</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```
