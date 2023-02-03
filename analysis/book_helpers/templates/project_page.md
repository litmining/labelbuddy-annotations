---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
{{ warning_automatically_generated_page | safe }}

# {{ project_name }}

You can see the full contents of this project [on GitHub](https://github.com/neurodatascience/labelbuddy-annotations/tree/main/projects/{{ project_name }}/).

{{ readme_content | safe }}

## Labels in this project

{% if not labels %}
(No labels have been added to this project yet)
{% endif%}

```{code-cell}
:tags: [remove-input]

from labelrepo import displays
text = """
<div class="detailed-label-set">
    {% for label in labels %}
    <details {{ 'style="--label-color: {};"'.format(label.color) if label.color }}>
        <summary class="label-display">{{ label.name }} ({{ label.n_annotated_docs }} docs)</summary>
        {% if label.n_annotated_docs > 0 %}
        <p><b>Example annotations:</b></p>
        <div class="annotation-set">
            {% for annotation in label.example_annotations %}
            <div class="annotation">
                <div class="context">
                    {{ annotation.prefix }}<mark class="annotated-text">{{ annotation.selected_text }}</mark>{{ annotation.suffix }}
                </div>
                <div class="annotation-footer">
                    {%- if annotation.extra_data %}
                    <div class="extra-data">{{ annotation.extra_data }}</div>
                    {%- endif %}
                    <div class="pcmid"><a target="_blank"
                                          href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{{ annotation.pmcid }}/"
                                       >PMC{{ annotation.pmcid }}</a></div>
                    <div class="annotator-name">{{ annotation.annotator_name }}</div>
                </div>
            </div>
            {% endfor %}
        </div>
        {% else %}
        <p>(No annotations with this label in the current project)</p>
        {% endif %}
    </details>
    {% endfor %}
</div>
"""
displays.HTMLDisplay(text)
```
