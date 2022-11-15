# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Overview of annotations in the repository

# The data in this repository is in the `projects/` directory and divided into
# projects, each of which contains separate directories for `documents/`,
# `labels/` and `annotations/`.
#
# Labels are stored in JSON files and documents and annotations are stored in
# JSONLines files (one JSON document per line). To load and analyze these
# annotations, we can read these files, or we can use the
# `scripts/make_database.py` script to collect all data in a SQLite database
# (by default in `analysis/data/database.sqlite3`).
#
# Once this is done, we can open a connection to the database to easily obtain
# information about labels, documents and annotations contained in this
# repository as shown below.

# ## Total number of annotations in the repository

# We can use the `annotutils` package provided in this repository, in
# `analysis/annotutils/`, to create the annotations database if necessary and
# obtain a connection from Python scripts.
#
# Install it with `pip install -e analysis/annotutils`

# +
from annotutils import database

connection = database.get_database_connection()
n_annotations = connection.execute(
    "SELECT COUNT(*) AS n_annotations FROM annotation"
).fetchone()["n_annotations"]

print(f"There are {n_annotations} annotations in the database.")
# -

# ## Count label occurrences in each project

# This illustrates collecting the results of a query in a pandas DataFrame for
# further processing, plotting etc.

# We first query the database to obtain how many times each label was used in
# each project, and store the results in a DataFrame.

# +
import pandas as pd

label_counts = pd.read_sql(
    """
    SELECT project, label.name AS label_name, COUNT(*) AS n_annotations
      FROM annotation
      INNER JOIN label ON annotation.label_id = label.id
      GROUP BY project, label_name
      ORDER BY n_annotations DESC
    """,
    connection,
)
label_counts.head()
# -

# Next, for each project we display the number of times each label was used in
# a bar plot.

# +
from matplotlib import pyplot as plt
import seaborn as sns

projects = label_counts.groupby("project")

for project_name, data in projects:
    fig, ax = plt.subplots(figsize=(4, data.shape[0] / 3))
    sns.barplot(
        data=data, x="n_annotations", y="label_name", ax=ax, color="blue"
    )
    ax.set_title(
        f'“{project_name}” project ({data["n_annotations"].sum()} annotations)'
    )
    ax.set_ylabel("")
    sns.despine()
# -
