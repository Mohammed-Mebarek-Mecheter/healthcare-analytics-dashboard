# components/charts.py
import plotly.express as px
from dash import dcc, html
import dash_bootstrap_components as dbc

def patients_by_medical_condition(data, gender=None):
    if gender:
        data = data[data['gender'] == gender]

    condition_counts = data['medical_condition'].value_counts().reset_index()
    condition_counts.columns = ['medical_condition', 'count']

    fig = px.bar(
        condition_counts,
        x='medical_condition',
        y='count',
        title='<b>Patients by Medical Condition</b>',
        labels={'medical_condition': 'Medical Condition', 'count': 'Number of Patients'},
        color_discrete_sequence=['#5DADE2']
    )
    fig.update_layout(
        plot_bgcolor='#F2F3F4',
        paper_bgcolor='#F2F3F4',
        font_color='#2874A6'
    )

    return dcc.Graph(id='patients-by-medical-condition-chart', figure=fig)

def gender_distribution(data):
    gender_counts = data['gender'].value_counts().reset_index()
    gender_counts.columns = ['gender', 'count']

    fig = px.pie(
        gender_counts,
        names='gender',
        values='count',
        title='<b>Gender Distribution</b>',
        color_discrete_sequence=['#48C9B0', '#58D68D']
    )
    fig.update_layout(
        plot_bgcolor='#F2F3F4',
        paper_bgcolor='#F2F3F4',
        font_color='#2874A6'
    )

    return dcc.Graph(id='gender-distribution-chart', figure=fig)

def admission_type_distribution(data):
    admission_counts = data['admission_type'].value_counts().reset_index()
    admission_counts.columns = ['admission_type', 'count']

    fig = px.pie(
        admission_counts,
        names='admission_type',
        values='count',
        title='<b>Admission Type Distribution</b>',
        color_discrete_sequence=['#5DADE2', '#48C9B0', '#58D68D']
    )
    fig.update_layout(
        plot_bgcolor='#F2F3F4',
        paper_bgcolor='#F2F3F4',
        font_color='#2874A6'
    )

    return dcc.Graph(id='admission-type-distribution-chart', figure=fig)


def admissions_over_time(data, group_by=None):
    data['admission_count'] = 1
    if group_by:
        admissions = data.groupby([group_by, 'date_of_admission']).size().reset_index(name='count')
        fig = px.area(
            admissions,
            x='date_of_admission',
            y='count',
            color=group_by,
            title='<b>Admissions Over Time</b>',
            labels={'date_of_admission': 'Date of Admission', 'count': 'Number of Admissions', group_by: group_by},
            template='plotly_dark'
        )
    else:
        admissions = data.groupby('date_of_admission').size().reset_index(name='count')
        fig = px.line(
            admissions,
            x='date_of_admission',
            y='count',
            title='<b>Admissions Over Time</b>',
            labels={'date_of_admission': 'Date of Admission', 'count': 'Number of Admissions'},
            template='plotly_dark'
        )

    fig.update_layout(
        plot_bgcolor='#F2F3F4',
        paper_bgcolor='#F2F3F4',
        font_color='#2874A6',
        xaxis_tickformat='%b %d, %Y'
    )

    return dcc.Graph(id='admissions-over-time-chart', figure=fig)


def billing_amount_by_medical_condition(data):
    fig = px.box(
        data,
        x='medical_condition',
        y='billing_amount',
        title='<b>Billing Amount by Medical Condition</b>',
        labels={'medical_condition': 'Medical Condition', 'billing_amount': 'Billing Amount'},
        color_discrete_sequence=px.colors.sequential.Plasma
    )
    fig.update_layout(
        plot_bgcolor='#F2F3F4',
        paper_bgcolor='#F2F3F4',
        font_color='#2874A6'
    )

    return dcc.Graph(id='billing-amount-by-condition-chart', figure=fig)


def age_vs_billing_amount(data, color_by=None):
    fig = px.scatter(
        data,
        x='age',
        y='billing_amount',
        color=color_by,
        title='<b>Age vs. Billing Amount</b>',
        labels={'age': 'Age', 'billing_amount': 'Billing Amount', color_by: color_by},
        color_discrete_sequence=px.colors.sequential.Plasma
    )
    fig.update_layout(
        plot_bgcolor='#F2F3F4',
        paper_bgcolor='#F2F3F4',
        font_color='#2874A6'
    )

    return dcc.Graph(id='age-vs-billing-amount-chart', figure=fig)


def layout(data):
    charts = html.Div([
        html.Hr(),
        # html.H3("Healthcare Data Visualizations", className="mt-4 mb-4"),
        patients_by_medical_condition(data),
        gender_distribution(data),
        admission_type_distribution(data),
        admissions_over_time(data),
        billing_amount_by_medical_condition(data),
        age_vs_billing_amount(data)
    ])

    return charts

def layout(data):
    """
    Generates the layout for all chart components.

    :param data: The dataset used to populate the charts.
    :return: A Dash HTML component containing all the charts.
    """
    charts = html.Div([
        html.Hr(),
        # html.H3("Healthcare Data Visualizations", className="mt-4 mb-4"),
        patients_by_medical_condition(data),
        gender_distribution(data),
        admission_type_distribution(data),
        admissions_over_time(data),
        billing_amount_by_medical_condition(data),
        age_vs_billing_amount(data)
    ])

    return charts
