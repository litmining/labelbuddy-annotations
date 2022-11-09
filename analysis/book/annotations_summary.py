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

# +
from annotutils import database

connection = database.get_database_connection()
n_annotations = connection.execute(
    "select count(*) as n_annotations from annotation"
).fetchone()["n_annotations"]

print(f"There are {n_annotations} annotations in the database.")
# -

# +
import pandas as pd

label_counts = pd.read_sql(
    "select project, label.name as label_name, count(*) as n_annotations "
    "from annotation inner join label on annotation.label_id = label.id "
    "group by project, label_name having n_annotations > 0 "
    "order by n_annotations desc",
    connection,
)
label_counts.head()
# -

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
