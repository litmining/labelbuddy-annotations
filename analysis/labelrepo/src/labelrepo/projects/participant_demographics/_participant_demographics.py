import argparse
import sqlite3
import pathlib
import contextlib
from typing import Dict, List, Optional, Tuple

import jinja2
import pandas as pd

from labelrepo import database, repo, displays

_SEX_NAMES = ("female", "male")
_GROUP_NAMES = ("healthy", "patients")
_PAYLOAD_NAMES = (
    "count",
    "age mean",
    "age minimum",
    "age maximum",
    "age median",
    "diagnosis",
)
_DEMOGRAPHICS_LABELS = _SEX_NAMES + _GROUP_NAMES + _PAYLOAD_NAMES


class AnnotationError(Exception):
    pass


def _format_error_annotation(annotation: Dict, indent=0) -> str:
    extra_repr = (
        f"'{annotation['extra_data']}' "
        if annotation["extra_data"] is not None
        else ""
    )
    return (
        f"{' ' * indent}(char {annotation['start_char']} "
        f"– char {annotation['end_char']}) "
        f"'{annotation['label_name']}' "
        f"{extra_repr}"
        f"on '{annotation['selected_text']}'"
    )


def _format_error_token(token: Dict, indent=0) -> str:
    keys = ["group_name", "subgroup_name", "sex"]
    values = [
        f"'{token[k]}'"
        for k in keys
        if not pd.isnull(token[k]) and token[k] != "_"
    ]
    return (
        f"{' ' * indent}"
        f"(char {token['start_char']} – char {token['end_char']}) "
        f"{', '.join(values)}, "
        f"'{token['label_name']}', '{token['coalesced']}'"
    )


def _get_tokens(annotations: pd.DataFrame) -> pd.DataFrame:
    annotation_stacks = annotations.groupby(["start_char", "end_char"])
    tokens = []
    for position, anno_stack in annotation_stacks:
        tokens.append(_token_from_annotations(anno_stack, *position))
    return pd.DataFrame(tokens)


def _get_group_and_subgroup(
    annotation_stack: pd.DataFrame,
) -> Dict:
    group_anno = annotation_stack[
        annotation_stack["label_name"].isin(_GROUP_NAMES)
    ]
    if group_anno.shape[0] == 0:
        return {"group_name": None, "subgroup_name": None}
    if group_anno.shape[0] == 1:
        group_name = group_anno.iloc[0]["label_name"]
        subgroup_name = group_anno.iloc[0]["extra_data"]
        if pd.isnull(subgroup_name):
            subgroup_name = None
        return {"group_name": group_name, "subgroup_name": subgroup_name}
    formatted_annotations = "\n".join(
        _format_error_annotation(anno, 2)
        for anno in group_anno.to_dict(orient="records")
    )
    raise AnnotationError(
        "Too many participant group qualifiers applied "
        f"to the same text:\n\n{formatted_annotations}"
    )


def _get_sex(annotation_stack: pd.DataFrame) -> Dict:
    sex_anno = annotation_stack[
        annotation_stack["label_name"].isin(_SEX_NAMES)
    ]
    sex = sex_anno["label_name"].unique()
    if sex.shape[0] == 0:
        return {"sex": None}
    if sex.shape[0] == 1:
        return {"sex": sex[0]}
    formatted_annotations = "\n".join(
        _format_error_annotation(anno, 2)
        for anno in sex_anno.drop_duplicates(subset="label_name").to_dict(
            orient="records"
        )
    )
    raise AnnotationError(
        "Conflicting sex qualifiers applied to the same text:"
        f"\n\n{formatted_annotations}"
    )


def _get_payload(annotation_stack: pd.DataFrame) -> Dict:
    payload_anno = annotation_stack[
        ~annotation_stack["label_name"].isin(_GROUP_NAMES + _SEX_NAMES)
    ]
    if payload_anno.shape[0] == 0:
        return {"label_name": None, "extra_data": None}
    if payload_anno.shape[0] == 1:
        return {
            "label_name": payload_anno.iloc[0]["label_name"],
            "extra_data": payload_anno.iloc[0]["extra_data"],
        }
    formatted_annotations = "\n".join(
        _format_error_annotation(anno, 2)
        for anno in payload_anno.to_dict(orient="records")
    )
    raise AnnotationError(
        "Too many data labels applied to the same text:\n\n"
        f"{formatted_annotations}"
    )


