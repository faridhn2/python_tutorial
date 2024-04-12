from dash import Dash,dcc,html # pip install dash
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components
# print(dir(dcc))
app = Dash(__name__)
my_text = dcc.Markdown(children='# سلام به همه')

app.layout = dbc.Container([my_text])
if __name__=='__main__':
    app.run_server(port='8000')