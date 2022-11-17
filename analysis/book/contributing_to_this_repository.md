# Contributing to this repository


## Clone the repository

```bash
git clone https://github.com/neurodatascience/labelbuddy-annotations.git
# or using ssh (recommended):
# git clone git@github.com:neurodatascience/labelbuddy-annotations.git

cd labelbuddy-annotations
export REPO_ROOT="$(pwd)"
```

## Adding annotations to an existing project

### Create the labelbuddy file

`````{tab-set}
````{tab-item} Command-line
```bash
python3 scripts/start_project.py projects/autism_mri
cd projects/autism_mri
```

or

```bash
cd projects/autism_mri
labelbuddy annotations/Firstname_Lastname.labelbuddy \
  --import-labels labels/Article_Terms.json          \
  --import-docs documents/documents_00001.jsonl
```
````

````{tab-item} GUI

Open labelbuddy, click **File > Open database**.
In the file dialog, navigate to `projects/autism_mri/annotations/` in the repository, and name the file `Firstname_Lastname.labelbuddy`.

Next, import the labels and documents.
Go to the **Import / Export tab**.
Click **Import labels**, select the `Article_Terms.json` file which is in `projects/autism_mri/labels/`.
Click **Import docs & annotations**, select the `docs_00001.jsonl` file which is in `projects/autism_mri/documents/`.

You can now start creating annotations.
````
`````

### Create some annotations

```bash
labelbuddy annotations/Firstname_Lastname.labelbuddy
```

### Export the annotations

`````{tab-set}
````{tab-item} Command-line

```bash
cd "$REPO_ROOT"
make annotations
```

or 

```bash
labelbuddy annotations/Firstname_Lastname.labelbuddy \
  --export-docs annotations/Firstname_Lastname.jsonl \
  --no-text                                          \
  --labelled-only                                    \
```
````

````{tab-item} GUI 

Go to the **Import / Export** tab.
Make sure that the checkboxes are in these states:
```
[X] Export only annotated documents
[ ] Include document text
[X] Include annotations
```

(You only need to check this once, {{ lb }} will remember your choices next time.)
Click **Export docs & annotations**, and select in `projects/autism_mri/annotations/` a file name `Firstname_Lastname.jsonl`.
````
`````


### Push the new annotations

```bash
git status
```

```bash
git add projects/autism_mri/annotations/Firstname_Lastname.jsonl
git commit -m "Add annotations from Firstname"
```

## Adding a new project

