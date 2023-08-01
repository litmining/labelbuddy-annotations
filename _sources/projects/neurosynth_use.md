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


# neurosynth_use

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/neurosynth_use/).

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
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">specific_thing_used (6 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … from observed patterns of brain activity and thus to make quite specific statements about the role of a region in the function under question. Also the NeuroSynth framework allows one to compute the <mark class="annotated-text">posterior probability</mark>, i.e., to quantify the probability, that an activated voxel is associated with a particular cognitive function (Yarkoni et al.,  ). We used the NeuroSynth framework to compute the reverse inference  …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4009443/"
                                       >PMC4009443</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rated component 22 thresholded at   p   &lt; 0.01 FDR. The SCA cluster map and the component 22 are significantly correlated (  r   = 0.51;   p   &lt; 0.001 corrected for multiple comparisons).   (C)   The <mark class="annotated-text">z mask</mark> for the feature “language” from the meta-analysis platform NeuroSynth thresholded at   p   &lt; 0.001 FDR. The SCA cluster map and the z mask “language” are significantly correlated (  r   = 0.47;   p  …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4009443/"
                                       >PMC4009443</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …d dorsal/posterior IFG to the response we observed in pMTG. Full details of this sample can be found in  . (ii) Data from  , implemented in Neurosynth ( ), was used in a final step to investigate the <mark class="annotated-text">functional connectivity</mark> of the pMTG site we obtained across different analyses. We compared the functional behaviour of the pMTG across these different cohorts to minimise the duration of specific testing sessions and to al…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4927261/"
                                       >PMC4927261</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … functional connectivity. The resulting map overlapped with the   meta-analysis in inferior frontal gyrus and also showed connectivity with temporal parietal junction and pre-SMA (  right panel). The <mark class="annotated-text">connectivity map</mark> for pMTG was also compared with the DMN and the multiple-demand network ( ) and it extended into both of these networks, including overlap with the MDN in IFS, precentral gyrus (PCG), dorsal IFG, IPS…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4927261/"
                                       >PMC4927261</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …diction, the remaining nodes in the whole-brain prediction, the important nodes in the default mode network-based prediction, and the remaining nodes in the default mode network-based prediction. The <mark class="annotated-text">Neurosynth Image Decode</mark>r enabled us to compare each map to meta-analytic images related to various psychological constructs in the Neurosynth database. 


### Specificity of the Predictive Effects 
  
We tested the specific…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8278332/"
                                       >PMC8278332</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tentional networks. This involves brain regions like dorsolateral prefrontal cortex (DLPFC), anterior cingulate (AC), inferior frontal gyrus (IFG), and parietal regions. Map prepared using Neurosynth <mark class="annotated-text">meta-analysis</mark> of the term working memory (Yarkoni et al.,  ). Similar neural networks show decreased signals in attention deficit hyperactivity disorder (ADHD) patients performing working memory tasks. 
  
Two gen…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8334010/"
                                       >PMC8334010</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …x, bilateral temporal poles (SPM Anatomy Toolbox ), as well as the dorsomedial prefrontal cortex (dmPFC) derived from Neurosynth  by searching the term “dmPFC” in the automated meta-analysis tool and <mark class="annotated-text">downloading the relevant mask</mark>. Because Neurosynth meta-analytic maps can include regions that simply co-occur with the search term, we masked the resulting map with the medial frontal gyrus from the Wake Forest University (WFU) P…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9582022/"
                                       >PMC9582022</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e Neurosynth database contains activation maps of 1335 behavioral terms that describe nearly all aspects of human behavior. For each term, cross-sample correlation analyses were performed between its <mark class="annotated-text">activation values</mark> and gene expression measures, resulting in a set of correlation coefficients corresponding to the genes. A positive correlation coefficient indicates that a brain region with higher gene expression t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9968350/"
                                       >PMC9968350</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">using_neurosynth_data (5 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ent with the highest correlation coefficient was identified. The significance of that correlation was corrected for multiple comparisons by means of the same procedure proposed by Smith et al. ( ). 

<mark class="annotated-text">The relevance of the observed SCA cluster map for language was evaluated with the NeuroSynth database ( ). NeuroSynth is an internet based platform for large-scale, automated synthesis of functional magnetic resonance imaging (fMRI) data extracted from over 4393 published articles, which cover over 147,493 activations (Yarkoni et al.,  ). The most appealing advantage of that platform is its ability to quantitatively distinguish forward inference from reverse inference. While a forward inference is able to identify brain regions that are consistently activated during a cognitive function in question, the reverse inference identifies brain regions that are preferentially involved in that specific function. A forward inference may not be very specific because some brain regions like the anterior cingulate are consistently active during many different cognitive tasks. However, by means of reverse interference it is possible to quantitatively identify cognitive states or functions from observed patterns of brain activity and thus to make quite specific statements about the role of a region in the function under question. Also the NeuroSynth framework allows one to compute the posterior probability, i.e., to quantify the probability, that an activated voxel is associated with a particular cognitive function (Yarkoni et al.,  ). We used the NeuroSynth framework to compute the reverse inference   z  -value of the two seeds used for the SCA for the NeuroSynth feature “language” as well to test their posterior probability for that feature. As database for the NeuroSynth feature “language” serves an automated meta-analysis of the 553 task evoked fMRI studies. Also the NeuroSynth framework provides an option to generate and download a z mask for the investigated feature thresholded at   p   = 0.05 (FWE corrected). We used that mask “language” from NeuroSynth as a template to perform a second spatial sorting of the 70 independent components from the ICA and then compared these results with the results of the previous sorting by means of the cluster mask, that was generated by the SCA. </mark>


### Definition of the nodes, construction of an adjacency matrix, and modeling a graph-network 
  
The cluster map of the two seeds in Broca&#39;s area showed totally 24 clusters (  k   = 56–6454 voxel…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4009443/"
                                       >PMC4009443</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …onents by a correlation analysis revealed that component 22 correlated significantly at   r   = 0.51 (  p   &lt; 0.001, corrected for multiple comparisons) with the cluster mask from the previous SCA. 

<mark class="annotated-text">By means of the NeuroSynth framework, we computed for the two seeds which were used for the SCA a reverse inference z map as well as the posterior probability that the two seeds from the SCA are language relevant indeed. The seed located within the pars triangularis (−53 +20 +15) showed a z score of 8.17 corresponding to the likelihood that the feature “language” is used in a study given the presence of this activation, and posterior probability of 0.77 corresponding to the estimated probability of the feature “language” being used given the presence of an activation at this location. The seed located within the pars opercularis (−46 +16 +8) showed a z score of 4.69 for the reverse inference and a posterior probability of 0.69, that the feature “language” is used given an activation peak at this location. The result of the second spatial sorting of the 70 components with the corresponding z map for the feature “language,” that is based on an automated meta-analysis of 553 studies on language by the NeuroSynth platform, as the spatial template yielded a correlation with the component 22 of   r   = 0.47, which is highly significant at   p   &lt; 0.001 (corrected for multiple comparisons). Thus, the highly significant correlations of independent component 22 with the cluster mask from the SCA as well as with the reverse inference z map for the feature “language” may indicate, that the here investigated network represents a language relevant function indeed (Figure  ). </mark>
  
 Results of the evaluation of the functional plausibility of the language relevant RSN. (A)   The cluster map for the SCA with seeds within the pars triangularis and the pars opercularis, with an …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4009443/"
                                       >PMC4009443</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …land Enhanced Sample ( ) were used to relate the connectivity patterns of ventral/anterior and dorsal/posterior IFG to the response we observed in pMTG. Full details of this sample can be found in  . <mark class="annotated-text">(ii) Data from  , implemented in Neurosynth ( ), was used in a final step to investigate the functional connectivity of the pMTG site we obtained across different analyses. We compared the functional behaviour of the pMTG across these different cohorts to minimise the duration of specific testing sessions and to allow us to capitalize on the power of large scale publicly available data sets. </mark>


### Study design 
  
Semantic knowledge for items from two semantic categories (animals and tools) was probed using three tasks (see  ). (  i  ) The first task   (global associations  ) involved ma…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4927261/"
                                       >PMC4927261</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ity was taken into account. Prediction analyses of the uncertain network were not performed because the function of the uncertain network was unspecified or unknown. 


### Meta-Analytic Decoding 
  
<mark class="annotated-text">To understand the structural location and psychological function related to the important nodes in whole-brain prediction and in network-based prediction, we performed meta-analytic decoding using the Neurosynth Image Decoder ( ). We chose the important nodes in the default mode network to represent the network-based prediction. We pooled the important nodes or the remaining nodes together as a map and generated four maps: the important nodes in the whole-brain prediction, the remaining nodes in the whole-brain prediction, the important nodes in the default mode network-based prediction, and the remaining nodes in the default mode network-based prediction. The Neurosynth Image Decoder enabled us to compare each map to meta-analytic images related to various psychological constructs in the Neurosynth database. 
</mark>

### Specificity of the Predictive Effects 
  
We tested the specificity of SDNV or life satisfaction change scores in the predictive effects. 

#### Effects of Neural Variability or Interdependent S…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8278332/"
                                       >PMC8278332</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e smoothing effects of other kernels . Non-gridded (i.e., surface) re-samplings were performed using mri_vol2surf (FreeSurfer). 




### Data analysis 
  
#### Region of interest (ROI) definition 
  
<mark class="annotated-text">To assess intrinsic network connectivity, we defined region of interest (ROI) masks for four a priori brain networks implicated in social decision making  (Table  ): the mentalizing network, the cognitive control network, the motivational relevance network, and the affective salience network (see NeuroVault :  ). We defined ROIs using anatomical segmentation for smaller subcortical regions that are easily defined anatomically (e.g., amygdala, ventral striatum). For large cortical regions that perform multiple different functions (e.g., dmPFC, TPJ), we further constrained the ROI based on additional functional information (e.g., from NeuroSynth or the Saxe lab mask). Mentalizing regions included bilateral temporoparietal junction (TPJ) defined from the Saxe Lab , bilateral posterior superior temporal sulcus , posterior cingulate cortex, bilateral temporal poles (SPM Anatomy Toolbox ), as well as the dorsomedial prefrontal cortex (dmPFC) derived from Neurosynth  by searching the term “dmPFC” in the automated meta-analysis tool and downloading the relevant mask.</mark> Because Neurosynth meta-analytic maps can include regions that simply co-occur with the search term, we masked the resulting map with the medial frontal gyrus from the Wake Forest University (WFU) Pi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9582022/"
                                       >PMC9582022</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …he Human Brain Transcriptome database ( ) was employed to characterize the spatial-temporal expression trajectory of hub genes with the highest degree values. 


### Behavioral relevance analysis 
  
<mark class="annotated-text">To capture the behavioral relevance of the genes related to brain functional alterations in DFP, we tested the associations between gene expression and behavioral domains via the Neurosynth ( ), a well-validated and publicly available platform for meta-analysis of neuroimaging literature . The Neurosynth database contains activation maps of 1335 behavioral terms that describe nearly all aspects of human behavior. For each term, cross-sample correlation analyses were performed between its activation values and gene expression measures, resulting in a set of correlation coefficients corresponding to the genes. A positive correlation coefficient indicates that a brain region with higher gene expression tends to show greater neural activation, while a negative correlation coefficient means that a brain region with lower gene expression tends to show greater neural activation. Thus, both positive and negative correlation coefficients indicate that a gene contributes to a behavioral term. To avoid biases due to offset, we averaged the absolute values of these correlation coefficients (|  r   | mean) to index the extent to which this set of genes was linked to each behavioral term. Finally, the behavioral terms were ordered based on their |  r   |   and those with the highest |  r   |   were selected to capture the behavioral relevance of the genes related to brain functional alterations in DFP. Here, a threshold of |  r   |   &gt; 0.2 was chosen for ease of interpretability. </mark>



## Results 
  
### Resting-state brain functional alterations in DFP 
  
After a comprehensive literature search and selection, our meta-analysis included 8 studies comprising 500 DFP and 469 HC. …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9968350/"
                                       >PMC9968350</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #fce94f;">
        <summary class="label-display">citing_study_using_neurosynth (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ssessing shared representation is whether the overlapping brain activity observed really reflects shared   pain-related   processes. Several recent lines of evidence suggest this may not be the case. <mark class="annotated-text">In a meta-analysis of over 3500 neuroimaging studies available from Neurosynth.org, activation in the aINS and dACC were among the most frequently observed findings across all kinds of tasks ( ), suggesting that activation in these regions frequently has nothing to do with pain.</mark> It is possible that activity in portions of the dACC is   preferentially   related to pain on average; for example,   used Neurosynth.org to identify a statistical association between studies using t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4907690/"
                                       >PMC4907690</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rg, activation in the aINS and dACC were among the most frequently observed findings across all kinds of tasks ( ), suggesting that activation in these regions frequently has nothing to do with pain. <mark class="annotated-text">It is possible that activity in portions of the dACC is   preferentially   related to pain on average; for example,   used Neurosynth.org to identify a statistical association between studies using the term &#39;pain&#39; and activation of the dACC. </mark>However, this does not mean that dACC activity is sufficient to infer pain, as the dACC responds to a variety of cognitive and emotional events that are not painful ( ). For instance, electrophysiolog…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4907690/"
                                       >PMC4907690</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ngages executive and dorsal attentional networks. This involves brain regions like dorsolateral prefrontal cortex (DLPFC), anterior cingulate (AC), inferior frontal gyrus (IFG), and parietal regions. <mark class="annotated-text">Map prepared using Neurosynth meta-analysis of the term working memory (Yarkoni et al.,  ).</mark> Similar neural networks show decreased signals in attention deficit hyperactivity disorder (ADHD) patients performing working memory tasks. 
  
Two general mechanisms explain the effects of working m…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8334010/"
                                       >PMC8334010</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …d particular cognitive functions. However, the features in this study were relatively task-focused (e.g. stimulus or response features), unlike the function-focused features used in the present paper.<mark class="annotated-text"> Another recent study ( ) showed the effectiveness of metadata-based features in an encoding model to predict brain activity and to decode tasks (instead of concepts), using subject-level data (103 total tasks) ( ). This study also demonstrated the ability to predict activation patterns for unseen tasks, using a latent feature space derived from the Neurosynth database ( ). </mark>The ability to predict activation patterns for novel tasks based on data from other tasks was also demonstrated by Pinho et al., ( ), using the extensive Individualized Brain Charting database ( ). 

…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9981816/"
                                       >PMC9981816</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">using_neurosynth_figure (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … selection tasks and showed no preference for the global association task over size matching: thus, percentage signal change in this dorsal region largely mirrored the difficulty of the conditions. 

<mark class="annotated-text">Our final analysis directly examined the similarity between the functional architecture of the pMTG region, identified by our analyses as important in event semantics, with the network associated with semantic control by the meta-analysis of  . We calculated the conjunction of the previous three analyses (the task-based conjunction for action/relational semantic decisions; the resting-state connectivity conjunction for ATL and IFS; and the resting-state connectivity contrast of ventral IFG &gt; dorsal IFG). This identified a common region centred on − 57 − 55 3 (  left panel). We entered this coordinate in Neurosynth ( ,  ) to examine its resting-state functional connectivity. The resulting map overlapped with the   meta-analysis in inferior frontal gyrus and also showed connectivity with temporal parietal junction and pre-SMA (  right panel). The connectivity map for pMTG was also compared with the DMN and the multiple-demand network ( ) and it extended into both of these networks, including overlap with the MDN in IFS, precentral gyrus (PCG), dorsal IFG, IPS and LOC, plus overlap with the DMN in ventral IFG and MTG. </mark>



## Discussion 
  
This study set out to better characterise the functional role of the posterior middle temporal gyrus (pMTG) in semantic processing. Left pMTG is thought to play a key role in bot…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4927261/"
                                       >PMC4927261</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ngages executive and dorsal attentional networks. This involves brain regions like dorsolateral prefrontal cortex (DLPFC), anterior cingulate (AC), inferior frontal gyrus (IFG), and parietal regions. <mark class="annotated-text">Map prepared using Neurosynth meta-analysis of the term working memory (Yarkoni et al.,  ).</mark> Similar neural networks show decreased signals in attention deficit hyperactivity disorder (ADHD) patients performing working memory tasks. 
  
Two general mechanisms explain the effects of working m…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8334010/"
                                       >PMC8334010</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">not_sure_what_they_used (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```