def _token_from_annotations(
    annotation_stack: pd.DataFrame, start_char: int, end_char: int
) -> Dict:
    token = {
        "start_char": start_char,
        "end_char": end_char,
        "selected_text": annotation_stack.iloc[0]["selected_text"],
    }
    token.update(_get_group_and_subgroup(annotation_stack))
    token.update(_get_sex(annotation_stack))
    token.update(_get_payload(annotation_stack))
    return token


def _build_group_tree(tokens: pd.DataFrame) -> Dict:
    root: Dict = {"children": {}}
    # if any group is mentioned explicitly, both groups are present if we have
    # a total count, otherwise only mentioned groups are present
    if tokens["group_name"].notnull().any():
        if (
            tokens["group_name"].isnull() & (tokens["label_name"] == "count")
        ).any():
            used_groups = _GROUP_NAMES
        else:
            used_groups = tokens["group_name"].dropna().unique()
        root["children"] = {g_name: {} for g_name in used_groups}
    # if no group is mentioned explicitly, we assume all patients if there is a
    # diagnosis and all healthy otherwise.
    elif "diagnosis" in tokens["label_name"].values:
        root["children"] = {"patients": {}}
        tokens["group_name"] = "patients"
    else:
        root["children"] = {"healthy": {}}
        tokens["group_name"] = "healthy"
    for group_name, group in root["children"].items():
        group_idx = tokens[tokens["group_name"] == group_name].index
        subgroup_names = set(
            tokens.loc[group_idx, "subgroup_name"].dropna().values
        )
        if not subgroup_names:
            tokens.loc[group_idx, "subgroup_name"] = "_"
            subgroup_names = {"_"}
        group["children"] = {
            sg_name: {
                "children": {
                    "female": {},
                    "male": {},
                },
            }
            for sg_name in subgroup_names
        }
    return root


def _coalesce_extra_selected(tokens: pd.DataFrame) -> None:
    values = tokens["extra_data"].copy()
    values[values.isnull()] = tokens["selected_text"][values.isnull()]
    tokens["coalesced"] = values


def _check_conflicts(tokens: pd.DataFrame) -> None:
    for _, token_group in tokens.groupby(
        ["group_name", "subgroup_name", "sex", "label_name"], dropna=False
    ):
        if token_group["coalesced"].nunique() > 1:
            formatted_tokens = "\n".join(
                _format_error_token(tok, 2)
                for tok in token_group.to_dict(orient="records")
            )
            raise AnnotationError(
                "The following annotations provide conflicting "
                f"information:\n\n{formatted_tokens}"
            )


def _add_info(tokens: pd.DataFrame, root: Dict) -> None:
    _coalesce_extra_selected(tokens)
    _check_conflicts(tokens)
    tokens = (
        tokens.drop_duplicates(
            subset=("group_name", "subgroup_name", "sex", "label_name")
        )
        .set_index(["group_name", "subgroup_name", "sex", "label_name"])
        .sort_index()
    )
    _add_subtree_info(root, (None, None, None), 0, tokens)
    _infer_info_up("all participants", root)
    _infer_info_down("all participants", root)


def _format_conversion_error(
    node_index: Tuple[Optional[str], ...],
    label_name: str,
    token: Dict,
    target_dtype: str,
) -> str:
    value = token["coalesced"]
    formatted_token = _format_error_token(
        token
        | dict(zip(("group_name", "subgroup_name", "sex"), node_index))
        | {"label_name": label_name},
        2,
    )
    return (
        f"Could not convert '{value}' to "
        f"{target_dtype}:"
        f"\n{formatted_token}"
    )


