import json
import ast
from pathlib import Path

import pandas as pd

from nimf.data import constants

projects_folder_path = Path(__file__).resolve().parent / "projects"
projects_list = projects_folder_path.iterdir()
pmids_and_pmcids = pd.read_csv(constants.PATH_TO_OPEN_FMRI_PMIDS_AND_PMCIDS)


def get_documents(project_path):
    all_docs = {}
    docs_folder = project_path / "documents"
    for doc_path in docs_folder.glob("*.jsonl"):
        j_df = pd.read_json(doc_path, lines=True)
        if "pmcid" in j_df.iloc[0]["metadata"].keys():
            for i, row in j_df.iterrows():
                all_docs[row["metadata"]["pmcid"]] = row
        else:
            for i, row in j_df.iterrows():
                pmid = row["metadata"]["pmid"]
                pmcid = int(pmids_and_pmcids[pmids_and_pmcids["pmid"] == pmid]["pmcid"])
                row["metadata"]["pmcid"] = pmcid
                all_docs[row["metadata"]["pmcid"]] = row
    df = pd.DataFrame.from_dict(all_docs, orient="index")
    df.index = df.index.set_names(["pmcid"])
    df.reset_index(inplace=True)
    df["docs_from_project"] = project_path.name
    return df


def get_annotations(project_path):
    all_anns = {}
    anns_folder = project_path / "annotations"
    ann_counts = []
    counter = -1
    for ann_path in anns_folder.glob("*.json*"):
        if str(ann_path)[-1] == "l":
            df = pd.read_json(ann_path, lines=True)
        else:
            df = pd.read_json(ann_path)

        if not "pmcid" in df.iloc[0]["metadata"].keys():
            for i, row in df.iterrows():
                pmid = row["metadata"]["pmid"]
                pmcid = int(pmids_and_pmcids[pmids_and_pmcids["pmid"] == pmid]["pmcid"])
                df.at[i, "metadata"]["pmcid"] = pmcid

        for i, row in df.iterrows():
            counter = counter + 1
            df.at[counter, "pmcid"] = row["metadata"]["pmcid"]
            ann_counts.append(len(row["annotations"]))
        df["annotation_file"] = ann_path.name

    # df = pd.DataFrame.from_dict(all_anns, orient="index")
    # df.index = df.index.set_names(["pmcid"])
    # df.reset_index(inplace=True)
    df["annotations_from_project"] = project_path.name

    return df, ann_counts


def get_project_data(project_path):
    anns, ann_counts = get_annotations(project_path)
    docs = get_documents(project_path)
    df = pd.merge(anns, docs, how="inner", on="pmcid")
    print(len(df), project_path.name)
    # df.dropna(axis='index', subset=['annotations'], inplace=True)

    # check if we've matched the docs and annotations by
    # checking if the metadata is the same in the annotations & documents
    # assert df["metadata_x"].equals(df["metadata_y"])

    # add the metadata in columns of their own instead of a nested dict
    metadata = pd.json_normalize(df["metadata_x"])
    df = pd.merge(df, metadata, how="inner", on="pmcid")
    df.drop(labels=["metadata_x", "metadata_y"], axis="columns", inplace=True)
    return df, ann_counts


total_ann_count = []
for i_project, project_path in enumerate(projects_list):
    if i_project == 0:
        df_dense, ann_counts1 = get_project_data(project_path)
    else:
        df_temp, ann_counts2 = get_project_data(project_path)
        df_dense = pd.concat([df_dense, df_temp])
    # total_ann_count = total_ann_count + ann_counts

# expand df so there's one row per annotation
dense_cols = list(df_dense.columns)
dense_cols.remove("text")
cols = dense_cols + ["annotated_text", "annotated_sentence", "annotated_paragraph"]
################## there's something wrong with the total_ann_count
# df = pd.DataFrame(index=range(total_ann_count), columns=cols)
df = pd.DataFrame(columns=cols)
i = -1
is_ = []
for i_row_dense, row in df_dense.iterrows():
    text = row["text"]
    for ann in row["annotations"]:
        i = i + 1
        is_.append(i)

        df.loc[i, "annotated_text"] = text[ann["start_char"] : ann["end_char"]]

        i_start_sentence = text[: ann["start_char"]].rfind(". ") + 1
        i_end_sentence = text[ann["end_char"] :].find(". ") + ann["end_char"] + 1
        df.loc[i, "annotated_sentence"] = text[i_start_sentence:i_end_sentence]

        if not text.find("\n") == text.rfind("\n"):
            i_start_paragraph = text[: ann["start_char"]].rfind("\n") + 1
            i_end_paragraph = text[ann["end_char"] :].find("\n") + ann["end_char"] + 1
            df.loc[i, "annotated_paragraph"] = text[i_start_paragraph:i_end_paragraph]
        else:
            start = i_start_sentence - 100
            end = i_end_sentence + 100
            df.loc[i, "annotated_paragraph"] = text[start:end]

        df.loc[i, dense_cols] = row[dense_cols]

        # surrounding_sentence

import matplotlib.pyplot as plt

plt.plot(is_)


x = 1
