from dash import dcc
from dash import html

from ui.upload import upload_ui
from ui.player import player_ui

def view_upload_data_ui(app):
    return html.Div(
        className="cards", #view_upload_data_ui--container
        children=[
            upload_ui(app),
            html.Div(
                className="view_upload_data_ui--separator"
            ),
            html.Div(
                id='output-video-upload',
                className="view_upload_data_ui--container--video",
                #children=[
                    #player_ui(),
                #]

            )
    ])