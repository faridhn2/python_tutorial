from dash import Dash,dcc , Output, Input # pip install dash
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components
import dash_html_components as html # pip install dash-html-components
import os
app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])

my_div = html.Div()

my_btn = dbc.Button('دیدن تصاویر',style={'margin-top':'20px'})

@app.callback(
    Output(my_div,component_property='children'),
    Output(my_btn,component_property='n_clicks'),
    Input(my_btn,component_property='n_clicks')
)
def show_images(n_clicks):
    if n_clicks>0:
        content = []
        image_list = os.listdir('assets/images')
        for image_name in image_list:
            img = html.Img(src=app.get_asset_url(f'images/{image_name}'),width='150px',height='150px')
            content.append(img)


        return content , n_clicks

app.layout = dbc.Container(
    
    [
        dbc.Row([my_div,my_btn],className='text-center')      
        ])
if __name__=='__main__':
    app.run_server(port='8000')