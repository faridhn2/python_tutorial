from dash import Dash,html # pip install dash
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

my_img = html.Img(src=app.get_asset_url(r'flask-horizontal.webp'))
# my_img = html.Img(src=r'D:\rasa_tutorial\Advanced_python\webscraping\image_name.jpg')
my_img2 = html.Img(src='https://upload.wikimedia.org/wikipedia/commons/d/dc/Steve_Jobs_Headshot_2010-CROP_%28cropped_2%29.jpg', width=350 ,height=400)

app.layout = dbc.Container([my_img,my_img2])


if __name__=='__main__':
    app.run()
# print(r'\n\t\i')