#! /usr/bin/env python3

import pandas as pd

from labelrepo import repo, database
from labelrepo.projects.participant_demographics import (
    get_participant_demographics,
)

subgroups = get_participant_demographics()

docs_info = pd.read_sql(
    "select pmcid, publication_year, title from document "
    "where title is not null",
    database.get_database_connection(),
)
subgroups = subgroups.merge(docs_info, on="pmcid").drop_duplicates(
    subset=("pmcid", "project_name", "annotator_name")
)

out_dir = repo.repo_root() / "analysis" / "book" / "assets" / "generated"
out_dir.mkdir(exist_ok=True, parents=True)
subgroups.to_csv(out_dir / "participant_groups.csv", index=False)
