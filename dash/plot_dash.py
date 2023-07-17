from dash import Dash,dcc , Output, Input # pip install dash
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components
import dash_html_components as html # pip install dash-html-components
import os
import  plotly.graph_objects as go # pip install plotly
app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])

my_graph = dcc.Graph(figure={})


my_btn = dbc.Button('نمایش نمودار',style={'margin-top':'20px'})

@app.callback(
    Output(my_graph,component_property='figure'),
    Output(my_btn,component_property='n_clicks'),
    Input(my_btn,component_property='n_clicks')
)
def show_images(n_clicks):
    if n_clicks>0:
        
        with open('prices.txt') as f:
            number_list = f.read().split('\n')
        
        number_list = list(map(int,number_list))
        print(number_list)
        figure = go.Figure(data=go.Scatter(x=list(range(0,len(number_list))), y=number_list))
        return figure , n_clicks

app.layout = dbc.Container(
    
    [
        dbc.Row([my_graph,my_btn],className='text-center')      
        ])
if __name__=='__main__':
    app.run_server(port='8000')