from __future__ import annotations
import abc

import dataclasses
import math
import re
from typing import Dict, Optional, Any, Set

import pandas as pd

_GROUP_NAMES = ("healthy", "patients")
_SEX_NAMES = ("female", "male")


class _ValueParser:
    def __init__(self, value_type):
        self.value_type = value_type
        self.name = value_type.__name__

    def __call__(self, raw_value):
        return self.value_type(raw_value)


class _RangeParser:
    name = "range"

    def __call__(self, raw_value):
        match = re.match(
            r"\s*\b(\d+(?:[.]\d+)?)\b"
            r"\s*(?:\S|to|and)\s*"
            r"\b(\d+(?:[.]\d+)?)\b\s*",
            raw_value,
        )
        assert match is not None
        return float(match.group(1)), float(match.group(2))


class _Completer:
    @staticmethod
    def collect(attribute_name, node):
        if len(node.children) != 1:
            return
        child = _head(node.children.values())
        if attribute_name not in child.attributes:
            return
        if attribute_name not in node.attributes:
            node.attributes[attribute_name] = child.attributes[attribute_name]
            return
        if (
            node.attributes[attribute_name].value
            == child.attributes[attribute_name].value
        ):
            return
        raise AnnotationValueError(
            "Conflicting annotations",
            node.attributes[attribute_name].sources.union(
                child.attributes[attribute_name].sources
            ),
        )

    @staticmethod
    def broadcast(attribute_name, node):
        if len(node.children) != 1:
            return
        child = _head(node.children.values())
        if attribute_name not in node.attributes:
            return
        if attribute_name not in child.attributes:
            child.attributes[attribute_name] = node.attributes[attribute_name]
        if (
            node.attributes[attribute_name].value
            == child.attributes[attribute_name].value
        ):
            return
        raise AnnotationValueError(
            "Conflicting annotations",
            node.attributes[attribute_name].sources.union(
                child.attributes[attribute_name].sources
            ),
        )


class _DiagnosisCompleter(_Completer):
    @staticmethod
    def broadcast(attribute_name, node):
        if "healthy" in node.children and (
            attribute_name in node.children["healthy"].attributes
        ):
            raise AnnotationValueError(
                "Healthy group cannot have a diagnosis",
                node.children["healthy"].attributes[attribute_name].sources,
            )
        if attribute_name not in node.attributes:
            return
        if not any(
            attribute_name in child.attributes
            for child in node.children.values()
        ):
            for child_name, child in node.children.items():
                if child_name != "healthy":
                    child.attributes[attribute_name] = node.attributes[
                        attribute_name
                    ]
        if "healthy" in node.children:
            del node.attributes[attribute_name]


class _SumCompleter(_Completer):
    @staticmethod
    def collect(attribute_name, node):
        if len(node.children) <= 1:
            return _Completer.collect(attribute_name, node)
        children_sum = 0
        missing_count = False
        sources = set()
        reason_parts = []
        for child in node.children.values():
            if attribute_name in child.attributes:
                children_sum += child.attributes[attribute_name].value
                reason_parts.append(
                    child.attributes[attribute_name]._get_reason()
                )
                sources = sources.union(
                    child.attributes[attribute_name].sources
                )
            else:
                missing_count = True
        if attribute_name not in node.attributes:
            if not missing_count:
                reason = " + ".join(reason_parts)
                node.attributes[attribute_name] = _Attribute(
                    children_sum, sources, f"{children_sum} = {reason}"
                )
            return
        if (
            not missing_count
            and node.attributes[attribute_name].value != children_sum
        ) or node.attributes[attribute_name].value < children_sum:
            raise AnnotationValueError(
                "Conflicting annotations. "
                "Total count is not the sum of subgroup counts",
                sources.union(node.attributes[attribute_name].sources),
            )

    @staticmethod
    def broadcast(attribute_name, node):
        if len(node.children) <= 1:
            return _Completer.broadcast(attribute_name, node)
        if attribute_name not in node.attributes:
            return
        children_sum = 0
        reason_parts = []
        missing_count = []
        sources = set(node.attributes[attribute_name].sources)
        for child in node.children.values():
            if attribute_name in child.attributes:
                children_sum += child.attributes[attribute_name].value
                reason_parts.append(
                    child.attributes[attribute_name]._get_reason()
                )
                sources = sources.union(
                    child.attributes[attribute_name].sources
                )
            else:
                missing_count.append(child)
        if (
            not missing_count
            and node.attributes[attribute_name].value != children_sum
        ) or node.attributes[attribute_name].value < children_sum:
            raise AnnotationValueError(
                "Conflicting annotations. Total count is not "
                "the sum of subgroup counts",
                sources,
            )
        if len(missing_count) != 1:
            return
        computed_count = node.attributes[attribute_name].value - children_sum
        total_reason = node.attributes[attribute_name]._get_reason()
        sum_reason = " + ".join(reason_parts)
        if len(reason_parts) > 1:
            sum_reason = f"( {sum_reason} )"
        reason = f"{computed_count} = {total_reason} - {sum_reason}"
        missing_count[0].attributes[attribute_name] = _Attribute(
            computed_count, sources, reason
        )


