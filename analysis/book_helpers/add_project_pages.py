#! /usr/bin/env python3
import json
import pathlib
import re

import jinja2

from labelrepo import database, repo


def get_readme(project_dir):
    readme_path = project_dir / "README.md"
    if not readme_path.is_file():
        return ""
    content = readme_path.read_text(encoding="UTF-8")
    return re.sub(r"^#", r"##", content)


def get_labels(project_name):
    all_label_ids = [
        row["label_id"]
        for row in connection.execute(
            "select label_id from project_label where project_name = :pname "
            "union "
            "select label_id from annotation where project_name = :pname ",
            {"pname": project_name},
        )
    ]
    all_labels = []
    for label_id in all_label_ids:
        label_info = dict(
            connection.execute(
                "select * from label where id = ?", (label_id,)
            ).fetchone()
        )
        example_annotations = connection.execute(
            "select * from detailed_annotation "
            "where project_name = ? and label_name = ? "
            "order by pmcid, start_char limit 10",
            (project_name, label_info["name"]),
        )
        label_info["example_annotations"] = list(
            map(dict, example_annotations)
        )
        n_docs = connection.execute(
            "select count(distinct doc_id) from "
            "annotation where project_name = ? and label_id = ?",
            (project_name, label_id),
        ).fetchone()[0]
        label_info["n_annotated_docs"] = n_docs
        for annotation in label_info["example_annotations"]:
            prefix = annotation["context"][
                : annotation["start_char"] - annotation["context_start_char"]
            ]
            if annotation["context_start_char"] != 0:
                prefix = "…" + prefix
            annotation["prefix"] = prefix
            suffix = annotation["context"][
                annotation["end_char"] - annotation["context_start_char"] :
            ]
            if annotation["context_end_char"] != annotation["doc_length"]:
                suffix = suffix + "…"
            annotation["suffix"] = suffix

        all_labels.append(label_info)
    return sorted(all_labels, key=lambda a: -a["n_annotated_docs"])


def escape_quotes(value, jsonify=True):
    if jsonify:
        value = json.loads(json.dumps(value))
    if isinstance(value, str):
        return (
            value.replace('"""', '"​"​"')
            .replace("'''", "'​'​'")
            .replace("```", "`​`​`")
        )
    if isinstance(value, dict):
        return {k: escape_quotes(v, False) for k, v in value.items()}
    if isinstance(value, list):
        return [escape_quotes(v) for v in value]
    return value


helpers_dir = pathlib.Path(__file__).parent.resolve()

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(helpers_dir / "templates", encoding="UTF-8")
)

connection = database.get_database_connection()
all_projects = [
    p["name"]
    for p in connection.execute("select name from project order by name")
]

output_dir = repo.repo_root() / "analysis" / "book" / "projects"
output_dir.mkdir(exist_ok=True)

WARNING_AUTO_GEN = """
% !!!
%
% Don't edit this page directly!
% It has been automatically generated.
% Instead, edit the project's README.md file which gets inserted here,
% or the templates in /analysis/book_helpers/templates/
%
% !!!
"""

DIR_WARNING_AUTO_GEN = """Don't edit the pages in this directory directly!
They have been automatically generated.
Instead, edit the projects' README.md file which gets inserted here,
or the templates in /analysis/book_helpers/templates/
"""

for project_name in all_projects:
    project_dir = repo.repo_root() / "projects" / project_name
    project_info = {"project_name": project_name}
    project_info["readme_content"] = get_readme(project_dir)
    project_info["labels"] = get_labels(project_name)
    project_info["warning_automatically_generated_page"] = WARNING_AUTO_GEN
    try:
        template = jinja_env.get_template(f"{project_name}.md")
    except jinja2.TemplateNotFound:
        template = jinja_env.get_template("project_page.md")
    rendered = template.render(**escape_quotes(project_info))
    (output_dir / f"{project_name.replace('.', '__')}.md").write_text(
        rendered, encoding="UTF-8"
    )
    (
        output_dir / "DONT_EDIT_THIS_DIRECTORY_IT_IS_AUTOMATICALLY_GENERATED"
    ).write_text(DIR_WARNING_AUTO_GEN, encoding="UTF-8")
