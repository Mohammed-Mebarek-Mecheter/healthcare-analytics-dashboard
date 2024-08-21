# kpi_cards
import dash_bootstrap_components as dbc
from dash import html

def generate_kpi_card(title, value, icon_class):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.H6(title, className="card-subtitle mb-2 text-muted"),
                html.Div(className="d-flex align-items-center", children=[
                    html.I(className=f"bi {icon_class} me-2"),
                    html.H4(value, className="mb-0")
                ]),
            ]),
            className="shadow-sm h-100"
        ),
        md=4,
        className="mb-4"
    )

def layout(data):
    total_patients = data['name'].nunique()
    avg_billing_amount = f"${round(data['billing_amount'].mean(), 2):,.2f}"
    avg_length_of_stay = f"{round(data['length_of_stay'].mean(), 1)} days"
    most_common_condition = data['medical_condition'].mode()[0]
    gender_distribution = f"M: {round(data['gender'].value_counts(normalize=True)['Male']*100, 1)}% F: {round(data['gender'].value_counts(normalize=True)['Female']*100, 1)}%"

    kpi_cards = dbc.Row([
        generate_kpi_card("Total Patients", total_patients, "bi-person"),
        generate_kpi_card("Avg. Billing", avg_billing_amount, "bi-currency-dollar"),
        generate_kpi_card("Avg. Stay", avg_length_of_stay, "bi-clock-history"),
        generate_kpi_card("Top Condition", most_common_condition, "bi-heart-pulse"),
        generate_kpi_card("Gender Ratio", gender_distribution, "bi-gender-ambiguous")
    ])

    return kpi_cards