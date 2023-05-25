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
        <summary class="label-display">Sliding Window (14 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
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
                    …cients were calculated for each pair of regions, representing the functional connectivity between these two nodes in the network. 

When measuring dynamic functional connectivity (d-FC), we adopted a <mark class="annotated-text">sliding-window</mark> method, with window length = 100 TR (200 s) and step size = 3 TR (6 s). A previous research proved that this combination can extract as much features while minimizing computation costs [ ]. The prepr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7485713/"
                                       >PMC7485713</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … ROI were obtained in the subject’s fMRI space. Static FC were estimated by computing the Pearson’s correlation coefficient between time series from each ROI pair. Dynamic FC were estimated using the <mark class="annotated-text">sliding-window</mark> method with both SSTD window-sizes and multiple conventional fixed window-sizes. Pearson’s correlation between time series from all ROI pairs were computed within the defined window and the window wa…
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
                    …removal of detected outliers, and (d) low‐pass filtering with a cutoff frequency of 0.15 Hz. 


### Dynamic functional network connectivity 
  
For each subject, dynamic FNC (dFNC) was estimated by a <mark class="annotated-text">sliding window</mark> approach. A tapered window, created by convolving a rectangle (width = 20 TRs = 40 s, TR = 2 s) with a Gaussian (  σ   = 3 TRs), was used to segment the TCs. We slid the window in steps of 1 TR, resu…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7721229/"
                                       >PMC7721229</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … patients with ASDs. 

In the current study, rs-fMRI data from Autism Brain Imaging Data Exchange II (ABIDE II) were used, and 29 core seeds of 10 classic functional networks were selected to perform <mark class="annotated-text">sliding-window</mark> seed-to-whole-brain DFC analyses in a comprehensive manner. Moreover, the relationships between significant DFC changes and symptom severity were further explored in patients with ASDs. Furthermore, …
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
                    …brain sFC matrix was generated. In this experiment, one resting‐state sFC matrix and one natural viewing sFC matrix was separately obtained for each subject during each session. 


####  dFC  
  
The <mark class="annotated-text">sliding‐window</mark> strategy was adopted to assess the dFC time series. Briefly, a rectangle time window with an interval of one TR was applied. Within each sliding window, the Pearson correlation coefficients between e…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8837589/"
                                       >PMC8837589</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">Clustering (8 docs)</summary>
        
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
            
            <div class="annotation">
                <div class="context">
                    …### Dynamic FC analysis 
  
Dynamic FC analysis was performed using the Dynamic Brain Connectome (Dynamic BC) toolbox (Liao et al.  ) (V2.1  ). Temporal dynamic patterns were characterized by using a <mark class="annotated-text">sliding-window approach</mark>, which was created by convolving a rectangle with a Gaussian kernel (σ = 3TRs). Previous studies have revealed that a frequency interval of [0 − 1/w] Hz should be the target due to the low-pass filte…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7275001/"
                                       >PMC7275001</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …of windows was calculated and the Fisher Z-transformed used to acquire variables similar to a normal distribution (Liao et al.  ). 


### Clustering analysis 
  
To assess reoccurring dFC patterns, a <mark class="annotated-text">k-means clustering algorithm</mark> was used to analyze dFC estimates of all subjects (combining the lung cancer and HC groups) (Allen et al.  ). We used the L1 distance function to assess the similarity between sliding window FCs, as …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7275001/"
                                       >PMC7275001</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">clinical application (8 docs)</summary>
        
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
                    …, the graph-theory method is applied to generate the topological organization of whole-brain connectivity networks and determine differences in topological properties among healthy controls (HCs) and <mark class="annotated-text">patients with WMHs</mark>. Moreover, comprehensive neuropsychological scales were used to assess cognitive function in multiple cognitive domains in patients with WMHs. We hypothesized that patients with WMHs would show incre…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9688268/"
                                       >PMC9688268</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e need for the window-size parameter used in many dynamic connectivity studies. 

To thoroughly validate DICE’s performance, we conduct a series of experiments on four neuroimaging datasets that span <mark class="annotated-text">three disorders</mark> (schizophrenia, autism, and dementia) and cover a wide age range. We train the model on classification tasks for each of these brain disorders, age prediction, and gender classification, and analyze …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9844250/"
                                       >PMC9844250</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">others (5 docs)</summary>
        
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
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">Hidden Makrov Model (4 docs)</summary>
        
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
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">cognitive application (4 docs)</summary>
        
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
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">not applied dFC (3 docs)</summary>
        
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
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">Time-Frequency (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
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
