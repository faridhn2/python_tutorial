from dash import Dash , Output, Input # pip install dash
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components

import dash_table # pip install dash-table


class MyApp():
    def __init__(self) -> None:
        self.app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])

        self.btn = dbc.Button('نمایش جدول',style={'margin-top':'20px'},id='btn1')
        self.my_table = dash_table.DataTable(
            data=[],columns=[],
            style_cell={'color':'black','textAlign':'center'},id='table1'
        )
        self.app.layout = dbc.Container(
    
        [
        dbc.Row([self.my_table,self.btn],className='text-center')      
        ])
        self.app.callback(
                           Output("table1", "data"),
                            Output("table1", "columns"),
                            Output("btn1", "n_clicks"),
                            
                            Input("btn1", "n_clicks"),
                                                    
                          prevent_initial_call=True)(self.create_table)
    
    def run(self):
        self.app.run(port=8000)
    
    def create_table(self,n_clicks):
        print('________--')
        print(n_clicks)
        
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
            
if __name__ == '__main__':

    myapp = MyApp()
    myapp.run()