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
        <summary class="label-display">N participants (96 docs)</summary>
        
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
            
            <div class="annotation">
                <div class="context">
                    …ely, we hypothesized that the activation of the insular cortices during a visual experience of a loved one's pain would differ according to group. 


## Materials and Methods 
  
### Participants 
  
<mark class="annotated-text">Fifteen participants were phobic prone (PP) (6 females; mean age 39.2; standard deviation [SD] 7.4) and 15 were eating disorders prone (EDP) (5 females; mean age 34.4; standard deviation [SD] 8.65).</mark> The couples enrolled had been together in a committed relationship for the last three years and had been living together for at least one year. To assign the participants to a group, they were assess…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">30</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3002948/"
                                       >PMC3002948</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">N included (34 docs)</summary>
        
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
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">count (18 docs)</summary>
        
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
                    …is experiment do not represent the full range of religious commitment found in the general population. 

Our final study consisted of data acquired from 30 subjects (15 Christians; 15 Nonbelievers; 7 <mark class="annotated-text">men</mark> and 8 women in each group). The mean full-scale WASI scores, years of education, and ages for the groups appear in  . 
   Subject Data: The mean full-scale WASI scores, years of education, and ages f…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">14</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2748718/"
                                       >PMC2748718</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ent do not represent the full range of religious commitment found in the general population. 

Our final study consisted of data acquired from 30 subjects (15 Christians; 15 Nonbelievers; 7 men and 8 <mark class="annotated-text">women</mark> in each group). The mean full-scale WASI scores, years of education, and ages for the groups appear in  . 
   Subject Data: The mean full-scale WASI scores, years of education, and ages for all subje…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">16</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2748718/"
                                       >PMC2748718</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nal changes in the extra-motor areas in amyotrophic lateral sclerosis (ALS) patients. The aim of this study is to investigate functional cerebral abnormalities in ALS patients on a whole brain scale. <mark class="annotated-text">Twenty</mark> ALS patients and twenty age- and sex-matched healthy volunteers were enrolled. Voxel-based analysis was used to characterize the alteration of amplitude of low frequency fluctuation (ALFF). Compared …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">20</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3447931/"
                                       >PMC3447931</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …-motor areas in amyotrophic lateral sclerosis (ALS) patients. The aim of this study is to investigate functional cerebral abnormalities in ALS patients on a whole brain scale. Twenty ALS patients and <mark class="annotated-text">twenty</mark> age- and sex-matched healthy volunteers were enrolled. Voxel-based analysis was used to characterize the alteration of amplitude of low frequency fluctuation (ALFF). Compared with the controls, the A…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">20</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3447931/"
                                       >PMC3447931</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rmany). The final stimulus set consisted of 20 samples of joy and sadness, 22 samples of anger and 18 samples of fear, both for authentic and play-acted sets. 


### PARTICIPANTS 
  
#### Study 1 
  
