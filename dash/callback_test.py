from dash import Dash,dcc , Output, Input # pip install dash
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components
import dash_html_components as html # pip install dash-html-components
from googletrans import Translator
translator = Translator()
app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])

my_text = html.H1('a',style={'color':'green'})
my_input = dbc.Input(value='تایپ کنید',style={'text-align':'right'})

@app.callback(
Output(my_text,component_property='children'),
Input(my_input,component_property='value'))
def translate(inp_text):
    result = translator.translate(inp_text ,dest='fa', src='en')
    return result.text

    
# def update_text(inp_text):
#     return inp_text

app.layout = dbc.Container(
    
    [
        dbc.Row([my_text,my_input],className='text-center')      
        ])
if __name__=='__main__':
    app.run_server(port='8000')