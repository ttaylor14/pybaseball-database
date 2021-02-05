# from flask import Flask
# server = Flask('my app')

# ***




import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px #(need to pip install plotly==4.4.1)

df = pd.read_csv("batting_stats_all.csv")

# you need to include __name__ in your Dash constructor if
# you plan to use a custom CSS or JavaScript in your Dash apps
app = dash.Dash(__name__)

#---------------------------------------------------------------
app.layout = html.Div([
    html.Div([
        html.Label(['Baseball Visualization']),

        dcc.RangeSlider(
            id='Season',
            min=-2000,
            max=2020,
            step=1,
            marks={
                2000: {'label': '2000', 'style': {'color': '#77b0b1'}},
                2010: {'label': '2010'},
                2015: {'label': '2015'},
                2020: {'label': '2020', 'style': {'color': '#f50'}}
            },
            value=[2018, 2020]
        ),  

        dcc.RangeSlider(
            id='Player_Age',
            min=-16,
            max=45,
            step=1,
            marks={
                16: {'label': '16', 'style': {'color': '#77b0b1'}},
                24: {'label': '24'},
                30: {'label': '30'},
                35: {'label': '35', 'style': {'color': '#f50'}}
            },
            value=[26, 29]
        ),  

        dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': 'Age', 'value': 'Age'},
                     {'label': 'Team', 'value': 'Team'},
                     {'label': 'Games Played', 'value': 'G'},
                     {'label': 'HomeRun', 'value': 'HR'},
                     {'label': 'Hits', 'value': 'H'},
                     {'label': 'Stolen Base', 'value': 'SB'}
            ],
            value='Age',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
    ]),

    html.Div([
        dcc.Graph(id='Pie_graph')
    ]),


])

#---------------------------------------------------------------
@app.callback(
    Output(component_id='Pie_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value'),
    Input(component_id='Season',component_property='value'),
    Input(component_id='Player_Age',component_property='value')]
)

def update_graph(my_dropdown,Season,Player_Age):
    print(Player_Age[0])
    dff = df

    min = Player_Age[0]
    max = Player_Age[1]
    dff = dff[(dff.Age >= min) & (dff.Age <= max)]

    print(Season[0])
    Smin = Season[0]
    Smax = Season[1]
    dff = dff[(dff.Season >= Smin) & (dff.Season <= Smax)]


    piechart=px.pie(
            data_frame=dff,
            names=my_dropdown,
            hole=.3,
            )

    return (piechart)


if __name__ == '__main__':
    app.run_server(debug=True)

#  Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)

