from dash import dcc
from dash import html

from ui.list import list_ui

def view_list_ui():
    return html.Div(
        id="list_ui",
        className="cards",
    )