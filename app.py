from pathlib import Path

from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# load the data. Each row is an annotation. There may be several annotations per paper
data_path = Path(__file__).resolve().parent / "examples" / "all_annotations.csv"
full_df = pd.read_csv(data_path, index_col=False)
full_df.pmcid = full_df.pmcid.astype(int)
full_df["index"] = list(full_df.index)

select_columns = [
    "index",
    "pmcid",
    "annotation_project",
    "annotation_label_name",
    "annotated_text",
]

df = full_df[select_columns]

# the following code is based on https://dash.plotly.com/datatable/interactivity

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Label("All annotations (in the table, you can filter/order which projects, labels, etc. you want to see in the graph below)"),
        dash_table.DataTable(
            id="datatable-interactivity",
            columns=[
                {"name": i, "id": i, "deletable": True, "selectable": True}
                for i in df.columns
            ],
            data=df.to_dict("records"),
            editable=True,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            row_selectable="multi",
            row_deletable=True,
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            page_current=0,
            page_size=8,
            style_cell={
                "whiteSpace": "normal",
                "height": "auto",
            },
        ),
        html.Div(id="datatable-interactivity-container"),
    ]
)


@app.callback(
    Output("datatable-interactivity", "style_data_conditional"),
    Input("datatable-interactivity", "selected_columns"),
)
def update_styles(selected_columns):
    return [
        {"if": {"column_id": i}, "background_color": "#D2F3FF"}
        for i in selected_columns
    ]


@app.callback(
    Output("datatable-interactivity-container", "children"),
    Input("datatable-interactivity", "derived_virtual_data"),
    Input("datatable-interactivity", "derived_virtual_selected_rows"),
)
def update_graphs(rows, derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = df if rows is None else pd.DataFrame(rows)

    colors = [
        "#7FDBFF" if i in derived_virtual_selected_rows else "#0074D9"
        for i in range(len(dff))
    ]

    return [
        dcc.Graph(
            id=column,
            figure={
                "data": [
                    {
                        "x": dff["annotation_label_name"],
                        "y": dff[column],
                        "type": "bar",
                        "marker": {"color": colors},
                    }
                ],
                "layout": {
                    "xaxis": {
                        "automargin": True,
                        "title": "Annotation label",
                        "tickangle": 45,
                    },
                    "yaxis": {"automargin": True, "title": "Number of uses"},
                    "height": 500,
                    "margin": {"t": 100, "l": 10, "r": 10},
                    "title": "Unique annotation labels in this selection of data",
                },
            },
        )
        # check if column exists - user may have deleted it
        # If `column.deletable=False`, then you don't
        # need to do this check.
        for column in ["annotation_label_name"]
        if column in dff
    ]


if __name__ == "__main__":
    app.run_server(debug=True)
