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

# # Plot the number of participants

# +
import os

import pandas as pd
import matplotlib.pyplot as plt
# -

# ## Load the data
# it's a .csv that contains all the annotations in this repo, with one row per annotation

current_folder = globals()['_dh'][0]
data_path = os.path.join(current_folder, "all_annotations.csv")
df = pd.read_csv(data_path, index_col=False)
df.pmcid = df.pmcid.astype(int)
df.head(3)

# ## View labels used in each project

for project, group in df.groupby("document_from_project"):
    print('Project: ', project.upper())
    labels = list(set(group['annotation_label_name']))
    labels.sort()
    print('Labels: ')
    for label in labels:
        print("\t", label)
    print('-----------------------')
    

# ## Choose which labels to use
# by inspecting the lists above

select_labels = [
    "N included",
    "n_participants",
    "n_participants_total",
    "N_Total"
]

# ## Select the subset of the dataframe that contains one of our select labels

df_subset = df[df["annotation_label_name"].isin(select_labels)]
df_subset.head(3)

# ## [make sure there's only one row for each pmid]

# ## Convert the annotated text to integers
# this is not the best way, I think. 

# +
from participants_demographics import _reading


class TextToNumber:
    def __init__(self):
        self.parser = _reading._get_parser(
            start="number", ambiguity="resolve", grammar="numbers_grammar"
        )
        self.transformer = _reading.ParticipantsTransformer(0)

    def __call__(self, text):
        try:
            parse_tree = self.parser.parse(text)
            return self.transformer.transform(parse_tree).value
        except Exception:
            return None
text_to_num = TextToNumber()

for i, row in df_subset.iterrows():
    n_str = row['annotated_text']
    n_int = text_to_num(n_str)
    df_subset.loc[i, "n_ptp_int"] = n_int
# -

fig, ax = plt.subplots()
df_subset['n_ptp_int'].hist()
ax.set_ylabel('Number of papers')
ax.set_xlabel('Number of participants')
