from dash import dash_table, html

# Enhance the Data Table
def layout(data):
    table = dash_table.DataTable(
        id='patient-table',
        columns=[
            {"name": col, "id": col} for col in data.columns
        ],
        data=data.to_dict('records'),
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        page_action="native",
        page_current=0,
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={
            'padding': '10px',
            'textAlign': 'left',
            'minWidth': '150px', 'width': '150px', 'maxWidth': '150px',
            'whiteSpace': 'normal',
            'font-size': '0.9rem',
            'font-family': 'Roboto, sans-serif'
        },
        style_header={
            'backgroundColor': '#f0f0f0',
            'fontWeight': 'bold',
            'font-size': '1rem'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#f8f8f8'
            }
        ],
        export_format='csv',
        export_headers='display'
    )

    return html.Div([
        html.Hr(),
        html.H3("Patient Records Table", className="mt-4 mb-4"),
        table
    ])
