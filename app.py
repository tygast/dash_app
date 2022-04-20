import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import dcc, html, callback

from callbacks import *
from layouts.charts import chart_page
from layouts.home import home_page
from layouts.tables import *

external_stylesheets = [dbc.themes.DARKLY]

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, maximum-scale=1.5, minimum-scale=0.5",
        }
    ],
)
server = app.server


app.layout = html.Div(
    [dcc.Location(id="url", refresh=True), html.Div(id="page-content"),],
)

app.title = "LocationDetailViewer"


@callback(Output("page-content", "children"), [Input("url", "pathname"),])
def display_page(pathname):
    if pathname == "/area_1-page":
        return area_1_page
    elif pathname == "/area_2-page":
        return area_2_page
    elif pathname == "/area_3-page":
        return area_3_page
    elif pathname == "/charts":

        return chart_page
    else:
        return home_page


if __name__ == "__main__":
    app.run_server(debug=True)
