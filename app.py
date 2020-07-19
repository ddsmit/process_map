import dash
import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from data import load
import command

app = dash.Dash(__name__)

elements =  load.all()


dropdown_options_nodes = [
    {'label':element['data']['label'], 'value':element['data']['id']}
    for element in elements
    if 'label' in element['data']
]

dropdown_options_commands = command.build_options()
app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Dropdown(
                    id='command',
                    options = dropdown_options_nodes+dropdown_options_commands,
                    value=[],
                    multi=True,
                ),
            ]
        ),
        html.Div(id='command_output'),
        html.Div(id='selected'),

        html.Div(
            [
                cyto.Cytoscape(
                    id='main',
                    layout={'name':'grid'},
                    style={'width':'100%','height': '400px'},
                    elements=elements,
                ),
            ]
        ),
    ]
)


@app.callback(
    [
        Output(component_id='command_output', component_property='children'),
    ],
    [
        Input(component_id='command',component_property='value'),
        Input(component_id='main',component_property='selectedNodeData'),
    ],
)
def input_handler(input):
    functions = command.get_functions(input)
    output = list(','.join([function() for function in functions]))
    # for function in functions:
    #     function(previous_node, current_node)
    print(output)
    return [output]
# @app.callback(
#     [
#         Output(component_id='command', component_property='value'),
#     ],
#     [
#         Input(component_id='output',component_property='children')
#     ],
# )
# def input_handler(input):
#     return ['']

if __name__ == '__main__':
    app.run_server(debug=True)