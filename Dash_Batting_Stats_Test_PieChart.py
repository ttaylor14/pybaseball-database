# from flask import Flask
# server = Flask('my app')

# ***

"""
from pybaseball import batting_stats
batting_stats = batting_stats(2017)
print(batting_stats.head())

batting_stats.to_csv('batting_stats.csv', index=False)


"""

import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px #(need to pip install plotly==4.4.1)

df = pd.read_csv("batting_stats.csv")

# you need to include __name__ in your Dash constructor if
# you plan to use a custom CSS or JavaScript in your Dash apps
app = dash.Dash(__name__)

#---------------------------------------------------------------
app.layout = html.Div([
    html.Div([
        html.Label(['Baseball Visualization']),
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
        dcc.Graph(id='the_graph')
    ]),

])

#---------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    dff = df

    piechart=px.pie(
            data_frame=dff,
            names=my_dropdown,
            hole=.3,
            )

    return (piechart)


if __name__ == '__main__':
    app.run_server(debug=True)

#  Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

