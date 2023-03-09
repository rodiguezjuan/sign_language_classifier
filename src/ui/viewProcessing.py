from dash import dcc
from dash import html

def view_processing_ui():
    return html.Div(
        className="cards",
        children=[
            html.Img(
                id="processing-out-0",
                src="./assets\icoon_close.svg",
            ),
        ]
    )