def _add_subtree_info(
    node: Dict,
    node_index: Tuple[Optional[str], ...],
    level: int,
    tokens: pd.DataFrame,
) -> None:
    dtypes = {
        "count": int,
        "age mean": float,
        "age minimum": float,
        "age maximum": float,
        "age median": float,
        "diagnosis": str,
    }
    for label_name in dtypes.keys():
        if node_index + (label_name,) in tokens.index:
            tok = tokens.loc[node_index + (label_name,)]
            value = tok["coalesced"]
            try:
                node[label_name] = dtypes[label_name](value)
            except (TypeError, ValueError):
                raise AnnotationError(
                    _format_conversion_error(
                        node_index,
                        label_name,
                        tok.to_dict(),
                        dtypes[label_name].__name__,
                    )
                )
    if node_index + ("count",) not in tokens.index:
        male_index = (*node_index[:-1], "male", "count")
        has_male = male_index in tokens.index
        female_index = (*node_index[:-1], "female", "count")
        has_female = female_index in tokens.index
        if has_male and not has_female:
            _set_single_sex(node, "male")
        elif has_female and not has_male:
            _set_single_sex(node, "female")
    for child_name, child in node.get("children", {}).items():
        child_index = list(node_index)
        child_index[level] = child_name
        _add_subtree_info(child, tuple(child_index), level + 1, tokens)


def _set_single_sex(root: Dict, sex: str) -> None:
    remove_sex = {"male": "female", "female": "male"}[sex]
    if "children" not in root:
        return
    if remove_sex in root["children"]:
        del root["children"][remove_sex]
    for child in root["children"].values():
        _set_single_sex(child, sex)


def _check_count_conflict(
    root_name: str, root: Dict, children_sum: int
) -> None:
    if "count" not in root:
        return
    if root["count"] == children_sum:
        return
    msg = (
        "The group count is not the sum of subgroup counts:\n\n"
        f"  '{root_name}': {root['count']}\n\n  subgroups:\n\n"
    ) + "\n".join(
        f"    '{root_name}', '{n}': {c.get('count', '??')}"
        for (n, c) in root["children"].items()
    )
    raise AnnotationError(msg)


def _infer_info_up(root_name: str, root: Dict) -> None:
    if "children" not in root:
        return
    for child in root["children"].items():
        _infer_info_up(*child)
    children = root["children"].values()
    if all("count" in child for child in children):
        children_sum = sum(child["count"] for child in children)
        _check_count_conflict(root_name, root, children_sum)
        root["count"] = children_sum
        if (
            all("age mean" in child for child in children)
            and "age mean" not in root
        ):
            root["age mean"] = (
                sum(child["count"] * child["age mean"] for child in children)
                / children_sum
            )
    if (
        all("age minimum" in child for child in children)
        and "age minimum" not in root
    ):
        root["age minimum"] = min(child["age minimum"] for child in children)
    if (
        all("age maximum" in child for child in children)
        and "age maximum" not in root
    ):
        root["age maximum"] = max(child["age maximum"] for child in children)


def _infer_info_down(root_name: str, root: Dict) -> None:
    if "children" not in root:
        return
    missing_count = [
        child for child in root["children"].values() if "count" not in child
    ]
    if "count" in root and len(missing_count) == 1:
        rest = sum(
            child.get("count", 0) for child in root["children"].values()
        )
        if rest > root["count"]:
            _check_count_conflict(root_name, root, rest)
        missing_count[0]["count"] = root["count"] - rest
    for child_name, child in root["children"].items():
        for label_name in ("age minimum", "age maximum"):
            if label_name in root and label_name not in child:
                child[label_name] = root[label_name]
        if (
            "diagnosis" in root
            and "diagnosis" not in child
            and child_name != "healthy"
        ):
            child["diagnosis"] = root["diagnosis"]
    for child in root["children"].items():
        _infer_info_down(*child)


def _prune_empty_groups(root: Dict) -> None:
    if "children" not in root:
        return
    root["children"] = {
        c_name: c
        for c_name, c in root["children"].items()
        if c.get("count", -1) != 0
    }
    for child in root["children"].values():
        _prune_empty_groups(child)


