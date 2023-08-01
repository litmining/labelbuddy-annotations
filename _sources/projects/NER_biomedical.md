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


# NER_biomedical

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/NER_biomedical/).

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
    
    <details style="--label-color: #fcaf3e;">
        <summary class="label-display">NER method (9 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … algorithm to identify such structures and modify the results of our ML-based tagger. This is called pattern-based post-processing. 


## Results 
  
To develop our ML-based Bio-NER system, we employ <mark class="annotated-text">conditional random fields</mark>, which have performed effectively in several well-known tasks, as our underlying ML model. Adding selected conjunction features, applying numerical normalization, and employing pattern-based post-pro…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1764467/"
                                       >PMC1764467</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …any natural language processing system aimed at managing the wealth
of biomedical information that is available electronically. To support term recognition
in the biomedical domain, we have developed <mark class="annotated-text">Termino</mark>, a large-scale terminological
resource for text processing applications, which has two main components: first, a
database into which very large numbers of terms can be loaded from resources such
as U…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2448598/"
                                       >PMC2448598</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … has two main components: first, a
database into which very large numbers of terms can be loaded from resources such
as UMLS, and stored together with various kinds of relevant information; second,
a <mark class="annotated-text">finite state recognizer</mark>, for fast and efficient identification and mark-up of terms
within text. Since many biomedical applications require this functionality, we have
made Termino available to the community as a web servic…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2448598/"
                                       >PMC2448598</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rmance. The proposed method includes Natural Language Processing (NLP) tasks for text preprocessing, learning word representation features from a large amount of text data for feature extraction, and <mark class="annotated-text">conditional random fields</mark> for token classification. Other than the free text in the domain, the proposed method does not rely on any lexicon nor any dictionary in order to keep the system applicable to other NER tasks in bio-…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … free text in the domain, the proposed method does not rely on any lexicon nor any dictionary in order to keep the system applicable to other NER tasks in bio-text data. 


## Results 
  
We extended <mark class="annotated-text">BANNER</mark>, a biomedical NER system, with the proposed method. This yields an integrated system that can be applied to chemical and drug NER or biomedical NER. We call our branch of the BANNER system BANNER-CHE…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ic information are matched to the tokens to give orthographic information. These baseline features are summarized in Table  . 
  
The baseline features. 
  
For word representation features, we train <mark class="annotated-text">Brown clustering models</mark> [ ] and Word Vector (WV) models [ ] on a large PubMed and PMC document collection. Brown clustering is a hierarchical word clustering method, grouping words in an input corpus to maximize the mutual …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e tokens to give orthographic information. These baseline features are summarized in Table  . 
  
The baseline features. 
  
For word representation features, we train Brown clustering models [ ] and <mark class="annotated-text">Word Vector (WV) models</mark> [ ] on a large PubMed and PMC document collection. Brown clustering is a hierarchical word clustering method, grouping words in an input corpus to maximize the mutual information of bigrams. Therefor…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …arized in Table  . 
  
The baseline features. 
  
For word representation features, we train Brown clustering models [ ] and Word Vector (WV) models [ ] on a large PubMed and PMC document collection. <mark class="annotated-text">Brown clustering is a hierarchical word clustering method</mark>, grouping words in an input corpus to maximize the mutual information of bigrams. Therefore, the quality of a partition can be computed as a sum of mutual information weights between clusters. It run…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …quality of a partition can be computed as a sum of mutual information weights between clusters. It runs in time O(V × K ), where V is the size of the vocabulary and K is the number of clusters. 

The <mark class="annotated-text">VW model is induced via a Recurrent Neural Network (RNN)</mark> and can be seen as a language model that consists of   n  -dimensional continuous valued vectors, each of which represents a word in the training corpus. The RNN instance is trained to predict either…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ns of documents to process within an hour. We used a tool implemented by Mikolov et al. [ ] to build our WV model from the PubMed collection. 

Further, the word vectors are clustered using a K-means <mark class="annotated-text">algorithm</mark> to drive a Word Vector Class (WVC) model. Since Brown clustering is a bigram model, this model may not be able to carry wide context information of a word, whereas the WVC model is an   n  -gram mode…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #729fcf;">
        <summary class="label-display">entity (7 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    … into other systems by using the BANNER Unstructured Information Management Architecture (UIMA) interface. 

BANNER-CHEMDNER achieved an 85.68% and an 86.47% F-measure on the testing sets of CHEMDNER <mark class="annotated-text">Chemical</mark> Entity Mention (CEM) and Chemical Document Indexing (CDI) subtasks, respectively, and achieved an 87.04% F-measure on the official testing set of the BioCreative II gene mention task, showing remarka…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … testing sets of CHEMDNER Chemical Entity Mention (CEM) and Chemical Document Indexing (CDI) subtasks, respectively, and achieved an 87.04% F-measure on the official testing set of the BioCreative II <mark class="annotated-text">gene</mark> mention task, showing remarkable performance in both chemical and biomedical NER. BANNER-CHEMDNER system is available at:  . 

 

# Body
 
## Background 
  
As biomedical literature on servers grows …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … word classes. Finally, we apply the CRF sequence-labeling method to the extracted feature vectors to train the NER model. These steps will be described in subsequent sections. 
  
 System design for <mark class="annotated-text">chemical</mark> and drug Named Entity Recognition  . The solid lines represent the flow of labeled data, and the dotted lines represent the flow of unlabeled data. 
  
### Preprocessing 
  
Preprocessing is where te…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …. Finally, we apply the CRF sequence-labeling method to the extracted feature vectors to train the NER model. These steps will be described in subsequent sections. 
  
 System design for chemical and <mark class="annotated-text">drug</mark> Named Entity Recognition  . The solid lines represent the flow of labeled data, and the dotted lines represent the flow of unlabeled data. 
  
### Preprocessing 
  
Preprocessing is where text data i…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Xu, Kai and Zhou, Zhanfan and Gong, Tao and Hao, Tianyong and Liu, Wenyin
BMC Med Inform Decis Mak, 2018

# Title

SBLC: a hybrid model for <mark class="annotated-text">disease</mark> named entity recognition based on semantic bidirectional LSTMs and conditional random fields

# Keywords

Biomedical informatics
Text mining
Machine learning
Neural networks


# Abstract
 
## Backgro…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6284263/"
                                       >PMC6284263</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    Hemati, Wahed and Mehler, Alexander
J Cheminform, 2019

# Title

LSTMVoter: <mark class="annotated-text">chemical</mark> named entity recognition using a conglomerate of sequence labeling tools

# Keywords

BioCreative V.5
CEMP
CHEMDNER
BioNLP
Named entity recognition
Deep learning
LSTM
Attention mechanism


# Abstract…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6689880/"
                                       >PMC6689880</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …mework for bacterial named entity recognition with domain features

# Keywords

Named entity recognition
Biomedical text mining
Conditional random field
Deep learning


# Abstract
 
## Background 
  
<mark class="annotated-text">Microbes</mark> have been shown to play a crucial role in various ecosystems. Many human diseases have been proved to be associated with bacteria, so it is essential to extract the interaction between bacteria for m…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6886245/"
                                       >PMC6886245</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …e drug events
natural language processing
deep learning
information extraction
adverse drug reaction reporting systems
named entity recognition
relation extraction


# Abstract
 
## Background 
  
An <mark class="annotated-text">adverse drug event </mark>(ADE) is commonly defined as “an injury resulting from medical intervention related to a drug.” Providing information related to ADEs and alerting caregivers at the point of care can reduce the risk o…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7382020/"
                                       >PMC7382020</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …hian Dinani, Soudabeh and Millagaha Gedara, Nuwan Indika and Xu, Xuan and Richards, Emily and Maunsell, Fiona and Zad, Nader and Tell, Lisa A.
Front Vet Sci, 2021

# Title

Large-Scale Data Mining of <mark class="annotated-text">Rapid Residue Detection Assay Data </mark>From HTML and PDF Documents: Improving Data Access and Visualization for Veterinarians

# Keywords

MRL and tolerance
commercial rapid assay test
machine learning
large scale data mining
table extract…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8334182/"
                                       >PMC8334182</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ummaries in popup windows containing knowledge related to the identified terms along with links to various databases. It uses the EXTRACT tagging service to perform named entity recognition (NER) for <mark class="annotated-text">genes/proteins, chemical compounds, organisms, tissues, environments, diseases, phenotypes and gene ontology terms</mark>. Multiple files can be analyzed, whereas identified terms such as proteins or genes can be explored through functional enrichment analysis or be associated with diseases and PubMed entries. Finally, …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8494211/"
                                       >PMC8494211</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ef2929;">
        <summary class="label-display">performance (5 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …have performed effectively in several well-known tasks, as our underlying ML model. Adding selected conjunction features, applying numerical normalization, and employing pattern-based post-processing <mark class="annotated-text">improve the F-scores by 1.67%, 1.04%, and 0.57%, respectively. The combined increase of 3.28% yields a total score of 72.98%,</mark> which is better than the baseline system that only uses singleton features. 


## Conclusion 
  
We demonstrate the benefits of using the sequential forward search algorithm to select effective conju…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1764467/"
                                       >PMC1764467</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …cuments per minute, is configurable via XML, and can be plugged into other systems by using the BANNER Unstructured Information Management Architecture (UIMA) interface. 

BANNER-CHEMDNER achieved an <mark class="annotated-text">85.68% and an 86.47% F-measure</mark> on the testing sets of CHEMDNER Chemical Entity Mention (CEM) and Chemical Document Indexing (CDI) subtasks, respectively, and achieved an 87.04% F-measure on the official testing set of the BioCreat…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …

BANNER-CHEMDNER achieved an 85.68% and an 86.47% F-measure on the testing sets of CHEMDNER Chemical Entity Mention (CEM) and Chemical Document Indexing (CDI) subtasks, respectively, and achieved an <mark class="annotated-text">87.04% F-measure</mark> on the official testing set of the BioCreative II gene mention task, showing remarkable performance in both chemical and biomedical NER. BANNER-CHEMDNER system is available at:  . 

 

# Body
 
## Ba…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …l through comparing with nine state-of-the-art baseline methods including cTAKES, MetaMap, DNorm, C-Bi-LSTM-CRF, TaggerOne and DNER. 


## Results 
  
The results show that the SBLC model achieves an <mark class="annotated-text">F1 score of 0.862</mark> and outperforms the other methods. In addition, the model does not rely on external domain dictionaries, thus it can be more conveniently applied in many aspects of medical text processing. 


## Con…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6284263/"
                                       >PMC6284263</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …mechanism. LSTMVoter outperforms each extractor integrated by it in a series of experiments. On the BioCreative IV chemical compound and drug name recognition (CHEMDNER) corpus, LSTMVoter achieves an <mark class="annotated-text">F1-score of 90.04%</mark>; on the BioCreative V.5 chemical entity mention in patents corpus, it achieves an F1-score of 89.01%. 


## Availability and implementation 
  
Data and code are available at  . 

 

# Body
 
## Intr…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6689880/"
                                       >PMC6689880</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ioCreative IV chemical compound and drug name recognition (CHEMDNER) corpus, LSTMVoter achieves an F1-score of 90.04%; on the BioCreative V.5 chemical entity mention in patents corpus, it achieves an <mark class="annotated-text">F1-score of 89.01%</mark>. 


## Availability and implementation 
  
Data and code are available at  . 

 

# Body
 
## Introduction 
  
In order to advance the fields of biological, chemical and biomedical research, it is im…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6689880/"
                                       >PMC6689880</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …cognition, which integrates domain features into a deep learning framework combining bidirectional long short-term memory network and convolutional neural network. When domain features are not added, <mark class="annotated-text">F1-measure of the model achieves 89.14%</mark>. After part-of-speech (POS) features and dictionary features are added, F1-measure of the model achieves 89.7%. Hence, our model achieves an advanced performance in bacterial NER with the domain feat…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6886245/"
                                       >PMC6886245</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …rm memory network and convolutional neural network. When domain features are not added, F1-measure of the model achieves 89.14%. After part-of-speech (POS) features and dictionary features are added, <mark class="annotated-text">F1-measure of the model achieves 89.7%</mark>. Hence, our model achieves an advanced performance in bacterial NER with the domain features. 


## Conclusions 
  
We propose an efficient method for bacterial named entity recognition which combine…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6886245/"
                                       >PMC6886245</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #8ae234;">
        <summary class="label-display">document type (4 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …7.04% F-measure on the official testing set of the BioCreative II gene mention task. 


## Methods 
  
Our chemical and drug NER system design is shown in Figure  . First, we perform preprocessing on <mark class="annotated-text">MEDLINE and PMC document collection</mark> and then extract two different feature sets, a base feature set and a word representation feature set, in the feature processing phase. The unlabeled set of the collection is fed to unsupervised lear…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    … is essential to extract the interaction between bacteria for medical research and application. At the same time, many bacterial interactions with certain experimental evidences have been reported in <mark class="annotated-text">biomedical literature</mark>. Integrating this knowledge into a database or knowledge graph could accelerate the progress of biomedical research. A crucial and necessary step in interaction extraction (IE) is named entity recogn…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6886245/"
                                       >PMC6886245</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …ecords (EHRs) as either coded problems or allergies are often incomplete, leading to underreporting. Therefore, it is important to develop capabilities to process unstructured EHR data in the form of <mark class="annotated-text">clinical notes</mark>, which contain a richer documentation of a patient’s ADE. Several natural language processing (NLP) systems have been proposed to automatically extract information related to ADEs. However, the resul…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7382020/"
                                       >PMC7382020</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …biomedical terms from such files in an automated way is absolutely necessary. In this article, we present OnTheFly , a web application for extracting biomedical entities from individual files such as <mark class="annotated-text">plain texts, office documents, PDF files or images</mark>. OnTheFly  can generate informative summaries in popup windows containing knowledge related to the identified terms along with links to various databases. It uses the EXTRACT tagging service to perfo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8494211/"
                                       >PMC8494211</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #4e9a06;">
        <summary class="label-display">processing (pre or post) (2 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …an be beneficial, but it would be infeasible to include all conjunction features in an NER model since memory resources are limited and some features are ineffective. To resolve the problem, we use a <mark class="annotated-text">sequential forward search algorithm</mark> to select an effective set of features. Second, variations in the numerical parts of biomedical terms (e.g., &#34;2&#34; in the biomedical term IL2) cause data sparseness and generate many redundant features…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1764467/"
                                       >PMC1764467</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …et of features. Second, variations in the numerical parts of biomedical terms (e.g., &#34;2&#34; in the biomedical term IL2) cause data sparseness and generate many redundant features. In this case, we apply <mark class="annotated-text">numerical normalization</mark>, which solves the problem by replacing all numerals in a term with one representative numeral to help classify named entities. Third, the assignment of NE tags does not depend solely on the target wo…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1764467/"
                                       >PMC1764467</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …g and two subsequent words). We use global patterns generated by the Smith-Waterman local alignment algorithm to identify such structures and modify the results of our ML-based tagger. This is called <mark class="annotated-text">pattern-based post-processing.</mark> 


## Results 
  
To develop our ML-based Bio-NER system, we employ conditional random fields, which have performed effectively in several well-known tasks, as our underlying ML model. Adding selecte…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1764467/"
                                       >PMC1764467</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …labeled data. 
  
### Preprocessing 
  
Preprocessing is where text data is cleaned and processed via NLP tasks and is a preparatory task for feature processing. 

First, the text data is cleansed by <mark class="annotated-text">removing non-informative characters</mark> and replacing special characters with corresponding spellings. The text is then tokenized with a tokenization tool. We evaluated two different tokenization strategies: a simple white space tokenizer …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …Preprocessing is where text data is cleaned and processed via NLP tasks and is a preparatory task for feature processing. 

First, the text data is cleansed by removing non-informative characters and <mark class="annotated-text">replacing special characters with corresponding spellings</mark>. The text is then tokenized with a tokenization tool. We evaluated two different tokenization strategies: a simple white space tokenizer and the BANNER simple tokenizer. The white space tokenizer spl…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …is a preparatory task for feature processing. 

First, the text data is cleansed by removing non-informative characters and replacing special characters with corresponding spellings. The text is then <mark class="annotated-text">tokenized</mark> with a tokenization tool. We evaluated two different tokenization strategies: a simple white space tokenizer and the BANNER simple tokenizer. The white space tokenizer splits the text simply, based o…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #f57900;">
        <summary class="label-display">features (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …enizer splits the text simply, based on blanks within it, whereas the BANNER tokenizer breaks tokens into either a contiguous block of letters and/or digits or a single punctuation mark. Finally, the <mark class="annotated-text">lemma</mark> and the part-of-speech (POS) information were obtained for a further usage in the feature extraction phase. In BANNER-CHEMDNER, BioLemmatizer [ ] was used for lemma extraction, which resulted in a si…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …the text simply, based on blanks within it, whereas the BANNER tokenizer breaks tokens into either a contiguous block of letters and/or digits or a single punctuation mark. Finally, the lemma and the <mark class="annotated-text">part-of-speech (POS) information</mark> were obtained for a further usage in the feature extraction phase. In BANNER-CHEMDNER, BioLemmatizer [ ] was used for lemma extraction, which resulted in a significant improvement in overall system p…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331699/"
                                       >PMC4331699</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #ad7fa8;">
        <summary class="label-display">location (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …for drug names or other fields were observed while extracting data tables. 


### Desired Information From Structured or Unstructured Documents 
  
Below we review multiple cases to extract data from <mark class="annotated-text">tables</mark>. For these cases, it is required to check if the keywords determined important in the real-time data collection via PDF and webpage parsing are clearly characterized in the extracted tables provided …
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8334182/"
                                       >PMC8334182</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
            <div class="annotation">
                <div class="context">
                    …g beta-lactams, tetracyclines, aminoglycosides, and sulfonamides from the website   ( ). Therefore, using our trained model based on the Python packages of   requests   and   BeautifulSoup  , all the <mark class="annotated-text">rapid assay URL links </mark>for dairy tests are parsed and automatically examined for potentially available tables on each page. Below we presented an example of adaptable parsing of real-time data extracting. When the query pin…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8334182/"
                                       >PMC8334182</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #888a85;">
        <summary class="label-display">exclude (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    Xing, Yuting and Wu, Chengkun and Yang, Xi and Wang, Wei and Zhu, En and Yin, Jianping
Molecules, 2018

# Title

<mark class="annotated-text">ParaBTM</mark>: A Parallel Processing Framework for Biomedical Text Mining on Supercomputers

# Keywords

biomedical text mining
big data
Tianhe-2
parallel computing
load balancing


# Abstract
 
A prevailing way o…
                </div>
                <div class="annotation-footer">
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6099625/"
                                       >PMC6099625</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #eeeeec;">
        <summary class="label-display">interesting (1 docs)</summary>
        
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            
            <div class="annotation">
                <div class="context">
                    …ications are helpful in finding the gene, disease, chemical, drugs, protein entities. Finding entities relation such as gene–gene entities, drug-disease interaction, and chemical protein relation the <mark class="annotated-text">PubExN</mark> can be helpful for these types of biomedical applications. In most cases, domain experts do this extraction process on their own. Human interference makes this process time-consuming and there is a h…
                </div>
                <div class="annotation-footer">
                    <div class="extra-data">similar to pubget?</div>
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10132428/"
                                       >PMC10132428</a></div>
                    <div class="annotator-name">Kendra_Oudyk</div>
                </div>
            </div>
            
        </div>
        
    </details>
    
    <details style="--label-color: #babdb6;">
        <summary class="label-display">note (0 docs)</summary>
        
        <p>(No annotations with this label in the current project)</p>
        
    </details>
    
</div>
"""
displays.HTMLDisplay(text)
```
