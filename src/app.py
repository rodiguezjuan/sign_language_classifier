import datetime
import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from ui.viewUploadData import view_upload_data_ui
from ui.viewProcessing import view_processing_ui
from ui.viewList import view_list_ui
from ui.nav import nav_ui
from ui.player import player_ui
from ui.list import list_ui

from utilities.videoSplit import video_split
from utilities.evaluationData import evaluation_data
from utilities.loadModel import load_model

# varaibles globales
model = None
data_video = None
flag_process_video = False


external_stylesheets = ['..\assets\styles.css']

app = Dash(
    __name__, 
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
    )

app.layout = html.Div(
    className="layout-container",
    children=[
        dcc.Store(
            id='prosess',
        ),
        dcc.Store(
            id='classifier',
        ),
        nav_ui(),
        html.Div(
            className="header--container",
            children=[
                view_upload_data_ui(app),
                view_processing_ui(),
                view_list_ui(),
            ]
        ),
        
])

# Cargar Video
@app.callback(
        Output('output-video-upload', 'children'),
        Output('prosess', 'data'),
        Input('upload-video', 'contents'),
    )
def update_output(list_of_contents):
    global data_video

    if list_of_contents is not None:
        data_video = list_of_contents

        data = {'prosess': 1}
        
        return [player_ui(list_of_contents)], data
    else:
        data = {'prosess': 0}
        return [player_ui("https://youtu.be/ICm7cIlsrSY")], data
    
# Analizar video
@app.callback(
    Output('classifier', 'data'),
    Input('prosess', 'modified_timestamp'),
    State('prosess', 'data')
)
def prosess_video(ts, data):
    global data_video

    if ts is None:
        raise PreventUpdate
    
    if data.get('prosess') == 1:
        video_split(data_video)
        data = {'classifier': 1}

        return  data
    else:
        data = {'classifier': 0}
        return data
    
@app.callback(
    Output('processing-out-0', 'src'),
    Output('list_ui', 'children'),
    Input('classifier', 'modified_timestamp'),
    State('classifier', 'data')
)
def classification_list(ts, data):
    global model
    if ts is None:
        raise PreventUpdate
    
    if data.get('classifier') == 1:
        index = evaluation_data(model)
        return "./assets\icoon_check.svg", list_ui(index)
    else:
        return "./assets\icoon_close.svg", list_ui("")



if __name__ == '__main__':
    model = load_model()
    app.run_server(debug=False)
