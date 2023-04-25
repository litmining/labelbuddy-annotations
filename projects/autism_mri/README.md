# autism_mri

Repo to do LabelBuddy annotations of a corpus of Autism MRI literature

## Papers

### How the papers were obtained
We ran the following bash command:

```bash
pubget run -q "Brain Volume MRI 2022 Autism" pubget/test --labelbuddy --n_jobs 4
```
### Where the full papers are stored
The full pubget output is stored on OSF: [https://osf.io/meya4](https://osf.io/meya4).
## Annotations
### File(s) being annotated: 
- `/projects/autism_mri/documents/documents_00001.jsonl`
  - corresponding file in the pubget output: 
    - `query_6b2c09de69c29c29626f794757ea4c68/subset_allArticles_labelbuddyData/documents_00001.jsonl`
  
### Annotation labels:
- FieldStrength: `<description of label1>`
- Diagnosis: `<description of label2>` 
- N_Total:
- N_Total_Male:
- N_Total_Female
- N_Patients
- N_Controls
- N_Controls_Male
- N_Controls_Female
- N_Patients_Male
- N_Patients_Female
- Age_Mean
- Age_Min
- Age_Max
- Scanner
- AnalysisTool
- MRI_Modality
### Labels found in other projects as well:
- `<label2>`

### Instructions for annotators
`<description>`

