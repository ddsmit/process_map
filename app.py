import dash
import dash_cytoscape as cyto
import dash_html_components as dash_html_components

app = dash.Dash(__name__)

elements = [
    {
        'data':
        {
            'id':'home',
            'label':'home',
        },
        'position':
        {
            'x':75,
            'y':75,
        }
    },
        {
        'data':
        {
            'id':'away',
            'label':'away',
        },
        'position':
        {
            'x':200,
            'y':200,
        }
    },
        {
        'data':
        {
            'source':'home',
            'target':'away',
        },
    },
]

app.layout = html.Div(
    [
        cyto.Cytoscrap(
            id='main',
            layout={'name':'preset'},
            style={'width':'100%'},
            elements=elements,
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)