from digi_scraper import DigiScraper
from dash import Dash,dcc , Output, Input # pip install dash
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components
import dash_html_components as html # pip install dash-html-components
import os
import plotly.express as px
import  plotly.graph_objects as go
import httpcore
setattr(httpcore, 'SyncHTTPTransport', 'AsyncHTTPProxy')
from googletrans import Translator
translator = Translator()

def translate(text):
    text = text.replace(',','')
    result = translator.translate(text,dest='en', src='fa')
    text = result.text
    
    return text


app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])
my_graph = dcc.Graph(figure={})

my_div = html.Div()
my_input = dbc.Input(value='',style={'text-align':'right'})
my_btn = dbc.Button('جستجو',style={'margin-top':'20px'})

@app.callback(
    Output(my_graph,component_property='figure'),
    Output(my_div,component_property='children'),
    Output(my_btn,component_property='n_clicks'),
    Input(my_btn,component_property='n_clicks'),
    Input(my_input,component_property='value')
)
def show_images(n_clicks,search_key):
    if n_clicks>0:
        dg_scr = DigiScraper(search_key)
        dg_scr.process()
        content = []
        for image_name in dg_scr.images[:3]:
            img = html.Img(src=image_name,width='150px',height='150px')
            content.append(img)
            print(dg_scr.prices)
            dg_scr.prices = list(map(lambda x :translate(x),dg_scr.prices))
            print(dg_scr.prices)
            dg_scr.prices = list(map(lambda x :int(x),dg_scr.prices))
            figure = go.Figure(data=go.Bar(x=list(range(0,len(dg_scr.prices))), y=dg_scr.prices ))
        
        return figure, content , n_clicks




app.layout = dbc.Container(
    
    [
        dbc.Row([my_input,my_btn,my_div,my_graph],className='text-center')      
        ])
if __name__=='__main__':
    app.run_server(port='8000')