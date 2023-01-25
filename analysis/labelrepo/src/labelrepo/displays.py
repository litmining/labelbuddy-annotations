import collections
import collections.abc
import html
import os
import sqlite3
import string
from typing import Any, Mapping, Sequence, Union

import pandas as pd

from labelrepo import _utils

_SIMPLE_ANNOTATION_TEMPLATE = """
<div>
    <h5 style="margin-bottom: 0px;">
        <span style="background-color: ${label_color};">${label_name}</span>
    </h5>
    <p style="padding-left: 40px;">
    …${prefix}<span
        style="font-weight: bold; background-color: ${label_color};"
        >${selected_text}</span>${suffix}…
    </p>
</div>
"""

_STYLED_ANNOTATION_TEMPLATE = """
<div class="annotation"
    style='--label-name:"${label_name}"; --label-color:${color}'>
    <div class="annotation-header">${label_name}</div>
    <div class="context">
        …${prefix}<span class="annotated-text"
            >${selected_text}</span>${suffix}…
    </div>
    <div class="annotation-footer">
        <div class="extra-data">${extra_data}</div>
        <div class="project-name">${project}</div>
        <div class="annotator-name">${annotator_name}</div>
    </div>
</div>
"""


def _get_annotation_template() -> str:
    if ("LABELREPO_CSS_AVAILABLE" in os.environ) or (
        "JUPYTER_BOOK" in os.environ
    ):
        return _STYLED_ANNOTATION_TEMPLATE
    return _SIMPLE_ANNOTATION_TEMPLATE


class AnnotationsDisplay:
    def __init__(
        self,
        annotations: Union[
            Mapping[str, Any], Sequence[Mapping[str, Any]], pd.DataFrame
        ],
    ) -> None:
        if isinstance(annotations, (collections.abc.Mapping, sqlite3.Row)):
            self.annotations = [annotations]
        elif hasattr(annotations, "to_dict"):
            self.annotations = annotations.to_dict(orient="records")
        else:
            self.annotations = annotations

    @staticmethod
    def _repr_annotation(annotation: Mapping[str, Any]) -> str:
        prefix = annotation["context"][
            : annotation["start_char"] - annotation["context_start_char"]
        ]
        suffix = annotation["context"][
            annotation["end_char"] - annotation["context_start_char"] :
        ]
        color = annotation["label_color"]
        if not color or pd.isnull(color):
            color = "#e0e0e0"
        extra_data = annotation["extra_data"]
        if pd.isnull(extra_data):
            extra_data = ""
        info = {
            "prefix": prefix,
            "suffix": suffix,
            "color": color,
            "extra_data": extra_data,
            **{
                k: str(v) for k, v in dict(annotation).items() if pd.notnull(v)
            },
        }
        return string.Template(_get_annotation_template()).safe_substitute(
            {key: html.escape(value) for key, value in info.items()}
        )

    def _repr_html_(self) -> str:
        annotations = "\n".join(
            self._repr_annotation(anno) for anno in self.annotations
        )
        return f"""<div class='annotation-set'>{annotations}</div>"""
