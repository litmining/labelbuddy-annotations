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

# cluster_inference

See also this project's [folder on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/cluster_inference/).



## Labels in this project

```{code-cell}
:tags: [remove-input]

from labelrepo import displays
text = """
<div class="detailed-label-set">
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">smoothing_snippet (175 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ing and B splines interpolation algorithm. The images were then normalized into standard atlas space (using the T2* weighted template from SPM2), written out at a 2 × 2 × 2 voxel resolution, and then <mark class="annotated-text">smoothed with an 8 mm full-width, half-maximum Gaussian kernel</mark>.      Data analysis    Analyses of the time-series data were performed using the General Linear Model using the Statistical Parametric Mapping (SPM2) statistical software [  ]. For each participant, …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1373642/"
                                       >PMC1373642</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ing and B splines interpolation algorithm. The images were then normalized into standard atlas space (using the T2* weighted template from SPM2), written out at a 2 × 2 × 2 voxel resolution, and then <mark class="annotated-text">smoothed with an 8 mm full-width, half-maximum Gaussian kernel</mark>.      Data analysis    Analyses of the time-series data were performed using the General Linear Model using the Statistical Parametric Mapping (SPM2) statistical software [  ]. For each participant, …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1373642/"
                                       >PMC1373642</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …uding patients, as they did not have anatomical brain deformation, confirming by MRI. To conform to the underlying assumption in SPM that the data are normally distributed, the functional images were <mark class="annotated-text">spatially smoothed by an 8 mm FWHM (Full Width at Half Maximum) Gaussian kernel</mark>. Time-series for each voxel were high-pass filtered (1/128 Hz cutoff) to remove low-frequency noise and signal drift.    The general linear model was then used to generate parameter estimates of acti…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2515912/"
                                       >PMC2515912</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …zation parameters to the standard Montreal Neurological Institute echo planar image (MNI EPI) template, which were then applied to all EPI volumes. Normalized images were resliced to 3 × 3 × 3 mm and <mark class="annotated-text">smoothed with an 8-mm full-width half-maximum isotropic Gaussian kernel</mark>. The data were high-pass filtered to a maximum of 1/128 Hz and grand mean scaled to 100.    Statistical analysis was performed in 2 stages. In the first stage, neural activity was modeled by a sequen…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2517104/"
                                       >PMC2517104</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …motion correction (  ), producing six motion-correction parameters that were then used as regressors in the general linear model (GLM). Brain extraction tool (BET) was used for brain extraction (  ). <mark class="annotated-text">Spatial smoothing used a Gaussian kernel of FWHM 5 mm</mark>. Grand mean scaling was applied across all volumes by the same factor. High-pass temporal filtering [Gaussian-weighted line spread function (LSF)] used straight line fitting, with sigma = 64 s. All r…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2544456/"
                                       >PMC2544456</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …removed to allow the hemodynamics to achieve a steady state and to minimize transient effects of magnetic saturation. Further preprocessing involved slice scan time correction, 3-D motion correction, <mark class="annotated-text">smoothing with a Gaussian kernel of 6 mm FWHM</mark>, normalization (each voxels's time series was divided by its mean intensity to convert the data from arbitrary image intensity units to percent signal modulation) and linear trend removal. Group anal…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2607027/"
                                       >PMC2607027</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …removed to allow the hemodynamics to achieve a steady state and to minimize transient effects of magnetic saturation. Further preprocessing involved slice scan time correction, 3-D motion correction, <mark class="annotated-text">smoothing with a Gaussian kernel of 6 mm FWHM</mark>, normalization (each voxels's time series was divided by its mean intensity to convert the data from arbitrary image intensity units to percent signal modulation) and linear trend removal. Group anal…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2607027/"
                                       >PMC2607027</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …xpert Analysis Tool) Version 5.63, part of FSL (FMRIB’s Software Library,  ;  ). The following pre-statistics processing was applied; motion correction using MCFLIRT  ; non-brain removal using BET  ; <mark class="annotated-text">spatial smoothing using a Gaussian kernel of FWHM 5 mm</mark>; mean-based intensity normalisation of all volumes by the same factor; high pass temporal filtering (Gaussian-weighted least-squares straight line fitting, with sigma = 50.0 s). Time-series statistic…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2743811/"
                                       >PMC2743811</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …g SPM5 software (SPM5, Wellcome Institute of Cognitive Neurology, London, UK). Preprocessing comprised within-subject realignment, spatial normalization of images to a template in standard space, and <mark class="annotated-text">spatial smoothing using an 8-mm Gaussian kernel</mark>. Unified normalization was used, which improves upon standard normalization by correcting for magnetic field inhomogeneity and fitting to the template using only brain tissue.    Following preprocess…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2803734/"
                                       >PMC2803734</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …g SPM5 software (SPM5, Wellcome Institute of Cognitive Neurology, London, UK). Preprocessing comprised within-subject realignment, spatial normalization of images to a template in standard space, and <mark class="annotated-text">spatial smoothing using an 8-mm Gaussian kernel.</mark> Unified normalization was used, which improves upon standard normalization by correcting for magnetic field inhomogeneity and fitting to the template using only brain tissue.    Following preprocessi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2803734/"
                                       >PMC2803734</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">cluster_thresh_used (152 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …roup analysis on the contrast images from individual analyses (  ), using one-sample t tests. Clusters of activated voxels were then identified as significant at a voxel level of p < 0.001, T > 4.50, <mark class="annotated-text">extended threshold</mark> of 15 voxels. The group analysis allowed identifying language regions significantly more activated within one hemisphere with respect to the other one. The brain regions were reported according to th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2515912/"
                                       >PMC2515912</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tions and inhomogeneity of variance across groups. All main effects of condition (across groups) and group-by-condition interaction SPMs were evaluated under an uncorrected alpha level of 0.001 and a <mark class="annotated-text">minimum cluster size</mark> of 5 contiguous voxels. The SPM for the main effect of condition was masked exclusively with the SPM for the group-by-condition interaction, using a liberal uncorrected threshold of   P   < 0.05 for …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2517104/"
                                       >PMC2517104</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …excluding regions from the masked SPM.) All T-contrasts were 1-tailed. Simple effect SPMs (for within-group comparisons) were similarly evaluated under an uncorrected threshold of   P   < 0.001 and a <mark class="annotated-text">minimum cluster size</mark> of 5. Maxima of significant clusters were localized on individual normalized structural images.       Results     Neuropsychological Test Results    Group characteristics and standardized   Z   -scor…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2517104/"
                                       >PMC2517104</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … (  ;  ;  )]. Then a third-level analysis (combining participants) used the “full” version of FLAME.   Z-   statistic images were thresholded using clusters determined by   z   >2.3 and a (corrected) <mark class="annotated-text">cluster significance threshold</mark> of   P   < 0.01 (  ;  ).      ROI analyses    The ROI analyses tested for any differences between areas within the cluster of activated medial frontal cortical regions reported in the whole-brain ana…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2544456/"
                                       >PMC2544456</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ient of each predictor independently for each voxel. Significance maps of the brain were computed by t-tests of pairwise comparisons between relevant conditions. Significance levels were corrected by <mark class="annotated-text">taking into account cluster size</mark> and its false detection probability  (   p    = 0.05 corrected). This type of analysis was used to contrast the high and low information conditions for detection and individuation as well as faces ve…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2607027/"
                                       >PMC2607027</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …or independently for each voxel. Significance maps of the brain were computed by t-tests of pairwise comparisons between relevant conditions. Significance levels were corrected by taking into account <mark class="annotated-text">cluster size</mark> and its false detection probability  (   p    = 0.05 corrected). This type of analysis was used to contrast the high and low information conditions for detection and individuation as well as faces ve…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2607027/"
                                       >PMC2607027</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s was carried out using FILM with local autocorrelation correction  .   Z   (Gaussianised   T   /   F   ) statistic images were thresholded using clusters determined by   Z    > 2.3 and a (corrected) <mark class="annotated-text">cluster significance threshold</mark> of   P    = 0.05  . Registration to high resolution and/or standard images was carried out using FLIRT  .    Higher-level analysis was carried out using FLAME (FMRIB’s Local Analysis of Mixed Effects…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2743811/"
                                       >PMC2743811</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …   T   /   F   ) Statistical images were thresholded using clusters determined by   Z    > 1.9 and a (corrected) cluster significance threshold of   P    = 0.05  .    The use of a combined height and <mark class="annotated-text">cluster threshold</mark> is a standard and generally accepted method to solve the problem of multiple comparisons with functional imaging data  . The combined height and cluster threshold is the default option with FSL, and …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2743811/"
                                       >PMC2743811</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …   t   -tests were used to assess the group-level significance of each contrast. Results were subject to voxel-level thresholds of   P   < 0.001, within this we report clusters that yielded corrected <mark class="annotated-text">cluster-level significance</mark> of   P   < 0.05. Montreal Neurological Institute coordinates are reported. In order to identify anatomical regions within clusters and cluster maxima the Montreal Neurological Institute coordinates w…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2803734/"
                                       >PMC2803734</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …   t   -tests were used to assess the group-level significance of each contrast. Results were subject to voxel-level thresholds of   P   < 0.001, within this we report clusters that yielded corrected <mark class="annotated-text">cluster-level significance</mark> of   P   < 0.05. Montreal Neurological Institute coordinates are reported. In order to identify anatomical regions within clusters and cluster maxima the Montreal Neurological Institute coordinates w…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2803734/"
                                       >PMC2803734</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #98df8a;">
        <summary class="label-display">cluster_thresh_in_voxels (82 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ontrast images from individual analyses (  ), using one-sample t tests. Clusters of activated voxels were then identified as significant at a voxel level of p < 0.001, T > 4.50, extended threshold of <mark class="annotated-text">15</mark> voxels. The group analysis allowed identifying language regions significantly more activated within one hemisphere with respect to the other one. The brain regions were reported according to the ster…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2515912/"
                                       >PMC2515912</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …of variance across groups. All main effects of condition (across groups) and group-by-condition interaction SPMs were evaluated under an uncorrected alpha level of 0.001 and a minimum cluster size of <mark class="annotated-text">5</mark> contiguous voxels. The SPM for the main effect of condition was masked exclusively with the SPM for the group-by-condition interaction, using a liberal uncorrected threshold of   P   < 0.05 for the m…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2517104/"
                                       >PMC2517104</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …he masked SPM.) All T-contrasts were 1-tailed. Simple effect SPMs (for within-group comparisons) were similarly evaluated under an uncorrected threshold of   P   < 0.001 and a minimum cluster size of <mark class="annotated-text">5</mark>. Maxima of significant clusters were localized on individual normalized structural images.       Results     Neuropsychological Test Results    Group characteristics and standardized   Z   -scores fo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2517104/"
                                       >PMC2517104</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …h contrast (i.e., ‘retention (ss5 + ss2) - baseline’ and ‘baseline - retention’) at a corrected voxel threshold of p<0.05 using family-wise error correction  ,  and a cluster threshold of p<0.01 (k = <mark class="annotated-text">27</mark> resampled voxels, corrected for multiple comparisons using Monte Carlo simulations with 1000 iterations,  ).The cluster threshold method was applied to control for the overall type I error.    For th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2858659/"
                                       >PMC2858659</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …h contrast (i.e., ‘retention (ss5 + ss2) - baseline’ and ‘baseline - retention’) at a corrected voxel threshold of p<0.05 using family-wise error correction  ,  and a cluster threshold of p<0.01 (k = <mark class="annotated-text">27</mark> resampled voxels, corrected for multiple comparisons using Monte Carlo simulations with 1000 iterations,  ).The cluster threshold method was applied to control for the overall type I error.    For th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2858659/"
                                       >PMC2858659</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …essors.    For all frequency bands, EEG-BOLD signal correlations were considered significant at an uncorrected voxel threshold of p<0.001 (t = 3.1) and at a corrected cluster threshold of p<0.01 (k = <mark class="annotated-text">27</mark> resampled voxels using Monte Carlo simulations). The same voxel threshold has been used in a recent EEG-fMRI WM study  .    For the load specific analysis first load sensitive regions from the BOLD c…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2858659/"
                                       >PMC2858659</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …chieved through setting a cluster-size criterion, combined with a voxelwise threshold of   P   < 0.01. Monte Carlo simulations with the AFNI program “Alphasim” were used to set a cluster criterion of <mark class="annotated-text">220</mark> contiguous voxels (1.76 mL), for a whole-brain family-wise error of   P   < 0.05. In one case, a smaller search volume was used, as indicated in the Results section. For display of time courses, sphe…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2901020/"
                                       >PMC2901020</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … For pS-SS trials, the first stop included both error and success trials as there were not enough of either to consider separating the two in GLM analyses. At a threshold of p<0.005, uncorrected, and <mark class="annotated-text">5</mark> voxels in the extent of activation, this contrast (pS-SS > pG-SS) involved activation of several prefrontal structures, including the right lateral orbitofrontal cortex (OFC), bilateral lateral prefr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2950843/"
                                       >PMC2950843</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … For pS-SS trials, the first stop included both error and success trials as there were not enough of either to consider separating the two in GLM analyses. At a threshold of p<0.005, uncorrected, and <mark class="annotated-text">5</mark> voxels in the extent of activation, this contrast (pS-SS > pG-SS) involved activation of several prefrontal structures, including the right lateral orbitofrontal cortex (OFC), bilateral lateral prefr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2950843/"
                                       >PMC2950843</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …on was used with parameters based on a Monte Carlo simulation (Forman et al.,  ). The cluster-threshold correction required a voxelwise threshold of   P    ≤ 0.005 within a volume of at least 351 μl (<mark class="annotated-text">13</mark> contiguous voxels) to yield an effective alpha ≤ 0.050.       Results     Individuation task    The central ROI-based analysis revealed that faces, watches, and diverse object produced virtually iden…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3009480/"
                                       >PMC3009480</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">n_participants_total (76 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …canner error, 3 subjects who did not achieve 90% accuracy on the fMRI task, and 1 subject who had a previously undiagnosed tumor. The final number of subjects included in the statistical analysis was <mark class="annotated-text">40</mark> (23 ε3/4 heterozygotes and 17 ε3/3 homozygotes). Athena Diagnostics (Worchester, MA) conducted APOE genotyping for all subjects using their patented procedures.      fMRI task    Blood oxygen level d…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1373642/"
                                       >PMC1373642</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … to attend, an additional “memory” block was performed in which participants are instructed to attend to the same or different location as in the previous trial or are free to choose.      METHODS    <mark class="annotated-text">Nineteen</mark> right-handed participants (aged 19–33, 10 female) all had normal or corrected-to-normal vision and were native speakers of a Latin-alphabet language. Between 1 and 7 days prior to participating in an…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2544456/"
                                       >PMC2544456</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s-correlation thresholds in this case were kept fixed at the values that maximized task-specific information within the training set.        Behavioral Experiment 1–Face Detection     Participants    <mark class="annotated-text">Sixteen</mark> adults from the Brown University community volunteered to participate in the experiment in exchange for pay. All participants had normal or corrected-to-normal vision. All participants provided writt…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2607027/"
                                       >PMC2607027</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …he information given to the participants about the expected treatment in the placebo session. This session also allowed us to control for habituation effects.      2. Methods     2.1. Participants    <mark class="annotated-text">Eleven</mark> healthy, (six female, five male) neurologically normal, right handed participants (age range 19–36 years) gave their informed consent to take part in the study. Participants had two experimental sess…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2743811/"
                                       >PMC2743811</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …to not only include contralateral (RH) recruitment but could also include the recruitment of other cognitive processes supported by other neural regions.      Methods     Participants    We recruited <mark class="annotated-text">58</mark> healthy right-handed adults from the Cambridge community (27 female, 31 male). These included 14 younger adults aged 19–34 (   M   = 23.9, standard deviation [SD] = 4.1), to establish the baseline yo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2803734/"
                                       >PMC2803734</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …science pertains to the innate nature of language development and the underlying factors that determine this faculty. We explored the neural correlates associated with language processing in a unique <mark class="annotated-text">individual</mark> who is early blind, congenitally deaf, and possesses a high level of language function. Using functional magnetic resonance imaging (fMRI), we compared the neural networks associated with the tactile…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2805429/"
                                       >PMC2805429</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …egatively correlated with the BOLD signal during the retention phase of a WM task. However, the coupling of higher (beta and gamma) frequencies with the BOLD signal during WM is unknown.MethodologyIn <mark class="annotated-text">16</mark> healthy adult subjects, we first investigated EEG-BOLD signal correlations for theta (5–7 Hz), alpha1 (8–10), alpha2 (10–12 Hz), beta1 (13–20), beta2 (20–30 Hz), and gamma (30–40 Hz) during the reten…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2858659/"
                                       >PMC2858659</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …nd gamma exhibit positive correlations. We further expect that load sensitive WM areas should demonstrate both BOLD and frequency band related load effects.      Materials and Methods     Subjects    <mark class="annotated-text">Sixteen</mark> healthy volunteers (mean age 24.8±3.8 years, 8 females) participated in this study. All subjects were right-handed and had normal or corrected-to-normal vision. The study falls under the ethical appr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2858659/"
                                       >PMC2858659</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …resent fMRI study we therefore sought to investigate the impact of the   COMT   val  met polymorphism on the blood oxygen level-dependent (BOLD) response to painful laser stimulation.      Results    <mark class="annotated-text">57</mark> subjects were studied. We found that subjects homozygous for the met158 allele exhibit a higher BOLD response in the anterior cingulate cortex (ACC), foremost in the mid-cingulate cortex, than carrie…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2887789/"
                                       >PMC2887789</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …d intermediate phenotypes revealed by neuroimaging methods such as fMRI may be a useful concept to study genotype-phenotype relationships in pain research.      Methods     Subjects    A total of N = <mark class="annotated-text">57</mark> healthy subjects (27 males) with a mean age of 35.3 (SD 11.1) years were recruited both from a larger population-based sample that will be described in more detail elsewhere (Mobascher et al., unpubl…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2887789/"
                                       >PMC2887789</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c5b0d5;">
        <summary class="label-display">nonparametric_cluster_thresh (55 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    ….05 corrected) using minimum cluster size estimation (  ). After setting the voxel-level threshold to   P   < 0.01 (uncorrected), the maps were corrected at whole brain level using 1000 iterations of <mark class="annotated-text">Monte Carlo</mark> simulation to estimate the minimum cluster size threshold that would yield a false positive rate of 5%. Voxels activated above the indicated threshold (   P   < 0.05 corrected) were selected and the …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2820702/"
                                       >PMC2820702</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …line - retention’) at a corrected voxel threshold of p<0.05 using family-wise error correction  ,  and a cluster threshold of p<0.01 (k = 27 resampled voxels, corrected for multiple comparisons using <mark class="annotated-text">Monte Carlo</mark> simulations with 1000 iterations,  ).The cluster threshold method was applied to control for the overall type I error.    For the load dependent fMRI analysis we calculated the contrasts ‘ss5–ss2’ an…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2858659/"
                                       >PMC2858659</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …line - retention’) at a corrected voxel threshold of p<0.05 using family-wise error correction  ,  and a cluster threshold of p<0.01 (k = 27 resampled voxels, corrected for multiple comparisons using <mark class="annotated-text">Monte Carlo simulations</mark> with 1000 iterations,  ).The cluster threshold method was applied to control for the overall type I error.    For the load dependent fMRI analysis we calculated the contrasts ‘ss5–ss2’ and ‘ss2–ss5’.…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2858659/"
                                       >PMC2858659</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …cy bands, EEG-BOLD signal correlations were considered significant at an uncorrected voxel threshold of p<0.001 (t = 3.1) and at a corrected cluster threshold of p<0.01 (k = 27 resampled voxels using <mark class="annotated-text">Monte Carlo</mark> simulations). The same voxel threshold has been used in a recent EEG-fMRI WM study  .    For the load specific analysis first load sensitive regions from the BOLD contrast ‘ss5> ss2’ were identified …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2858659/"
                                       >PMC2858659</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ests run and their interpretations. Correction for multiple comparisons in whole-brain maps was achieved through setting a cluster-size criterion, combined with a voxelwise threshold of   P   < 0.01. <mark class="annotated-text">Monte Carlo simulations</mark> with the AFNI program “Alphasim” were used to set a cluster criterion of 220 contiguous voxels (1.76 mL), for a whole-brain family-wise error of   P   < 0.05. In one case, a smaller search volume was…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2901020/"
                                       >PMC2901020</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … for multiple comparisons in whole-brain maps was achieved through setting a cluster-size criterion, combined with a voxelwise threshold of   P   < 0.01. Monte Carlo simulations with the AFNI program <mark class="annotated-text">“Alphasim”</mark> were used to set a cluster criterion of 220 contiguous voxels (1.76 mL), for a whole-brain family-wise error of   P   < 0.05. In one case, a smaller search volume was used, as indicated in the Result…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2901020/"
                                       >PMC2901020</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …t produced a significant main effect of stimulus (P ≤ 0.010 uncorrected). To correct that statistics for multiple comparisons, a voxel-cluster-threshold correction was used with parameters based on a <mark class="annotated-text">Monte Carlo</mark> simulation (Forman et al.,  ). The cluster-threshold correction required a voxelwise threshold of   P    ≤ 0.005 within a volume of at least 351 μl (13 contiguous voxels) to yield an effective alpha …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3009480/"
                                       >PMC3009480</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tor GROUP and the interaction are reported on p<.001 (uncorrected). For all reported comparisons, the likelihood of Type I error was reduced based on cluster size threshold estimation  ,  involving a <mark class="annotated-text">Monte Carlo</mark> simulation calculating the likelihood to obtain different cluster sizes. Calculations resulted in a cluster size threshold of 16 voxels. Active voxels are displayed in native resolution without inter…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3026801/"
                                       >PMC3026801</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tor GROUP and the interaction are reported on p<.001 (uncorrected). For all reported comparisons, the likelihood of Type I error was reduced based on cluster size threshold estimation  ,  involving a <mark class="annotated-text">Monte Carlo simulation</mark> calculating the likelihood to obtain different cluster sizes. Calculations resulted in a cluster size threshold of 16 voxels. Active voxels are displayed in native resolution without interpolation an…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3026801/"
                                       >PMC3026801</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …xact masks for both networks are available from the authors by request.    Significant activity within each network mask was corrected for multiple comparisons using a cluster size criterion based on <mark class="annotated-text">Monte Carlo</mark> simulations  ,  , via the AlphaSim software within AFNI  . To assure a multiple comparisons corrected   p   <.05 criteria, significant regions were identified based on a per-voxel minimum   z   >2.32…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3052361/"
                                       >PMC3052361</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">voxel_size_snippet (50 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …rformed using a nonlinear pixel shifting and B splines interpolation algorithm. The images were then normalized into standard atlas space (using the T2* weighted template from SPM2), written out at a <mark class="annotated-text">2 × 2 × 2 voxel resolution</mark>, and then smoothed with an 8 mm full-width, half-maximum Gaussian kernel.      Data analysis    Analyses of the time-series data were performed using the General Linear Model using the Statistical Pa…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1373642/"
                                       >PMC1373642</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …l phased-array head coil. Functional images were acquired with an ascending interleaved echo-planar imaging (EPI) pulse sequence (90 time points per time series; TR = 3 s; TE = 30 ms; flip angle 90°; <mark class="annotated-text">3 mm isotropic voxels</mark>; field of view 192×192×144 mm3; 48 slices covering the entire cerebral cortex). At the beginning of each session, we also acquired a T1-weighted anatomical image (1 mm isotropic voxels; 160 slices of…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2607027/"
                                       >PMC2607027</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …atch the Montreal Neurological Institute (MNI) EPI template. Two of eighteen subjects were excluded from the analysis due to major head movements (i.e., translation >1.5 mm) during scanning. Finally, <mark class="annotated-text">functional volumes were resampled to isotropic 3 mm3 voxels</mark> and spatially smoothed with a 9 mm full width at half maximum isotropic Gaussian kernel. Functional images were temporally high-pass filtered with a cut-off period of 128 s, and serial correlations w…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2858659/"
                                       >PMC2858659</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ns were acquired using T1-weighted MRI sequences (Magnetization prepared rapid gradient echo (MP-RAGE): TR/TE = 1,700/3.5 ms, flip angle = 9°, 208 sagittal slices, FOV 240 × 195 mm, matrix 320 × 260, <mark class="annotated-text">voxel size 0.75 × 0.75 × 0.75 mm</mark>.      fMRI analysis    fMRI-analysis was performed with FSL (FMRIB's Software Library,  ). The following pre-processing procedure was applied: Employing different modules of the FSL-software package,…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2887789/"
                                       >PMC2887789</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …D high resolution T1-weighted isotropic volume, MPRAGE-sequence (MPRAGE = Magnetization Prepared Rapid Gradient Echo;  ); TR = 2.3 s, FOV = 256×256×176 mm, TE = 4.38 ms, TI = 900 ms, flip angle = 8°, <mark class="annotated-text">1 mm isovoxel</mark>, total acquisition time 14.45 min). Functional scans were performed using a single shot echo planar imaging sequence (EPI). A total of 365 T2*-weighted whole brain volumes were acquired (EPI-sequence…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3026801/"
                                       >PMC3026801</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ch scanning run were discarded to allow for T1 equilibration effects. Images were preprocessed and analyzed using SPM5 (  ). They were realigned to the first volume of the first experimental session, <mark class="annotated-text">resliced to a final voxel resolution of 3 × 3 × 3 mm</mark>  , normalized to the Montreal Neurological Institute (MNI) reference brain in Talairach space, and smoothed spatially with a Gaussian kernel of 8-mm full width at half maximum. All coordinates are in…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3041008/"
                                       >PMC3041008</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …versity School of Medicine. High-resolution anatomical images were acquired for each participant using a sagittal T1-weighted MP-RAGE sequence (TE = 3.16 ms, TR = 2400 ms, flip angle = 8° 176 slices, <mark class="annotated-text">1×1×1 mm voxels</mark>). Anatomical images were aligned with each individual's functional images. To facilitate registration of the T1 and functional scans, a T2-weighted image was also acquired in the same space as the fu…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3052361/"
                                       >PMC3052361</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … derives the cluster volume needed to hold the false-positive rate for cluster detection at a desired level. Using a voxel-wise threshold of   P   <0.005, a cluster volume threshold of 102 contiguous <mark class="annotated-text">2-mm  voxels</mark> was determined necessary to hold the probability of map-wise false-positive detection at   P   <0.05 in whole-brain analyses. Owing to an   a priori   interest in the amygdala, a small volume correct…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3309492/"
                                       >PMC3309492</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …30 ms/90°). Thirty-two axial slices were acquired per volume. An intra-session high-resolution structural scan was acquired using a T1-weighted 3D magnetization prepared rapid gradient echo sequence (<mark class="annotated-text">1 mm3voxel size</mark>).    The functional imaging data were analyzed using BrainVoyager QX (Brain innovation; Goebel et al.,  ). The first four volumes of each subject's functional data set were discarded to allow for T1 …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3373207/"
                                       >PMC3373207</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …lation in any axis and less than 3° angular rotation in any axis. All realigned data were then spatially normalized to the standard Montreal Neurological Institute (MNI) EPI template and resampled to <mark class="annotated-text">2×2×2 mm cubic voxels</mark>. To further reduce the effects of confounding factors, six motion parameters, linear drift and the mean time series of all voxels within the white matter and the cerebrospinal fluid were removed from…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3427333/"
                                       >PMC3427333</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">n_participants_in_subgroup (49 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …er error, 3 subjects who did not achieve 90% accuracy on the fMRI task, and 1 subject who had a previously undiagnosed tumor. The final number of subjects included in the statistical analysis was 40 (<mark class="annotated-text">23</mark> ε3/4 heterozygotes and 17 ε3/3 homozygotes). Athena Diagnostics (Worchester, MA) conducted APOE genotyping for all subjects using their patented procedures.      fMRI task    Blood oxygen level depen…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1373642/"
                                       >PMC1373642</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …id not achieve 90% accuracy on the fMRI task, and 1 subject who had a previously undiagnosed tumor. The final number of subjects included in the statistical analysis was 40 (23 ε3/4 heterozygotes and <mark class="annotated-text">17</mark> ε3/3 homozygotes). Athena Diagnostics (Worchester, MA) conducted APOE genotyping for all subjects using their patented procedures.      fMRI task    Blood oxygen level dependent (BOLD) signal was det…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1373642/"
                                       >PMC1373642</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …r cognitive processes supported by other neural regions.      Methods     Participants    We recruited 58 healthy right-handed adults from the Cambridge community (27 female, 31 male). These included <mark class="annotated-text">14</mark> younger adults aged 19–34 (   M   = 23.9, standard deviation [SD] = 4.1), to establish the baseline young adult neural system, and an older group of 44 participants aged 49–86 (   M   = 67.4, SD = 8.…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2803734/"
                                       >PMC2803734</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … community (27 female, 31 male). These included 14 younger adults aged 19–34 (   M   = 23.9, standard deviation [SD] = 4.1), to establish the baseline young adult neural system, and an older group of <mark class="annotated-text">44</mark> participants aged 49–86 (   M   = 67.4, SD = 8.0), in order to sample a wide age range of older adults. All gave informed consent, and the study was approved by the Suffolk Local Research Ethics Comm…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2803734/"
                                       >PMC2803734</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s become a topic of debate in recent years. In a jittered functional magnetic resonance imaging study, sub-threshold presentations of anxious faces permitted an examination of amygdala recruitment in <mark class="annotated-text">12</mark> high functioning adult males with ASD and 12 matched controls. We found heightened neural activation of the amygdala in both high functioning adults with ASD and matched controls. Neither the intensi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2876036/"
                                       >PMC2876036</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …n a jittered functional magnetic resonance imaging study, sub-threshold presentations of anxious faces permitted an examination of amygdala recruitment in 12 high functioning adult males with ASD and <mark class="annotated-text">12</mark> matched controls. We found heightened neural activation of the amygdala in both high functioning adults with ASD and matched controls. Neither the intensity nor the time-course of amygdala activation…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2876036/"
                                       >PMC2876036</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …articipants were excluded from study if they had a previous or current neurological disorder, head trauma, substance use, or medical contraindications to magnetic resonance imaging. Participants were <mark class="annotated-text">12</mark> high functioning male adults with ASD (x = 31.8 years old; range 19–52 years) and 12 typically developed male controls (x = 32 years old; range 19–57 years). The two groups did not differ significant…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2876036/"
                                       >PMC2876036</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …isorder, head trauma, substance use, or medical contraindications to magnetic resonance imaging. Participants were 12 high functioning male adults with ASD (x = 31.8 years old; range 19–52 years) and <mark class="annotated-text">12</mark> typically developed male controls (x = 32 years old; range 19–57 years). The two groups did not differ significantly in age (t(22) = −0.04, p<0.97). The study groups were matched on age, sex and non-…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2876036/"
                                       >PMC2876036</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …imuli used are often unspecific to depression. This study explored hemodynamic responses of the brain in patients with depression while processing individualized and clinically derived stimuli.Methods<mark class="annotated-text">Eighteen</mark> unmedicated patients with recurrent major depressive disorder and 17 never-depressed control subjects took part in standardized clinical interviews from which individualized formulations of core inte…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3026801/"
                                       >PMC3026801</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …mic responses of the brain in patients with depression while processing individualized and clinically derived stimuli.MethodsEighteen unmedicated patients with recurrent major depressive disorder and <mark class="annotated-text">17</mark> never-depressed control subjects took part in standardized clinical interviews from which individualized formulations of core interpersonal dysfunction were derived. In the patient group such formula…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3026801/"
                                       >PMC3026801</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">n_participants_excluded (29 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ause there was an insufficient number of individuals with other APOE genotypes (e.g. ε4/4 homozygotes or ε2/3 heterozygotes) to make meaningful inferencesregarding other APOE genotypes. The data from <mark class="annotated-text">6</mark> additional subjects (3 ε3/3 homozygotes and 3 ε3/4 heterozygotes) were excluded from the overall statistical analyses: 1 subject for excessive motion during scanning, 1 subject for scanner error, 3 s…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1373642/"
                                       >PMC1373642</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ir eyes, and therefore optimize later performance of the task in the scanner. Real-time infrared eye-tracking (iScan, Burlington, MA) was used to measure the position of gaze during task performance. <mark class="annotated-text">One</mark> participant was excluded from the experiment at this stage due to being unable to fixate during the task. The remaining 18 participants proceeded to the functional magnetic resonance imaging (fMRI) e…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2544456/"
                                       >PMC2544456</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rt level to receive the corresponding reward amount.      Participants    Eighteen right-handed participants [5 females, age: 27 ± 3 (SD) yr] were recruited through a university participant database. <mark class="annotated-text">One</mark> participant was excluded from the analysis of brain activity due to excess motion artifact but was included in the behavioral analysis. All participants were paid £25–30 depending on duration of expe…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2904211/"
                                       >PMC2904211</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …participate in the study, in accordance with the Declaration of Helsinki and with the approval of the Ethics Committee of the National Hospital for Neurology and Neurosurgery, London, United Kingdom. <mark class="annotated-text">One</mark> subject was excluded due to problems with recording the button presses and 2 others were excluded because they fell asleep during the experiment. The results from 14 subjects (10 male, mean age = 28.…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3041008/"
                                       >PMC3041008</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …th the approval of the Ethics Committee of the National Hospital for Neurology and Neurosurgery, London, United Kingdom. One subject was excluded due to problems with recording the button presses and <mark class="annotated-text">2</mark> others were excluded because they fell asleep during the experiment. The results from 14 subjects (10 male, mean age = 28.5 years [range 23–40], 2 left handed) were analyzed and are reported here.   …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3041008/"
                                       >PMC3041008</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ation, ophthalmoscopy, binocular alignment, ocular motility, and random-dot butterfly stereograms. In total, fourteen amblyopic patients and twenty-two healthy individuals were enrolled in the study. <mark class="annotated-text">Two</mark> participants (1 healthy volunteer, 1 patient with amblyopia) had excessive head motion during scanning (see data preprocessing) and were excluded, leaving twenty-one healthy volunteers and thirteen p…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3427333/"
                                       >PMC3427333</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ircuitry in SAD patients compared to healthy controls, which could explain their improper anxiety management under social stress.      Methods     Participants    19 social anxiety disorder patients (<mark class="annotated-text">1 </mark>exclusion due to positive drug screening, 1 exclusion due to unacceptable image distortions within the orbitofrontal cortex caused by a dental implant, 1 exclusion due to hardware error, and 1 exclusi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510234/"
                                       >PMC3510234</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … controls, which could explain their improper anxiety management under social stress.      Methods     Participants    19 social anxiety disorder patients (1 exclusion due to positive drug screening, <mark class="annotated-text">1</mark> exclusion due to unacceptable image distortions within the orbitofrontal cortex caused by a dental implant, 1 exclusion due to hardware error, and 1 exclusion due to non-compliance with our study pro…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510234/"
                                       >PMC3510234</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …pants    19 social anxiety disorder patients (1 exclusion due to positive drug screening, 1 exclusion due to unacceptable image distortions within the orbitofrontal cortex caused by a dental implant, <mark class="annotated-text">1</mark> exclusion due to hardware error, and 1 exclusion due to non-compliance with our study protocol) and 17 healthy subjects (2 exclusions due to non-compliance with our study protocol) were recruited fro…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510234/"
                                       >PMC3510234</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …tients (1 exclusion due to positive drug screening, 1 exclusion due to unacceptable image distortions within the orbitofrontal cortex caused by a dental implant, 1 exclusion due to hardware error, and<mark class="annotated-text"> 1</mark> exclusion due to non-compliance with our study protocol) and 17 healthy subjects (2 exclusions due to non-compliance with our study protocol) were recruited from the local community via billboard ann…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510234/"
                                       >PMC3510234</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">n_participants (23 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …d A Brain-Based Theory of Beauty        ABSTRACT           We wanted to learn whether activity in the same area(s) of the brain correlate with the experience of beauty derived from different sources. <mark class="annotated-text">21</mark> subjects took part in a brain-scanning experiment using functional magnetic resonance imaging. Prior to the experiment, they viewed pictures of paintings and listened to musical excerpts, both of whi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3130765/"
                                       >PMC3130765</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …say, regardless of whether it is derived from the auditory or visual sense. This turned out to be so and led us to formulate a brain-based theory of beauty.      Materials and Methods     Subjects    <mark class="annotated-text">21</mark> healthy right-handed volunteers (9 male, 12 female, mean age 27.5 years) participated in this study. All had normal or corrected-to-normal vision, and none had a history of neurological or psychiatri…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3130765/"
                                       >PMC3130765</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e used the method of functional magnetic resonance imaging (fMRI) and a motor imagery task, in order to explore the dynamic neuro-functional changes induced by a highly complex physical training. The <mark class="annotated-text">11</mark> golf novices between the age of 40 and 60 years practiced the motor training as leisure activity. Additionally, data from an age and sex-matched control group without golf training was collected. As …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3315099/"
                                       >PMC3315099</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ized that the neural activations during mental rehearsal of the golf swing will change, in terms of a reduced hemodynamic response, as a consequence of golf practice.      Methods     Participants    <mark class="annotated-text">Twenty-two</mark> healthy volunteers (18 women, 4 men) with a mean age of 51.2 (SD = 7.2) years participated in the present study. A previous study investigating the structural correlates of training-induced plasticit…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3315099/"
                                       >PMC3315099</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …population (Bezzola et al.,  ). None of the participants had any history of neurological or psychiatric disorder. The study sample consisted of the following two groups, a golf novice group (   n   = <mark class="annotated-text">11</mark>; 9 women, 2 men) and an age-, sex, and handedness-matched control group (   n   = 11). Handedness was verified by means of the Annett Handedness questionnaire (Annett,  ). According to this test, 20 …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3315099/"
                                       >PMC3315099</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …cal or psychiatric disorder. The study sample consisted of the following two groups, a golf novice group (   n   = 11; 9 women, 2 men) and an age-, sex, and handedness-matched control group (   n   = <mark class="annotated-text">11</mark>). Handedness was verified by means of the Annett Handedness questionnaire (Annett,  ). According to this test, 20 participants (10 golf group, 10 control group) were classified as consistent right-ha…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3315099/"
                                       >PMC3315099</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …es of cocaine addiction are unclear. We assessed blood-oxygenation-level dependent (BOLD) signal in ventral and dorsal striatum during functional magnetic resonance imaging (fMRI) in current (CCD; n =<mark class="annotated-text"> 30</mark>) and former (FCD; n = 28) cocaine dependent subjects as well as healthy control (HC; n = 31) subjects while playing an interactive competitive Domino game involving risk-taking and reward/punishment …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3351439/"
                                       >PMC3351439</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …re unclear. We assessed blood-oxygenation-level dependent (BOLD) signal in ventral and dorsal striatum during functional magnetic resonance imaging (fMRI) in current (CCD; n = 30) and former (FCD; n =<mark class="annotated-text"> 28</mark>) cocaine dependent subjects as well as healthy control (HC; n = 31) subjects while playing an interactive competitive Domino game involving risk-taking and reward/punishment processing. Out-of-scanne…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3351439/"
                                       >PMC3351439</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …gnal in ventral and dorsal striatum during functional magnetic resonance imaging (fMRI) in current (CCD; n = 30) and former (FCD; n = 28) cocaine dependent subjects as well as healthy control (HC; n =<mark class="annotated-text"> 31</mark>) subjects while playing an interactive competitive Domino game involving risk-taking and reward/punishment processing. Out-of-scanner impulsivity-related measures were also collected. Although both F…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3351439/"
                                       >PMC3351439</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ided written informed consent after the study had been fully explained to them. Participants were paid for participating in the imaging study.      Study Participants    Participants included   n    =<mark class="annotated-text"> 36</mark> CCD,   n    = 28 FCD and   n    = 33 HC subjects. After removing subjects for excessive reaction times (discussed later), 30 CCD, 28 FCD and 31 HC subjects remained.  (top) shows demographic data; gr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3351439/"
                                       >PMC3351439</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ff9896;">
        <summary class="label-display">cluster_thresh_in_mm (22 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …eshold of FDR   q   < 0.05 resulted in corrected statistical thresholds of   p   < 0.0038 for w > p and   p   < 0.0036 for   p   > w. Only clusters of voxels that exceeded a minimum cluster volume of <mark class="annotated-text">100</mark> mm  are reported.    In describing the pattern of differential responses observed for words and pseudowords we will focus on responses in left hemisphere regions that as reviewed previously have been…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2846311/"
                                       >PMC2846311</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rom 97 peak voxels from 11 functional imaging studies comparing neural responses to spoken words and pseudowords. ALE maps are thresholded at   p   < 0.05 FDR corrected, and only clusters larger than <mark class="annotated-text">100</mark> mm  are shown. Additional activation for pseudowords compared with words (red) and words compared with pseudowords (blue) is shown (   a   ) rendered onto the left hemisphere, (   b   ) displayed on …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2846311/"
                                       >PMC2846311</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …r 29 peak voxels in studies reporting a greater neural response to spoken pseudowords than words (shown in red in  ). Results thresholded at   p   < 0.05 FDR corrected, and with clusters greater than <mark class="annotated-text">100</mark> mm  reported. Entries shown in bold are cluster summary statistics (including centre of mass and volume), entries in plain type show local maxima.      In the superior portion of the left temporal lo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2846311/"
                                       >PMC2846311</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … a cluster-size criterion, combined with a voxelwise threshold of   P   < 0.01. Monte Carlo simulations with the AFNI program “Alphasim” were used to set a cluster criterion of 220 contiguous voxels (<mark class="annotated-text">1.76 mL</mark>), for a whole-brain family-wise error of   P   < 0.05. In one case, a smaller search volume was used, as indicated in the Results section. For display of time courses, spherical regions of interest (…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2901020/"
                                       >PMC2901020</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …diverse objects and scrambled stimuli. To correct against Type I errors, a cluster-threshold correction was applied that used a voxel-wise threshold of   P    ≤ 0.001 with a minimum cluster volume of <mark class="annotated-text">225</mark> μl resulting in an effective alpha level = 0.01 (Forman et al.,  ). The LOC region of interest was defined as the areas within the inferior and middle occipital gyri where diverse object stimuli prod…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3009480/"
                                       >PMC3009480</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …al.,  ; Moore and Engel,  ; Kourtzi et al.,  ; Haushofer et al.,  ,  ). A cluster-threshold correction was applied that used a voxel-wise threshold of   P    ≤ 0.0001 with a minimum cluster volume of <mark class="annotated-text">225</mark> μl resulting in an effective alpha = 0.001. The location of the FFA, OFA, and LOC regions from each participant were confirmed against their respective high-resolution anatomical scan to insure that …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3009480/"
                                       >PMC3009480</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …correction was used with parameters based on a Monte Carlo simulation (Forman et al.,  ). The cluster-threshold correction required a voxelwise threshold of   P    ≤ 0.005 within a volume of at least <mark class="annotated-text">351</mark> μl (13 contiguous voxels) to yield an effective alpha ≤ 0.050.       Results     Individuation task    The central ROI-based analysis revealed that faces, watches, and diverse object produced virtual…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3009480/"
                                       >PMC3009480</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ed based on cluster size threshold estimation  ,  involving a Monte Carlo simulation calculating the likelihood to obtain different cluster sizes. Calculations resulted in a cluster size threshold of <mark class="annotated-text">16</mark> voxels. Active voxels are displayed in native resolution without interpolation and plotted on the Talairach-transformed brain.       Results     Behavioral Data    shows behavioral data for patients …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3026801/"
                                       >PMC3026801</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …g in ROIs was then set to   p   <0.05 uncorrected (due to an anticipated loss of power from a between-group ANOVA second-level analysis) with a minimum cluster size of   k    = 10 contiguous voxels (><mark class="annotated-text">270</mark> mm3). The SPM5 toolbox ‘rfxplot’ was used to calculate effects sizes for the random effects group SPM5 analyses and was also used to create subsequent effect size bar graphs  .      Correlation of fM…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3351439/"
                                       >PMC3351439</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …g., the ventral striatum) for whole brain analyses in each group. Significant differences in the between-group analysis were reported using the criteria of   P   <0.001, uncorrected, cluster size ≥7 (<mark class="annotated-text">189</mark> µl), which corresponds to a corrected threshold of   P   <0.05 as determined by AlphaSim in AFNI (  ). Our previous report also described this threshold in order to prevent detection of false positiv…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3447818/"
                                       >PMC3447818</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">difficult_annotation_example (21 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …g steps    The detailed processing methodology for VBM has previously been reported in detail. Briefly, we used the optimized VBM approach described by Good et al. [  ] (see also [  ,  ]) using SPM2. <mark class="annotated-text">This procedure involves segmentation of the images into gray matter (GM), white matter (WM) and cerebrospinal fluid (CSF), and normalization of the GM images to the GM template in standard space. The GM images were then modulated using the Jacobian values derived from spatial normalization and smoothed with a 12 mm isotropic Gaussian kernel.</mark> The smoothed GM images were then entered into a random-effects two-sample t-test in SPM2 to examine GM volume differences between the groups.       Results     Neuropsychological functioning and fMRI…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1373642/"
                                       >PMC1373642</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … design because familiar violin excerpts were unfamiliar to actors and familiar dramatic monologues were unfamiliar to violinists. A correction for nonsphericity was included. Unless otherwise stated,<mark class="annotated-text"> results are reported at   P   < 0.05 at the cluster and/or peak level using a height threshold of   P   < 0.001 (uncorrected)</mark>, Family-Wise Error (FWE) corrected for multiple comparisons across the whole brain. Probabilistic mapping was determined by comparing the overlap between the projected activations on the cortical sur…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3059891/"
                                       >PMC3059891</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …so that the lesioned hemisphere could be overlaid with images from the patients with left hemisphere strokes. All echo planar imaging data were de-noised using MELODIC prior to further analysis (  ). <mark class="annotated-text">Standard preprocessing and registration was applied</mark> (  ).    For each subject, we acquired separate functional MRI runs for pre- and post-tDCS with anodal, cathodal and sham conditions. We analysed these data using three levels (see  for details): (i)…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3267983/"
                                       >PMC3267983</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …he visual transfer task as dependent variable. Within this analysis a main effect of Time would reflect unspecific effects of task repetition from pre-to post-test and was therefore, not evaluated.   <mark class="annotated-text">To achieve a desirable balance between Types I and II error rates i.e., not to miss any potential activity by avoiding an unnecessarily high rate false of positives, the resulting F-maps were thresholded at a more liberal threshold of   p   < 0.005 (uncorrected) using clusters determined by the number of anatomical voxels > 135 </mark>(see Lieberman and Cunningham,  , for a detailed discussion). To further specify the Time by Group interaction we defined functional volumes-of-interest (VOI) on the basis of these cluster activations…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3373207/"
                                       >PMC3373207</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …   Increases in BOLD signal intensity in the PFC were observed not only during performance of the dual task (PR), but also during performance of the single tasks (P and R) (Figure  a and b, Table  ). <mark class="annotated-text">In R, the BOLD signal cluster size in bilateral PFC was smaller (29 voxels) than that in PR (374 voxels). Activated regions decreased by 6.7% and 8.4% in left and right PFC, respectively. In P, cluster size (366 voxels) was similar to that in PR. Maximal t values in R were lower than in PR. </mark>Maximal t values in P were higher in the left PFC and lower in the right PCF than those in PR respectively.    To detect regional activation clusters attributed to dual task processing, independent co…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3464709/"
                                       >PMC3464709</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …gnificance threshold for the main effects of winning versus losing or vice versa, or for the interaction effects between wins versus losses and active versus vicarious playing or vice versa. However, <mark class="annotated-text">using a small-volume correction for our   a priori   regions of interest (FWE-corrected threshold   P   < 0.05 at cluster-level)</mark> and a slightly more lenient threshold   P   < 0.001 (uncorrected) at voxel-level, we found stronger activations for wins versus losses in omPFC and bilateral ventral striatum. Furthermore, ventral st…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3680713/"
                                       >PMC3680713</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … of the normalized iEMG regressor.    In the group-level SPM, the threshold was initially set at a voxel-wise height-level of   P   < 0.05 corrected for multiple comparisons (family-wise error; FWE). <mark class="annotated-text">Clusters exceeding a height threshold of uncorrected   P   < 0.005 were reported as a trend.</mark> The cytoarchitectonic nomenclature of significant brain activity was identified according to the SPM5 anatomy toolbox when applicable.      Distribution of TMS- and afferent-induced brain activity in…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3774999/"
                                       >PMC3774999</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s of group activation clusters (  ) were further elucidated by a qualitative single subject analysis (  ) in which locations were compared with those established in the clinical patient reports (  ). <mark class="annotated-text">This revealed that activation strength, cluster size and position of activation clusters relative to surrounding neuroanatomy were quite stable</mark>. In addition, the atypical “Wernicke activations” found for not-deskulled input data and standard normalization (inferior parietal, anterior superior temporal, middle temporal) were not evident in th…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3814956/"
                                       >PMC3814956</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    PMID24456150        TITLE         A coordinate-based ALE functional MRI <mark class="annotated-text">meta-analysis</mark> of brain activation during verbal fluency tasks in healthy control subjects        ABSTRACT            Background    The processing of verbal fluency tasks relies on the coordinated activity of a num…
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
                    …rom the 3-dimensional volumes onto the 2-dimensional surfaces. Both the surface representations and the pre-processed time-series were standardized to a common mesh reference system (Saad et al.,  ). <mark class="annotated-text">The time-series were smoothed on the surface to achieve a target smoothing value of 6 mm using a Gaussian full width half maximum (FWHM) filter</mark>. Smoothing on the surface as opposed to the volume ensures that white matter values are not included, and that functional data located in anatomically distant locations on the cortical surface are no…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4086203/"
                                       >PMC4086203</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">bad_methods_example (11 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ns and cluster size for all significantly activated regions for the genotype effect. There were no significant differences in MTL activation for the contrast of familiar relative to novel pictures.   <mark class="annotated-text"> The whole brain analyses for the novel vs familiar and familiar vs novel contrasts (p < 0.05; FDR corrected for multiple comparisons) revealed no significant differences between the groups for either contrast. In order to examine potential compensatory activity in the cortical regions of ε3/4 heterozygotes, we conducted a follow-up analysis (p < 0.01, uncorrected) using a two-sample t-test in which the analysis was constrained to include only those regions that were active for each contrast (i.e. novel versus familiar or familiar versus novel) collapsed across all 40 subjects (i.e. a one-sample t-test). </mark>In addition to reduced MTL activation, the ε3/4 heterozygotes also displayed reduced activation compared to the ε3/3 homozygotes for the novel versus familiar contrast in the right ventral temporal co…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1373642/"
                                       >PMC1373642</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …eir selected options from the preceding choice period, by gripping (or simply holding) a hand device at the corresponding effort level to receive the corresponding reward amount.      Participants    <mark class="annotated-text">Eighteen right-handed participants [5 females, age: 27 ± 3 (SD) yr] were recruited through a university participant database. One participant was excluded from the analysis of brain activity due to excess motion artifact but was included in the behavioral analysis. </mark>All participants were paid £25–30 depending on duration of experiment they participated in. The study was approved by the University College London (UCL) ethics committee.      Stimuli and material   …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2904211/"
                                       >PMC2904211</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … significance of the t-statistics was estimated by randomly re-labeling the groups so that at least 4 participants in each group were changed and recalculating the t-values using 10,000 permutations. <mark class="annotated-text">We then calculated the 95th percentile of t-values for each permutation and selected the maximum value over the permutations as the threshold of significance thereby controlling the false discovery rate (FDR)</mark>. The association of ISC and other measures was estimated by constructing matrices of average pairwise scores of each subject pair and correlating the upper triangle entries of these matrices with the…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3830058/"
                                       >PMC3830058</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ed under the General Linear Model (GLM), setting up individual orthogonalization of ratings versus main effect in order to prevent overestimation. All analyses were performed as whole-brain analyses. <mark class="annotated-text">Statistical significance for whole brain analysis was set at p<0.05, Z score > 2.3</mark>.       Supporting Information
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3855767/"
                                       >PMC3855767</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …or each participant, based on the data from the localization run, by computing a GLM with the nuisance predictors and task predictors convolved with a standard two-gamma hemodynamic response function.<mark class="annotated-text"> The ROIs were defined by selecting the 20 most significant functional voxels from the activation cluster closest to the respective coordinates reported in the meta-analysis  . In a second step the average time courses of these ROIs were extracted from the pre-processed and spatially normalized data from the experimental runs. Pearson’s correlation coefficients of the activation-level changes in the selected ROIs were computed block-wise for the 128 experimental task blocks of each individual.</mark> Three different sets of correlations were calculated using three different time windows: 1) a wider task window that included task on- and offset responses to measure the overall task connectivity (2…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3896435/"
                                       >PMC3896435</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … .    We performed a whole-brain voxel-wise analysis. The study design allows the calculation of various effects, i.e. main effect of Group, main effect of Type, and interaction effect Group by Type. <mark class="annotated-text">An uncorrected statistical threshold (i.e., voxel level of significance uncorrected (unc.) for multiple testing) of p<0.005 was set for the main effects and interaction effect. The minimum cluster-size was set at 10 voxels.  </mark>  Our main hypotheses were tested using one-sided t-tests. The participants were measured as ANP and EP in the patient group (DIDanp/DIDep) and in the control group (SIManp/SIMep). Group differences b…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4055615/"
                                       >PMC4055615</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …al activity related to both color or motion concepts remained unchanged. Statistical comparison of concept vs. non-concept activity yielded identical results with or without masking (concept color:   <mark class="annotated-text">p   < 0.05, FWE bilateral; concept motion   p   < 0.05, FWE right hemisphere</mark>). The distinctness of color and motion representations is illustrated in   Figure 8   , showing separable groupings of concept related activity (plotted at a significant level of   p   < 0.001). Cons…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4112936/"
                                       >PMC4112936</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …OS) with sparse sampling functional magnetic resonance imaging (fMRI) to measure task-related BOLD signal changes and to delineate the supraspinal contribution specific to active and passive stepping.<mark class="annotated-text"> Twenty-four</mark> healthy participants underwent fMRI during active and passive, periodic, bilateral, multi-joint, lower limb flexion and extension akin to human gait. Active and passive stepping engaged several corti…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4211402/"
                                       >PMC4211402</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …t comparing musicians and nonmusicians (   P   < 0.005). Correction for multiple comparisons was applied at the cluster level following Monte Carlo simulations conducted in the AlphaSim program [  ]. <mark class="annotated-text">To better detect differences between the two groups, we only included the clusters which were found significantly different between the two groups after five consecutive Tc values of FCD comparisons in the following analysis. Then, for each cluster in which a significant difference was found, the intersection was used as region of interest (ROI) in the subsequent functional connectivity analyses</mark>.      2.6. Functional Connectivity among ROIs    We adopted two strategies to evaluate the relationships among the regions with different local FCD between musicians and nonmusicians: functional conn…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4247966/"
                                       >PMC4247966</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … that particular component were entered into a random-effect analysis model (1 sample   t   -test in SPM5). Brain regions were considered to be within each network if they met a height threshold of   <mark class="annotated-text">P<   0.00001 corrected for multiple comparisons using the family-wise error (FWE) correction and an extent threshold of 50 voxels</mark>.      Second-level analyses of networks of interest    Translations and rotations of the head estimated during realignment stage of pre-processing were regressed out from the time course of each of t…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5315540/"
                                       >PMC5315540</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">info_removed_in_text_extract (6 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ifferences  , realignment to compensate for bulk head motion, segmentation  , normalization to standard MNI space (at  isotropic voxel size), and spatial smoothing with an isotropic Gaussian kernel of<mark class="annotated-text">  </mark>FWHM.    First-level single-subject analysis was conducted using the general linear model (GLM) framework provided by SPM8. Stick functions of the onsets of the two task conditions were convolved with…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510234/"
                                       >PMC3510234</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …fferences  , realignment to compensate for bulk head motion, segmentation  , normalization to standard MNI space (at  isotropic voxel size), and spatial smoothing with an isotropic Gaussian kernel of <mark class="annotated-text"> </mark>FWHM.    First-level single-subject analysis was conducted using the general linear model (GLM) framework provided by SPM8. Stick functions of the onsets of the two task conditions were convolved with…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510234/"
                                       >PMC3510234</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …anges in brain activation consistent at inter-subject level. Significance threshold was set to  (FWE whole-brain corrected for multiple comparisons) and a minimum cluster size of 75 voxels (equates to<mark class="annotated-text">  </mark>) was chosen.    Regions that showed task-related activations were further analyzed for time-dependent changes. We performed GLM analyses for each subject by modeling each task block individually. As …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510234/"
                                       >PMC3510234</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …anges in brain activation consistent at inter-subject level. Significance threshold was set to  (FWE whole-brain corrected for multiple comparisons) and a minimum cluster size of 75 voxels (equates to<mark class="annotated-text">  </mark>) was chosen.    Regions that showed task-related activations were further analyzed for time-dependent changes. We performed GLM analyses for each subject by modeling each task block individually. As …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510234/"
                                       >PMC3510234</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … ,  ; ODT:  ,  ) and response time (EDT:  ,  ; ODT:  ,  ).      fMRI Data     Task-related Effects    The main result of the second-level ANOVA is displayed in  (  FWE corrected, minimum cluster size <mark class="annotated-text"> </mark>). Our contrast of interest was the difference between facial emotion processing and object discrimination tasks. The following clusters were identified: left and right temporal gyrus, posterior cingu…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510234/"
                                       >PMC3510234</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …cted along the upper bank of the superior temporal sulcus (STS); 3 clusters were identified surviving a threshold of 6.5 (threshold   T   value for a   P   < 0.05 familywise error [FWE] corrected, see<mark class="annotated-text">  </mark>and  ).      Effect of Voice Gender    As hypothesized by the overlapping neuronal population model, the regressor modeling the degree of morph did not reveal any regions showing greater activity to e…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3593579/"
                                       >PMC3593579</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …along the upper bank of the superior temporal sulcus (STS); 3 clusters were identified surviving a threshold of 6.5 (threshold   T   value for a   P   < 0.05 familywise error [FWE] corrected, see  and<mark class="annotated-text">  </mark>).      Effect of Voice Gender    As hypothesized by the overlapping neuronal population model, the regressor modeling the degree of morph did not reveal any regions showing greater activity to either…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3593579/"
                                       >PMC3593579</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …f and other descriptiveness   vs   performance of the experimental component of the VV-SORP-T). Results concerning individual differences are reported in  and  , and  and  .    We report within Tables<mark class="annotated-text"> </mark>clusters of size   k    ≥ 67 voxels (approximating the volume of the smoothing kernel) with uncorrected voxel-wise   P    < 0.005 as a criterion selected so as to balance risk against type-I and type-…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3682439/"
                                       >PMC3682439</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … are weighted by their associated   z   -score value as seen in Figure  . This way, regions showing higher correlations are displayed predominantly over less correlated ones. Interactive correlation (<mark class="annotated-text">   z   -</mark>score) and cluster-size (η   min   ) thresholds are also available for visualization purposes. A flood fill algorithm is responsible for determining the minimum number of connected voxels (faces touch…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4531323/"
                                       >PMC4531323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …   z   -score value as seen in Figure  . This way, regions showing higher correlations are displayed predominantly over less correlated ones. Interactive correlation (   z   -score) and cluster-size (<mark class="annotated-text">η   min   </mark>) thresholds are also available for visualization purposes. A flood fill algorithm is responsible for determining the minimum number of connected voxels (faces touching) to form and display fMRI-clust…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4531323/"
                                       >PMC4531323</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">_bad_practice (6 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … and MuR showed small clusters of bilateral occipital activity due to the presence of a picture of the target word throughout each prose trial and the absence of a picture in the baseline MuR trials. <mark class="annotated-text">Because these activations are not relevant to language processing, they are not reported</mark>.    We used correlational methods to examine the relationship between activity, age, and performance. We first identified significant clusters from the separate whole-brain random-effects analyses ca…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2803734/"
                                       >PMC2803734</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ssibility that the discrepancy may simply reflect differences in behavioral tasks. Fourth, the current results were obtained with a relatively liberal threshold. In reporting the correlation results, <mark class="annotated-text">we used an arbitrary threshold </mark>of p<0.005 to highlight the differences between error and non-error processes. These results are thus preliminary and need to be replicated in the future.      Conclusions    We have two main conclusi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2950843/"
                                       >PMC2950843</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …s in the ROIs using a statistical threshold of   p   = 0.05 family-wise error (FWE) corrected for height using small volume correction. We also examined voxel-by-voxel associations in the whole brain <mark class="annotated-text">at a more lenient threshold of   p   = 0.001 uncorrected</mark> for height to examine whether there are any clusters outside the ROIs that showed significant effects at this more lenient threshold.      Statistical analyses of fMRI data: control analyses    Contr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3958698/"
                                       >PMC3958698</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ical task and these aforementioned non-handwriting motor and writing abilities were performed. Statistical threshold was set similarly to the main analysis at   p   = 0.05 FWE corrected for the ROIs (<mark class="annotated-text">and   p   = 0.001 uncorrected for the whole brain to examine whether there are any clusters outside the ROIs that showed significant effects at this more lenient threshold</mark>). Third, whole-brain and ROI analyses were performed correlating brain activation during the supplemental visual-symbol matching and color matching tasks and handwriting skills (rank order of WJ-III …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3958698/"
                                       >PMC3958698</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …TS) but in the left STS.    Unexpectedly, our analysis failed to identify higher activation for reading material compared with non-reading material in left inferior frontal language regions. However, <mark class="annotated-text">after omitting the cluster-level correction</mark>, reading-related activation was identified in opercular and triangular parts of the left inferior frontal gyrus (IFG), as well as in the left insula. This tendency was also evident from stronger and …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4153805/"
                                       >PMC4153805</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …subsequent memory effect model were used to identify regions related to face perception (family-wise correction   p   < 0.05) and successful memory formation (subsequent memory effect:   p   < 0.001, <mark class="annotated-text">uncorrected</mark>) at the group level. Due to the robust effect in left hippocampus, we limited our regions of interest to the left hemisphere, which was also motivated by Smith et al. (  ). As a result, face percepti…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4407577/"
                                       >PMC4407577</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …re used to identify regions related to face perception (family-wise correction   p   < 0.05) and successful memory formation (subsequent memory effect:   p   < 0.001, uncorrected) at the group level. <mark class="annotated-text">Due to the robust effect in left hippocampus, we limited our regions of interest to the left hemisphere</mark>, which was also motivated by Smith et al. (  ). As a result, face perception related regions included the inferior occipital gyrus (IOG:   x   = −40,   y   = −78,   z   = −10) and fusiform gyrus (FUS…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4407577/"
                                       >PMC4407577</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …el random effects analysis for PPI was first FWE corrected at   P    < 0.05. However, because we did not find any significant functional connectivity between brain regions at this threshold level, we <mark class="annotated-text">decided to apply a more lenient threshold</mark> for PPI analysis to investigate any possible connectivity during vicarious reward (for discussion of employing a lenient threshold in social neuroscience studies, see  ): the   t   -images were first…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4769636/"
                                       >PMC4769636</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #dbdb8d;">
        <summary class="label-display">discard_this_paper (5 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ral ACC and amygdala ROIs, as these regions have been specifically implicated in emotional conflict processing  ,  . The amygdala was part of the general EMO mask, but the additional analyses focused <mark class="annotated-text">exclu</mark>sively on amygdala and rACC regions, and as such utilized a more liberal corrected threshold specific to the size of each ROI (i.e., small-volume correction). Thus, for these analyses a reduced cluste…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3052361/"
                                       >PMC3052361</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ponents was performed by a trained operator, The data were later segmented around the event markers, 100 ms before the onset time and 500 ms after. Segments with residual artefacts were automatically <mark class="annotated-text">exclu</mark>ded using the following amplitude parameters: amplitudes of more than −80 µV, or 80 µV, respectively, were considered as artefacts. The non-excluded segments were later averaged. Two peaks were detect…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4184873/"
                                       >PMC4184873</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    PMID25943794        TITLE         Imaging learned fear circuitry in awake <mark class="annotated-text">mice</mark> usingfMRI        ABSTRACT           Abstract    Functional magnetic resonance imaging (   fMRI   ) of learned behaviour in ‘awake rodents’ provides the opportunity for translational preclinical studi…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4744695/"
                                       >PMC4744695</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">PMID25773646</mark>        TITLE         Immediate memory for “when, where and what”: Short‐delay retrieval using dynamic naturalistic material        ABSTRACT           We investigated the neural correlates supporting …
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">abstract only</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5006857/"
                                       >PMC5006857</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">PMID26096737</mark>        TITLE         Impaired planning in Parkinson's disease is reflected by reduced brain activation and connectivity        ABSTRACT           ObjectiveParkinson's disease (PD) often entails impai…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5033031/"
                                       >PMC5033031</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">PMID26096737</mark>        TITLE         Impaired planning in Parkinson's disease is reflected by reduced brain activation and connectivity        ABSTRACT           ObjectiveParkinson's disease (PD) often entails impai…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5033031/"
                                       >PMC5033031</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #f7b6d2;">
        <summary class="label-display">is_annotated (3 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">PMID17389911</mark>        TITLE         Competing Neural Responses for Auditory and Visual Decisions        ABSTRACT           Why is it hard to divide attention between dissimilar activities, such as reading and liste…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1824707/"
                                       >PMC1824707</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">PMID24465794</mark>        TITLE         Windowed Correlation: A Suitable Tool for Providing Dynamic fMRI-Based Functional Connectivity Neurofeedback on Task Difficulty        ABSTRACT           The goal of neurofeedbac…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3896435/"
                                       >PMC3896435</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    <mark class="annotated-text">PMID26257961</mark>        TITLE         Decoding the Formation of New Semantics: MVPA Investigation of Rapid Neocortical Plasticity during Associative Encoding through Fast Mapping        ABSTRACT           Neocortical…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4519547/"
                                       >PMC4519547</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">_not_sure (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ts exceeded an uncorrected threshold of   p   <.001. Clusters were considered significant with a {t} threshold of 3.58, and a “k” extent of 150 voxels. As the “k” extent threshold was estimated using <mark class="annotated-text">resels</mark>, all clusters reached significance after correction for multiple comparisons (p<.05). Interactions between the   shape/category   and   same/different   dimensions were initially evaluated using samp…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3316621/"
                                       >PMC3316621</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …r. Hence, nodes with fewer than 10 voxels were eliminated from the analysis, resulting in 415 nodes for the obtained networks. The total number of voxels which were removed due to this threshold of a <mark class="annotated-text">minimum cluster size</mark> was 313 voxels out of 13407 (eliminated nodes had 3.86 voxels on average with a 2.42 standard deviation, while remaining nodes had 31.55 ± 18.4 voxels on average). Of note is that one possible outcom…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5565317/"
                                       >PMC5565317</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #b8b8b8;">
        <summary class="label-display">annotation_in_progress (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …al MNI space. The SPM anatomy toolbox  was used to establish cytoarchitectonic reference where possible. To investigate the overall effects of tactile stimulation, we used a significance threshold of <mark class="annotated-text">pcluster</mark><0.05, family-wise error (FWE) corrected. To investigate stimulus-specific differences within the network associated with tactile stimulation, this contrast was used as a mask and, based on a priori a…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3174219/"
                                       >PMC3174219</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">_note (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …nse to the CS in the PG mice    Within‐group analysis of brain activation in response to the CS compared with baseline in the PG mice revealed activation of the left amygdala region (   P    = 0.013, <mark class="annotated-text">cluster extent</mark> = 751 voxels, peak   T    = 10.0, coordinates 24, −18, −49; Table   ; Fig.   A). There was a trend for a cluster of activation that extended over the left ectorhinal cortex (Ect), perirhinal cortex (…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">"cluster extent" used here to give the actual size of the cluster, not the min/threshold size AFAICT</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4744695/"
                                       >PMC4744695</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details >
        <summary class="label-display">funny_topic (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    PMID25136305        TITLE         <mark class="annotated-text">The influence of expertise on brain activation of the action observation network during anticipation of tennis and volleyball serve</mark>s        ABSTRACT           In many daily activities, and especially in sport, it is necessary to predict the effects of others' actions in order to initiate appropriate responses. Recently, researche…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4117995/"
                                       >PMC4117995</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #c49c94;">
        <summary class="label-display">info_removed_in_name_extract (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```