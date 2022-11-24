import collections
import collections.abc
import sqlite3
from typing import Any, Mapping, Sequence, Union

import pandas as pd


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
            color = "LightGray"
        return f"""
        <div>
        <h5 style="margin-bottom: 0px;">
        <span
        style="background-color: {color};">
        {annotation["label_name"]}
        </span>
        </h5>
        <p style="padding-left: 40px;">
        …{prefix}<span style="font-weight: bold; background-color: {color};"
           >{annotation["selected_text"]}</span>{suffix}…
        </p>
        </div>
        """

    def _repr_html_(self) -> str:
        return "<div>{}</div>".format(
            "\n".join(self._repr_annotation(anno) for anno in self.annotations)
        )
