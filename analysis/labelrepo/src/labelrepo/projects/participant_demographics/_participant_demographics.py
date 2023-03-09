import argparse
import re
import sqlite3
import pathlib
import contextlib
import secrets
import hashlib
from typing import Dict, List, Optional, Union

import jinja2
import pandas as pd

from labelrepo import database, repo, displays


class AgeRange:
    name = "range"

    def __init__(self, text: str, label_name, start_char, end_char) -> None:
        del label_name
        match = re.match(
            r"\s*\b(\d+(?:[.]\d+)?)\b"
            r"\s*(?:\S|to|and)\s*"
            r"\b(\d+(?:[.]\d+)?)\b\s*",
            text,
        )
        assert match is not None
        self.data = {
            "age minimum": {
                "value": float(match.group(1)),
                "source": {"start_char": start_char, "end_char": end_char},
            },
            "age maximum": {
                "value": float(match.group(2)),
                "source": {"start_char": start_char, "end_char": end_char},
            },
        }


def _vtype(dtype):
    class Value:
        name = dtype.__name__

        def __init__(
            self, text: str, label_name, start_char, end_char
        ) -> None:
            self.data = {
                label_name: {
                    "value": dtype(text),
                    "source": {
                        "start_char": start_char,
                        "end_char": end_char,
                    },
                }
            }

    return Value


_SEX_NAMES = ("female", "male")
_GROUP_NAMES = ("healthy", "patients")
_PAYLOAD_TYPES = {
    "count": _vtype(int),
    "age mean": _vtype(float),
    "age minimum": _vtype(float),
    "age maximum": _vtype(float),
    "age range": AgeRange,
    "age median": _vtype(float),
    "diagnosis": _vtype(str),
}
_PAYLOAD_NAMES = tuple(_PAYLOAD_TYPES.keys())

_DEMOGRAPHICS_LABELS = _SEX_NAMES + _GROUP_NAMES + _PAYLOAD_NAMES


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
    formatted = (
        f"{' ' * indent}"
        f"(char {token['start_char']} – char {token['end_char']}) "
        f"{' / '.join(values)}{', ' if values else ''}"
        f"'{token['label_name']}'"
    )
    if "coalesced" in token:
        formatted += f", '{token['coalesced']}'"
    return formatted


def _format_error(annotation_or_token: Dict, indent=0) -> str:
    if "group_name" in annotation_or_token:
        return _format_error_token(annotation_or_token, indent)
    return _format_error_annotation(annotation_or_token, indent)


