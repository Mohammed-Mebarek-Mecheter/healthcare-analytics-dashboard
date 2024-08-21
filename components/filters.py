# filters

import dash_bootstrap_components as dbc
from dash import dcc, html

def layout(data):
    filters = dbc.Row([
        dbc.Col(
            dcc.DatePickerRange(
                id='date-range-picker',
                start_date=data['date_of_admission'].min(),
                end_date=data['date_of_admission'].max(),
                display_format='YYYY-MM-DD',
            ),
            width="auto"
        ),
        dbc.Col(
            dcc.Dropdown(
                id='condition-dropdown',
                options=[{'label': condition, 'value': condition} for condition in data['medical_condition'].unique()],
                multi=True,
                placeholder="Medical Condition(s)",
            ),
            width=2
        ),
        dbc.Col(
            dcc.Dropdown(
                id='doctor-dropdown',
                options=[{'label': doctor, 'value': doctor} for doctor in data['doctor'].unique()],
                placeholder="Doctor",
            ),
            width=2
        ),
        dbc.Col(
            dcc.Dropdown(
                id='hospital-dropdown',
                options=[{'label': hospital, 'value': hospital} for hospital in data['hospital'].unique()],
                placeholder="Hospital",
            ),
            width=2
        ),
        dbc.Col(
            dcc.Dropdown(
                id='gender-dropdown',
                options=[
                    {'label': 'Male', 'value': 'Male'},
                    {'label': 'Female', 'value': 'Female'}
                ],
                placeholder="Gender",
            ),
            width=2
        ),
        dbc.Col(
            dcc.RangeSlider(
                id='age-slider',
                min=data['age'].min(),
                max=data['age'].max(),
                step=1,
                marks={i: str(i) for i in range(data['age'].min(), data['age'].max() + 1, 10)},
                value=[data['age'].min(), data['age'].max()],
            ),
            width=3
        )
    ], className="mb-4 g-2 align-items-end")

    return filters