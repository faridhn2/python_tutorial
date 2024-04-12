from dash import Dash,dcc , Output, Input,html # pip install dash
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components
app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

my_text = html.H1('salam',style={'color':'green'})

my_input = dbc.Input(placeholder='تایپ کنید',style={'text-align':'right'})
app.layout = dbc.Container([my_text,my_input])

@app.callback(
Output(my_text,component_property='children'),
Input(my_input,component_property='value'))
def text_update(my_text):
    # my_text*=2
    
    color_rate = min(len(my_text)*10,255)

    return html.Span(my_text,style={'color':'rgb({},{},{})'.format(color_rate,color_rate,color_rate)})




if __name__=='__main__':
    app.run()
