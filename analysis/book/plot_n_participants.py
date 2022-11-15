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

# # Plot the number of participants

# ## Load the data
# By using pandas to run sql code to query the sqlite database

# +
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from annotutils import database
from participants_demographics import _reading


connection = database.get_database_connection()

select_labels = [
    "N included",
    "n_participants",
    "n_participants_total",
    "N_Total"
]

df = pd.read_sql(
    """
    SELECT * FROM  detailed_annotation
        WHERE label_name in ("N included", "n_participants", "n_participants_total", "N_Total");
    
    """,
    connection,
)

df.head()
# -

# ## Convert the annotated text to integers
# this is not the best way, I think. 

# +


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

for i, row in df.iterrows():
    if row['extra_data']:
        n_int = text_to_num(row['extra_data'])
    else:
        n_int = text_to_num(row['selected_text'])
    df.loc[i, "n_ptp_int"] = n_int
    
df.dropna(subset=['n_ptp_int'], inplace=True)
df['n_ptp_int'] = df['n_ptp_int'].astype(int)
# -

df.head()

# ## Frequency of differt sample sizes

fig, ax = plt.subplots(figsize=(10,5))
df['n_ptp_int'].hist(bins=100)
ax.set_ylabel('Number of papers')
ax.set_xlabel('Number of participants')

# ## Sample sizes over time

fig, ax = plt.subplots()
df.plot.scatter(x='publication_year', y='n_ptp_int', ax=ax, alpha=.3)

fig, ax = plt.subplots()
sns.lineplot(
    data = df,
    x="publication_year",
    y="n_ptp_int",
    ax=ax
)
