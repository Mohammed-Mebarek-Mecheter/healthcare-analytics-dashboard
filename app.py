# app.py

import dash_bootstrap_components as dbc
from dash import dcc, html, dash, Dash
from components import kpi_cards, filters, charts, table
import pandas as pd
from callbacks.callbacks import setup_callbacks

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, '/assets/style.css'])

# Load the dataset
data = pd.read_csv('data/healthcare_data.csv')
data['date_of_admission'] = pd.to_datetime(data['date_of_admission'])
data['discharge_date'] = pd.to_datetime(data['discharge_date'])

# Define the layout
app.layout = dbc.Container([
    dbc.NavbarSimple(
        brand="Healthcare Analytics Dashboard",
        brand_href="#",
        color="#2874A6",
        dark=True,
        className="mb-4"
    ),
    kpi_cards.layout(data),
    filters.layout(data),
    dbc.Tabs(
        [
            dbc.Tab(charts.layout(data), label="Charts", tab_id="charts-tab"),
            dbc.Tab(table.layout(data), label="Data Table", tab_id="table-tab"),
        ],
        id="dashboard-tabs",
        active_tab="charts-tab",
        className="mb-4"
    ),
    dcc.Store(id='filtered-data', data=data.to_json(date_format='iso', orient='split'))
], fluid=True)

setup_callbacks(app, data)  # Initialize the callbacks with the app and data

server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)