# callbacks/callbacks.py
from dash.dependencies import Input, Output, State
import pandas as pd

from components import charts, table


def setup_callbacks(app, data):
    @app.callback(
        [Output('patient-table', 'data'),
         Output('patients-by-medical-condition-chart', 'figure'),
         Output('gender-distribution-chart', 'figure'),
         Output('admission-type-distribution-chart', 'figure'),
         Output('admissions-over-time-chart', 'figure'),
         Output('billing-amount-by-condition-chart', 'figure'),
         Output('age-vs-billing-amount-chart', 'figure')],
        [Input('date-range-picker', 'start_date'),
         Input('date-range-picker', 'end_date'),
         Input('condition-dropdown', 'value'),
         Input('doctor-dropdown', 'value'),
         Input('hospital-dropdown', 'value'),
         Input('gender-dropdown', 'value'),
         Input('age-slider', 'value')]
    )
    def update_dashboard(start_date, end_date, conditions, doctor, hospital, gender, age_range):
        filtered_data = data.copy()

        # Apply filters
        if start_date and end_date:
            filtered_data = filtered_data[(filtered_data['date_of_admission'] >= start_date) &
                                          (filtered_data['date_of_admission'] <= end_date)]
        if conditions:
            filtered_data = filtered_data[filtered_data['medical_condition'].isin(conditions)]
        if doctor:
            filtered_data = filtered_data[filtered_data['doctor'] == doctor]
        if hospital:
            filtered_data = filtered_data[filtered_data['hospital'] == hospital]
        if gender:
            filtered_data = filtered_data[filtered_data['gender'] == gender]
        if age_range:
            filtered_data = filtered_data[(filtered_data['age'] >= age_range[0]) &
                                          (filtered_data['age'] <= age_range[1])]

        # Update charts
        return (
            filtered_data.to_dict('records'),
            charts.patients_by_medical_condition(filtered_data).figure,
            charts.gender_distribution(filtered_data).figure,
            charts.admission_type_distribution(filtered_data).figure,
            charts.admissions_over_time(filtered_data).figure,
            charts.billing_amount_by_medical_condition(filtered_data).figure,
            charts.age_vs_billing_amount(filtered_data).figure
        )