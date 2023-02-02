import collections
import collections.abc
import html
import json
import os
import sqlite3
import string
from typing import Any, Dict, Mapping, Sequence, Union
import urllib

from labelrepo import _utils

_SIMPLE_ANNOTATION_TEMPLATE = """<div>
    <h5 style="margin-bottom: 0px;">
        <span style="background-color: ${color};">${label_name}</span>
    </h5>
    <p style="padding-left: 40px;">
    ${prefix}<span
        style="font-weight: bold; background-color: ${color};"
        >${selected_text}</span>${suffix}
    </p>
</div>
"""

_STYLED_ANNOTATION_TEMPLATE = """<div class="annotation"
    style='--label-name:"${label_name}"; --label-color:${color}'>
    <div class="annotation-header">${label_name}</div>
    <div class="context">
        ${prefix}<span class="annotated-text"
            >${selected_text}</span>${suffix}
    </div>
    <div class="annotation-footer">
        <div class="extra-data">${extra_data}</div>
        <div class="pcmid"><a target="_blank"
          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC${pmcid}/"
          >PMC${pmcid}</a></div>
        <div class="project-name">${project_name_or_link}</div>
        <div class="annotator-name">${annotator_name}</div>
    </div>
</div>
"""

_SIMPLE_LABEL_TEMPLATE = (
    """<div style="background-color: ${color}; """
    """padding: 0.5rem; margin: 0.5rem">${name}</div>"""
)

_STYLED_LABEL_TEMPLATE = (
    """<div class="label-display" """
    """style='--label-color:${color};'>${name}</div>"""
)

_TEMPLATES = {
    "simple": {
        "annotation": _SIMPLE_ANNOTATION_TEMPLATE,
        "label": _SIMPLE_LABEL_TEMPLATE,
    },
    "styled": {
        "annotation": _STYLED_ANNOTATION_TEMPLATE,
        "label": _STYLED_LABEL_TEMPLATE,
    },
}


def _get_template(kind: str, force_styled: bool = False) -> str:
    if (
        force_styled
        or ("LABELREPO_CSS_AVAILABLE" in os.environ)
        or ("JUPYTER_BOOK" in os.environ)
    ):
        return _TEMPLATES["styled"][kind]
    return _TEMPLATES["simple"][kind]


def _get_project_name_or_link(project_name):
    repo_url = os.environ.get("LABELREPO_REPOSITORY_URL")
    if repo_url is None:
        return html.escape(project_name)
    return (
        """<a target="_blank" """
        f"""href="{urllib.parse.urljoin(repo_url, "tree/main/projects/")}"""
        f"""{urllib.parse.quote(project_name)}/">"""
        f"""{html.escape(project_name)}</a>"""
    )


def _get_color(color: Any) -> str:
    if not color:
        return "#e0e0e0"
    return str(color)


def _get_css(basename: str) -> str:
    return (_utils.package_data() / "css" / f"{basename}.css").read_text(
        "UTF-8"
    )


def _escape_values(data: Mapping[str, Any]) -> Dict[str, str]:
    return {k: html.escape(str(v)) for k, v in data.items() if v is not None}


class Display:
    def _repr_html_(self) -> str:
        return self.get_div()

    def get_html(self) -> str:
        return f"""<html>
        <head>
        <title>labelrepo data</title>
        <style>
        {self._get_css()}
        </style>
        </head>
        <body>
        {self.get_div(True)}
        </body>
        </html>
        """

    def _get_css(self) -> str:
        return ""

    def get_div(self, force_styled: bool = False) -> str:
        del force_styled
        return ""


class AnnotationsDisplay(Display):
    def __init__(
        self,
        annotations: Union[Mapping[str, Any], Sequence[Mapping[str, Any]]],
    ) -> None:
        if isinstance(annotations, (collections.abc.Mapping, sqlite3.Row)):
            self.annotations = [annotations]
        elif hasattr(annotations, "to_json"):
            self.annotations = json.loads(
                annotations.to_json(orient="records")
            )
        else:
            self.annotations = annotations

    @staticmethod
    def _repr_annotation(
        annotation: Mapping[str, Any], force_styled: bool
    ) -> str:
        prefix = annotation["context"][
            : annotation["start_char"] - annotation["context_start_char"]
        ]
        if annotation["context_start_char"] != 0:
            prefix = "…" + prefix
        suffix = annotation["context"][
            annotation["end_char"] - annotation["context_start_char"] :
        ]
        if annotation["context_end_char"] != annotation["doc_length"]:
            suffix = suffix + "…"
        color = _get_color(annotation["label_color"])
        extra_data = annotation["extra_data"]
        if extra_data is None:
            extra_data = ""
        info = _escape_values(
            {
                **dict(annotation),
                "prefix": prefix,
                "suffix": suffix,
                "color": color,
                "extra_data": extra_data,
            }
        )
        info["project_name_or_link"] = _get_project_name_or_link(
            info["project_name"]
        )
        return string.Template(
            _get_template("annotation", force_styled)
        ).substitute(info)

    def get_div(self, force_styled: bool = False) -> str:
        annotations = "\n".join(
            self._repr_annotation(anno, force_styled)
            for anno in self.annotations
        )
        return f"""<div class='annotation-set'>{annotations}</div>"""

    def _get_css(self) -> str:
        return _get_css("annotation-set")


class LabelsDisplay(Display):
    def __init__(
        self,
        labels: Union[Mapping[str, Any], Sequence[Mapping[str, Any]]],
    ) -> None:
        if isinstance(labels, (collections.abc.Mapping, sqlite3.Row)):
            self.labels = [labels]
        elif hasattr(labels, "to_json"):
            self.labels = json.loads(labels.to_json(orient="records"))
        else:
            self.labels = labels

    def get_div(self, force_styled: bool = False) -> str:
        label_snippets = []
        template = string.Template(_get_template("label", force_styled))
        for label in self.labels:
            color = _get_color(label["color"])
            info = _escape_values({**dict(label), "color": color})
            label_snippets.append(template.substitute(info))
        content = "\n".join(label_snippets)
        return f"""<div class="label-set">
            <div class="label-set-wrap">{content}</div>
            </div>"""

    def _get_css(self) -> str:
        return _get_css("label-set")
