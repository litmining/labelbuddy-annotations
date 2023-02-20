{% extends "project_page.md" %}

{% block main_content %}

## Participant demographics summaries

Here we show the information about participants that has been extracted from all the annotated documents.

```{code-cell}
:tags: [remove-input]

from labelrepo import displays
from labelrepo.projects import participant_demographics
text = participant_demographics.get_report_for_repo(remove_failed_docs=True)
displays.HTMLDisplay(text)
```

{% endblock %}
