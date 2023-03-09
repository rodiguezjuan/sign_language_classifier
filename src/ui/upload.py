from dash import dcc
from dash import html

def upload_ui(app):
    return html.Div(
        className="upload--container",
        children=[
        dcc.Upload(
            id='upload-video',
            children=html.Div([
                'Drag and Drop or ',
                html.Br(),
                html.A('Select Files')
            ]),
            multiple=False
        )
    ])
