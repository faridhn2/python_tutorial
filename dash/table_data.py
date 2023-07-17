from dash import Dash,dcc , Output, Input # pip install dash
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components
import dash_html_components as html # pip install dash-html-components
import os
import dash_table # pip install dash-table
import  plotly.graph_objects as go # pip install plotly
app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])

my_table = dash_table.DataTable(
    data='',columns=[{'name':i,'id':i} for i in ['قیمت','عنوان' ] ],
    style_cell={'color':'black','textAlign':'center'},
)


my_btn = dbc.Button('نمایش جدول',style={'margin-top':'20px'})

@app.callback(
    Output(my_table,component_property='data'),
    
    Input(my_btn,component_property='n_clicks')
)
def create_table(n_clicks):
    # print(n_clicks)
    if n_clicks:
        data =[]
        with open('titles.txt',encoding='utf-8') as f:
            titles = f.read().split('\n')
        with open('prices.txt') as f:
            prices = f.read().split('\n')
        for t,p in zip(titles,prices):
            d = {'عنوان':t,'قیمت':' تومان '+p}
            
            data.append(d)
        return data 

app.layout = dbc.Container(
    
    [
        dbc.Row([my_table,my_btn],className='text-center')      
        ])
if __name__=='__main__':
    app.run_server(port='8000')