import base64

from dash import dcc
from dash import html

from ui.player import player_ui
from utilities.videoSplit import video_split

def upload_video(contents):
    if contents != []:
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        fh = open("../data/data.mp4", "wb")
        fh.write(decoded)
        fh.close()
        print("Data upload")

        video_split("../data\data.mp4")
        print("Start analysis of data")

    return html.Div([

        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        player_ui(contents),
    ])