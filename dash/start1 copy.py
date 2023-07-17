from dash import Dash,dcc,html # pip install dash
import dash_bootstrap_components as dbc
app = Dash(__name__)
text = dcc.Markdown('# Salam')

# app.layout = html.Div([text])
app.layout = dbc.Container([text])

if __name__=='__main__':
    # app.run_server(port='8000')
    app.run(port='8000')
