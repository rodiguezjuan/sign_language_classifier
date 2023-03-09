from dash import dcc
from dash import html

def button_analyse_ui ():
    
    return html.Div(
        children=[
            html.Button(
                "Analyse Data",
                id="button_analyseData",
                disabled=False,
            )
        ]
    )
