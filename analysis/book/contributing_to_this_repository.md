# Contributing to this repository

Here we describe how to contribute new annotations to a project in this repository, then how to add a new project. 
If you run into any difficulties don't hesitate to ask for help by {{ "[opening an issue]({})".format(repo_issues_url) }}.

(clone_the_repository)=
## Cloning the repository

The first step is to obtain a local clone of the repository.
[Fork](https://github.com/neurodatascience/labelbuddy-annotations/fork) the repository and clone your fork:

```bash
git clone https://github.com/yourgithubusername/labelbuddy-annotations.git
# or using ssh (recommended):
# git clone git@github.com:yourgithubusername/labelbuddy-annotations.git

cd labelbuddy-annotations
export REPO_ROOT="$(pwd)"
```

(adding_annotations_to_an_existing_project)=
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

(create_the_labelbuddy_file)=
### Creating the `.labelbuddy` file

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

### Creating some annotations

If you haven't opened {{ lb }} yet you can invoke it with this command:

```bash
labelbuddy annotations/Firstname_Lastname.labelbuddy
```

In the graphical interface, select the **Annotate** tab and start creating annotations.
See the {{ labelbuddy_doc }} for more information about {{ lb }}.

### Exporting the annotations

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

````{tab-item} Using {{ lb }}'s graphical interface 

Go to the **Import / Export** tab.
Make sure that the checkboxes are in these states:
- 🗹 Export only annotated documents
- ☐ Include document text
- 🗹 Include annotations

(You only need to check this once, {{ lb }} will remember your choices next time.)

Click **Export docs & annotations**, and select in `projects/autism_mri/annotations/` a file named `Firstname_Lastname.jsonl`.
````
`````


### Publishing the new annotations

The last step is to get our work included in the upstream repository.
We commit and push the changes, then open a Pull Request.

```bash
git add projects/autism_mri/annotations/Firstname_Lastname.jsonl
git commit -m "Add annotations from Firstname"
```

## Adding a new project

Rather than contributing to an existing project you can also start a new one.
If you haven't yet, {ref}`Clone the repository <clone_the_repository>`, then create a new directory for your project in `projects/`.

Suppose we want to start a project in which we will annotate imaging modalities.

```bash
cd projects/
mkdir imaging_modalities
cd imaging_modalities
mkdir documents labels annotations
```

Please also add a `README` file describing your project.

### Adding documents

#### Reusing documents from another project

Whenever it makes sense, different projects should annotate the same documents.
Indeed, this makes it possible to combine the annotations from different projects and obtain rich annotations for the shared documents.
For example, if our `imaging_modalities` project uses the same documents as the `participant_demographics` project, by combining them we obtain documents richly annotated with these two types of information.

To reuse the documents from another project, simply add a symbolic link:

```bash
cd documents
ln -s ../../participant_demographics/documents/documents_00001.jsonl
cd ..
```
And if it exists also link the `doc_sources.json` file, which tells how the full dataset from which documents were obtained can be downloaded:

```bash
cd documents
ln -s ../../participant_demographics/documents/doc_sources.json
cd ..
```

(See a more detailed explanation {ref}`here<add-doc-sources-json>`.)

#### Downloading new documents with {{ pg }}

If none of the existing document sets suit your project, you can create a new one using {{ pubget_home }}.
{{ pg }} lets you download articles from {{ pmc_home }} and store them in the format used by this repository.
The articles to download can be selected from a list of PMCIDs, or from a search query for PMC. 
To construct a query, you can use the [PMC advanced search](https://www.ncbi.nlm.nih.gov/pmc/advanced).
Then use it for the {{ pg }} command, for example:

```bash
pubget run                                                                 \
  ./pubget_data                                                            \
  -q "EEG[Abstract] AND MRI[Abstract] AND (2018[PubDate] : 2020[PubDate])" \
  --labelbuddy 
```

Note the `--labelbuddy` option that tells {{ pg }} to prepare the documents in {{ lb }}'s JSONL format.
See the {{ pubget_home }} documentation for details.

Note here we are storing the data in the current directory for simplicity, and `pubget_data` is listed in this repository's `.gitignore` so it will not be tracked by {{ git }}.
However we could store the data anywhere we want; outside of the repository is even better, otherwise we have to make sure we don't add it to the repository by mistake.

Once the download has finished, we recommend uploading the whole output to [OSF](https://osf.io/d2qbh/) and adding the link to the annotation project's `README`.
For example, with the command above {{ pg }} creates a directory named `pubget_data/query_9e14fc5ada411b2f16031d3d1b3c8dd3`.
We can compress it with

```bash
zip -r pubget_data/query_9e14fc5ada411b2f16031d3d1b3c8dd3.zip pubget_data/query_9e14fc5ada411b2f16031d3d1b3c8dd3
```

Then upload the resulting `.zip` file to OSF.
To tell the repository where to find the full archive, add a `documents/doc_sources.json` file as explained {ref}`below<add-doc-sources-json>`.

Finally, we can get the documents.
The directory created by {{ pg }} contains a subdirectory called `subset_allArticles_labelbuddyData`, containing `.jsonl` files.
Those are the files we will be adding to the annotations repository, importing into {{ lb }}, and annotating.
By default {{ pg }} splits its output into files containing 500 articles each; to begin with copying only the first one is enough.

```bash
cp pubget_data/query_9e14fc5ada411b2f16031d3d1b3c8dd3/subset_allArticles_labelbuddyData/documents_00001.jsonl documents/
```

(add-doc-sources-json)=
#### Adding the source dataset location information

This repository provides an easy way to {ref}`download the full dataset<obtaining-the-full-datasets>`.
For this to work, we must tell it where to find it by adding a JSON file in our project's `documents/` directory.
The file must be in `projects/my_project/documents/doc_sources.json`.
It contains a list of JSON objects, each having 2 keys:
- `url`: the URL from which to download the archive we created, typically an OSF download URL.
- `name`: the name of the directory contained in the archive, ie the name of the directory created by {{ pg }} -- in our case, `"query_9e14fc5ada411b2f16031d3d1b3c8dd3"`. 
Note this is not the name of the archive itself but of the single directory that the archive contains.
In particular, the `name` does not have an extension (such as `.zip` or `.tar.gz`).

Therefore in our case the file would look like:
```
[
    {
    "url": "https://osf.io/download/[ ... ]",
    "name": "query_9e14fc5ada411b2f16031d3d1b3c8dd3"
    }
]
```

See the corresponding files in existing projects for more examples.

If we have not downloaded new documents but added a symlink to documents already in another project, we can copy the `url` and `name` from that project's `doc_sources.json`.

### Adding the labels

Next we need to create the labels.
Here also, when it makes sense consider reusing some labels from other projects, possibly using GitHub issues to communicate with other contributors about harmonizing labels.
Indeed, if all projects agree that for example the number of study participant is denoted `n_participants`, that makes it easier to aggregate and reuse annotations than if one project calls it `n_participants` and another uses `Participants count`.
If we want to reuse exactly the same labels as another project we can create a symbolic link. 
To create a new labels file we can either manually edit a JSON file, or create the labels within {{ lb }}.
The latter is probably more convenient, especially if we decide on the labels as we start reading and annotating the first few documents.

To create the labels in {{ lb }}, create a `.labelbuddy` as explained {ref}`above<create_the_labelbuddy_file>`.
Thus you will end up with a file like `annotations/Firstname_Lastname.labelbuddy` containing the documents.
Open it, and add some labels in the **Dataset** tab.
Then export the labels.

`````{tab-set}
````{tab-item} Using the command-line

```bash
labelbuddy annotations/Firstname_Lastname.labelbuddy \
  --export-labels labels/imaging_modality_labels.json
```
````

````{tab-item} Using {{ lb }}'s graphical interface

In the **Import / Export** tab, click **Export labels**, and select a file in the `annotations` directory; make sure the extension is `.json`.
````
`````

### Publishing the new project

Once all of this is done you can `git add` and `git push` your changes, open a Pull Request, and the new project will become visible in the upstream repository.
You can start creating annotations as explained {ref}`above<adding_annotations_to_an_existing_project>`.

## Adding pages to this documentation

Another way to contribute is to add pages to this documentation, to share analyses, describe a project in depth etc.

The contents are in `analysis/book` below the root of the repository.

```bash
cd analysis/book
pip install -r requirements.txt
```

The html version is built with [jupyter-book](https://jupyterbook.org/en/stable/start/overview.html), see its documentation for details.

To add a new page you will need to create a `.py` or `.md` file in the books directory, and add it to the list of chapters in `analysis/book/_toc.yml`.
To build the book locally, run `make book-full` from the root of the repository.
(Once the database and CSV file have already been built, you can just use `make book` which is faster.)
You can then see it by pointing your browser to `analysis/book/_build/html/index.html`.
