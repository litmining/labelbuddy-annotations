from pathlib import Path

import pandas as pd

id_file = Path(__file__).resolve().parents[1] / "utils" / "pmids_and_pmcids_for_nimf_papers.txt"
PMIDS_AND_PMCIDS = pd.read_csv(id_file)


def get_documents(project_path):
    counter = -1
    docs_folder = project_path / "documents"
    for doc_path in docs_folder.glob("*.jsonl"):
        df = pd.read_json(doc_path, lines=True)
        if not "pmcid" in df.iloc[0]["metadata"].keys():
            for i, row in df.iterrows():
                pmid = row["metadata"]["pmid"]
                pmcid = int(PMIDS_AND_PMCIDS[PMIDS_AND_PMCIDS["pmid"] == pmid]["pmcid"])
                df.at[i, "metadata"]["pmcid"] = pmcid

        for i, row in df.iterrows():
            counter = counter + 1
            df.at[counter, "pmcid"] = row["metadata"]["pmcid"]
        df["document_file"] = doc_path.name

    df["document_from_project"] = project_path.name
    return df


def get_annotations(project_path):
    anns_folder = project_path / "annotations"
    ann_count = 0
    counter = -1
    for ann_path in anns_folder.glob("*.json*"):
        if str(ann_path)[-1] == "l":
            df = pd.read_json(ann_path, lines=True)
        else:
            df = pd.read_json(ann_path)

        if not "pmcid" in df.iloc[0]["metadata"].keys():
            for i, row in df.iterrows():
                pmid = row["metadata"]["pmid"]
                pmcid = int(
                    PMIDS_AND_PMCIDS[PMIDS_AND_PMCIDS["pmid"] == pmid]["pmcid"]
                )
                df.at[i, "metadata"]["pmcid"] = pmcid
        df["annotation_file"] = ann_path.name
        
    for i, row in df.iterrows():
        counter = counter + 1
        df.at[counter, "pmcid"] = row["metadata"]["pmcid"]
        ann_count = ann_count + len(row["annotations"])
        
    df["annotation_project"] = project_path.name
    df.dropna(axis="index", subset=["annotations"], inplace=True)
    return df, ann_count


def get_project_data(project_path):
    anns, ann_count = get_annotations(project_path)
    docs = get_documents(project_path)
    df = pd.merge(anns, docs, how="inner", on="pmcid")

    # add the metadata in columns of their own instead of a nested dict
    metadata = pd.json_normalize(df["metadata_y"])
    df = pd.merge(df, metadata, how="inner", on="pmcid")

    # check if we've matched the docs and annotations
    assert df["metadata_x"].equals(df["metadata_y"])
    return df, ann_count


# script starts here#################################
projects_folder_path = Path(__file__).resolve().parents[1] / "projects"
projects_list = projects_folder_path.iterdir()

total_ann_count = 0
for i_project, project_path in enumerate(projects_list):
    if i_project == 0:
        df_dense, ann_count = get_project_data(project_path)
    else:
        df_temp, ann_count = get_project_data(project_path)
        df_dense = pd.concat([df_dense, df_temp])

    total_ann_count = total_ann_count + ann_count

# expand df so there's one row per annotation
dense_cols = list(df_dense.columns)
dense_cols.remove("text")
cols = dense_cols + [
    "annotation_label_name",
    "annotated_text",
    "annotated_sentence",
    "annotated_paragraph",
]

df = pd.DataFrame(index=range(total_ann_count), columns=cols)
i = -1
for i_row_dense, row in df_dense.iterrows():
    text = row["text"]
    for ann in row["annotations"]:
        i = i + 1
        df.loc[i, "annotation_label_name"] = ann["label_name"]
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

assert df["utf8_text_md5_checksum_x"].equals(df["utf8_text_md5_checksum_y"])

# remake dataframe so it's more understandable
df["document_utf8_text_md5_checksum"] = df["utf8_text_md5_checksum"]
df["labelbuddy_display_title"] = df["display_title"]

df_useful_cols = [
    "pmcid",
    "doi",
    "document_utf8_text_md5_checksum",
    "document_file",
    "document_from_project",
    "annotation_label_name",
    "annotated_text",
    "annotated_sentence",
    "annotated_paragraph",
    "annotation_file",
    "annotation_project",
    "labelbuddy_display_title",
]
df = df[df_useful_cols]
df.to_csv(Path(__file__).resolve().parent / "all_annotations.csv", index=False)