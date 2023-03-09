from dash import dcc
from dash import html

def nav_ui():
    return html.Div(
        className="nav_ui--container",
        children=[
            html.Img(
                className="nav_ui--container--img",
                src="./assets\logo.svg"
            ),
            html.Div(
        className="nav_ui--container--text",
                children=[
                    "Classify",
                    html.Br(), 
                    "Sign Language"
                ]
            )
        ]
    )