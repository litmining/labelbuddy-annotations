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


# participant_demographics

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/participant_demographics/).

Annotating information about participants (for now just the sample size) in articles that match the query `fMRI[Abstract]`.

The full pubget output can be found here: https://osf.io/kfmdp/


## Labels in this project

```{code-cell}
:tags: [remove-input]

from labelrepo import displays
text = """
<div class="detailed-label-set">
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">N participants (113 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …e not involved in the fMRI experiments to avoid learning and habituation effects. A number of behavioral and dispositional measures were also taken from the fMRI participants. 


### Participants 
  
<mark class="annotated-text">Twenty-three</mark> right-handed volunteers (19 females, mean = 27.69 years, S.D. = 3.5) participated in the behavioral experiment designed for stimulus selection and validation. Eighteen different right-handed healthy …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">23</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2144768/"
                                       >PMC2144768</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ts. 


### Participants 
  
Twenty-three right-handed volunteers (19 females, mean = 27.69 years, S.D. = 3.5) participated in the behavioral experiment designed for stimulus selection and validation. <mark class="annotated-text">Eighteen</mark> different right-handed healthy volunteers (9 females) aged between 19 and 35 years (mean = 23.67 years, S.D. = 3.99) participated in the two fMRI experiments (role of evaluative focus; role of apprai…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">18</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2144768/"
                                       >PMC2144768</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …edominantly left-hemispheric temporo-parietal areas, whereas non-verbal memory is associated with medial and right-hemispheric frontal brain activity. 


## Materials and methods 
  
### Subjects 
  
<mark class="annotated-text">Twelve</mark> right-handed adults (6 male, 6 female), aged between 20 and 40 years (mean= 25.4 yrs), participated in the study. All participants gave their written informed consent. All had normal or corrected-to-…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">12</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2151069/"
                                       >PMC2151069</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …means of achieving a relaxed state, based on a pain management technique developed by Kabat-Zinn   et al  . ( ). 

## Methods 
  
### Participants 
  
All participants gave written, informed consent. <mark class="annotated-text">Thirteen</mark> participants (11 males, 2 females, age range 32–75 years, mean 52.92 years, SD 13.6), with unilateral, upper limb amputation at least above the wrist and phantom limb pain of at least one year's dura…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">13</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2494616/"
                                       >PMC2494616</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nections between the cerebellum and AIP, an area which is fundamental for the visuomotor transformations underlying grasping. 



## Materials and Methods 
  
### Functional MRI 
  
#### Subjects 
  
<mark class="annotated-text">Nineteen right-handed (12 women and 7 men; age range: 19–30 years; mean age: 24,7 years) and fifteen left-handed (10 women and 5 men; age range: 21–35 years; mean age: 26,1 years) participated in the experiment.</mark> They all had normal or corrected-to-normal vision, and they had no neurologic or psychiatric history, or any motor pathology. Handedness (right-handedness, left-handedness) was assessed by using a te…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">34</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2561002/"
                                       >PMC2561002</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ion in ill-structured circumstances ( ). We expected activity in medial rostral PFC to be particularly associated with the stimulus-oriented phases of this task. 

## Methods 
  
### Participants 
  
<mark class="annotated-text">Thirty-three </mark>individuals participated in the study: 15 participants with Autism Spectrum Disorder (12 males; 3 females) and 18 non-autistic control participants (13 males; 5 females). Groups were matched on age (A…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">33</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … to understanding how the practice of science itself, and truth-claims generally, emerge from the biology of the human brain. 


## Materials and Methods 
  
### Experimental Subjects 
  
We enrolled <mark class="annotated-text">54</mark> subjects who were (1) between the ages of 18–30, (2) not taking anti-depressants, (3) neurologically healthy, (4) free of obvious psychiatric illness or suicidal ideation, and (5) native speakers of …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2748718/"
                                       >PMC2748718</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tation-related activation would be expected in both auditory regions as well as in ventral premotor regions associated with speech production ( ). 


## Materials and methods 
  
### Participants 
  
<mark class="annotated-text">Twenty-two </mark>participants (13M, 9F) took part in the study although four (2M, 2F) were subsequently excluded due to: i) excessive head motion (> 10 mm), ii) an unexpected brain abnormality, iii) chance level perfo…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">22</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2775905/"
                                       >PMC2775905</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …cted analysis to subjects for whom we could localize both a right FG seed and right control seed (we failed to localize the FG seed in three subjects and the control seed in two subjects). A total of <mark class="annotated-text">12</mark> right-handed subjects with normal or corrected-to-normal vision met these criteria. They received monetary compensation for participating. Informed consent was obtained from all subjects, and the stu…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2995581/"
                                       >PMC2995581</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ment 1  . 
    


## Experiment 2 
  
### Materials and methods 
  
#### Subjects 
  
To replicate and extend our findings of Experiment 1, we collected resting and localizer data from a new group of <mark class="annotated-text">18</mark> naive subjects. All subjects were right-handed, had normal or corrected-to-normal vision, and received monetary compensation for participating. Informed consent was obtained from subjects, and the st…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2995581/"
                                       >PMC2995581</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">N included (39 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …note, however, that the subjects retained in this experiment do not represent the full range of religious commitment found in the general population. 

Our final study consisted of data acquired from <mark class="annotated-text">30</mark> subjects (15 Christians; 15 Nonbelievers; 7 men and 8 women in each group). The mean full-scale WASI scores, years of education, and ages for the groups appear in  . 
   Subject Data: The mean full-s…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2748718/"
                                       >PMC2748718</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … subsequently excluded due to: i) excessive head motion (> 10 mm), ii) an unexpected brain abnormality, iii) chance level performance in the scanner, and iv) an error acquiring the scanning data. The <mark class="annotated-text">18</mark> remaining participants were right-handed, native speakers of British English (mean 26.7 years, median 22.5 years, range 18–60 years) without any history of neurological or psychiatric disease. The be…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2775905/"
                                       >PMC2775905</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …w on their performance of the task. Two subjects reported sleepiness and lack of concentration during fMRI and one subject showed several movement artefacts (sudden head movements of more than 3 mm). <mark class="annotated-text">The data for these three subjects were, therefore, excluded </mark>from the analysis. The other subjects confirmed that they had been able to follow the instructions. 

Prior to scanning photographs of each subject (‘self’) or for each subject of a person known to hi…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">22</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3483694/"
                                       >PMC3483694</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …eported life-time psychiatric or neurological disease and medication. Prior to analysis, we excluded 2 left handed participants and 1 participant with abnormal brain anatomy leaving a final sample of <mark class="annotated-text">58</mark> (26 men) right-handed, participants with a mean age of 24.02 years (SD = 2.26). All participants gave informed consent and were paid 400 SEK (approximately 55 USD) for their participation. Due to tec…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3492343/"
                                       >PMC3492343</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …lities were diagnosed that might have an influence on their functional images. In addition, one younger adult was excluded due to experience in professional modern dance for six years in adolescence. <mark class="annotated-text">The final sample consisted of 19 younger (14 women, mean age = 22.6±2.27 years, range 18–27) and 15 older adults (10 women, mean age = 61.1±5.68 years, range 51–71),   t  (32) = 24.7,   p  <0.001</mark>. The majority of the participants already took part in the behavioral action prediction experiment reported in Diersch et al.  . One younger adult and four older adults were additionally recruited fr…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">34</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3660406/"
                                       >PMC3660406</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …luded [one healthy control (HC) subject was excluded]. There were no significant differences in any of the six head motion parameters (all   p  s > 0.05) or the mean FD measure (  p   = 0.74) between <mark class="annotated-text">the remaining 17 TS subjects and 15 HC subjects. </mark>


### ALFF AND fALFF ANALYSIS 
  
The REST toolbox was used to calculate the ALFF/fALFF. After the above preprocessing, the fMRI data were temporally band-pass filtered (0.01–0.1 Hz) to reduce low-fr…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">32</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3877773/"
                                       >PMC3877773</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …). We had to exclude 40 adolescents from the analysis due to acute head movements (movements greater than 3 mm in any one direction), interruption in scanning, fault in data transfer or missing data. <mark class="annotated-text">Consequently we analysed data for 220 adolescents (115 male (52.27%), age range 14–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 20–39, mean age 25.24 years (SD=6.34))</mark>. Adolescents were screened with the structured diagnostic interview “development and well-being assessment” (DAWBA) ( ) according to the fourth edition of the diagnostic and statistical manual (DSM-I…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">248</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ubjects were excluded from this study due to a failure to record behavioral data during the Go-Stop task. In addition, two IA subjects were removed from further analyses due to excessive head motion. <mark class="annotated-text">Finally, 23 controls and 18 IA subjects were included in the analysis</mark>. There were no significant differences between the two groups in age (mean ± S.D., IA: 15.1 ± 1.4 years versus control: 15.2 ± 0.5 years), ethnicity or education ( , p<0.05, two-sample   t   test). A…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">41</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4030253/"
                                       >PMC4030253</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rated participants were excluded from analysis due to poor task performance (e.g., drowsiness observed with real-time eyetracking,   n   = 3), or equipment malfunction/experimenter error (  n   = 4). <mark class="annotated-text">The final sample included 157 incarcerated and 46 non-incarcerated participants</mark>. Demographic characteristics of each group are provided in Table  . 
  
 Descriptive statistics and group differences between non-incarcerated and incarcerated participants  . 
    
All participants …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">203</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4174863/"
                                       >PMC4174863</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …5 excluded participants were 4 RH and 11 LH. We also excluded the 4 forced RH participants because of potential variation in hand motor dominance mechanisms in this case. The study sample was thus of <mark class="annotated-text">284</mark> participants (age: 25 ± 6 years, 140 women). 

Among the 284 participants, 142 considered themselves RH (71 men), and 142 considered themselves LH (73 men). RH and LH had significantly different mean…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4319399/"
                                       >PMC4319399</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```