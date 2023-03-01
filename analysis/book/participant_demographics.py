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

# # Participant demographics

# We started annotating information about each study's participants: their number, sex, age, and possible diagnosis.
# More annotations are needed, but these annotations can already give an approximation of the number of participants in typical fMRI studies, and be used to validate systems that aim to extract that information automatically.
# You can read more about the participant annotations in the corresponding [project page](../projects/participant_demographics.md).

#
# The `labelrepo` package provides helpers to work with these annotations.
# Here we illustrate loading the annotations to make a couple of simple plots.
# The `get_participant_demographics` function returns a `pd.DataFrame` in which each row corresponds to a group of participants in a study, according to one annotator.

# +
from labelrepo.projects.participant_demographics import (
    get_participant_demographics,
)

subgroups = get_participant_demographics()
subgroups.iloc[0]
# -

# In this dataframe, each row contains the information collected by one annotator about a subgroup of participants in a study.
# You can read more about the nature of the annotations in the [project page](../projects/participant_demographics.md).
# The participants are divided into groups ("patients" or "healthy"), then each group is divided into an arbitrary number of *subgroups* (usually there is only one, but there can be several, eg "adolescents" and "adults" within the "healthy" group), and finally each subgroup is divided into "females" and "males".
# The summary dataframe provides information at the level of the subgroup: its name, the group it belongs to, the number of males and females in the subgroup.

# If several annotators have annotated a paper, the information each of them has annotated about each participant subgroup is stored in a separate row.
# We don't want to end up counting participant groups several times so here we simply keep the output of the first annotator for each study.

# +
subset = ["pmcid", "project_name", "annotator_name"]

kept_annotators = set(
    subgroups.loc[:, subset]
    .drop_duplicates(subset=("pmcid",))
    .itertuples(index=False),
)
subgroups = subgroups.loc[
    [
        r in kept_annotators
        for r in subgroups.loc[:, subset].itertuples(index=False)
    ]
]
# -

# The `labelrepo` package also provides a way to load information about documents, labels and annotations in the repository in general.
# Here we use it to read some complementary information about each paper.
# We also add the PMC url to turn scatter plot points into links later.
# Finally, we turn the publication year into a `datetime` to facilitate using it in plots.

# +
from labelrepo.database import get_database_connection

import pandas as pd

docs_info = pd.read_sql(
    "select pmcid, publication_year from document", get_database_connection()
)
subgroups = subgroups.merge(docs_info, on="pmcid")
subgroups["pmc_url"] = [
    f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pmcid}/"
    for pmcid in subgroups["pmcid"].values
]
subgroups["publication_date"] = pd.to_datetime(
    subgroups["publication_year"], format="%Y"
)
# -

# Let's start by looking at the total number of participants in each study.

# +
import altair

total_counts = (
    subgroups.groupby(["pmcid", "pmc_url", "publication_date"])["count"]
    .sum()
    .reset_index()
)

altair.Chart(total_counts).mark_point(size=60).encode(
    x="publication_date:T",
    y=altair.Y("count", scale=altair.Scale(type="log")),
    tooltip=["pmcid"],
    href="pmc_url:N",
).interactive()
# -

# As we do not have too many annotated papers yet, we can look at them individually and inspect the age means and ranges.

# We start by selecting groups for which the mean age is known.

# +
data = subgroups.dropna(subset=("age mean",)).copy()
# -

# The rest is not especially interesting, it is just configuring the plot.

# +
data["subgroup_idx"] = data.groupby("pmcid").cumcount().values
ax = altair.Axis(ticks=False, grid=False, labels=False)
scale = altair.Scale(domain=[-1, 2])
tooltip = [
    "pmcid",
    "group_name",
    "subgroup_name",
    "female count",
    "male count",
    "diagnosis",
]
point = (
    altair.Chart(height=35)
    .mark_point()
    .encode(
        x="age mean",
        y=altair.Y("subgroup_idx", axis=ax, title=None, scale=scale),
        color="group_name",
        size="count",
        href="pmc_url:N",
        tooltip=tooltip,
    )
)
rule = (
    altair.Chart()
    .mark_rule()
    .encode(
        altair.X("age minimum"),
        altair.X2("age maximum"),
        y=altair.Y("subgroup_idx", axis=ax, title=None, scale=scale),
        color="group_name",
        href="pmc_url:N",
        tooltip=tooltip,
    )
)
altair.layer(point, rule, data=data).facet(
    row=altair.Row(
        "pmcid:N",
        header=altair.Header(labelAngle=0, labelAlign="left"),
        sort=altair.Sort(field="age mean", op="mean"),
    ),
).configure_facet(spacing=0).configure_view(stroke=None)
# -

# In the plot above,
#
# - The position of each circle represents the mean of the corresponding subgroup
# - The bar represents the age range (when it is known)
# - The size of the circle represents the number of participants in the subgroup.
