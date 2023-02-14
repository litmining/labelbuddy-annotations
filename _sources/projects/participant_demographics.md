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
    
    <details style="--label-color: #acacac;">
        <summary class="label-display">N participants (68 docs)</summary>
        
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
            
            <div class="annotation">
                <div class="context">
                    …ntersensory timing, we also speculated that the strength of striatal interactions with the cortex would differ for unimodal and crossmodal timing. 


## Materials and methods 
  
### Participants 
  
<mark class="annotated-text">Twenty</mark> healthy adults participated in the study (8 female and 12 male; mean age = 24.4 years, range: 19–35 years, SD = 4.5; mean education = 15.5 years, range: 13–20 years, SD = 1.6). Participants were excl…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">20</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3147157/"
                                       >PMC3147157</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #d1cbff;">
        <summary class="label-display">count (48 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
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
                    … activity in medial rostral PFC to be particularly associated with the stimulus-oriented phases of this task. 

## Methods 
  
### Participants 
  
Thirty-three individuals participated in the study: <mark class="annotated-text">15</mark> participants with Autism Spectrum Disorder (12 males; 3 females) and 18 non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rly associated with the stimulus-oriented phases of this task. 

## Methods 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (<mark class="annotated-text">12</mark> males; 3 females) and 18 non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ated with the stimulus-oriented phases of this task. 

## Methods 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (12 males; <mark class="annotated-text">3</mark> females) and 18 non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …timulus-oriented phases of this task. 

## Methods 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (12 males; 3 females) and <mark class="annotated-text">18</mark> non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ (ASD   M  : 119…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …

## Methods 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (12 males; 3 females) and 18 non-autistic control participants (<mark class="annotated-text">13</mark> males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ (ASD   M  : 119, SD: 14; control   M  : 119, SD: 11; …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ds 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (12 males; 3 females) and 18 non-autistic control participants (13 males; <mark class="annotated-text">5</mark> females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ (ASD   M  : 119, SD: 14; control   M  : 119, SD: 11;   t  (31)…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
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
            
        </div>
        
    </details>
    
    <details style="--label-color: #4aff13;">
        <summary class="label-display">healthy (43 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …timulus-oriented phases of this task. 

## Methods 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (12 males; 3 females) and <mark class="annotated-text">18</mark> non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ (ASD   M  : 119…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …

## Methods 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (12 males; 3 females) and 18 non-autistic control participants (<mark class="annotated-text">13</mark> males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ (ASD   M  : 119, SD: 14; control   M  : 119, SD: 11; …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ds 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (12 males; 3 females) and 18 non-autistic control participants (13 males; <mark class="annotated-text">5</mark> females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ (ASD   M  : 119, SD: 14; control   M  : 119, SD: 11;   t  (31)…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …articipants with Autism Spectrum Disorder (12 males; 3 females) and 18 non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : <mark class="annotated-text">32</mark> years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ (ASD   M  : 119, SD: 14; control   M  : 119, SD: 11;   t  (31) = 0.1,   p   = .93). Full-scale IQ was measured using the Wechsler Adult Intelligenc…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
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
                    …ough trial-by-trial sampling; intrinsic behavior that might even supersede that of financial experts deciding about explicitly described statistics. 


## Experimental Procedures 
  
### Subjects 
  
<mark class="annotated-text">Sixteen</mark> healthy subjects (7 female; 18–35 years old) with no history of neurological or psychiatric illness participated in the study. Two additional pilot subjects from the lab were excluded from the final …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3183226/"
                                       >PMC3183226</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #00ffff;">
        <summary class="label-display">female (27 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ated with the stimulus-oriented phases of this task. 

## Methods 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (12 males; <mark class="annotated-text">3</mark> females) and 18 non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ds 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (12 males; 3 females) and 18 non-autistic control participants (13 males; <mark class="annotated-text">5</mark> females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ (ASD   M  : 119, SD: 14; control   M  : 119, SD: 11;   t  (31)…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
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
                    …ng; intrinsic behavior that might even supersede that of financial experts deciding about explicitly described statistics. 


## Experimental Procedures 
  
### Subjects 
  
Sixteen healthy subjects (<mark class="annotated-text">7</mark> female; 18–35 years old) with no history of neurological or psychiatric illness participated in the study. Two additional pilot subjects from the lab were excluded from the final analysis, as they we…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3183226/"
                                       >PMC3183226</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … reported areas may be considered when investigating disturbed self-related processing in psychiatric disorders. 


## Methods 
  
### Participants 
  
Twenty-five healthy subjects (aged 23-41 years, <mark class="annotated-text">17</mark> females, all right-handed according to a handedness questionnaire [ ]) were contacted by direct address or mailing lists. Subjects were screened for exclusion criteria such as prior and current neuro…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3483694/"
                                       >PMC3483694</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …d show the same patterns of activation, whether actively produced or passively observed. 



## Methods 
  
### Participants 
  
Seventeen right-handed children (6.9–7.8 years, mean age of 7.4 years, <mark class="annotated-text">9</mark> female) participated in this study. Handedness was assessed using the Edinburgh Handedness Inventory (Oldfield,  ). All children could read at or above a normal level for their age, print their name …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3780305/"
                                       >PMC3780305</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …re less active in this condition, and we hypothesize that this reduced activity reflects reduced involvement.  


## Materials and Methods 
  
### Participants 
  
Nineteen adult volunteers (10 male, <mark class="annotated-text">9</mark> female; mean age = 22.8 years; sd = 3.03 years, range = 19-31 years) participated in the study after giving written informed consent. Subjects were recruited from the university campus through advert…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3869649/"
                                       >PMC3869649</a></div>
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
                    …e a clear increase of right-hemisphere lateralization associated to earlier age at epilepsy onset in LMTLE patients
[ , ]. 


## Methods 
  
### Participants 
  
Twenty-three native Spanish patients (<mark class="annotated-text">15</mark> women) with refractory epilepsy of the temporal lobe were evaluated using an fMRI passive language paradigm. Twelve patients had a left hemispheric focus (LMTLE group) with the remaining eleven exhib…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4017227/"
                                       >PMC4017227</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #d1cbff;">
        <summary class="label-display">age mean (23 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …s participated in the study: 15 participants with Autism Spectrum Disorder (12 males; 3 females) and 18 non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : <mark class="annotated-text">38</mark> years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ (ASD   M  : 119, SD: 14; control   M  : 119, SD: 11;   t  (31) = 0.1,   p   = .93). Full-scale IQ was measured usi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …articipants with Autism Spectrum Disorder (12 males; 3 females) and 18 non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : <mark class="annotated-text">32</mark> years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ (ASD   M  : 119, SD: 14; control   M  : 119, SD: 11;   t  (31) = 0.1,   p   = .93). Full-scale IQ was measured using the Wechsler Adult Intelligenc…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …medication. Prior to analysis, we excluded 2 left handed participants and 1 participant with abnormal brain anatomy leaving a final sample of 58 (26 men) right-handed, participants with a mean age of <mark class="annotated-text">24.02</mark> years (SD = 2.26). All participants gave informed consent and were paid 400 SEK (approximately 55 USD) for their participation. Due to technical problems, the behavioral rating data were missing for …
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
                    …tters should show the same patterns of activation, whether actively produced or passively observed. 



## Methods 
  
### Participants 
  
Seventeen right-handed children (6.9–7.8 years, mean age of <mark class="annotated-text">7.4</mark> years, 9 female) participated in this study. Handedness was assessed using the Edinburgh Handedness Inventory (Oldfield,  ). All children could read at or above a normal level for their age, print th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3780305/"
                                       >PMC3780305</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s condition, and we hypothesize that this reduced activity reflects reduced involvement.  


## Materials and Methods 
  
### Participants 
  
Nineteen adult volunteers (10 male, 9 female; mean age = <mark class="annotated-text">22.8</mark> years; sd = 3.03 years, range = 19-31 years) participated in the study after giving written informed consent. Subjects were recruited from the university campus through advertisement and rewarded for…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3869649/"
                                       >PMC3869649</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ater than 3 mm in any one direction), interruption in scanning, fault in data transfer or missing data. Consequently we analysed data for 220 adolescents (115 male (52.27%), age range 14–15, mean age <mark class="annotated-text">14.61</mark> years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 20–39, mean age 25.24 years (SD=6.34)). Adolesce…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … age range 14–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 20–39, mean age <mark class="annotated-text">25.24</mark> years (SD=6.34)). Adolescents were screened with the structured diagnostic interview “development and well-being assessment” (DAWBA) ( ) according to the fourth edition of the diagnostic and statisti…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …n (Battelli et al.,  ; Mort et al.,  ), lesions underlying visual extinction are less clear (Stone et al.,  ). 


## Materials and methods 
  
### Subjects 
  
Ten healthy subjects (mean age ±   SD   <mark class="annotated-text">27.72</mark> ± 5.99 years, 7 males) participated in the experiment; one subject was excluded from analysis due to excessive head motion in the MRI scanner. All subjects had normal or corrected-to-normal vision. A…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4029023/"
                                       >PMC4029023</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …fferent fMRI data analysis approaches applied on the exact same data. 


## Methods 
  
### Participants 
  
fMRI data of 272 healthy participants, 149 female (age range: 18–68 years; mean ±   SD   = <mark class="annotated-text">24.5</mark> ± 8.0) and 123 male (age range: 18–61 years; mean ±   SD   = 24.4 ± 6.5) with self-reported normal audition were analyzed. This study was conducted at the Institute of Neuroscience and Psychology (IN…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4115625/"
                                       >PMC4115625</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ta. 


## Methods 
  
### Participants 
  
fMRI data of 272 healthy participants, 149 female (age range: 18–68 years; mean ±   SD   = 24.5 ± 8.0) and 123 male (age range: 18–61 years; mean ±   SD   = <mark class="annotated-text">24.4</mark> ± 6.5) with self-reported normal audition were analyzed. This study was conducted at the Institute of Neuroscience and Psychology (INP) in Glasgow and approved by the ethics committee of the Universi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4115625/"
                                       >PMC4115625</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #dddddd;">
        <summary class="label-display">N included (21 docs)</summary>
        
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
            
            <div class="annotation">
                <div class="context">
                    …ress pattern without considering the actual task. Data of another participant was excluded, since the participant did not show any variance in behavior and always chose the exact same answer. Data of <mark class="annotated-text">fifteen</mark> participants were included in further analyses (mean age = 22.33; SD = 2.35). The study was approved by the local Ethical Committee of the Faculty of Psychology and Neuroscience at Maastricht Univers…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">15</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838249/"
                                       >PMC4838249</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …cipants were excluded from the placebo group owing to faulty cycle timing of the MRI scan and failure to comply with the task, respectively. Thus valid fMRI data from both sessions were available for <mark class="annotated-text">56</mark> women (age 24.3±5.0 years), 30 in the GnRHa group and 26 in the placebo group. 

Baseline fMRI was acquired in the midfollicular phase (cycle day 6.0±2.3) when ovarian hormone levels are most stable …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5068584/"
                                       >PMC5068584</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ring detected vs. undetected delays, three further subjects had to be excluded because of their small number of trials per experimental run (see   fMRI data analysis  ), resulting in a final group of <mark class="annotated-text">seventeen</mark> participants (7 males, age range 19–30, mean age 25 years) for the second analysis. The study was approved by the local ethics committee of the medical faculty of the Philipps-University Marburg, Ger…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">17</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5218407/"
                                       >PMC5218407</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …he study, given that debriefing revealed that they focused only on the technical aspects of the videos (one was a football player and the other person was a coach). In the functional imaging analysis <mark class="annotated-text">56</mark> subjects were included (54 males and 2 females, aged from 21 to 60 years, mean age 34.4 ± 10.7 years). Fifty-five out of 56 used the joystick in the right hand given their handedness. All the subject…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5460049/"
                                       >PMC5460049</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff5100;">
        <summary class="label-display">patients (19 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … activity in medial rostral PFC to be particularly associated with the stimulus-oriented phases of this task. 

## Methods 
  
### Participants 
  
Thirty-three individuals participated in the study: <mark class="annotated-text">15</mark> participants with Autism Spectrum Disorder (12 males; 3 females) and 18 non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rly associated with the stimulus-oriented phases of this task. 

## Methods 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (<mark class="annotated-text">12</mark> males; 3 females) and 18 non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ated with the stimulus-oriented phases of this task. 

## Methods 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (12 males; <mark class="annotated-text">3</mark> females) and 18 non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s participated in the study: 15 participants with Autism Spectrum Disorder (12 males; 3 females) and 18 non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : <mark class="annotated-text">38</mark> years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ (ASD   M  : 119, SD: 14; control   M  : 119, SD: 11;   t  (31) = 0.1,   p   = .93). Full-scale IQ was measured usi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
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
                    … to using the original independent component time series as seeds since it recovers more features for an individual subject's correlation map. 


## Methods 
  
### Subjects 
  
Participants (  n   = <mark class="annotated-text">16</mark> DLB and   n   = 17 controls) were recruited from the local dwelling population of patients who had been referred to local old age psychiatry and neurology services. Approval for the current study was…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3984441/"
                                       >PMC3984441</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …revious studies, we expected to observe a clear increase of right-hemisphere lateralization associated to earlier age at epilepsy onset in LMTLE patients
[ , ]. 


## Methods 
  
### Participants 
  
<mark class="annotated-text">Twenty-three</mark> native Spanish patients (15 women) with refractory epilepsy of the temporal lobe were evaluated using an fMRI passive language paradigm. Twelve patients had a left hemispheric focus (LMTLE group) wit…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4017227/"
                                       >PMC4017227</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e a clear increase of right-hemisphere lateralization associated to earlier age at epilepsy onset in LMTLE patients
[ , ]. 


## Methods 
  
### Participants 
  
Twenty-three native Spanish patients (<mark class="annotated-text">15</mark> women) with refractory epilepsy of the temporal lobe were evaluated using an fMRI passive language paradigm. Twelve patients had a left hemispheric focus (LMTLE group) with the remaining eleven exhib…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4017227/"
                                       >PMC4017227</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ior DMN. This report details the results of the preliminary study. 


## Materials & methods 
  
### Participants 
  
Under protocols approved by the McLean Hospital Institutional Review Board (IRB), <mark class="annotated-text">11</mark> depressed patients (5 males/6 females, age: 61 ± 8, HAM-D = 21.6 ± 3.2, YMRS = 4.6 ± 3.7) ( ), two of them were diagnosed with major depressive disorder (MDD) and nine with BPD depression, were recru…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4589842/"
                                       >PMC4589842</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tails the results of the preliminary study. 


## Materials & methods 
  
### Participants 
  
Under protocols approved by the McLean Hospital Institutional Review Board (IRB), 11 depressed patients (<mark class="annotated-text">5</mark> males/6 females, age: 61 ± 8, HAM-D = 21.6 ± 3.2, YMRS = 4.6 ± 3.7) ( ), two of them were diagnosed with major depressive disorder (MDD) and nine with BPD depression, were recruited to participate in…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4589842/"
                                       >PMC4589842</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #d1cbff;">
        <summary class="label-display">age min (19 docs)</summary>
        
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
                    …sic behavior that might even supersede that of financial experts deciding about explicitly described statistics. 


## Experimental Procedures 
  
### Subjects 
  
Sixteen healthy subjects (7 female; <mark class="annotated-text">18</mark>–35 years old) with no history of neurological or psychiatric illness participated in the study. Two additional pilot subjects from the lab were excluded from the final analysis, as they were already …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3183226/"
                                       >PMC3183226</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ocessing. The reported areas may be considered when investigating disturbed self-related processing in psychiatric disorders. 


## Methods 
  
### Participants 
  
Twenty-five healthy subjects (aged <mark class="annotated-text">23</mark>-41 years, 17 females, all right-handed according to a handedness questionnaire [ ]) were contacted by direct address or mailing lists. Subjects were screened for exclusion criteria such as prior and …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3483694/"
                                       >PMC3483694</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …then all learned cursive letters should show the same patterns of activation, whether actively produced or passively observed. 



## Methods 
  
### Participants 
  
Seventeen right-handed children (<mark class="annotated-text">6.9</mark>–7.8 years, mean age of 7.4 years, 9 female) participated in this study. Handedness was assessed using the Edinburgh Handedness Inventory (Oldfield,  ). All children could read at or above a normal le…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3780305/"
                                       >PMC3780305</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …this reduced activity reflects reduced involvement.  


## Materials and Methods 
  
### Participants 
  
Nineteen adult volunteers (10 male, 9 female; mean age = 22.8 years; sd = 3.03 years, range = <mark class="annotated-text">19</mark>-31 years) participated in the study after giving written informed consent. Subjects were recruited from the university campus through advertisement and rewarded for their participation. The Mini Inte…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3869649/"
                                       >PMC3869649</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s (movements greater than 3 mm in any one direction), interruption in scanning, fault in data transfer or missing data. Consequently we analysed data for 220 adolescents (115 male (52.27%), age range <mark class="annotated-text">14</mark>–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 20–39, mean age 25.24 years (…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …5 male (52.27%), age range 14–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range <mark class="annotated-text">20</mark>–39, mean age 25.24 years (SD=6.34)). Adolescents were screened with the structured diagnostic interview “development and well-being assessment” (DAWBA) ( ) according to the fourth edition of the diag…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e direct comparison of two different fMRI data analysis approaches applied on the exact same data. 


## Methods 
  
### Participants 
  
fMRI data of 272 healthy participants, 149 female (age range: <mark class="annotated-text">18</mark>–68 years; mean ±   SD   = 24.5 ± 8.0) and 123 male (age range: 18–61 years; mean ±   SD   = 24.4 ± 6.5) with self-reported normal audition were analyzed. This study was conducted at the Institute of …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4115625/"
                                       >PMC4115625</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … applied on the exact same data. 


## Methods 
  
### Participants 
  
fMRI data of 272 healthy participants, 149 female (age range: 18–68 years; mean ±   SD   = 24.5 ± 8.0) and 123 male (age range: <mark class="annotated-text">18</mark>–61 years; mean ±   SD   = 24.4 ± 6.5) with self-reported normal audition were analyzed. This study was conducted at the Institute of Neuroscience and Psychology (INP) in Glasgow and approved by the e…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4115625/"
                                       >PMC4115625</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …c preferences and overt behavioral choices. 


## Methods 
  
### Participants 
  
Eighteen neurologically healthy subjects, recruited from the University of Gothenburg participated in the study (age <mark class="annotated-text">20</mark>–32, 9 males). The procedures were approved by the ethics committee of the University of Gothenburg, in accordance with the Declaration of Helsinki. Participants gave informed consent and were compens…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4318429/"
                                       >PMC4318429</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #d1cbff;">
        <summary class="label-display">age max (18 docs)</summary>
        
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
                    … behavior that might even supersede that of financial experts deciding about explicitly described statistics. 


## Experimental Procedures 
  
### Subjects 
  
Sixteen healthy subjects (7 female; 18–<mark class="annotated-text">35</mark> years old) with no history of neurological or psychiatric illness participated in the study. Two additional pilot subjects from the lab were excluded from the final analysis, as they were already fam…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3183226/"
                                       >PMC3183226</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ssing. The reported areas may be considered when investigating disturbed self-related processing in psychiatric disorders. 


## Methods 
  
### Participants 
  
Twenty-five healthy subjects (aged 23-<mark class="annotated-text">41</mark> years, 17 females, all right-handed according to a handedness questionnaire [ ]) were contacted by direct address or mailing lists. Subjects were screened for exclusion criteria such as prior and cur…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3483694/"
                                       >PMC3483694</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … all learned cursive letters should show the same patterns of activation, whether actively produced or passively observed. 



## Methods 
  
### Participants 
  
Seventeen right-handed children (6.9–<mark class="annotated-text">7.8</mark> years, mean age of 7.4 years, 9 female) participated in this study. Handedness was assessed using the Edinburgh Handedness Inventory (Oldfield,  ). All children could read at or above a normal level …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3780305/"
                                       >PMC3780305</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s reduced activity reflects reduced involvement.  


## Materials and Methods 
  
### Participants 
  
Nineteen adult volunteers (10 male, 9 female; mean age = 22.8 years; sd = 3.03 years, range = 19-<mark class="annotated-text">31</mark> years) participated in the study after giving written informed consent. Subjects were recruited from the university campus through advertisement and rewarded for their participation. The Mini Interna…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3869649/"
                                       >PMC3869649</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …movements greater than 3 mm in any one direction), interruption in scanning, fault in data transfer or missing data. Consequently we analysed data for 220 adolescents (115 male (52.27%), age range 14–<mark class="annotated-text">15</mark>, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 20–39, mean age 25.24 years (SD=…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ale (52.27%), age range 14–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 20–<mark class="annotated-text">39</mark>, mean age 25.24 years (SD=6.34)). Adolescents were screened with the structured diagnostic interview “development and well-being assessment” (DAWBA) ( ) according to the fourth edition of the diagnos…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …irect comparison of two different fMRI data analysis approaches applied on the exact same data. 


## Methods 
  
### Participants 
  
fMRI data of 272 healthy participants, 149 female (age range: 18–<mark class="annotated-text">68</mark> years; mean ±   SD   = 24.5 ± 8.0) and 123 male (age range: 18–61 years; mean ±   SD   = 24.4 ± 6.5) with self-reported normal audition were analyzed. This study was conducted at the Institute of Neu…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4115625/"
                                       >PMC4115625</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …plied on the exact same data. 


## Methods 
  
### Participants 
  
fMRI data of 272 healthy participants, 149 female (age range: 18–68 years; mean ±   SD   = 24.5 ± 8.0) and 123 male (age range: 18–<mark class="annotated-text">61</mark> years; mean ±   SD   = 24.4 ± 6.5) with self-reported normal audition were analyzed. This study was conducted at the Institute of Neuroscience and Psychology (INP) in Glasgow and approved by the ethi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4115625/"
                                       >PMC4115625</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …references and overt behavioral choices. 


## Methods 
  
### Participants 
  
Eighteen neurologically healthy subjects, recruited from the University of Gothenburg participated in the study (age 20–<mark class="annotated-text">32</mark>, 9 males). The procedures were approved by the ethics committee of the University of Gothenburg, in accordance with the Declaration of Helsinki. Participants gave informed consent and were compensate…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4318429/"
                                       >PMC4318429</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #fff700;">
        <summary class="label-display">male (16 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …rly associated with the stimulus-oriented phases of this task. 

## Methods 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (<mark class="annotated-text">12</mark> males; 3 females) and 18 non-autistic control participants (13 males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …

## Methods 
  
### Participants 
  
Thirty-three individuals participated in the study: 15 participants with Autism Spectrum Disorder (12 males; 3 females) and 18 non-autistic control participants (<mark class="annotated-text">13</mark> males; 5 females). Groups were matched on age (ASD   M  : 38 years, SD: 13; control   M  : 32 years, SD: 8;   t  (31) = 1.6,   p   = .13), and IQ (ASD   M  : 119, SD: 14; control   M  : 119, SD: 11; …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2648877/"
                                       >PMC2648877</a></div>
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
                    …ted life-time psychiatric or neurological disease and medication. Prior to analysis, we excluded 2 left handed participants and 1 participant with abnormal brain anatomy leaving a final sample of 58 (<mark class="annotated-text">26</mark> men) right-handed, participants with a mean age of 24.02 years (SD = 2.26). All participants gave informed consent and were paid 400 SEK (approximately 55 USD) for their participation. Due to technic…
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
                    …regions are less active in this condition, and we hypothesize that this reduced activity reflects reduced involvement.  


## Materials and Methods 
  
### Participants 
  
Nineteen adult volunteers (<mark class="annotated-text">10</mark> male, 9 female; mean age = 22.8 years; sd = 3.03 years, range = 19-31 years) participated in the study after giving written informed consent. Subjects were recruited from the university campus throug…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3869649/"
                                       >PMC3869649</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …is due to acute head movements (movements greater than 3 mm in any one direction), interruption in scanning, fault in data transfer or missing data. Consequently we analysed data for 220 adolescents (<mark class="annotated-text">115</mark> male (52.27%), age range 14–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 2…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …data for 220 adolescents (115 male (52.27%), age range 14–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (<mark class="annotated-text">17</mark> male (58.62%), age range 20–39, mean age 25.24 years (SD=6.34)). Adolescents were screened with the structured diagnostic interview “development and well-being assessment” (DAWBA) ( ) according to th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … ; Mort et al.,  ), lesions underlying visual extinction are less clear (Stone et al.,  ). 


## Materials and methods 
  
### Subjects 
  
Ten healthy subjects (mean age ±   SD   27.72 ± 5.99 years, <mark class="annotated-text">7</mark> males) participated in the experiment; one subject was excluded from analysis due to excessive head motion in the MRI scanner. All subjects had normal or corrected-to-normal vision. All participants …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4029023/"
                                       >PMC4029023</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …a analysis approaches applied on the exact same data. 


## Methods 
  
### Participants 
  
fMRI data of 272 healthy participants, 149 female (age range: 18–68 years; mean ±   SD   = 24.5 ± 8.0) and <mark class="annotated-text">123</mark> male (age range: 18–61 years; mean ±   SD   = 24.4 ± 6.5) with self-reported normal audition were analyzed. This study was conducted at the Institute of Neuroscience and Psychology (INP) in Glasgow a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4115625/"
                                       >PMC4115625</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … applied on the exact same data. 


## Methods 
  
### Participants 
  
fMRI data of 272 healthy participants, 149 female (age range: 18–68 years; mean ±   SD   = 24.5 ± 8.0) and 123 male (age range: <mark class="annotated-text">18</mark>–61 years; mean ±   SD   = 24.4 ± 6.5) with self-reported normal audition were analyzed. This study was conducted at the Institute of Neuroscience and Psychology (INP) in Glasgow and approved by the e…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4115625/"
                                       >PMC4115625</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffb300;">
        <summary class="label-display">group 1 (5 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …s from the analysis due to acute head movements (movements greater than 3 mm in any one direction), interruption in scanning, fault in data transfer or missing data. Consequently we analysed data for <mark class="annotated-text">220</mark> adolescents (115 male (52.27%), age range 14–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …is due to acute head movements (movements greater than 3 mm in any one direction), interruption in scanning, fault in data transfer or missing data. Consequently we analysed data for 220 adolescents (<mark class="annotated-text">115</mark> male (52.27%), age range 14–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 2…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s (movements greater than 3 mm in any one direction), interruption in scanning, fault in data transfer or missing data. Consequently we analysed data for 220 adolescents (115 male (52.27%), age range <mark class="annotated-text">14</mark>–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 20–39, mean age 25.24 years (…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …movements greater than 3 mm in any one direction), interruption in scanning, fault in data transfer or missing data. Consequently we analysed data for 220 adolescents (115 male (52.27%), age range 14–<mark class="annotated-text">15</mark>, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 20–39, mean age 25.24 years (SD=…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ater than 3 mm in any one direction), interruption in scanning, fault in data transfer or missing data. Consequently we analysed data for 220 adolescents (115 male (52.27%), age range 14–15, mean age <mark class="annotated-text">14.61</mark> years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 20–39, mean age 25.24 years (SD=6.34)). Adolesce…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …cluded from analysis due to poor task performance (e.g., drowsiness observed with real-time eyetracking,   n   = 3), or equipment malfunction/experimenter error (  n   = 4). The final sample included <mark class="annotated-text">157</mark> incarcerated and 46 non-incarcerated participants. Demographic characteristics of each group are provided in Table  . 
  
 Descriptive statistics and group differences between non-incarcerated and in…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4174863/"
                                       >PMC4174863</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
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
            
            <div class="annotation">
                <div class="context">
                    …ts. We obtained informed consent/assent from all participants. The University’s Institutional Review Board approved all procedures and materials. 

#### Study 1 (Behavioral) 
  
Participants included <mark class="annotated-text">51</mark> adults (M  = 43.71 years,   SD   = 6.76 years, range = 27.49–55.91 years; 41 female; 31 White, 13 African American/Black, 2 Asian/Pacific Islander, 2 Latino/Hispanic, and 3 multiethnic) and 55 adoles…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6664004/"
                                       >PMC6664004</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …informed consent/assent from all participants. The University’s Institutional Review Board approved all procedures and materials. 

#### Study 1 (Behavioral) 
  
Participants included 51 adults (M  = <mark class="annotated-text">43.71</mark> years,   SD   = 6.76 years, range = 27.49–55.91 years; 41 female; 31 White, 13 African American/Black, 2 Asian/Pacific Islander, 2 Latino/Hispanic, and 3 multiethnic) and 55 adolescents. Two adolesce…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6664004/"
                                       >PMC6664004</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nts. The University’s Institutional Review Board approved all procedures and materials. 

#### Study 1 (Behavioral) 
  
Participants included 51 adults (M  = 43.71 years,   SD   = 6.76 years, range = <mark class="annotated-text">27.49</mark>–55.91 years; 41 female; 31 White, 13 African American/Black, 2 Asian/Pacific Islander, 2 Latino/Hispanic, and 3 multiethnic) and 55 adolescents. Two adolescent participants were excluded from study 1…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6664004/"
                                       >PMC6664004</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff75f4;">
        <summary class="label-display">group 2 (5 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …anning, fault in data transfer or missing data. Consequently we analysed data for 220 adolescents (115 male (52.27%), age range 14–15, mean age 14.61 years (SD=0.32)). As a control group we recruited <mark class="annotated-text">28</mark> adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 20–39, mean age 25.24 years (SD=6.34)). Adolescents were screened with the structured diagnostic inte…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …data for 220 adolescents (115 male (52.27%), age range 14–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (<mark class="annotated-text">17</mark> male (58.62%), age range 20–39, mean age 25.24 years (SD=6.34)). Adolescents were screened with the structured diagnostic interview “development and well-being assessment” (DAWBA) ( ) according to th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …5 male (52.27%), age range 14–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range <mark class="annotated-text">20</mark>–39, mean age 25.24 years (SD=6.34)). Adolescents were screened with the structured diagnostic interview “development and well-being assessment” (DAWBA) ( ) according to the fourth edition of the diag…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ale (52.27%), age range 14–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 20–<mark class="annotated-text">39</mark>, mean age 25.24 years (SD=6.34)). Adolescents were screened with the structured diagnostic interview “development and well-being assessment” (DAWBA) ( ) according to the fourth edition of the diagnos…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … age range 14–15, mean age 14.61 years (SD=0.32)). As a control group we recruited 28 adult participants (adult group) by board and Internet announcements (17 male (58.62%), age range 20–39, mean age <mark class="annotated-text">25.24</mark> years (SD=6.34)). Adolescents were screened with the structured diagnostic interview “development and well-being assessment” (DAWBA) ( ) according to the fourth edition of the diagnostic and statisti…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3991323/"
                                       >PMC3991323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …due to poor task performance (e.g., drowsiness observed with real-time eyetracking,   n   = 3), or equipment malfunction/experimenter error (  n   = 4). The final sample included 157 incarcerated and <mark class="annotated-text">46</mark> non-incarcerated participants. Demographic characteristics of each group are provided in Table  . 
  
 Descriptive statistics and group differences between non-incarcerated and incarcerated participa…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4174863/"
                                       >PMC4174863</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
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
            
            <div class="annotation">
                <div class="context">
                    …ific Islander, 2 Latino/Hispanic, and 3 multiethnic) and 55 adolescents. Two adolescent participants were excluded from study 1 due to an inability to follow the task instructions, leaving a total of <mark class="annotated-text">53</mark> adolescent participants (M  = 13.37 years,   SD   = 0.61 years, range = 12.18–14.82 years; 27 female; 25 White, 14 African American/Black, 4 Asian/Pacific Islander, 2 Latino/Hispanic, and 8 multiethn…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6664004/"
                                       >PMC6664004</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … and 3 multiethnic) and 55 adolescents. Two adolescent participants were excluded from study 1 due to an inability to follow the task instructions, leaving a total of 53 adolescent participants (M  = <mark class="annotated-text">13.37</mark> years,   SD   = 0.61 years, range = 12.18–14.82 years; 27 female; 25 White, 14 African American/Black, 4 Asian/Pacific Islander, 2 Latino/Hispanic, and 8 multiethnic; Maternal education: 1 some high …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6664004/"
                                       >PMC6664004</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …o adolescent participants were excluded from study 1 due to an inability to follow the task instructions, leaving a total of 53 adolescent participants (M  = 13.37 years,   SD   = 0.61 years, range = <mark class="annotated-text">12.18</mark>–14.82 years; 27 female; 25 White, 14 African American/Black, 4 Asian/Pacific Islander, 2 Latino/Hispanic, and 8 multiethnic; Maternal education: 1 some high school, 3 high school degree, 12 some coll…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6664004/"
                                       >PMC6664004</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c4c4c4;">
        <summary class="label-display">_to discuss (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …w on their performance of the task. Two subjects reported sleepiness and lack of concentration during fMRI and one subject showed several movement artefacts (sudden head movements of more than 3 mm). <mark class="annotated-text">The data for these three subjects were, therefore, excluded from the analysis</mark>. The other subjects confirmed that they had been able to follow the instructions. 

Prior to scanning photographs of each subject (‘self’) or for each subject of a person known to him/her (‘known’; w…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">how to annotate when true number not reported explicitly</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3483694/"
                                       >PMC3483694</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ed via flyers, listservs, and outreach at local events. We obtained informed consent/assent from all participants. The University’s Institutional Review Board approved all procedures and materials. 

<mark class="annotated-text">####</mark> Study 1 (Behavioral) 
  
Participants included 51 adults (M  = 43.71 years,   SD   = 6.76 years, range = 27.49–55.91 years; 41 female; 31 White, 13 African American/Black, 2 Asian/Pacific Islander, 2…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">how to annotate papers with several studies or experiments</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6664004/"
                                       >PMC6664004</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ormed consent document after receiving a full explanation of the study protocol. The experiment was carried out in accordance with the latest version of the Declaration of Helsinki. In data analysis, <mark class="annotated-text">five participants of the control group and one participant of the postpartum group were excluded</mark> for the following reasons: head movement exceeding the priori maximum of 3 mm (n = 2), severe signal loss in the parietal lobe (n = 2), and an age 1.5 standard deviations below the mean age (n = 1). …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">the true number of participants is not mentioned explicitly</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7272423/"
                                       >PMC7272423</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #d1cbff;">
        <summary class="label-display">age median (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … ; Gorgolewski et al.,  ). Three task-related fMRI time series (motor, covert verb generation, and landmark tasks) were selected to validate our proposed FMICA model. Ten healthy subjects (median age <mark class="annotated-text">52.5</mark> years, min = 50, max = 58) included four males and six females, of which three were left-handed and seven right-handed. Each subject was scanned twice, either 2 (eight subjects) or 3 (two subjects) d…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5596109/"
                                       >PMC5596109</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```