class AnnotationError(Exception):
    def __init__(self, message, error_tokens=[], error_positions=None):
        if isinstance(error_tokens, pd.DataFrame):
            error_tokens = error_tokens.to_dict(orient="records")
        self.error_tokens = error_tokens
        if error_positions is None:
            self.error_positions = {
                (tok["start_char"], tok["end_char"])
                for tok in self.error_tokens
            }
        else:
            self.error_positions = error_positions
        formatted_tokens = "\n".join(
            _format_error(tok, 2) for tok in self.error_tokens
        )
        formatted_message = f"""{message}\n\n{formatted_tokens}"""
        super().__init__(formatted_message)


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
    raise AnnotationError(
        "Too many participant group qualifiers applied to the same text:",
        group_anno,
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
    raise AnnotationError(
        "Conflicting sex qualifiers applied to the same text:",
        sex_anno.drop_duplicates(subset=("label_name",)),
    )


def _get_payload(annotation_stack: pd.DataFrame) -> Dict:
    payload_anno = annotation_stack[
        ~annotation_stack["label_name"].isin(_GROUP_NAMES + _SEX_NAMES)
    ]
    if payload_anno.shape[0] == 0:
        raise AnnotationError(
            "Group descriptors applied "
            "but data label (eg 'count', 'age mean', etc.) is missing:",
            annotation_stack,
        )
    if payload_anno.shape[0] == 1:
        payload = {
            "label_name": payload_anno.iloc[0]["label_name"],
            "extra_data": payload_anno.iloc[0]["extra_data"],
        }
        if pd.isnull(payload["extra_data"]):
            payload["coalesced"] = payload_anno.iloc[0]["selected_text"]
        else:
            payload["coalesced"] = payload["extra_data"]
        return payload
    raise AnnotationError(
        "Too many data labels applied to the same text:", payload_anno
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
    root: Dict = {}
    _build_groups(root, tokens)
    return root


def _check_sex_on_non_leaf_nodes(tokens: pd.DataFrame) -> None:
    bad_tokens = tokens.loc[
        tokens["group_name"].isnull() & tokens["sex"].notnull()
    ]
    if bad_tokens.shape[0]:
        drop_group_msg = ""
        groups = tokens["group_name"].dropna().unique()
        if len(groups) == 1:
            drop_group_msg = (
                "If there is only one group of participants, "
                f"you can solve this by removing the '{groups[0]}' label. "
                "Otherwise please add group labels "
                "to the 'female' and 'male' counts.\n\n"
            )
        raise AnnotationError(
            "When explicit group labels are used, "
            "'female' and 'male' counts should be "
            "attached to specific groups.\n\n"
            f"{drop_group_msg}"
            "'patients' or 'healthy' label is missing:",
            bad_tokens,
        )


def _build_groups(root: Dict, tokens: pd.DataFrame) -> None:
    # if any group is mentioned explicitly, both groups are present if we have
    # a total count, otherwise only mentioned groups are present
    if tokens["group_name"].notnull().any():
        _check_sex_on_non_leaf_nodes(tokens)
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
    else:
        root["children"] = {"healthy": {}}
    if len(root["children"]) == 1:
        tokens["group_name"] = tuple(root["children"].keys())[0]
    for group_name, group in root["children"].items():
        _build_subgroups(group_name, group, tokens)


def _build_subgroups(group_name, group, tokens):
    group_idx = tokens[tokens["group_name"] == group_name].index
    subgroup_names = tokens.loc[group_idx, "subgroup_name"].dropna().unique()
    if not len(subgroup_names):
        tokens.loc[group_idx, "subgroup_name"] = "_"
        subgroup_names = ("_",)
    group["children"] = {sg_name: {} for sg_name in subgroup_names}
    for sg_name, sg in group["children"].items():
        _build_sexes(group_name, sg_name, sg, tokens)


def _build_sexes(group_name, subgroup_name, subgroup, tokens):
    sg_tokens = tokens[
        (tokens["group_name"] == group_name)
        & (tokens["subgroup_name"] == subgroup_name)
    ]
    used_sexes = _SEX_NAMES
    mentioned_sexes = sg_tokens["sex"].dropna().unique()
    if (
        len(mentioned_sexes)
        and not (
            sg_tokens["sex"].isnull() & (sg_tokens["label_name"] == "count")
        ).any()
    ):
        used_sexes = mentioned_sexes
    subgroup["children"] = {s_name: {} for s_name in used_sexes}


def _find_node(token: pd.Series, root: Dict) -> Dict:
    node = root
    for step in ("group_name", "subgroup_name", "sex"):
        if token[step] is None:
            return node
        node = node["children"][token[step]]
    return node


def _add_info(tokens: pd.DataFrame, root: Dict) -> None:
    for _, tok in tokens.iterrows():
        node = _find_node(tok, root)
        payload = _get_payload_from_token(tok)
        _update_node(node, tok, payload)
    _infer_info_up(["all participants"], root)
    _infer_info_down(["all participants"], root)


def _get_payload_from_token(token) -> Dict:
    raw_value = token["coalesced"]
    label_name = token["label_name"]
    try:
        return _PAYLOAD_TYPES[label_name](
            raw_value,
            label_name,
            int(token["start_char"]),
            int(token["end_char"]),
        ).data
    except Exception:
        raise AnnotationError(
            f"Could not convert '{raw_value}' to "
            f"{_PAYLOAD_TYPES[label_name].name}:",
            [token],
        )


def _update_node(node, token, payload):
    for key, data in payload.items():
        if key in node and node[key]["value"] != data["value"]:
            new_token = token.to_dict()
            new_token.update(label_name=key, coalesced=data["value"])
            old_token = token.to_dict()
            old_token.update(
                node[key]["source"],
                coalesced=node[key]["value"],
                label_name=key,
            )
            raise AnnotationError(
                "The following annotations provide conflicting information:",
                [old_token, new_token],
            )
        else:
            node[key] = data


def _check_count_conflict(
    parent_path: List[str], root: Dict, children_sum: int
) -> None:
    if "count" not in root:
        return
    root_count = root["count"]["value"]
    if root_count == children_sum:
        return
    parent_name = " / ".join(f"'{p}'" for p in parent_path)
    msg = (
        "The group count is not the sum of subgroup counts:\n\n"
        f"{parent_name}: {root_count}\n\nsubgroups:\n\n"
    ) + "\n".join(
        f"  {parent_name} / '{n}': {c.get('count', {}).get('value', '??')}"
        for (n, c) in root["children"].items()
    )
    raise AnnotationError(
        msg,
        error_positions=[
            (
                n["count"]["source"]["start_char"],
                n["count"]["source"]["end_char"],
            )
            for n in (root,) + tuple(root["children"].values())
            if "count" in n and "source" in n["count"]
        ],
    )


def _infer_info_up(parent_path: List[str], root: Dict) -> None:
    if "children" not in root:
        return
    for child_name, child in root["children"].items():
        _infer_info_up(parent_path + [child_name], child)
    children = root["children"].values()
    if all("count" in child for child in children):
        children_sum = sum(child["count"]["value"] for child in children)
        _check_count_conflict(parent_path, root, children_sum)
        root["count"] = {"value": children_sum}
        if (
            all("age mean" in child for child in children)
            and "age mean" not in root
        ):
            root["age mean"] = {
                "value": (
                    sum(
                        child["count"]["value"] * child["age mean"]["value"]
                        for child in children
                    )
                    / children_sum
                )
            }
    if (
        all("age minimum" in child for child in children)
        and "age minimum" not in root
    ):
        root["age minimum"] = {
            "value": min(child["age minimum"]["value"] for child in children)
        }
    if (
        all("age maximum" in child for child in children)
        and "age maximum" not in root
    ):
        root["age maximum"] = {
            "value": max(child["age maximum"]["value"] for child in children)
        }
    if len(root["children"]) == 1:
        child = tuple(root["children"].values())[0]
        for label_name in _PAYLOAD_NAMES:
            if (
                "source" in child.get(label_name, {})
                and label_name in root
                and "source" not in root[label_name]
            ):
                root[label_name]["source"] = child[label_name]["source"]


def _infer_info_down(parent_path: List[str], root: Dict) -> None:
    if "children" not in root:
        return
    missing_count = [
        child for child in root["children"].values() if "count" not in child
    ]
    if "count" in root and len(missing_count) == 1:
        rest = sum(
            child.get("count", {}).get("value", 0)
            for child in root["children"].values()
        )
        if rest > root["count"]["value"]:
            _check_count_conflict(parent_path, root, rest)
        if len(root["children"]) == 1:
            missing_count[0]["count"] = root["count"]
        else:
            missing_count[0]["count"] = {
                "value": root["count"]["value"] - rest
            }
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
    for child_name, child in root["children"].items():
        _infer_info_down(parent_path + [child_name], child)


def _prune_empty_groups(root: Dict) -> None:
    if "children" not in root:
        return
    root["children"] = {
        c_name: c
        for c_name, c in root["children"].items()
        if c.get("count", {}).get("value", -1) != 0
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
            "annotation_stacks": _get_annotation_stacks(anno),
            "doc_uid": secrets.token_hex(4),
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
            for sg in doc["participants"]["subgroups"].values():
                if sg["group_name"] == "patients":
                    doc["has_patients"] = True
                    if "diagnosis" not in sg:
                        doc["warnings"] = doc.get("warnings", []) + [
                            "missing diagnosis"
                        ]
                if "count" not in sg:
                    doc["warnings"] = doc.get("warnings", []) + [
                        "missing count"
                    ]
        except Exception as error:
            doc["participants"] = None
            doc["extraction_failed"] = True
            doc["error_message"] = str(error)
            if isinstance(error, AnnotationError):
                doc["error_positions"] = error.error_positions

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
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            pathlib.Path(__file__).resolve().parent / "_data" / "templates",
            encoding="UTF-8",
        )
    )
    env.filters["md5"] = lambda text: hashlib.md5(
        text.encode("utf-8")
    ).hexdigest()
    return env


def get_participant_demographics() -> pd.DataFrame:
    all_anno = select_participants_annotations()
    all_docs = _get_document_summaries(all_anno)
    all_rows = []
    for doc in all_docs:
        if doc.get("extraction_failed", False):
            continue
        doc_info = {
            k: doc[k] for k in ("project_name", "annotator_name", "pmcid")
        }
        for subgroup in doc["participants"]["subgroups"].values():
            row = {}
            row.update(doc_info)
            for k in ("group_name", "subgroup_name"):
                row[k] = subgroup.get(k)
            for k in _PAYLOAD_NAMES:
                row[k] = subgroup.get(k, {}).get("value")
            row["female count"] = (
                subgroup.get("female", {}).get("count", {}).get("value")
            )
            row["male count"] = (
                subgroup.get("male", {}).get("count", {}).get("value")
            )
            all_rows.append(row)
    return pd.DataFrame(all_rows)


def _get_template_data(
    database_file: Optional[Union[str, pathlib.Path]] = None
) -> Dict:
    if database_file is not None:
        connection = sqlite3.connect(database_file)
    else:
        connection = database.get_database_connection()
    with contextlib.closing(connection), connection:
        label_color_rows = connection.execute(
            "select name, color from label "
            "where name in ('patients', 'healthy')"
        ).fetchall()
    label_colors = {}
    for name, color in label_color_rows:
        match = re.match(r"#(..)(..)(..)", color)
        if match is not None:
            label_colors[name] = [int(p, 16) for p in match.groups()]
    return {"label_colors": label_colors}


def get_report(
    annotator_name: Optional[str] = None,
    project_name: Optional[str] = None,
    pmcid: Optional[int] = None,
    standalone: bool = False,
) -> str:
    all_anno = select_participants_annotations(
        annotator_name=annotator_name, project_name=project_name, pmcid=pmcid
    )
    all_docs = _get_document_summaries(all_anno)
    if (
        project_name is not None
        and annotator_name is not None
        and pmcid is None
    ):
        key = lambda d: (
            d.get("position_in_labelbuddy_file", -1),
            d["pmcid"],
        )
    else:
        key = lambda d: (d["pmcid"], d["project_name"], d["annotator_name"])
    all_docs = sorted(all_docs, key=key)
    jinja_env = _get_jinja_env()
    template = jinja_env.get_template("report.html")
    info = {
        "documents": all_docs,
        "standalone": standalone,
        "no_doc_positions": True,
    }
    info.update(_get_template_data())
    if annotator_name is not None:
        info["annotator_name"] = annotator_name
    if project_name is not None:
        info["project_name"] = project_name
    return template.render(info)


def report_command(args: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project_name", type=str, default=None)
    parser.add_argument("-a", "--annotator_name", type=str, default=None)
    parser.add_argument("-A", "--all_annotators", action="store_true")
    parsed_args = parser.parse_args(args)
    if parsed_args.all_annotators:
        annotator_name = None
    elif parsed_args.annotator_name is None:
        annotator_name = repo.annotator_name()
    else:
        annotator_name = parsed_args.annotator_name
    project_name = parsed_args.project_name
    html = get_report(
        annotator_name=annotator_name,
        project_name=project_name,
        standalone=True,
    )
    out_dir = repo.repo_root() / "analysis" / "data" / "reports"
    out_dir.mkdir(exist_ok=True, parents=True)
    proj_repr = "" if project_name is None else f"_{project_name}"
    annotator_repr = "" if annotator_name is None else f"_{annotator_name}"
    out_file = out_dir / f"participants_report{annotator_repr}{proj_repr}.html"
    out_file.write_text(html)
    print(f"Report saved in {out_file}")


def _get_annotation_stacks(annotations: pd.DataFrame) -> List[Dict]:
    stacks = []
    for _, anno in annotations.groupby(
        ["doc_md5", "project_name", "annotator_name", "start_char", "end_char"]
    ):
        first_anno = anno.iloc[0].to_dict()
        prefix, selected_text, suffix = displays.split_annotation_context(
            first_anno
        )
        anno_stack = {
            "start_char": first_anno["start_char"],
            "end_char": first_anno["end_char"],
            "prefix": prefix,
            "selected_text": selected_text,
            "suffix": suffix,
            "annotations": anno.to_dict(orient="records"),
        }
        stacks.append(anno_stack)
    return stacks


def get_annotation_stacks_display(
    annotations: pd.DataFrame, standalone=False
) -> str:
    stacks = _get_annotation_stacks(annotations)
    jinja_env = _get_jinja_env()
    template = jinja_env.get_template("annotation_stack_list.html")
    html = template.render(
        {"standalone": standalone, "annotation_stacks": stacks}
    )
    return html