class _MeanCompleter(_Completer):
    @staticmethod
    def collect(attribute_name, node):
        if len(node.children) <= 1:
            return _Completer.collect(attribute_name, node)
        values = []
        sources = set()
        for child in node.children.values():
            if (
                "count" not in child.attributes
                or attribute_name not in child.attributes
            ):
                return
            values.append(
                (
                    child.attributes[attribute_name].value,
                    child.attributes["count"].value,
                )
            )
            sources = sources.union(child.attributes[attribute_name].sources)
            sources = sources.union(child.attributes["count"].sources)
        total_count = sum(c for _, c in values)
        if total_count == 0:
            return
        mean = sum(m * c for (m, c) in values) / total_count
        wsum_reason = " + ".join(f"{m}*{c}" for m, c in values)
        tcount_reason = " + ".join(str(c) for _, c in values)
        reason = f"{mean:.4g} = ( {wsum_reason} ) / ( {tcount_reason} )"
        if attribute_name not in node.attributes:
            node.attributes[attribute_name] = _Attribute(mean, sources, reason)
            return
        if not math.isclose(
            mean, node.attributes[attribute_name].value, rel_tol=0.1
        ):
            raise AnnotationValueError(
                "Conflicting annotations. "
                "Overall mean and subgroup means do not match",
                sources.union(node.attributes[attribute_name].sources),
            )


class _BoundCompleter(_Completer):
    _aggregate_name = "bound"

    @abc.abstractstaticmethod
    def _aggregate(values):
        pass

    @classmethod
    def collect(cls, attribute_name, node):
        if len(node.children) <= 1:
            return _Completer.collect(attribute_name, node)
        values = []
        sources = set()
        for child in node.children.values():
            if attribute_name not in child.attributes:
                return
            values.append(child.attributes[attribute_name].value)
            sources = sources.union(child.attributes[attribute_name].sources)
        bound = cls._aggregate(values)
        if attribute_name not in node.attributes:
            values_repr = ", ".join(map(str, values))
            reason = f"{bound} = {cls._aggregate_name}( {values_repr} )"
            node.attributes[attribute_name] = _Attribute(
                bound, sources, reason
            )
            return
        if (
            cls._aggregate([bound, node.attributes[attribute_name].value])
            != node.attributes[attribute_name].value
        ):
            raise AnnotationValueError(
                "Conflicting annotations."
                "Subgroup bounds not contained in overall bounds.",
                sources.union(node.attributes[attribute_name].sources),
            )

    @classmethod
    def broadcast(cls, attribute_name, node):
        if len(node.children) <= 1:
            return _Completer.broadcast(attribute_name, node)
        if attribute_name not in node.attributes:
            return
        for child in node.children.values():
            if attribute_name not in child.attributes:
                child.attributes[attribute_name] = node.attributes[
                    attribute_name
                ]
                continue
            if (
                cls._aggregate(
                    [
                        child.attributes[attribute_name].value,
                        node.attributes[attribute_name].value,
                    ]
                )
                != node.attributes[attribute_name].value
            ):
                raise AnnotationValueError(
                    "Conflicting annotations"
                    "Subgroup bounds not contained in overall bounds.",
                    node.attributes[attribute_name].sources.union(
                        child.attributes[attribute_name].sources
                    ),
                )


