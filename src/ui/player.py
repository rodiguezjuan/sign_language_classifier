from dash import dcc
from dash import html

import dash_player as dp


def player_ui(data):
    return html.Div(
            className="player_ui--container",
            children=[
                dp.DashPlayer(
                    className="player",
                    url=data,
                    controls=False,
                    width="100%",
                    height="264px",
                    playing=True,
                    loop=True,
                    muted=True,
                    playbackRate=1,
                )
            ])
