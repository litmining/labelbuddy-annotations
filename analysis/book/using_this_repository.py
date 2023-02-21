# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Using this repository

# + [markdown]
# Start by cloning the repository:
# ```bash
# git clone https://github.com/neurodatascience/labelbuddy-annotations.git
# cd labelbuddy-annotations
# ```
# -
#
# The documents, labels and annotations are stored in JSON or JSONLines files in the `projects/` directory.

# ## Building the database
#
# We can easily create a [SQLite](https://www.sqlite.org/) database containing all the information in the repository (but if you don't like SQL you can [use a CSV file instead](#using-a-csv-rather-than-a-database)):
# ```bash
# make database
# ```
# Or equivalently, _e.g._ if `make` is not available:
# ```bash
# python3 ./scripts/make_database.py
# ```
# We can then use this database to query the contents of the repository, either with the `sqlite3` interactive command:
# ```bash
# sqlite3 analysis/data/database.sqlite3
# ```
# or using **SQLite** bindings that are available in many languages, including Python's standard library module [sqlite3](https://docs.python.org/3/library/sqlite3.html).
#
# A small Python package containing a few utilities for working with this repository is also provided in `analysis/labelrepo`. You can install it with
# ```bash
# pip install -e "analysis/labelrepo[all]"
# ```
# (note the `-e`, or `--editable`, option).


# The main tables are `annotation`, `document` and `label`.
# `detailed_annotation` is a view gathering detailed information about each annotation, such as the `selected_text`, a snippet of surrounding text (`context`), the `label_name` and `annotator_name`, etc.
# For example, to display a few annotations:

# +
from labelrepo import database, displays

connection = database.get_database_connection()

annotations = connection.execute("SELECT * FROM detailed_annotation limit 5")
displays.AnnotationsDisplay(annotations)
# -

# As another example (this time collecting results in a Pandas DataFrame), selecting all snippets of text that have been annotated with "Diagnosis":

# +
import pandas as pd

pd.read_sql(
    """
    SELECT selected_text, COUNT(*) as occurrences
    FROM detailed_annotation
    WHERE label_name = "Diagnosis"
    GROUP BY selected_text
    ORDER BY occurrences DESC
    """,
    connection,
)
# -


# ## Using a CSV rather than a database

# If you prefer working with CSVs than SQL, you can also run (at the root of the repository)
# ```bash
# make csv
# ```
# That will create a file `analysis/data/detailed_annotation.csv` containing the detailed annotations table:

# +
from labelrepo import repo

csv_file = repo.data_dir() / "detailed_annotation.csv"
annotations = pd.read_csv(csv_file, nrows=3)
displays.AnnotationsDisplay(annotations)
# -

# Here is all the information in that table for the first annotation:

# +
(
    annotations.iloc[:1]
    .stack()
    .reset_index()
    .style.hide("level_0", axis=1)
    .hide(axis="index")
    .hide(axis="columns")
)
# -

# ## Using the JSON and JSONLines files directly

# `.jsonl` (JSONLines) files contain one JSON dictionary per line. They can
# easily be parsed for example with the [json](https://docs.python.org/3/library/json.html) Python standard library module. Moreover the
# `labelrepo` package contains a convenience function for parsing JSON or
# JSONLines files:

# +
from labelrepo import read_json

annotations_file = (
    repo.repo_root()
    / "projects"
    / "participant_demographics"
    / "annotations"
    / "Jerome_Dockes.jsonl"
)

for row in read_json(annotations_file)[:3]:
    print(row)
# -

# Loading labels from a JSON file:

labels_file = (
    repo.repo_root()
    / "projects"
    / "autism_mri"
    / "labels"
    / "Article_Terms.json"
)
read_json(labels_file)

#(obtaining-the-full-datasets)=
# ## Obtaining the full datasets

# This repository only contains the batches of documents currently being annotated.
# These are typically part of a larger dataset, usually created with {{ pubget_home }}.
# It is possible to obtain the full dataset from which the annotated documents were drawn.
# From the command-line this can be done with the `download_datasets.py` script:
#
# ```bash
# python3 ./scripts/download_datasets.py [ PROJECT NAME ]
# ```
#
# In Python, it can be done with the `labelrepo.datasets` module:
#
# ```python
# from labelrepo import datasets
# project_datasets = datasets.get_project_datasets(project_name)
# ```
#
# The datasets are stored in `analysis/data/datasets/`.
