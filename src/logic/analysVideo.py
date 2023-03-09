from dash import dcc
from dash import html

from ui.button import button_analyse_ui

def analyse_video():
    return html.Div(
        children=[
            button_analyse_ui,
            html.Div(
                id="message_analyse_ui"
            )
        ]
    )