class _MinCompleter(_BoundCompleter):
    _aggregate_name = "min"

    @staticmethod
    def _aggregate(values):
        return min(values)


class _MaxCompleter(_BoundCompleter):
    _aggregate_name = "max"

    @staticmethod
    def _aggregate(values):
        return max(values)


_VALUE_PARSERS = {
    "count": _ValueParser(int),
    "age mean": _ValueParser(float),
    "age minimum": _ValueParser(float),
    "age maximum": _ValueParser(float),
    "age range": _RangeParser(),
    "age median": _ValueParser(float),
    "diagnosis": _ValueParser(str),
}


def demographics_labels():
    return tuple(_VALUE_PARSERS.keys()) + _GROUP_NAMES + _SEX_NAMES


_COMPLETERS = {
    "count": _SumCompleter,
    "age mean": _MeanCompleter,
    "age minimum": _MinCompleter,
    "age maximum": _MaxCompleter,
    "age median": _Completer,
    "diagnosis": _DiagnosisCompleter,
}


def _head(seq):
    return next(iter(seq))


class AnnotationError(Exception):
    def __init__(self, message=""):
        self.message = message
        self.detailed_message = f"{self.__class__.__name__}: {self.message}"
        self.error_positions = set()

    def __str__(self):
        return self.detailed_message


class AnnotationParsingError(AnnotationError):
    def __init__(self, message="", error_annotations=()):
        self.message = message
        if isinstance(error_annotations, pd.DataFrame):
            error_annotations = error_annotations.to_dict(orient="records")
        self.error_annotations = error_annotations
        self.error_positions = {
            (anno["start_char"], anno["end_char"])
            for anno in self.error_annotations
        }
        anno = "\n".join(map(self._format_annotation, self.error_annotations))
        self.detailed_message = f"{self.message}:\n\n{anno}"

    @staticmethod
    def _format_annotation(annotation):
        extra_repr = (
            f"({annotation['extra_data']!r})"
            if annotation["extra_data"] is not None
            else ""
        )
        return (
            f"  {annotation['label_name']!r}{extra_repr} on "
            f"'{annotation['selected_text']}'"
        )


class AnnotationValueError(AnnotationError):
    def __init__(self, message="", error_tokens=()):
        self.message = message
        self.error_tokens = error_tokens
        self.error_positions = {
            (tok.start_char, tok.end_char) for tok in self.error_tokens
        }
        tokens = "\n".join(f"  {tok}" for tok in self.error_tokens)
        self.detailed_message = f"{self.message}:\n\n{tokens}"


@dataclasses.dataclass(frozen=True)
class _Token:
    group_name: str
    subgroup_name: str
    sex: str
    label_name: str
    raw_value: str = dataclasses.field(compare=False)
    start_char: int
    end_char: int
    value: Any = dataclasses.field(init=False)

    def __post_init__(self):
        parser = _VALUE_PARSERS[self.label_name]
        try:
            value = parser(self.raw_value)
        except Exception:
            raise ValueError(
                f"Could not convert {self.raw_value!r} to {parser.name}"
            )
        object.__setattr__(self, "value", value)

    def __str__(self):
        path = _truncate_trailing_none(
            ("all participants", self.group_name, self.subgroup_name, self.sex)
        )
        path = (repr(step) if step is not None else "" for step in path)
        path_repr = " / ".join(path)
        return f"{path_repr} : {self.label_name} = {self.value}"


@dataclasses.dataclass
class _Attribute:
    value: Any
    sources: Set[_Token]
    reason: Optional[str] = None

    def _get_reason(self, nestable=True):
        if self.reason is None:
            return repr(self.value)
        if not nestable:
            return self.reason
        return f"( {self.reason} )"

    def __str__(self):
        return repr(self.value)


