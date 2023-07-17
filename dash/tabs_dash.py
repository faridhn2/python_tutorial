from dash import Dash,dcc , Output, Input # pip install dash
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components
import dash_html_components as html # pip install dash-html-components
import os
import dash_table # pip install dash-table
import  plotly.graph_objects as go # pip install plotly

class MyApp():
    def __init__(self) -> None:
        self.app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])

        
        self.app.layout = dbc.Container(
            dbc.Tabs([
            dbc.Tab(self.page_1(), tab_id="page_1",label="Table Page"),
            dbc.Tab(self.page_2(), tab_id="page_2",label="Test"),
                        
                        ],
                        active_tab='page_1')
        )

        self.app.callback(
                           Output("table1", "data"),
                            Output("table1", "columns"),
                            Output("btn1", "n_clicks"),
                            
                            Input("btn1", "n_clicks"),
                                                    
                          prevent_initial_call=True)(self.create_table)
    
    def run(self):
        self.app.run(port=8000)
    
    def create_table(self,n_clicks):
        
        
        if n_clicks > 0 :
            data =[]
            with open('titles.txt',encoding='utf-8') as f:
                titles = f.read().split('\n')
            with open('prices.txt') as f:
                prices = f.read().split('\n')
            for t,p in zip(titles,prices):
                d = {'عنوان':t,'قیمت':' تومان '+p}
                
                data.append(d)
            print(data)
            cols = [{'name':i,'id':i} for i in ['قیمت','عنوان' ] ]
            return data ,cols , 0
    def page_1(self):
        self.btn = dbc.Button('نمایش جدول',style={'margin-top':'20px'},id='btn1')
        self.my_table = dash_table.DataTable(
            data=[],columns=[],
            style_cell={'color':'black','textAlign':'center'},id='table1'
        )
        
        
        row_div = dbc.Row([self.my_table,self.btn],className='text-center')      
        
        return  dbc.Container([row_div])
    def page_2(self):
        return dbc.Container(html.H1('salam'))
if __name__ == '__main__':

    myapp = MyApp()
    myapp.run()