def _summarize(root: Dict) -> Dict:
    summary = {}
    for label_name in _DEMOGRAPHICS_LABELS:
        if label_name in root:
            summary[label_name] = root[label_name]
    summary["subgroups"] = {}
    for group_name, group in root["children"].items():
        for subgroup_name, subgroup in group["children"].items():
            if len(group["children"]) == 1:
                subgroup_summary_name = group_name
            else:
                subgroup_summary_name = f"{group_name} {subgroup_name}"
            subgroup_summary = {
                "group_name": group_name,
                "subgroup_name": subgroup_name,
            }
            for label_name in _DEMOGRAPHICS_LABELS:
                if label_name in subgroup:
                    subgroup_summary[label_name] = subgroup[label_name]
            for sex in _SEX_NAMES:
                if subgroup["children"].get(sex):
                    subgroup_summary[sex] = subgroup["children"][sex]
            summary["subgroups"][subgroup_summary_name] = subgroup_summary
    return summary


def _get_participants_info(annotations: pd.DataFrame) -> Dict:
    tokens = _get_tokens(annotations)
    root = _build_group_tree(tokens)
    _add_info(tokens, root)
    _prune_empty_groups(root)
    summary = _summarize(root)
    return summary


def _get_labelbuddy_file(
    project_name: str, annotator_name: str
) -> pathlib.Path:
    return pathlib.Path(
        "projects",
        project_name,
        "annotations",
        f"{annotator_name}.labelbuddy",
    )


def _get_document_summaries(all_annotations: pd.DataFrame) -> List[Dict]:
    if not all_annotations.shape[0]:
        return []
    all_docs = []
    positions = {}
    for project_name, annotator_name in (
        all_annotations.loc[:, ["project_name", "annotator_name"]]
        .drop_duplicates()
        .values
    ):
        lb_file = _get_labelbuddy_file(project_name, annotator_name)
        positions[(project_name, annotator_name)] = _get_doc_positions_in_db(
            lb_file
        )
    for (
        project_name,
        annotator_name,
        doc_md5,
    ), anno in all_annotations.groupby(
        ["project_name", "annotator_name", "doc_md5"]
    ):
        pmcid = anno["pmcid"].iloc[0].tolist()
        doc = {
            "project_name": project_name,
            "annotator_name": annotator_name,
            "pmcid": pmcid,
            "title": anno["title"].iloc[0],
        }
        if doc_md5 in positions[(project_name, annotator_name)]:
            doc.update(
                {
                    "position_in_labelbuddy_file": positions[
                        (project_name, annotator_name)
                    ][doc_md5]["position"],
                    "labelbuddy_file": str(
                        _get_labelbuddy_file(project_name, annotator_name)
                    ),
                }
            )
        try:
            doc["participants"] = _get_participants_info(anno)
            if any(
                (sg["group_name"] == "patients")
                for sg in doc["participants"]["subgroups"].values()
            ):
                doc["has_patients"] = True
        except Exception as error:
            doc["participants"] = None
            doc["extraction_failed"] = True
            doc["error_message"] = str(error)
        all_docs.append(doc)
    return all_docs


def _get_doc_positions_in_db(db_path: pathlib.Path) -> Dict:
    full_db_path = repo.repo_root() / db_path
    if not full_db_path.is_file():
        return {}
    with contextlib.closing(sqlite3.connect(full_db_path)) as connection:
        with connection:
            docs = connection.execute(
                "select lower(hex(content_md5)), id from document order by id;"
            )
        return {
            row[0]: {"id": row[1], "position": i}
            for (i, row) in enumerate(docs)
        }


def select_participants_annotations(
    annotator_name: Optional[str] = None,
    project_name: Optional[str] = None,
    pmcid: Optional[int] = None,
) -> pd.DataFrame:
    demo_labels = ", ".join(map("'{}'".format, _DEMOGRAPHICS_LABELS))
    annotator_query = (
        "" if annotator_name is None else "and annotator_name = :annotator"
    )
    project_query = (
        "" if project_name is None else "and project_name = :project"
    )
    pmcid_query = "" if pmcid is None else "and pmcid = :pmcid"
    query = f"""
select pmcid, title, doc_md5, label_name, extra_data, selected_text,
    start_char, end_char, project_name, annotator_name, label_color, context,
    context_start_char, context_end_char, doc_length
from detailed_annotation where label_name in ({demo_labels})
{annotator_query}
{project_query}
{pmcid_query}
    """
    with contextlib.closing(database.get_database_connection()) as connection:
        with connection:
            all_anno = pd.DataFrame(
                map(
                    dict,
                    connection.execute(
                        query,
                        {
                            "annotator": annotator_name,
                            "project": project_name,
                            "pmcid": pmcid,
                        },
                    ).fetchall(),
                )
            )
    if not all_anno.shape[0]:
        all_anno = pd.DataFrame(
            columns="pmcid title doc_md5 label_name extra_data "
            "selected_text start_char end_char project_name "
            "annotator_name".split()
        )
    return all_anno


