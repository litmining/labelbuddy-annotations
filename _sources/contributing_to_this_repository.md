# Contributing to this repository

Here we describe how to contribute new annotations to a project in this repository, then how to add a new project. 
If you run into any difficulties don't hesitate to ask for help by {{ "[opening an issue]({})".format(repo_issues_url) }}.


## Clone the repository

The first step is to obtain a local clone of the repository.
[Fork](https://github.com/neurodatascience/labelbuddy-annotations/fork) the repository and clone your fork:

```bash
git clone https://github.com/yourgithubusername/labelbuddy-annotations.git
# or using ssh (recommended):
# git clone git@github.com:yourgithubusername/labelbuddy-annotations.git

cd labelbuddy-annotations
export REPO_ROOT="$(pwd)"
```

## Adding annotations to an existing project

Here we want to contribute to an existing annotation project, using the `autism_mri` project as an example.
The repository contains the documents we will annotate and the labels we will use.
Locally, we will
- Create a `.labelbuddy` file (a binary file which is ignored by **Git** and not added to the repository).
- Import the documents and labels in the `.labelbuddy` file.
- Use {{ lb }} to create some annotations.
- Export our annotations to a `.jsonl` file that will be added to the repository.

In the following we suppose your name is "Firstname Lastname"; you should replace that with your actual name.
We recommend using the same name as in your git configuration, ie the output of:

```bash
git config User.Name
```

This way the name of the annotations file you create and your name in the git log will match.

### Create the `.labelbuddy` file

We first need to install {{ lb }}, see the [installation instructions](https://jeromedockes.github.io/labelbuddy/labelbuddy/current/installation/).
Next we create our `.labelbuddy` file.

`````{tab-set}
````{tab-item} Using the command-line

This can be done using a script provided in the repository:
```bash
python3 scripts/start_project.py projects/autism_mri
cd projects/autism_mri
```

**Or** we can do the same thing manually, using the {{ lb }} command-line interface:

```bash
cd projects/autism_mri
labelbuddy annotations/Firstname_Lastname.labelbuddy \
  --import-labels labels/Article_Terms.json          \
  --import-docs documents/documents_00001.jsonl
```
````

````{tab-item} Using {{ lb }}'s graphical interface

Open labelbuddy from the applications menu, and click **File > Open database**.
In the file dialog, navigate from the root of the repository to `projects/autism_mri/annotations/`, and name the file `Firstname_Lastname.labelbuddy`.

Next, import the labels and documents.
Go to the **Import / Export** tab.
Click **Import labels**, select the `Article_Terms.json` file which is in `projects/autism_mri/labels/`.
Click **Import docs & annotations**, select the `docs_00001.jsonl` file which is in `projects/autism_mri/documents/`.

You can now start creating annotations.
````
`````

### Create some annotations

If you haven't opened {{ lb }} yet you can invoke it with this command:

```bash
labelbuddy annotations/Firstname_Lastname.labelbuddy
```

In the graphical interface, select the **Annotate** tab and start creating annotations.
See the {{ labelbuddy_doc }} for more information about {{ lb }}.

### Export the annotations

Once we have annotated a few documents, we want to push our work back to the upstream repository.
The first step is to export the annotations out of the `.labelbuddy` binary file into a `.jsonl` file.

`````{tab-set}
````{tab-item} Using the command-line

This can be done with `make`, using the `Makefile` found at the root of the repository:
```bash
cd "$REPO_ROOT"
make annotations
```

**Or** we can do the same thing manually:

```bash
labelbuddy annotations/Firstname_Lastname.labelbuddy \
  --export-docs annotations/Firstname_Lastname.jsonl \
  --no-text                                          \
  --labelled-only                                    \
```
````

````{tab-item} Using the graphical interface 

Go to the **Import / Export** tab.
Make sure that the checkboxes are in these states:
```
[X] Export only annotated documents
[ ] Include document text
[X] Include annotations
```

(You only need to check this once, {{ lb }} will remember your choices next time.)
Click **Export docs & annotations**, and select in `projects/autism_mri/annotations/` a file named `Firstname_Lastname.jsonl`.
````
`````


### Push the new annotations

The last step is to get our work included in the upstream repository.
We commit and push the changes, then open a Pull Request.

```bash
git add projects/autism_mri/annotations/Firstname_Lastname.jsonl
git commit -m "Add annotations from Firstname"
```

## Adding a new project

