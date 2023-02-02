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

# dynamic_functional_connectivity

See also this project's [folder on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/dynamic_functional_connectivity/).

## Dynamic Functional Connectivity methods

The focus of this project is to explore how methods for estimating Dynamic Functional Connectivity (DFC) are used in the literature.
Related code and documentation can be found in a dedicated GitHub [repository](https://github.com/neurodatascience/dfc_text_mining).

The documents have been collected with **pubget** and the whole **pubget** output can be found on [OSF](https://osf.io/2ekbd).


## Labels in this project

```{code-cell}
:tags: [remove-input]

from labelrepo import displays
text = """
<div class="detailed-label-set">
    
    <details style="--label-color: #aec7e8;">
        <summary class="label-display">N participants (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ons of subject specific time courses of each of the hidden unit expressed in a correlation matrix. 


### 2.3. An fMRI data application 
  
Data used in this work comprised of task-related scans from <mark class="annotated-text">28</mark> (five females) healthy participants, all of whom gave written, informed, IRB-approved consent at Hartford Hospital and were compensated for participation . All participants were scanned during an aud…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4138493/"
                                       >PMC4138493</a></div>
                    <div class="annotator-name">Jerome_Dockes</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ffbb78;">
        <summary class="label-display">N included (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```