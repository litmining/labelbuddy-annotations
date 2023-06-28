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


# dynamic_functional_connectivity

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/dynamic_functional_connectivity/).

## Dynamic Functional Connectivity methods

The focus of this project is to explore how methods for estimating Dynamic Functional Connectivity (DFC) are used in the literature.




## Labels in this project



```{code-cell}
:tags: [remove-input]

from labelrepo import displays
text = """
<div class="detailed-label-set">
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">Sliding Window (28 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …in Power et al. ( ) (see article for coordinates). sFC was computed by the Pearson correlation coefficient across all time points for all 34,716 unique edges. 


### Estimation of dFC 
  
We used the <mark class="annotated-text">sliding window</mark> method to create dFC time series. For each time point,   t  , a Pearson correlation coefficient was estimated using ±31 time points (63 volumes in total equaling 126 sec) for each combination of ROIs…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5175424/"
                                       >PMC5175424</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rical ROI in the medial primary motor cortex (Montreal Neurological Institute coordinates=−1, −8, 63), a region not previously linked to depression. 


### Sliding window correlation analysis 
  
The <mark class="annotated-text">sliding window</mark> analysis was performed using custom Python ( ) scripts. The data were split into 40 s Gaussian moving windows, staggered by one repetition time, created using a Gaussian kernel with a standard deviat…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5416685/"
                                       >PMC5416685</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …etween conditions and averaged across windows to derive areas that revealed significant changes with sedation. Beta values, which are a measure of the connectivity strength, were calculated from each <mark class="annotated-text">sliding window</mark>, and their fluctuations  were measured. The between-region correlation and multiband frequency analysis were also performed to further characterize the temporal covariance and frequency specificity o…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5561230/"
                                       >PMC5561230</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … minus resting-state); ΔdFC-DMN = difference in stationary functional connectivity between task-state and resting-state (task-state minus resting-state). 
  Fig. 1   


#### Dynamic FC 
  
For dFC, a <mark class="annotated-text">sliding-window</mark> approach was used with settings that were selected based on previous studies (see  A), resulting in 35 and 86 sliding windows for RS and task-state time series, respectively ( ;  ). For RS time serie…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6030565/"
                                       >PMC6030565</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …om all regions of interest (ROIs) of the Power atlas, resulting in a 264 × 264 matrix per window per subject, with a window length of 60.2 s (28 × TR) and a shift of 10.75 s (5 × TR), resulting in 34 <mark class="annotated-text">sliding windows</mark> per subject. The choice of window length was based on earlier studies (e.g., van Geest et al.,  ). The standard deviation for each connection was calculated and normalized for the average of that ind…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6266764/"
                                       >PMC6266764</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … Methods 
  
Whole-brain resting-state functional MRI data were acquired on a 3 T whole-body clinical MRI scanner from 18 subjects clinically diagnosed with JME and 25 healthy control subjects. 2-min <mark class="annotated-text">sliding-window</mark> approach was incorporated in the quantitative data-driven data analysis framework to assess both the dynamic and static functional connectivity in the resting brains. Two-sample   t  -tests were perf…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6412974/"
                                       >PMC6412974</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ROI pair between GM was calculated directly to construct a static FC of GM (sGFC). And static FC between GM and WM (sWGFC) was obtained by calculating each ROI pair&#39;s   r   between WM and GM. Then, a <mark class="annotated-text">sliding time window</mark> strategy was applied, and a complete time series was divided into several subsequent series by overlapping windows. We allowed the window length to be 30 and the step size to be 1. Then, the correlat…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6790327/"
                                       >PMC6790327</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …76 sampling points were obtained. 


### 2.3. Construction of Dynamic Functional Connectivity Brain Network 
  
In order to observe the continuous change of BOLD signal with time in our work, we used <mark class="annotated-text">sliding window</mark> technique [ ,  ] to combine several BOLD values at adjacent sampling time. As a result, we got a small window which includes all the BOLD information of 90 brain regions in consecutive time as our st…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6800976/"
                                       >PMC6800976</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rate and objective image-based diagnosis system for MDD. 


## Methods 
  
MRI images were collected from 99 participants including 56 healthy controls and 43 MDD patients. DFC was calculated using a <mark class="annotated-text">sliding-window</mark> algorithm. A non-linear support vector machine (SVM) approach was then used with the DFC matrices as features to distinguish MDD patients from healthy controls. The spatiotemporal characteristics of …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7118554/"
                                       >PMC7118554</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …pairwise Pearson correlation coefficients between the network activity time series. 

To study dynamic FC, pairwise Pearson correlation coefficients were calculated for each 1‐min window (24 volumes) <mark class="annotated-text">sliding</mark> in steps of one volume. We used 1‐min sliding windows so that reasonably reliable correlation coefficients could be estimated. The length of the correlation coefficient time series for each network p…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7154624/"
                                       >PMC7154624</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">Clustering (18 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ith risperidone (  n   = 24), as well as matched controls at baseline (  n   = 35) and after 6 weeks (  n   = 19). After identifying 41 independent components (ICs) comprising resting-state networks, <mark class="annotated-text">sliding window analysis</mark> was performed on IC timecourses using an optimal window size validated with linear support vector machines. Windowed correlation matrices were then clustered into three discrete connectivity states (…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5292583/"
                                       >PMC5292583</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ing resting-state networks, sliding window analysis was performed on IC timecourses using an optimal window size validated with linear support vector machines. Windowed correlation matrices were then <mark class="annotated-text">clustered</mark> into three discrete connectivity states (a relatively sparsely connected state, a relatively abundantly connected state, and an intermediately connected state). In unmedicated patients, static connec…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5292583/"
                                       >PMC5292583</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …relation of those windowed time series, on which Fisher transformation was then applied. One subject (SBJ 15) was dropped because of high similarity across all dFCs. 


###  K  -Means Clustering 
  
 <mark class="annotated-text">K  -means clustering</mark> was applied on the dFCs as an unsupervised vector quantization tool to explore the intrinsic structures of FC dynamics for each individual. The number of clusters was set to four, and Pearson’s corre…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6326730/"
                                       >PMC6326730</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ormed by all wFNC derivatives, and is referred to as the first order derivatives of the sliding window correlations. 

The tvFNC method pipeline is as follows, for all subjects (1) compute dFNC data (<mark class="annotated-text">sliding windowed</mark> correlations wFNC); (2) estimate DdFNC data (derivatives of sliding windowed correlations DwFNC); (3) concatenate row wise zero and first order windowed correlations [wFNC and DwFNC] divided by their…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6611425/"
                                       >PMC6611425</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …FNC data to identify reoccurring connectivity states and their derivatives patterns. 


### Clustering Analysis 
  
In both methods dFNC and tvFNC, time-varying connectivity is captured by performing <mark class="annotated-text">k-means clustering</mark> analysis, assigning all subjects’ temporal FNC data into a selected number of clusters representing distinct functional connectivity states. The clustering algorithm selection is based on previous co…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6611425/"
                                       >PMC6611425</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ion coefficient between the timecourses of each pair of ROIs, over the full scanning length. 


### Dynamic functional connectivity 
  
Dynamic connectivity matrices were derived using an overlapping <mark class="annotated-text">sliding-window approach</mark> . For each subject and each condition, tapered sliding windows were obtained by convolving a rectangle of 22 TRs (44s) with a Gaussian kernel of 3 TRs, sliding with 1 TR step size. This resulted in 2…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6787094/"
                                       >PMC6787094</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … modular and intra-modular connectivity. For each subject, the joint patterns were then used to assign each timepoint to one of two clusters, using an unsupervised machine learning algorithm known as <mark class="annotated-text">k-means clustering</mark> (setting   k   = 2) . To avoid the possibility of the algorithm becoming stuck in local minima, it was repeated 500 times with random re-initialisation of the two clusters’ initial points. This was p…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6787094/"
                                       >PMC6787094</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …. This range reaches a satisfactory temporal trade-off between the real dynamic fluctuation and the reliable temporal information ( ). 

To assess the re-occurrence of the dFC patterns, we used the   <mark class="annotated-text">k  -means clustering</mark> algorithm to cluster those FC matrices that were obtained from all the subjects in the present study. The correlation distance function was chosen as a   k  -means clustering algorithm because this a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6881656/"
                                       >PMC6881656</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …236 available ROIs were used to analyze DFC using DynamicBC toolbox ( ). Since there was no formal consensus on window length, dynamic functional network connectivity (dFNC) was constructed using the <mark class="annotated-text">sliding-window</mark> Pearson&#39;s correlation method with a length of 20 TRs (40 s) and a step size of 1TR, as previously performed ( ), resulting in 111 windows. In each window, we computed Pearson correlation coefficients…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6902076/"
                                       >PMC6902076</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …roups. The original FCV matrices were then Fisher   z  -transformed and were statistically compared. 


###  k  -means Clustering 
  
To identify dFNC patterns reoccurring across temporal matrices,   <mark class="annotated-text">k  -means clustering</mark> was employed on all the dynamic correlation matrices to divide the dFNC into discrete clusters. The   k  -means algorithm aggregates information with similarities into “  k  ” groups, ensuring that t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6902076/"
                                       >PMC6902076</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">clinical application (12 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …enables a better consideration of dynamic aspects without requiring a reduction of upstream data. 

Within the product HMM framework, this paper compares brain DFC between patients with dementia with <mark class="annotated-text">Lewy bodies (DLB)</mark> and healthy elderly controls. DLB is the second most prevalent form of neurodegenerative dementia after Alzheimer&#39;s disease, affecting from 16 to 20% of patients with dementia (Aarsland et al.,  ). T…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4918689/"
                                       >PMC4918689</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ge-scale dynamic functional connectome. Notably, if large-scale phase couplings hold functional information – as speculated – they may also be modulated in neurological and psychiatric disorders. 
  
<mark class="annotated-text">Schizophrenia  (SZ)</mark> is a severe psychiatric disorder, which has affected some 23.6 million people worldwide by 2013, with a lifetime prevalence of about 1% ( ). SZ is commonly known as a connectivity disorder . In 1998,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7118690/"
                                       >PMC7118690</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …on analysis using fMRI data with a low sampling rate and a regression analysis using fMRI data with a high sampling rate. Specifically, we achieved both a higher classification accuracy in predicting <mark class="annotated-text">cognitive impairment status</mark> in fighters and a larger explained behavioral variance in healthy young adults when using dynamic FC matrices computed with SSTD window-sizes as features, as compared to using dynamic FC matrices com…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7594665/"
                                       >PMC7594665</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …form sliding-window seed-to-whole-brain DFC analyses in a comprehensive manner. Moreover, the relationships between significant DFC changes and symptom severity were further explored in patients with <mark class="annotated-text">ASD</mark>s. Furthermore, transcription-neuroimaging association analyses were conducted to explore the molecular mechanisms of the DFC alterations in patients with ASDs by leveraging the Allen Human Brain Atla…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8784878/"
                                       >PMC8784878</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nd biomarkers of ADHD. However, no significant findings were yield to study the dFC of the insula in children with ADHD, and its contribution to social dysfunction. 

From a neurobiologic standpoint, <mark class="annotated-text">ADHD</mark> is increasingly being recognized as a disorder resulting from disruptions in large-scale brain networks. Extant studies of brain&#39;s FC in ADHD, however, have provided inconsistent outcomes, with some …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9197452/"
                                       >PMC9197452</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ds prediction of effective treatment responses. The study aims to examine the relationship between dynamic functional connectivity (dFC) of the hippocampal subregion and antidepressant improvement of <mark class="annotated-text">MDD patients</mark> and to estimate the capability of dFC to predict antidepressant efficacy.
 


## Methods 
  
 The data were from 70 MDD patients and 43 healthy controls (HC); the dFC of hippocampal subregions was es…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9334807/"
                                       >PMC9334807</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …o as bimanual synkinesis or mirror movement (MM), is considered physiological only during childhood (up to the age of 10) ( ). However, it could persist during adulthood in congenital conditions like <mark class="annotated-text">Kallmann syndrome (KS)</mark>. An imbalance of the developing brain motor circuit has been suggested as a possible cause for reduced suppression of involuntary contralateral hand movements ( ;  ). 

In a previous resting-state fM…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9477102/"
                                       >PMC9477102</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e signal contrast and enable advanced analyses to understand temporal interactions between brain regions as opposed to spatial interactions. In this work, we leverage such fast fMRI acquisitions from <mark class="annotated-text">Alzheimer’s disease</mark> Neuroimaging Initiative to understand temporal differences in the interactions between resting-state networks in 55 older adults with mild cognitive impairment (MCI) and 50 cognitively normal healthy…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9555083/"
                                       >PMC9555083</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e functional magnetic resonance imaging, we prospectively investigated whether changes in dynamic functional connectivity were associated with changes in memory and executive function. We examined 34 <mark class="annotated-text">breast cancer</mark> patients that received chemotherapy, 32 patients that did not receive chemotherapy, and 35 no-cancer controls. All participants were assessed prior to treatment and six months after completion of che…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9581823/"
                                       >PMC9581823</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …, the graph-theory method is applied to generate the topological organization of whole-brain connectivity networks and determine differences in topological properties among healthy controls (HCs) and <mark class="annotated-text">patients with WMHs</mark>. Moreover, comprehensive neuropsychological scales were used to assess cognitive function in multiple cognitive domains in patients with WMHs. We hypothesized that patients with WMHs would show incre…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9688268/"
                                       >PMC9688268</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">others (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …e) used as the feature vector for subject-level prediction. 
  

### Dynamic Conditional Correlation Model 
  
To model dynamic functional connectivity between resting-state networks, we consider the <mark class="annotated-text">Dynamic Conditional Correlation (DCC)</mark> model of [ ]. Let    Z    = (  Z  ,   Z  )′ be a random vector representing a pair of BOLD time series of any two ROIs in the brain at time   t  , for each of   i   = 1, …,   N   subjects. For simpli…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5761874/"
                                       >PMC5761874</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ase coherence, multiple temporal derivative, or dynamic conditional correlation approach (Glerean, Salmi, Lahnakoski, Jääskeläinen, &amp; Sams,  ; Lindquist et al.,  ; Shine et al.,  ). 

This study used <mark class="annotated-text">dynamic conditional correlation (DCC)</mark> without moving average (Engle,  ; Lindquist et al.,  ), which is based on the multivariate generalized autoregressive conditional heteroscedasticity model (Engle,  ) that can be effective for estimat…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7416060/"
                                       >PMC7416060</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ually is. Here, we propose an alternative approach that models changes in the mean brain activity and in the FC as being able to occur at different times to each other. We refer to this method as the <mark class="annotated-text">Multi-dynamic Adversarial Generator Encoder (MAGE)</mark> model, which includes a model of the network dynamics that captures long-range time dependencies, and is estimated on fMRI data using principles of Generative Adversarial Networks. We evaluated the a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8907871/"
                                       >PMC8907871</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … (CS + E), the unextinguished CS + (CS + U), and the CS−, to assess their extinction memory. 


### Dynamic functional connectivity 
  
As in our previous study [ ], we estimated the dynamic FC using <mark class="annotated-text">a jackknife procedure</mark>, such that we could measure the relative difference in FC at a specific trial compared to other trials [ ]. We divided the whole-brain into 432 regions, including 400 cortical regions [ ] and 32 subc…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9126814/"
                                       >PMC9126814</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … ;  ;  ;  ;  ;  ;  ;  ). 

Like these approaches, to estimate brain networks’ connectivity that is 1) directed, 2) interpretable, 3) flexible, and 4) dynamic, we have developed an approach called the <mark class="annotated-text">Directed Instantaneous Connectivity Estimator (DICE)</mark>: a predictive model to estimate dynamic directed connectivity between brain networks, represented as a dynamically varying directed graph by predicting the downstream binary label. Our model may be p…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9844250/"
                                       >PMC9844250</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …d subcortical regions of the Automated Anatomical Labeling (AAL) atlas ( ) were extracted. 


### Dynamic functional connectivity with LEiDA 
  
The dynamic functional connectivity was assessed using <mark class="annotated-text">LEiDA</mark>, a method that allowed us to determine changes in connectivity on a quasi-instantaneous level, by utilizing phase coherence between brain areas ( ). An overview of the steps of this method can be see…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9969260/"
                                       >PMC9969260</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …hosis (HCPEP) study (controls   n   = 53, non-affective psychosis   n   = 82) and the Cobre study (controls   n   = 71, cases   n   = 59). In this work we extend Leading Eigenvector Dynamic Analysis (<mark class="annotated-text">LEiDA</mark>) to capture specific features of dynamic functional connectivity and then implement a novel approach to estimate metastability. We used non-parametric testing to evaluate group-level differences and …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10035891/"
                                       >PMC10035891</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">not applied dFC (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ity related to cognition or behavior or do they represent changes in vigilance and arousal? The question of how ubiquitous is sleep during the resting-state is closely related to this issue ( ). 
  

<mark class="annotated-text">In this focused review </mark>we discuss how, when faced with such questions, the combination of fMRI with other neuroimaging methods (such as EEG and MEG) can help prove or disprove the neurophysiological relevance of dynamic cha…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4329798/"
                                       >PMC4329798</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ty networks (ICNs), which consist of spatially and temporally distributed, but functionally connected, nodes. The coordinated activity of the resting state can be explored via magnetoencephalography (<mark class="annotated-text">MEG</mark>) by studying frequency-dependent functional brain networks at the source level. Although many algorithms for the analysis of brain connectivity have been proposed, the reliability of network metrics …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6088195/"
                                       >PMC6088195</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …reflect functional integration of the brain. Alteration in brain functional connectivity (FC) is expected to provide potential biomarkers for classifying or predicting brain disorders. In this paper, <mark class="annotated-text">we present a comprehensive review</mark> in order to provide guidance about the available brain FC measures and typical classification strategies. We survey the state-of-the-art FC analysis methods including widely used static functional co…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6088208/"
                                       >PMC6088208</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …erent timescales and in separate brain areas so we can understand what is said? This is the language binding problem. Dynamic functional connectivity (brief periods of synchronization in the phase of <mark class="annotated-text">EEG</mark> oscillations) may provide some answers. Here we investigate time and frequency characteristics of oscillatory power and phase synchrony (dynamic functional connectivity) during speech comprehension. …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6194231/"
                                       >PMC6194231</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …f the temporal reconfigurations of FC occurring within RS fMRI sessions has been defined as   time-varying functional connectivity (TVC)   (Hutchison et al.,  ; Calhoun et al.,  ; Preti et al.,  ). 

<mark class="annotated-text">The main goal of this review is to summarize the main results obtained using TVC in healthy and diseased populations.</mark> A particular focus is given to studies of patients with MS; however, the main findings of investigations performed in neurodegenerative and psychiatric conditions are also reported. The review is str…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6636554/"
                                       >PMC6636554</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …on of brain electrophysiological activity. In this study, we investigated abnormal alterations due to mild Traumatic Brain Injury (mTBI) using DFC of the source reconstructed magnetoencephalographic (<mark class="annotated-text">MEG</mark>) resting-state recordings. Brain activity in several well-known frequency bands was first reconstructed using beamforming of the MEG data to determine ninety anatomical brain regions of interest. A D…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6974679/"
                                       >PMC6974679</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …EEG

# Keywords

EEG
HMM
dynamic functional connectivity
3D visual discomfort


# Abstract
 
Stereoscopic displays can induce visual discomfort despite their wide application. Electroencephalography (<mark class="annotated-text">EEG</mark>) technology has been applied to assess 3D visual discomfort, because it can capture brain activities with high temporal resolution. Previous studies explored the frequency and temporal features relev…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9313185/"
                                       >PMC9313185</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">Hidden Makrov Model (5 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ed by the product HMM. This large state space allowed by this multi-dimensional approach enables a better consideration of dynamic aspects without requiring a reduction of upstream data. 

Within the <mark class="annotated-text">product HMM</mark> framework, this paper compares brain DFC between patients with dementia with Lewy bodies (DLB) and healthy elderly controls. DLB is the second most prevalent form of neurodegenerative dementia after …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4918689/"
                                       >PMC4918689</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …EAL DATA 
  
Having demonstrated the utility of the NPC approach to relate FC to behavior in a synthetic scenario where the estimation was very noisy, we next evaluated it using real data by applying <mark class="annotated-text">the Hidden Markov model (HMM)</mark> to resting state fMRI data from the Human Connectome Project (HCP). The HMM assumes that the data can be described using a finite number of states. Each state is represented using a probability distr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6492297/"
                                       >PMC6492297</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …or and static, as compared to time-varying, rsFC. Static rsFC was estimated by computing a node-node correlation matrix across all regions of the brain. Time-varying rsFC was estimated by fitting a   <mark class="annotated-text">(HMM)</mark> to the data. The HMM allowed for the characterization of, and transition likelihood between, multiple latent “states” in a data-driven fashion as fast as the modality allowed, overcoming limitations …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7935045/"
                                       >PMC7935045</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …d a state-based model where each state is associated with a specific pattern of FC ( ), such that instantaneous changes in FC manifest as a change of state. This approach is based on a version of the <mark class="annotated-text">hidden Markov model (HMM)</mark> that, in comparison to previous versions of the HMM used on fMRI ( ;  ;  ;  ;  ), emphasises changes in FC over changes in amplitude. To model each subject, the HMM uses a temporally-organised mixtur…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7994296/"
                                       >PMC7994296</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … correlated) across brain regions. Any transient departure from (the time-averaged) orthogonality will be encoded by the HMM parameters   γ   and   Σ  , and can be considered an FC modulation. 


### <mark class="annotated-text">HMM-PCA</mark>: A new model for estimating time-varying FC 
  
I now introduce the HMM-PCA mathematically. Various of the elements of this model are analogous to the probabilistic mixture model of PCA analysers int…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8081334/"
                                       >PMC8081334</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">cognitive application (5 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …cy analysis were also performed to further characterize the temporal covariance and frequency specificity of these fluctuations. This study has enabled us to capture the dynamics of the resting brain <mark class="annotated-text">under sedation</mark> and used fMRI to validate theoretical models of consciousness. 


## Results 
  
In total, 14 patients (M:F, 8:6; mean age 46.9 ± 11.3 years) successfully completed both the baseline awake and sedate…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5561230/"
                                       >PMC5561230</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …c FC (dFC) patterns contain sufficient information to permit identification of ongoing tasks. Here, we hypothesize that dFC patterns carry fine-grained information that allows for tracking short-term <mark class="annotated-text">task engagement</mark> levels (i.e., 10s of seconds long). To test this hypothesis, 25 subjects were scanned continuously for 25 min while they performed and transitioned between four different tasks: working memory, visua…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6326730/"
                                       >PMC6326730</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …studies only had access to basic measures of human behavior, lacking access to measures typically employed by cognitive neuroscientists studying  , cognitive control, and  . 

To directly address the <mark class="annotated-text">behavioral</mark> differences captured by static and time-varying FC, we utilized resting-state blood oxygen level–dependent (BOLD) data collected alongside a battery of complex behavior and personality measures. Thes…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7935045/"
                                       >PMC7935045</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …, these are normally subtle effects, and other researchers have reported little or no differences in FC between task and rest ( ;  ). 

Here, we take a different route, by relating time-varying FC to <mark class="annotated-text">population variability in behavioural traits</mark>. For this purpose, we implemented a framework to predict subject behavioural traits from either time-varying FC, time-averaged FC, or structural data. Critically, this was done in such a way that the…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7994296/"
                                       >PMC7994296</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …iobank (13301 subjects). Importantly, we find that separating fluctuations in the mean activity levels from those in the FC reveals much stronger changes in FC over time, and is a better predictor of <mark class="annotated-text">individual behavioural variability. </mark>
 

# Body
 
## Introduction 
  
Large-scale networks of brain activity can be detected as fluctuations of blood oxygenation levels in functional magnetic resonance imaging (fMRI) ( ,  ). These functi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8907871/"
                                       >PMC8907871</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">Time-Frequency (4 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …unctional sequence. The detailed steps of spatial regression could be found in previous studies .   
Names of template ICNs. 
  


### Inter-ICN variability 
  
The inter-ICN variability was based on <mark class="annotated-text">Hilbert transform</mark> with the following procedures: 1) obtain pair-wise time-courses of ICNs; 2) apply Hilbert transform on the two time-courses; 3) obtain the instantaneous phases of each time-course; 4) compute the ins…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6081414/"
                                       >PMC6081414</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …are sensitive to nonlinear interdependences between subsystems. 

Estimates of dynamic, instantaneous interactions are obtained by examining the behavior of phase differences between time series. The <mark class="annotated-text">Hilbert transform</mark> is first applied to each system’s time series, allowing an estimate of the instantaneous phase (and amplitude) of a signal (Tass et al.,  ). The Hilbert transform of a time series   x  (  t  ) is giv…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6130444/"
                                       >PMC6130444</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s shaped the field of dynamic functional connectivity (DFC). Mainstream DFC research relies on (sliding window) correlations to identify recurrent FC patterns. Recently, functional relevance of the   <mark class="annotated-text">instantaneous phase synchrony   (IPS)</mark> of fMRI signals has been revealed using imaging studies and computational models. In the present paper, we identify the repertoire of whole-brain inter-network IPS states at rest. Moreover, we uncove…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7118690/"
                                       >PMC7118690</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …n different brain regions using resting-state
functional magnetic resonance imaging (rs-fMRI) data. One way to assess the
relationship between signals from different brain regions is to measure their
<mark class="annotated-text">phase synchronization</mark> (PS) across time. There are several ways to perform such
analyses, and we compare methods that utilize a PS metric together with a
sliding window, referred to here as windowed phase synchronization (…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8011682/"
                                       >PMC8011682</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">Co-Activation Patterns (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … clusters (in total, 58 clusters or CAPs) were evaluated. We aggregated the fMRI volumes assigned to each cluster. The mean image of such a cluster&#39;s volumes provided an overall view of the resulting <mark class="annotated-text">CAP</mark> and was then normalized by the standard error (within‐cluster and across fMRI volumes) to generate   z  ‐statistic maps, which quantify the degree of significance to which the CAP map values for each…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8213933/"
                                       >PMC8213933</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">Window-less (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">other application (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```
