python
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load data
data_path = 'Distribution_of_Pensioners_2022.xlsx'
data = pd.read_excel(data_path)

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1('Pensioners Distribution Dashboard'),
    dcc.Dropdown(
        id='gender-filter',
        options=[
            {'label': 'Male', 'value': 'Male'},
            {'label': 'Female', 'value': 'Female'},
            {'label': 'All', 'value': 'All'}
        ],
        value='All',
        placeholder='Select Gender'
    ),
    dcc.Graph(id='distribution-chart')
])

# Callback for updating the chart
@app.callback(
    dash.dependencies.Output('distribution-chart', 'figure'),
    [dash.dependencies.Input('gender-filter', 'value')]
)
def update_chart(gender):
    if gender == 'All':
        filtered_data = data
    else:
        filtered_data = data[data['Gender'] == gender]
    
    fig = px.bar(
        filtered_data,
        x='Quarter',
        y='Count',
        color='Gender',
        title='Pensioners Distribution by Gender and Quarter'
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