@dataclasses.dataclass
class _Node:
    count: Optional[int] = None
    attributes: Dict[str, _Attribute] = dataclasses.field(default_factory=dict)
    children: Dict[str, _Node] = dataclasses.field(default_factory=dict)

    def _format(self, indent=0):
        prefix = " " * indent
        if self.attributes:
            attributes = [
                prefix
                + ", ".join(
                    sorted(f"{k} = {v}" for k, v in self.attributes.items())
                )
            ]
        else:
            attributes = []
        if self.children:
            children = sorted(
                f"{prefix + k}\n{v._format(indent + 2)}"
                for k, v in self.children.items()
            )
        else:
            children = []
        return (
            "\n".join(attributes + children).replace("\n\n", "\n").strip("\n")
        )

    def __str__(self):
        return self._format().strip() or "<Empty participant tree>"


class DocAnnotations:
    def __init__(self, annotations):
        self.annotations = annotations
        self.tokens = []
        self.tree = _Node()
        self.error = None
        self._has_diagnosis = None
        try:
            self._parse()
            self._build_tree()
            self._add_values()
        except AnnotationError as error:
            self.error = error

    def _parse(self):
        stacks = self.annotations.groupby(["start_char", "end_char"])
        for (start_char, end_char), annotation_stack in stacks:
            self.tokens.append(
                _parse_token(annotation_stack, start_char, end_char)
            )

    def _build_tree(self):
        self._build_groups_and_subgroups()
        self._build_sexes()

    def _build_groups_and_subgroups(self):
        for tok in self.tokens:
            if tok.label_name == "diagnosis":
                self._has_diagnosis = True
            node = self.tree
            if tok.group_name is not None:
                node = node.children.setdefault(tok.group_name, _Node())
                if tok.subgroup_name is not None:
                    node = node.children.setdefault(tok.subgroup_name, _Node())
            if tok.sex is None and tok.label_name == "count":
                node.count = tok.value
        if len(self.tree.children) == 1:
            group = _head(self.tree.children.values())
            if self.tree.count is not None and self.tree.count != group.count:
                for group_name in _GROUP_NAMES:
                    self.tree.children.setdefault(group_name, _Node())
        elif not self.tree.children:
            group_name = "patients" if self._has_diagnosis else "healthy"
            self.tree.children[group_name] = _Node()
        if self.tree.count is not None and len(self.tree.children) == 1:
            _head(self.tree.children.values()).count = self.tree.count
        for group in self.tree.children.values():
            if not group.children:
                group.children["_"] = _Node()
            if group.count is not None and len(group.children) == 1:
                _head(group.children.values()).count = group.count

    def _find_node(self, tok):
        path = (tok.group_name, tok.subgroup_name, tok.sex)
        path = _truncate_trailing_none(path)
        node = self.tree
        for step in path:
            if step is None:
                if not node.children:
                    raise AnnotationValueError(
                        "Ambiguous group descriptors. Cannot find a group "
                        "for this annotation.",
                        {tok},
                    )
                if len(node.children) != 1:
                    details = ""
                    if path[-1] in _SEX_NAMES:
                        details = (
                            "When explicit groups or subgroups are used, "
                            "'female' and 'male' labels must be attached to "
                            "specific groups.\n"
                        )
                    candidates = list(node.children)
                    raise AnnotationValueError(
                        f"Ambiguous group descriptors.\n{details}"
                        "The annotation could belong to several groups: "
                        f"{candidates}",
                        {tok},
                    )
                node = _head(node.children.values())
            else:
                node = node.children.setdefault(step, _Node())
        return node

    def _build_sexes(self):
        for tok in self.tokens:
            if tok.sex is not None:
                node = self._find_node(tok)
                if tok.label_name == "count":
                    node.count = tok.value
        for group in self.tree.children.values():
            for subgroup in group.children.values():
                if (
                    len(subgroup.children) == 1
                    and subgroup.count is not None
                    and subgroup.count
                    != _head(subgroup.children.values()).count
                ) or not subgroup.children:
                    for sex in _SEX_NAMES:
                        subgroup.children.setdefault(sex, _Node())

    def _update_node(self, node, tok):
        new_attributes = _token_to_attributes(tok)
        for attribute_name, attribute in new_attributes.items():
            if (
                attribute_name in node.attributes
                and node.attributes[attribute_name].value != attribute
            ):
                raise AnnotationValueError(
                    "Conflicting annotations",
                    node.attributes[attribute_name].sources.union(
                        attribute.sources
                    ),
                )
            node.attributes.setdefault(attribute_name, attribute)

    def _add_values(self):
        for tok in self.tokens:
            node = self._find_node(tok)
            self._update_node(node, tok)
        # we could also do 1 first pass just for counts
        self._collect(self.tree)
        self._broadcast(self.tree)
        self._prune_empty_groups(self.tree)
        self._collect(self.tree)

    def _prune_empty_groups(self, node):
        node.children = {
            c_name: c
            for c_name, c in node.children.items()
            if "count" not in c.attributes or c.attributes["count"].value != 0
        }
        for child in node.children.values():
            self._prune_empty_groups(child)

    def _collect(self, node):
        if not node.children:
            return
        for _, child in node.children.items():
            self._collect(child)
        for attribute_name, completer in _COMPLETERS.items():
            completer.collect(attribute_name, node)

    def _broadcast(self, node):
        if not node.children:
            return
        for attribute_name, completer in _COMPLETERS.items():
            completer.broadcast(attribute_name, node)
        for _, child in node.children.items():
            self._broadcast(child)

    def subgroups(self):
        for group_name, group in self.tree.children.items():
            for subgroup_name, subgroup in group.children.items():
                yield group_name, subgroup_name, subgroup


