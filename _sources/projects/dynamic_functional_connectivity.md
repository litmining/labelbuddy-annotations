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
    
    <details style=&#34;--label-color: #ff9896;&#34;>
        <summary class="label-display">SW (14 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … while unmedicated (  n   = 34), after 1 week (  n   = 29) and 6 weeks of treatment with risperidone (  n   = 24), as well as matched controls at baseline (  n   = 35) and after 6 weeks (  n   = 19). <mark class="annotated-text">After identifying 41 independent components (ICs) comprising resting-state networks, sliding window analysis was performed on IC timecourses using an optimal window size validated with linear support vector machines. </mark>Windowed correlation matrices were then clustered into three discrete connectivity states (a relatively sparsely connected state, a relatively abundantly connected state, and an intermediately connect…
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
                    … outlined with a small black box are indicated if   p   &lt; 0.05. No significant differences were observed when week 1 patients were compared to baseline and week 6 patients. 
  

### dFNC Analysis 
  
<mark class="annotated-text">A sliding window technique was used to estimate dFNC where windowed segments of the component time courses were used to compute transient functional network connectivity patterns (Figure  ). Sliding window analysis was iteratively performed with window sizes of 30, 40, 44, 50, and 60 s. </mark>Window sizes were selected based on previous studies indicating functional connectivity can be robustly estimated using a window size between 30 and 60 s ( ,  ), as well as previous implementation of …
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
                    …spherical ROI in the medial primary motor cortex (Montreal Neurological Institute coordinates=−1, −8, 63), a region not previously linked to depression. 


### Sliding window correlation analysis 
  
<mark class="annotated-text">The sliding window analysis was performed using custom Python ( ) scripts. The data were split into 40 s Gaussian moving windows, staggered by one repetition time, created using a Gaussian kernel with a standard deviation of 8 s (see   for a detailed discussion of the sliding window methodology).</mark> This time period has been shown to be appropriate for characterizing dynamic functional connectivity  and provides a fine-grained picture of temporal changes in connectivity. For each window, correla…
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
                    … 


## Methods 
  
Whole-brain resting-state functional MRI data were acquired on a 3 T whole-body clinical MRI scanner from 18 subjects clinically diagnosed with JME and 25 healthy control subjects. <mark class="annotated-text">2-min sliding-window approach was incorporated in the quantitative data-driven data analysis framework to assess both the dynamic and static functional connectivity in the resting brains. </mark>Two-sample   t  -tests were performed voxel-wise to detect the differences in functional connectivity metrics based on connectivity strength and density. 


## Results 
  
The static functional connec…
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
                    … 2) Connection Count Index (CCI) which is the number of voxel pairs involving the current voxel in question with the absolute CC ≥ 0.3. 


### Dynamic functional connectivity with SWATCH analysis 
  
<mark class="annotated-text">To characterize the time variations of the CCI and CSI maps we incorporated a 2 min sliding window into the quantitative data-driven analysis procedure. We computed CCI and CSI maps for every 2 min window (60 time-frames). The increment between the adjacent sliding windows was one frame, therefore, we obtained a time series of CCI and CSI maps with 235 time-frames for each Resting-state functional MRI dataset. </mark>Then, we computed the voxel-wise temporal averages of the 2-min sliding window CCI and CSI time series for each Resting-state functional MRI dataset for further statistical analysis. The pipeline of t…
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
                    …he backward difference formula, Dw FNC = w FNC – w FNC. Subjects’ DdFNC data is formed by all wFNC derivatives, and is referred to as the first order derivatives of the sliding window correlations. 

<mark class="annotated-text">The tvFNC method pipeline is as follows, for all subjects (1) compute dFNC data (sliding windowed correlations wFNC); (2) estimate DdFNC data (derivatives of sliding windowed correlations DwFNC)</mark>; (3) concatenate row wise zero and first order windowed correlations [wFNC and DwFNC] divided by their corresponding standard deviations ( ). The tvFNC data is formed by stacking time-wise all subjec…
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
                    …a. Functional connectivity was estimated as the Pearson correlation coefficient between the timecourses of each pair of ROIs, over the full scanning length. 


### Dynamic functional connectivity 
  
<mark class="annotated-text">Dynamic connectivity matrices were derived using an overlapping sliding-window approach . For each subject and each condition, tapered sliding windows were obtained by convolving a rectangle of 22 TRs (44s) with a Gaussian kernel of 3 TRs, sliding with 1 TR step size. </mark>This resulted in 229 windows/timepoints per condition for the awake and anaesthetised subjects, and 273 windows for the DOC patients. 

Within each of the resulting overlapping temporal windows of 22 …
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
                    …ction of the “Uncertain” network is not specific, we mainly paid attention to the other 12 brain networks consisting of 236 seed sites. 


### Dynamic Functional Network Connectivity Construction 
  
<mark class="annotated-text">The 236 available ROIs were used to analyze DFC using DynamicBC toolbox ( ). Since there was no formal consensus on window length, dynamic functional network connectivity (dFNC) was constructed using the sliding-window Pearson&#39;s correlation method with a length of 20 TRs (40 s) and a step size of 1TR, as previously performed ( ), resulting in 111 windows.</mark> In each window, we computed Pearson correlation coefficients between the time series of each pair of the 236 ROIs. As a result, we obtained a 236 × 236 matrix of Pearson correlation coefficients betw…
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
                    …(DFC) and developed an accurate and objective image-based diagnosis system for MDD. 


## Methods 
  
MRI images were collected from 99 participants including 56 healthy controls and 43 MDD patients. <mark class="annotated-text">DFC was calculated using a sliding-window algorithm. </mark>A non-linear support vector machine (SVM) approach was then used with the DFC matrices as features to distinguish MDD patients from healthy controls. The spatiotemporal characteristics of the most dis…
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
                    … of the regions numbered 255 with a low probability density was not identified, thus 273 regions were left. Then, Pearson’s correlation coefficient was used for measuring the functional connectivity. <mark class="annotated-text">DFC between any pair of these regions was then calculated using a sliding-window algorithm. </mark>Sliding-window algorithm is one of the most widely used to evaluate dynamic brain functional connectivity. The functional connectivity between two nodes was first calculated using a subsection of the …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7118554/"
                                       >PMC7118554</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style=&#34;--label-color: #aec7e8;&#34;>
        <summary class="label-display">SWC (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … 41 independent components (ICs) comprising resting-state networks, sliding window analysis was performed on IC timecourses using an optimal window size validated with linear support vector machines. <mark class="annotated-text">Windowed correlation matrices were then clustered into three discrete connectivity states (a relatively sparsely connected state, a relatively abundantly connected state, and an intermediately connected state)</mark>. In unmedicated patients, static connectivity was increased between five pairs of ICs and decreased between two pairs of ICs when compared to controls, dynamic connectivity showed increased connectiv…
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
                    …y in differentiating control and patient ALFF-FC using the SVM classifier. This SVM classification was performed using the Statistics and Machine Learning Toolbox in MATLAB ( ). 


### Clustering 
  
<mark class="annotated-text">In order to characterize reoccurring patterns of connectivity across groups and time,   k  -means clustering was performed on the windowed correlation matrices for all subjects (Figure  B)</mark>. Clustering of a sub-sampled number of windows (i.e., windows with relative maxima of variance) for all groups and time points was carried out in order to estimate initial cluster centroids (cluster …
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
                    … of the sliding window correlations; (4) run clustering analysis on all subjects’ tvFNC data to identify reoccurring connectivity states and their derivatives patterns. 


### Clustering Analysis 
  
<mark class="annotated-text">In both methods dFNC and tvFNC, time-varying connectivity is captured by performing k-means clustering analysis, assigning all subjects’ temporal FNC data into a selected number of clusters representing distinct functional connectivity states. </mark>The clustering algorithm selection is based on previous connectivity studies that successfully applied k-means algorithm to identify reoccurring patterns of connectivity within and between subjects ac…
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
                    …e produced for each timepoint (using MATLAB code made freely available by Shine et al. at  ) , since together, these two measures quantify both a node’s inter- modular and intra-modular connectivity. <mark class="annotated-text">For each subject, the joint patterns were then used to assign each timepoint to one of two clusters, using an unsupervised machine learning algorithm known as k-means clustering (setting   k   = 2)</mark> . To avoid the possibility of the algorithm becoming stuck in local minima, it was repeated 500 times with random re-initialisation of the two clusters’ initial points. This was performed individuall…
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
                    …could be quantitatively estimated and compared between different groups. The original FCV matrices were then Fisher   z  -transformed and were statistically compared. 


###  k  -means Clustering 
  
<mark class="annotated-text">To identify dFNC patterns reoccurring across temporal matrices,   k  -means clustering was employed on all the dynamic correlation matrices to divide the dFNC into discrete clusters. </mark>The   k  -means algorithm aggregates information with similarities into “  k  ” groups, ensuring that the sum of squares within clusters is minimal. During the clustering estimation, the correlation d…
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
                    …viation of each voxel across a number of windows was calculated and the Fisher Z-transformed used to acquire variables similar to a normal distribution (Liao et al.  ). 


### Clustering analysis 
  
<mark class="annotated-text">To assess reoccurring dFC patterns, a k-means clustering algorithm was used to analyze dFC estimates of all subjects (combining the lung cancer and HC groups) (Allen et al.  )</mark>. We used the L1 distance function to assess the similarity between sliding window FCs, as L1 distance has been proved to be an effective measurement method for high-dimensional data (Aggarwal et al. …
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
                    …he functional connectivity matrices will be transformed to z-scores using Fisher’s z-transformation and covariates (age, gender, and education) will be regressed out. 


##### Clustering analysis 
  
<mark class="annotated-text">A K-means clustering algorithm will be applied to the windowed functional connectivity matrices to assess the recurring functional connectivity patterns (states), as expressed by the frequency and structure of these states</mark>. Then a cluster validity analysis will be performed on the exemplars of all subjects to estimate the optimal number of clusters. We will use a subset of windows (local maxima in functional connectivi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8461094/"
                                       >PMC8461094</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …t. We flipped the corresponding regions of the right hemisphere to the left hemisphere in right TLE‐HS patients and proportionate HC for the following analysis. 


### Dynamic functional analysis 
  
<mark class="annotated-text">Dynamic functional analysis was performed using DynamicBC toolbox ( ) with the sliding‐window approach and k‐mean clustering method (see Supporting Information Figure   in Appendix S1).</mark> First, to capture the hippocampal network time‐varying correlations, we segmented the whole time series into a fixed window with a width of 20 TRs. This setting has demonstrated good balance between …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8933317/"
                                       >PMC8933317</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … With a step‐wise slide of 1 TR along the 170‐TR length scan, we constructed 150 successive 24 × 24 matrices for each subject. The resulting correlation matrices were converted to z‐values with Fz. 

<mark class="annotated-text">Second, we used the K‐means clustering algorithm to cluster dynamic FC patterns across control and patients together (Lloyd,  ). </mark>This clustering algorithm was repeated 100 times to weaken the impact of local minima (Pascual‐Marqui, Michel, &amp; Lehmann,  ). The correlation distance function was used to measure similarity between F…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8933317/"
                                       >PMC8933317</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style=&#34;--label-color: #98df8a;&#34;>
        <summary class="label-display">others (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … temporal and spectral domains. (d) Temporal and spectral features are concatenated and (e) used as the feature vector for subject-level prediction. 
  

### Dynamic Conditional Correlation Model 
  
<mark class="annotated-text">To model dynamic functional connectivity between resting-state networks, we consider the Dynamic Conditional Correlation (DCC) model of [ ]</mark>. Let    Z    = (  Z  ,   Z  )′ be a random vector representing a pair of BOLD time series of any two ROIs in the brain at time   t  , for each of   i   = 1, …,   N   subjects. For simplicity, below w…
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
                    …instantaneous phase coherence, multiple temporal derivative, or dynamic conditional correlation approach (Glerean, Salmi, Lahnakoski, Jääskeläinen, &amp; Sams,  ; Lindquist et al.,  ; Shine et al.,  ). 

<mark class="annotated-text">This study used dynamic conditional correlation (DCC) without moving average (Engle,  ; Lindquist et al.,  ), which is based on the multivariate generalized autoregressive conditional heteroscedasticity model (Engle,  ) that can be effective for estimating nonstationary temporal associations when the model of time series is well‐known</mark> (Lebo &amp; Box‐Steffensmeier,  ). We used the code implemented by Lindquist et al. ( ) shared in  , which ran on MATLAB R2018b utilizing 120 high‐performance computing SLURM nodes. It first performs est…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7416060/"
                                       >PMC7416060</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style=&#34;--label-color: #ffbb78;&#34;>
        <summary class="label-display">HMM (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …t  ] 
  

## DYNAMIC FUNCTIONAL CONNECTIVITY IN REAL DATA 
  
Having demonstrated the utility of the NPC approach to relate FC to behavior in a synthetic scenario where the estimation was very noisy, <mark class="annotated-text">we next evaluated it using real data by applying the Hidden Markov model (HMM) to resting state fMRI data from the Human Connectome Project (HCP). The HMM assumes that the data can be described using a finite number of states. </mark>Each state is represented using a probability distribution, which in this case is chosen to be a Gaussian distribution (Vidaurre, Smith, &amp; Woolrich,  ); that is, each state is described by a character…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6492297/"
                                       >PMC6492297</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style=&#34;--label-color: #c5b0d5;&#34;>
        <summary class="label-display">CAP (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …e volumes and mask were later used with FSL randomise. 

The volumes were reshaped and concatenated, and the resulting data matrix was transferred to the R environment (Bengtsson,  ; R Core Team,  ). <mark class="annotated-text">We applied clustering to all the BOLD fMRI volumes acquired from the 55 participants that had survived censoring.</mark> As mentioned in the introduction, the volumes are described by their voxels&#39; signal amplitudes, and their relation to other volumes has to be defined via a suitable function. Here, individual volumes…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8213933/"
                                       >PMC8213933</a></div>
                    <div class="annotator-name">mtorabi59</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …r‐package function hclust (method = &#34;ward.D2&#34;) (Müllner,  ). The results from 30 to 2 clusters (in total, 58 clusters or CAPs) were evaluated. We aggregated the fMRI volumes assigned to each cluster. <mark class="annotated-text">The mean image of such a cluster&#39;s volumes provided an overall view of the resulting CAP and was then normalized by the standard error (within‐cluster and across fMRI volumes) to generate   z  ‐statistic maps, which quantify the degree of significance to which the CAP map values for each voxel deviate from zero (Liu et al.,  ,  ). </mark>


### Group comparison   t   tests 
  
The 11,930 RS‐fMRI volumes concatenated into one file were used as input for FSL&#39;s randomise (Anderson &amp; Robinson,  ; Winkler et al.,  ). The voxel‐wise differe…
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
    
</div>
"""
displays.HTMLDisplay(text)
```