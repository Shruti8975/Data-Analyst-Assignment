import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv(r'C:\Users\shaik\OneDrive\Desktop\sales-dashboard\sales.csv.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H2("📊 Simple Sales Dashboard"),

    dcc.DatePickerRange(
        id='date-picker',
        start_date=df['Date'].min(),
        end_date=df['Date'].max()
    ),

    dcc.Graph(id='line-sales'),
    dcc.Graph(id='bar-city'),
    dcc.Graph(id='pie-category')
])

# Callback for updating charts
@app.callback(
    [Output('line-sales', 'figure'),
     Output('bar-city', 'figure'),
     Output('pie-category', 'figure')],
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_charts(start_date, end_date):
    dff = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    line_fig = px.line(dff, x='Date', y='Total', title='Sales Over Time')
    bar_fig = px.bar(dff.groupby('City')['Total'].sum().reset_index(), x='City', y='Total', title='Sales by City')
    pie_fig = px.pie(dff, names='Category', values='Total', title='Sales by Category')

    return line_fig, bar_fig, pie_fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