<mark class="annotated-text">24</mark> female participants (mean 24 years old; range 20–30 years; right-handed; German mother-tongue), without a history of neurological or psychological complications (including the use of psychiatric medi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3965851/"
                                       >PMC3965851</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …aid afterward. The experimental standards were approved by the local ethics committee and data were handled pseudonymously. 


#### Study 2 
  
Selection criteria were identical to Experiment 1, with <mark class="annotated-text">18</mark> female participants selected (20–30 years, mean 24 years, right-handed, German mother-tongue). 



### TRIAL AND STIMULUS PRESENTATION 
  
#### Study 1 
  
The program NBS Presentation (Neurobehavior…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3965851/"
                                       >PMC3965851</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ctions, in the everyday sense, may be the result of an internal evaluation of the applicability and relative importance of the several different internal rules. 


## Methods 
  
### Participants 
  
<mark class="annotated-text">Twenty-three</mark> healthy participants took part in the study (5 female; mean age 22 ± 2 years). All participants gave written informed consent. Procedures were approved by the local ethical committee, and were in acc…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">23</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4330553/"
                                       >PMC4330553</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ernal evaluation of the applicability and relative importance of the several different internal rules. 


## Methods 
  
### Participants 
  
Twenty-three healthy participants took part in the study (<mark class="annotated-text">5</mark> female; mean age 22 ± 2 years). All participants gave written informed consent. Procedures were approved by the local ethical committee, and were in accordance with the Declaration of Helsinki. All p…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4330553/"
                                       >PMC4330553</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …and emotion regulation regions ( ), where we hypothesize this to be a modulating mechanism underlying reduced arousal after neurofeedback. 

## Method 
  
### Participants 
  
The sample consisted of <mark class="annotated-text">21</mark> participants who met DSM-IV criteria ( ) for a primary diagnosis of PTSD (see   for demographic and psychometric information), where all patients experienced childhood sexual and/or physical abuse. A…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5030332/"
                                       >PMC5030332</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">healthy (16 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … itself, and truth-claims generally, emerge from the biology of the human brain. 


## Materials and Methods 
  
### Experimental Subjects 
  
We enrolled 54 subjects who were (1) between the ages of <mark class="annotated-text">18</mark>–30, (2) not taking anti-depressants, (3) neurologically healthy, (4) free of obvious psychiatric illness or suicidal ideation, and (5) native speakers of English as their first language. These inclus…
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
                    …self, and truth-claims generally, emerge from the biology of the human brain. 


## Materials and Methods 
  
### Experimental Subjects 
  
We enrolled 54 subjects who were (1) between the ages of 18–<mark class="annotated-text">30</mark>, (2) not taking anti-depressants, (3) neurologically healthy, (4) free of obvious psychiatric illness or suicidal ideation, and (5) native speakers of English as their first language. These inclusion…
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
                    …is experiment do not represent the full range of religious commitment found in the general population. 

Our final study consisted of data acquired from 30 subjects (15 Christians; 15 Nonbelievers; 7 <mark class="annotated-text">men</mark> and 8 women in each group). The mean full-scale WASI scores, years of education, and ages for the groups appear in  . 
   Subject Data: The mean full-scale WASI scores, years of education, and ages f…
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
                    …ent do not represent the full range of religious commitment found in the general population. 

Our final study consisted of data acquired from 30 subjects (15 Christians; 15 Nonbelievers; 7 men and 8 <mark class="annotated-text">women</mark> in each group). The mean full-scale WASI scores, years of education, and ages for the groups appear in  . 
   Subject Data: The mean full-scale WASI scores, years of education, and ages for all subje…
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
                    …-motor areas in amyotrophic lateral sclerosis (ALS) patients. The aim of this study is to investigate functional cerebral abnormalities in ALS patients on a whole brain scale. Twenty ALS patients and <mark class="annotated-text">twenty</mark> age- and sex-matched healthy volunteers were enrolled. Voxel-based analysis was used to characterize the alteration of amplitude of low frequency fluctuation (ALFF). Compared with the controls, the A…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3447931/"
                                       >PMC3447931</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rmany). The final stimulus set consisted of 20 samples of joy and sadness, 22 samples of anger and 18 samples of fear, both for authentic and play-acted sets. 


### PARTICIPANTS 
  
#### Study 1 
  
<mark class="annotated-text">24</mark> female participants (mean 24 years old; range 20–30 years; right-handed; German mother-tongue), without a history of neurological or psychological complications (including the use of psychiatric medi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3965851/"
                                       >PMC3965851</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …aid afterward. The experimental standards were approved by the local ethics committee and data were handled pseudonymously. 


#### Study 2 
  
Selection criteria were identical to Experiment 1, with <mark class="annotated-text">18</mark> female participants selected (20–30 years, mean 24 years, right-handed, German mother-tongue). 



### TRIAL AND STIMULUS PRESENTATION 
  
#### Study 1 
  
The program NBS Presentation (Neurobehavior…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3965851/"
                                       >PMC3965851</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ctions, in the everyday sense, may be the result of an internal evaluation of the applicability and relative importance of the several different internal rules. 


## Methods 
  
### Participants 
  
<mark class="annotated-text">Twenty-three</mark> healthy participants took part in the study (5 female; mean age 22 ± 2 years). All participants gave written informed consent. Procedures were approved by the local ethical committee, and were in acc…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4330553/"
                                       >PMC4330553</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ernal evaluation of the applicability and relative importance of the several different internal rules. 


## Methods 
  
### Participants 
  
Twenty-three healthy participants took part in the study (<mark class="annotated-text">5</mark> female; mean age 22 ± 2 years). All participants gave written informed consent. Procedures were approved by the local ethical committee, and were in accordance with the Declaration of Helsinki. All p…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4330553/"
                                       >PMC4330553</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">patients (9 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …nal changes in the extra-motor areas in amyotrophic lateral sclerosis (ALS) patients. The aim of this study is to investigate functional cerebral abnormalities in ALS patients on a whole brain scale. <mark class="annotated-text">Twenty</mark> ALS patients and twenty age- and sex-matched healthy volunteers were enrolled. Voxel-based analysis was used to characterize the alteration of amplitude of low frequency fluctuation (ALFF). Compared …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3447931/"
                                       >PMC3447931</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …and emotion regulation regions ( ), where we hypothesize this to be a modulating mechanism underlying reduced arousal after neurofeedback. 

## Method 
  
### Participants 
  
The sample consisted of <mark class="annotated-text">21</mark> participants who met DSM-IV criteria ( ) for a primary diagnosis of PTSD (see   for demographic and psychometric information), where all patients experienced childhood sexual and/or physical abuse. A…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5030332/"
                                       >PMC5030332</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …renia. However, it remains unclear whether disrupted asymmetry originates from inter-hemispheric functional connectivity (FC) and/or intra-hemispheric FC in this patient population. 


## Methods 
  
<mark class="annotated-text">Forty-four</mark> patients with drug-naive, first-episode schizophrenia, 42 unaffected siblings, and 44 healthy controls underwent resting-state functional magnetic resonance imaging (fMRI) scan. The parameter of asym…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6197719/"
                                       >PMC6197719</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tal of Guangxi Medical University in China between June 2013 and July 2014; 46 healthy controls were recruited from the local community during the same time period. All subjects were in the age range <mark class="annotated-text">18</mark>–37 years old and right handed, and had >6 years of formal education. 

Patients were diagnosed with schizophrenia according to the Diagnostic and Statistical Manual of Mental Disorders-IV (DSM-IV). T…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6197719/"
                                       >PMC6197719</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … of Guangxi Medical University in China between June 2013 and July 2014; 46 healthy controls were recruited from the local community during the same time period. All subjects were in the age range 18–<mark class="annotated-text">37</mark> years old and right handed, and had >6 years of formal education. 

Patients were diagnosed with schizophrenia according to the Diagnostic and Statistical Manual of Mental Disorders-IV (DSM-IV). They…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6197719/"
                                       >PMC6197719</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ht-handed male heterosexual normal controls (NC) were recruited. After rigorous subject inclusion procedures (interview, physical examination and questionnaire evaluation), the remaining 52 subjects (<mark class="annotated-text">26</mark> pED subjects, 26.8 ± 5.0 years mean ± SD v.s. 26 NC subjects 28.5 ± 3.2years, mean ± SD) were recruited for the MRI scanning. All subjects were sexually experienced (Forbes et al.  ). 

In the initia…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6290711/"
                                       >PMC6290711</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …terosexual normal controls (NC) were recruited. After rigorous subject inclusion procedures (interview, physical examination and questionnaire evaluation), the remaining 52 subjects (26 pED subjects, <mark class="annotated-text">26.8</mark> ± 5.0 years mean ± SD v.s. 26 NC subjects 28.5 ± 3.2years, mean ± SD) were recruited for the MRI scanning. All subjects were sexually experienced (Forbes et al.  ). 

In the initial interview session…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6290711/"
                                       >PMC6290711</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tterns might represent the neural correlates of altered threat processing during the imagination of disorder-related stimuli in PD patients. 


## Methods 
  
### Subjects 
  
The sample consisted of <mark class="annotated-text">17</mark> PD patients (male   n   = 2) and 17 HC (male   n   = 4), matched for age, gender and years of education (Table  ). All participants were right-handed and native German speakers. Participants were rec…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6382839/"
                                       >PMC6382839</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ural correlates of altered threat processing during the imagination of disorder-related stimuli in PD patients. 


## Methods 
  
### Subjects 
  
The sample consisted of 17 PD patients (male   n   = <mark class="annotated-text">2</mark>) and 17 HC (male   n   = 4), matched for age, gender and years of education (Table  ). All participants were right-handed and native German speakers. Participants were recruited through public advert…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6382839/"
                                       >PMC6382839</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …examined, 48 of them convicted. All participants received a thorough clinical examination including the structured clinical interview (SCID), intelligence, empathy, impulsivity, and criminal history. <mark class="annotated-text">Sixty-one</mark> participants (38 convicted) underwent an inhibition performance task (Go/No-go paradigm) combined with functional magnetic resonance imaging (fMRI). Convicted and non-convicted pedophilic CSOs reveal…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6678781/"
                                       >PMC6678781</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">female (8 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ent do not represent the full range of religious commitment found in the general population. 

Our final study consisted of data acquired from 30 subjects (15 Christians; 15 Nonbelievers; 7 men and 8 <mark class="annotated-text">women</mark> in each group). The mean full-scale WASI scores, years of education, and ages for the groups appear in  . 
   Subject Data: The mean full-scale WASI scores, years of education, and ages for all subje…
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
                    …rmany). The final stimulus set consisted of 20 samples of joy and sadness, 22 samples of anger and 18 samples of fear, both for authentic and play-acted sets. 


### PARTICIPANTS 
  
#### Study 1 
  
<mark class="annotated-text">24</mark> female participants (mean 24 years old; range 20–30 years; right-handed; German mother-tongue), without a history of neurological or psychological complications (including the use of psychiatric medi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3965851/"
                                       >PMC3965851</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …aid afterward. The experimental standards were approved by the local ethics committee and data were handled pseudonymously. 


#### Study 2 
  
Selection criteria were identical to Experiment 1, with <mark class="annotated-text">18</mark> female participants selected (20–30 years, mean 24 years, right-handed, German mother-tongue). 



### TRIAL AND STIMULUS PRESENTATION 
  
#### Study 1 
  
The program NBS Presentation (Neurobehavior…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3965851/"
                                       >PMC3965851</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ernal evaluation of the applicability and relative importance of the several different internal rules. 


## Methods 
  
### Participants 
  
Twenty-three healthy participants took part in the study (<mark class="annotated-text">5</mark> female; mean age 22 ± 2 years). All participants gave written informed consent. Procedures were approved by the local ethical committee, and were in accordance with the Declaration of Helsinki. All p…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4330553/"
                                       >PMC4330553</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …sed measure reflecting relative engagement of control (  vs   reward) systems and used it characterize and predict the circumstances under which diets succeed (or fail) in real life. 

## Methods 
  
<mark class="annotated-text">Seventy-five</mark> females (  M   = 19.38, Range = 18–23) from the Dartmouth community participated in the study. All participants were chronic dieters (as assessed by the Restrained Eating Scale;  ;  ) and gave inform…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5460048/"
                                       >PMC5460048</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …(versus lenient) judgments, including anger  and sadness . 

### Experiment 1: Sitting in hard chairs makes people hard on thieves and murderers 
  
In Experiment 1, 41 students (mean age = 19 years, <mark class="annotated-text">25</mark> females) were randomly assigned to complete a paper and pencil questionnaire at a desk in the laboratory while seated in either a hard wooden chair or a soft cushioned chair. These chairs were identi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5902547/"
                                       >PMC5902547</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ional potential mediator of the relationship between chair hardness and punishment harshness: change in political attitudes. 

In Experiment 2, 44 students and community members (mean age = 22 years, <mark class="annotated-text">33</mark> females, 2 unspecified) were randomly assigned to sit in the hard or soft chair as in Experiment 1 while completing a paper-and-pencil questionnaire on a clipboard. Participants were recruited and co…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5902547/"
                                       >PMC5902547</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …g would cause the participants to be “hard” on crime and if this effect would be based on activity in the sensorimotor cortices. 


## Materials and Methods 
  
### Participants 
  
Seventeen people (<mark class="annotated-text">12</mark> females) with a mean age of 24 years (standard deviation +−3.58, range 18–31) took part in the study. All participants were right-handed native German volunteers with no neurological or psychiatric h…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5902547/"
                                       >PMC5902547</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ity within neural networks related to executive functions. 


## Materials and methods 
  
### Subjects 
  
Twenty-six, typically developing 8–16-year-old Caucasian children and adolescents (17 boys, <mark class="annotated-text">9</mark> girls,   M   = 11.4 ± 2 years) were recruited by board announcements in local primary and secondary schools. All subjects were carefully screened for childhood psychiatric disorders using a standardi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7005761/"
                                       >PMC7005761</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …he pSTS during the NCET, representing a reduction in the own-age bias. 


## Methods 
  
### Participants 
  
Thirty-eight healthy, childless adults (age M = 24.08; SD = 3.33) took part in the study: <mark class="annotated-text">19 (10 females) who were working with children at the time of the study or who had worked with them in the past for more than half a year and 19 (10 females)</mark> who had never worked with children or who had worked with them for less than half a year. The weekly number of hours the WC group spent working with children ranged from 3.5 to 37.5 (M = 14.31; SD = …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7395771/"
                                       >PMC7395771</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">age mean (6 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … the applicability and relative importance of the several different internal rules. 


## Methods 
  
### Participants 
  
Twenty-three healthy participants took part in the study (5 female; mean age <mark class="annotated-text">22</mark> ± 2 years). All participants gave written informed consent. Procedures were approved by the local ethical committee, and were in accordance with the Declaration of Helsinki. All participants had norm…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4330553/"
                                       >PMC4330553</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … to harsh (versus lenient) judgments, including anger  and sadness . 

### Experiment 1: Sitting in hard chairs makes people hard on thieves and murderers 
  
In Experiment 1, 41 students (mean age = <mark class="annotated-text">19</mark> years, 25 females) were randomly assigned to complete a paper and pencil questionnaire at a desk in the laboratory while seated in either a hard wooden chair or a soft cushioned chair. These chairs w…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5902547/"
                                       >PMC5902547</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e an additional potential mediator of the relationship between chair hardness and punishment harshness: change in political attitudes. 

In Experiment 2, 44 students and community members (mean age = <mark class="annotated-text">22</mark> years, 33 females, 2 unspecified) were randomly assigned to sit in the hard or soft chair as in Experiment 1 while completing a paper-and-pencil questionnaire on a clipboard. Participants were recrui…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5902547/"
                                       >PMC5902547</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …terosexual normal controls (NC) were recruited. After rigorous subject inclusion procedures (interview, physical examination and questionnaire evaluation), the remaining 52 subjects (26 pED subjects, <mark class="annotated-text">26.8</mark> ± 5.0 years mean ± SD v.s. 26 NC subjects 28.5 ± 3.2years, mean ± SD) were recruited for the MRI scanning. All subjects were sexually experienced (Forbes et al.  ). 

In the initial interview session…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6290711/"
                                       >PMC6290711</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … study was conducted at the Instituto de Neurobiología of the Universidad Nacional Autónoma de México (UNAM Juriquilla, Queretaro, Mexico). A fibromyalgia group (FM, n = 20, age range = 22–70, mean = <mark class="annotated-text">46.4</mark>, SD = 12.4) and an age-matched control group (HC, n = 20, age range = 21–70, mean = 42.1, SD = 12.5) participated in this study. Given the difficulties of obtaining male participants with a complete …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6820536/"
                                       >PMC6820536</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ma de México (UNAM Juriquilla, Queretaro, Mexico). A fibromyalgia group (FM, n = 20, age range = 22–70, mean = 46.4, SD = 12.4) and an age-matched control group (HC, n = 20, age range = 21–70, mean = <mark class="annotated-text">42.1</mark>, SD = 12.5) participated in this study. Given the difficulties of obtaining male participants with a complete diagnose of FM, and the fact that it affects predominantly women, our entire sample inclu…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6820536/"
                                       >PMC6820536</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … networks related to executive functions. 


## Materials and methods 
  
### Subjects 
  
Twenty-six, typically developing 8–16-year-old Caucasian children and adolescents (17 boys, 9 girls,   M   = <mark class="annotated-text">11.4</mark> ± 2 years) were recruited by board announcements in local primary and secondary schools. All subjects were carefully screened for childhood psychiatric disorders using a standardised semi-structured …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7005761/"
                                       >PMC7005761</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …characterized by increased activation in the pSTS during the NCET, representing a reduction in the own-age bias. 


## Methods 
  
### Participants 
  
Thirty-eight healthy, childless adults (age M = <mark class="annotated-text">24.08</mark>; SD = 3.33) took part in the study: 19 (10 females) who were working with children at the time of the study or who had worked with them in the past for more than half a year and 19 (10 females) who h…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7395771/"
                                       >PMC7395771</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">male (5 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …is experiment do not represent the full range of religious commitment found in the general population. 

Our final study consisted of data acquired from 30 subjects (15 Christians; 15 Nonbelievers; 7 <mark class="annotated-text">men</mark> and 8 women in each group). The mean full-scale WASI scores, years of education, and ages for the groups appear in  . 
   Subject Data: The mean full-scale WASI scores, years of education, and ages f…
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
                    …ess. Of those who participated, eight did not exhibit sufficient levels of learning on the task to be included in the analyses (see below). As such, analyses reported here used data from 15 subjects (<mark class="annotated-text">7</mark> male) with a mean age of 23.8 years (SD = 4.14). The study was approved by the Brighton and Sussex Medical school's Research Governance and Ethics Committee. 

During scanning participants learned a …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5324609/"
                                       >PMC5324609</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ural correlates of altered threat processing during the imagination of disorder-related stimuli in PD patients. 


## Methods 
  
### Subjects 
  
The sample consisted of 17 PD patients (male   n   = <mark class="annotated-text">2</mark>) and 17 HC (male   n   = 4), matched for age, gender and years of education (Table  ). All participants were right-handed and native German speakers. Participants were recruited through public advert…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6382839/"
                                       >PMC6382839</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …threat processing during the imagination of disorder-related stimuli in PD patients. 


## Methods 
  
### Subjects 
  
The sample consisted of 17 PD patients (male   n   = 2) and 17 HC (male   n   = <mark class="annotated-text">4</mark>), matched for age, gender and years of education (Table  ). All participants were right-handed and native German speakers. Participants were recruited through public advertisements and at an outpatie…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6382839/"
                                       >PMC6382839</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …connectivity within neural networks related to executive functions. 


## Materials and methods 
  
### Subjects 
  
Twenty-six, typically developing 8–16-year-old Caucasian children and adolescents (<mark class="annotated-text">17</mark> boys, 9 girls,   M   = 11.4 ± 2 years) were recruited by board announcements in local primary and secondary schools. All subjects were carefully screened for childhood psychiatric disorders using a s…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7005761/"
                                       >PMC7005761</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …cal approach used is suboptimal and liable to false positives. In the future, we will use more scientific methods to solve the problem. 



## MATERIALS AND METHODS 
  
This study recruited eighteen (<mark class="annotated-text">9</mark> men, 9 women) patients with nAMD from the Nanchang University’s First Affiliated Hospital. HADS scores were collected from those patients. They are composed of 14 items, including 7 items of self-rat…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8544331/"
                                       >PMC8544331</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …fficacy of injection; (5) history of myocardial infarction, stroke or other systemic diseases that are contraindications for injection. 

Eighteen age- and education-matched healthy control subjects (<mark class="annotated-text">9</mark> men, 9 women) were recruited based on the following criteria: (1) no ocular diseases (such as maculopathy, diabetic retinopathy, cataract or glaucoma); (2) corrected monocular visual acuities >1.0 de…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8544331/"
                                       >PMC8544331</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">age min (5 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … itself, and truth-claims generally, emerge from the biology of the human brain. 


## Materials and Methods 
  
### Experimental Subjects 
  
We enrolled 54 subjects who were (1) between the ages of <mark class="annotated-text">18</mark>–30, (2) not taking anti-depressants, (3) neurologically healthy, (4) free of obvious psychiatric illness or suicidal ideation, and (5) native speakers of English as their first language. These inclus…
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
                    …tal of Guangxi Medical University in China between June 2013 and July 2014; 46 healthy controls were recruited from the local community during the same time period. All subjects were in the age range <mark class="annotated-text">18</mark>–37 years old and right handed, and had >6 years of formal education. 

Patients were diagnosed with schizophrenia according to the Diagnostic and Statistical Manual of Mental Disorders-IV (DSM-IV). T…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6197719/"
                                       >PMC6197719</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … After rigorous subject inclusion procedures (interview, physical examination and questionnaire evaluation), the remaining 52 subjects (26 pED subjects, 26.8 ± 5.0 years mean ± SD v.s. 26 NC subjects <mark class="annotated-text">28.5</mark> ± 3.2years, mean ± SD) were recruited for the MRI scanning. All subjects were sexually experienced (Forbes et al.  ). 

In the initial interview session, the basic information (history of sexual rela…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6290711/"
                                       >PMC6290711</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ipants 
  
The study was conducted at the Instituto de Neurobiología of the Universidad Nacional Autónoma de México (UNAM Juriquilla, Queretaro, Mexico). A fibromyalgia group (FM, n = 20, age range = <mark class="annotated-text">22</mark>–70, mean = 46.4, SD = 12.4) and an age-matched control group (HC, n = 20, age range = 21–70, mean = 42.1, SD = 12.5) participated in this study. Given the difficulties of obtaining male participants …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6820536/"
                                       >PMC6820536</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …acional Autónoma de México (UNAM Juriquilla, Queretaro, Mexico). A fibromyalgia group (FM, n = 20, age range = 22–70, mean = 46.4, SD = 12.4) and an age-matched control group (HC, n = 20, age range = <mark class="annotated-text">21</mark>–70, mean = 42.1, SD = 12.5) participated in this study. Given the difficulties of obtaining male participants with a complete diagnose of FM, and the fact that it affects predominantly women, our ent…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6820536/"
                                       >PMC6820536</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e   DRD4  -48 bp repeat gene modulates functional connectivity within neural networks related to executive functions. 


## Materials and methods 
  
### Subjects 
  
Twenty-six, typically developing <mark class="annotated-text">8</mark>–16-year-old Caucasian children and adolescents (17 boys, 9 girls,   M   = 11.4 ± 2 years) were recruited by board announcements in local primary and secondary schools. All subjects were carefully scr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7005761/"
                                       >PMC7005761</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">age max (4 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …self, and truth-claims generally, emerge from the biology of the human brain. 


## Materials and Methods 
  
### Experimental Subjects 
  
We enrolled 54 subjects who were (1) between the ages of 18–<mark class="annotated-text">30</mark>, (2) not taking anti-depressants, (3) neurologically healthy, (4) free of obvious psychiatric illness or suicidal ideation, and (5) native speakers of English as their first language. These inclusion…
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
                    … of Guangxi Medical University in China between June 2013 and July 2014; 46 healthy controls were recruited from the local community during the same time period. All subjects were in the age range 18–<mark class="annotated-text">37</mark> years old and right handed, and had >6 years of formal education. 

Patients were diagnosed with schizophrenia according to the Diagnostic and Statistical Manual of Mental Disorders-IV (DSM-IV). They…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6197719/"
                                       >PMC6197719</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nts 
  
The study was conducted at the Instituto de Neurobiología of the Universidad Nacional Autónoma de México (UNAM Juriquilla, Queretaro, Mexico). A fibromyalgia group (FM, n = 20, age range = 22–<mark class="annotated-text">70</mark>, mean = 46.4, SD = 12.4) and an age-matched control group (HC, n = 20, age range = 21–70, mean = 42.1, SD = 12.5) participated in this study. Given the difficulties of obtaining male participants wit…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6820536/"
                                       >PMC6820536</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …onal Autónoma de México (UNAM Juriquilla, Queretaro, Mexico). A fibromyalgia group (FM, n = 20, age range = 22–70, mean = 46.4, SD = 12.4) and an age-matched control group (HC, n = 20, age range = 21–<mark class="annotated-text">70</mark>, mean = 42.1, SD = 12.5) participated in this study. Given the difficulties of obtaining male participants with a complete diagnose of FM, and the fact that it affects predominantly women, our entire…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6820536/"
                                       >PMC6820536</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …  DRD4  -48 bp repeat gene modulates functional connectivity within neural networks related to executive functions. 


## Materials and methods 
  
### Subjects 
  
Twenty-six, typically developing 8–<mark class="annotated-text">16</mark>-year-old Caucasian children and adolescents (17 boys, 9 girls,   M   = 11.4 ± 2 years) were recruited by board announcements in local primary and secondary schools. All subjects were carefully screen…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7005761/"
                                       >PMC7005761</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">group 1 (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ginates from inter-hemispheric functional connectivity (FC) and/or intra-hemispheric FC in this patient population. 


## Methods 
  
Forty-four patients with drug-naive, first-episode schizophrenia, <mark class="annotated-text">42</mark> unaffected siblings, and 44 healthy controls underwent resting-state functional magnetic resonance imaging (fMRI) scan. The parameter of asymmetry (PAS) and support vector machine (SVM) were used to …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6197719/"
                                       >PMC6197719</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">group 2 (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ic functional connectivity (FC) and/or intra-hemispheric FC in this patient population. 


## Methods 
  
Forty-four patients with drug-naive, first-episode schizophrenia, 42 unaffected siblings, and <mark class="annotated-text">44</mark> healthy controls underwent resting-state functional magnetic resonance imaging (fMRI) scan. The parameter of asymmetry (PAS) and support vector machine (SVM) were used to analyze the data. Patients w…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6197719/"
                                       >PMC6197719</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```