from dash import Dash,dcc , Output, Input # pip install dash
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components
import dash_html_components as html # pip install dash-html-components
import os
import plotly.graph_objects as go # pip install plotly
app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])
my_input1 = dbc.Input(placeholder='x')

figure = go.Figure(
    data=go.Scatter(x=list(range(0,10)), y=list(range(1,11)),mode='markers'))
        
my_graph = dcc.Graph(figure=figure)
my_btn = dbc.Button('نمایش نمودار',style={'margin-top':'20px'})
div = dbc.Row([my_btn],class_name='text-center')
app.layout = dbc.Container([my_input1,div,my_graph])
# @app.callback(
#     Output(my_graph,component_property='figure'),
#     Output(my_btn,component_property='n_clicks'),
#     Input(my_input1,component_property='value'),
#     Input(my_btn,component_property='n_clicks'),
    
# )
# def update_graph(my_string,nclick):
#     xy_list = my_string.split('/')
#     xs = []
#     ys = []
#     for xy in xy_list:
#         x,y = xy.split(',')
#         x = int(x)
#         y = int(y)
#         xs.append(x)
#         ys.append(y)
#     figure = go.Figure(
#     data=go.Scatter(x=xs, y=ys,mode='markers'))

#     return figure , nclick
@app.callback(
    Output(my_graph,component_property='figure'),
    
    Input(my_input1,component_property='value'),
    
    
)
def update_graph(my_string):
    xy_list = my_string.split('/')
    xs = []
    ys = []
    for xy in xy_list:
        x,y = xy.split(',')
        x = int(x)
        y = int(y)
        xs.append(x)
        ys.append(y)
    figure = go.Figure(
    data=go.Scatter(x=xs, y=ys,mode='markers'))

    return figure 

if __name__=='__main__':
    app.run_server(port='8000')