def _token_to_attributes(tok):
    if tok.label_name == "age range":
        age_min, age_max = tok.value
        return {
            "age minimum": _Attribute(age_min, {tok}),
            "age maximum": _Attribute(age_max, {tok}),
        }
    return {tok.label_name: _Attribute(tok.value, {tok})}


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
    raise AnnotationParsingError(
        "Too many participant group qualifiers applied to the same text",
        group_anno,
    )


def _get_sex(annotation_stack: pd.DataFrame) -> Dict:
    sex_anno = annotation_stack[
        annotation_stack["label_name"].isin(_SEX_NAMES)
    ]
    if sex_anno.shape[0] == 0:
        return {"sex": None}
    if sex_anno.shape[0] == 1:
        return {"sex": sex_anno.iloc[0]["label_name"]}
    raise AnnotationParsingError(
        "Conflicting sex qualifiers applied to the same text",
        sex_anno,
    )


def _get_payload_anno(annotation_stack):
    return annotation_stack[
        ~annotation_stack["label_name"].isin(_GROUP_NAMES + _SEX_NAMES)
    ]


def _get_payload(annotation_stack: pd.DataFrame) -> Dict:
    payload_anno = _get_payload_anno(annotation_stack)
    if payload_anno.shape[0] == 0:
        raise AnnotationParsingError(
            "Group descriptors applied "
            "but data label (eg 'count', 'age mean', etc.) is missing",
            annotation_stack,
        )
    if payload_anno.shape[0] == 1:
        payload = {
            "label_name": payload_anno.iloc[0]["label_name"],
            "raw_value": payload_anno.iloc[0]["extra_data"],
        }
        if pd.isnull(payload["raw_value"]):
            payload["raw_value"] = payload_anno.iloc[0]["selected_text"]
        return payload
    raise AnnotationParsingError(
        "Too many data labels applied to the same text",
        payload_anno,
    )


def _parse_token(
    annotation_stack: pd.DataFrame, start_char: int, end_char: int
) -> _Token:
    token_data = {
        "start_char": start_char,
        "end_char": end_char,
    }
    token_data.update(_get_group_and_subgroup(annotation_stack))
    token_data.update(_get_sex(annotation_stack))
    token_data.update(_get_payload(annotation_stack))
    try:
        token = _Token(**token_data)
    except ValueError as error:
        raise AnnotationParsingError(
            str(error), _get_payload_anno(annotation_stack)
        )
    return token


def _truncate_trailing_none(seq):
    while seq and seq[-1] is None:
        seq = seq[:-1]
    return seq