def _get_jinja_env() -> jinja2.Environment:
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            pathlib.Path(__file__).resolve().parent / "_data" / "templates",
            encoding="UTF-8",
        )
    )


def get_participant_demographics():
    all_anno = select_participants_annotations()
    all_docs = _get_document_summaries(all_anno)
    all_rows = []
    for doc in all_docs:
        doc_info = {
            k: doc[k] for k in ("project_name", "annotator_name", "pmcid")
        }
        for subgroup in doc["participants"]["subgroups"].values():
            row = doc_info | {
                k: subgroup.get(k)
                for k in ("group_name", "subgroup_name") + _PAYLOAD_NAMES
            }
            row["female count"] = subgroup.get("female", {}).get("count")
            row["male count"] = subgroup.get("male", {}).get("count")
            all_rows.append(row)
    return pd.DataFrame(all_rows)


def get_report_for_labelbuddy_file(
    project_name: str, annotator_name: str, standalone: bool = False
) -> str:
    all_anno = select_participants_annotations(
        project_name=project_name, annotator_name=annotator_name
    )
    all_docs = _get_document_summaries(all_anno)
    all_docs = sorted(all_docs, key=lambda d: d["position_in_labelbuddy_file"])
    jinja_env = _get_jinja_env()
    template = jinja_env.get_template("labelbuddy_file_report.html")
    return template.render(
        {
            "documents": all_docs,
            "project_name": project_name,
            "annotator_name": annotator_name,
            "standalone": standalone,
        }
    )


def get_report_for_repo(
    standalone: bool = False, remove_failed_docs: bool = False
) -> str:
    all_anno = select_participants_annotations()
    all_docs = _get_document_summaries(all_anno)
    if remove_failed_docs:
        all_docs = [
            doc for doc in all_docs if not doc.get("extraction_failed")
        ]
    all_docs = sorted(all_docs, key=lambda d: d["pmcid"])
    jinja_env = _get_jinja_env()
    template = jinja_env.get_template("repository_report.html")
    return template.render(
        {
            "documents": all_docs,
            "standalone": standalone,
            "no_doc_positions": True,
        }
    )


def labelbuddy_file_report_command(args: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("labelbuddy_file", type=str, nargs="?", default=None)
    parsed_args = parser.parse_args(args)
    if parsed_args.labelbuddy_file is None:
        labelbuddy_file = (
            repo.repo_root()
            / "projects"
            / "participant_demographics"
            / "annotations"
            / f"{repo.annotator_name()}.labelbuddy"
        )
    else:
        labelbuddy_file = pathlib.Path(parsed_args.labelbuddy_file)
    project_name = labelbuddy_file.parents[1].name
    annotator_name = labelbuddy_file.stem
    html = get_report_for_labelbuddy_file(
        project_name, annotator_name, standalone=True
    )
    out_file = labelbuddy_file.with_name(
        f"{annotator_name}_participants_report.html"
    )
    pathlib.Path(out_file).write_text(html)
    print(f"Report saved in {out_file}")


def get_annotation_stacks_display(annotations):
    stacks = []
    for _, anno in annotations.groupby(
        ["doc_md5", "project_name", "annotator_name", "start_char", "end_char"]
    ):
        first_anno = anno.iloc[0].to_dict()
        prefix, selected_text, suffix = displays.split_annotation_context(
            first_anno
        )
        anno_stack = {
            "prefix": prefix,
            "selected_text": selected_text,
            "suffix": suffix,
            "annotations": anno.to_dict(orient="records"),
        }
        stacks.append(anno_stack)
    jinja_env = _get_jinja_env()
    template = jinja_env.get_template("annotation_stack.html")
    html = template.render({"standalone": True, "annotation_stacks": stacks})
    return html
