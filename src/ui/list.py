from dash import dcc
from dash import html

def list_ui(item):

    class_name = "list_ui_index--container"
    
    children = []

    items = [
        "item_1",  "item_1",  "item_1",
        "item_1",  "item_1",  "item_1",
        "item_1",  "item_1",  "item_1",
        "item_1"
    ]

    count = 0
    print(item)
    for i in items:
        if count == item:
            print(count)
            elements = html.Div(
                className=class_name,
                id = "list"+str(count),
                children=[
                    html.P(i)
                ]
            )
            children.append(elements)
        else:
            elements = html.Div(
                id = "list"+str(count),
                className="list_ui--container",
                children=[
                    html.P(i)
                ]
            )
            children.append(elements)

        count= count+1

    return children