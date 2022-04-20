import copy
import dash_bootstrap_components as dbc
import datetime as dt

from dash import dcc, html
from data_tools.utilities.alter_table import get_location_data as get_data
from configs.components import *


end_date = dt.datetime.today() - dt.timedelta(minutes=1)
start_date = end_date - dt.timedelta(minutes=5)

table_header = [
    html.Thead(
        html.Tr([html.Th("Point"), html.Th("Value")], style={"text-align": "center"})
    )
]


def create_rows(type_b, tags):
    all_rows = []
    for tag in tags:
        if configs[type_b][tag][0]["tags"]:
            if tag == "inlet":
                names = configs[type_b][tag][0]["dash_name"]
            elif tag == "discharge" or tag == "fuel":
                names = configs[type_b][tag][0]["name"].title()
            else:
                names = configs[type_b][tag][0]["name"]
            points = configs[type_b][tag][0]["tags"]
            units = configs[type_b][tag][0]["units"]
            _len = list(range(0, len(points)))
            if tag in SPECIAL_TABLE_TAGS:
                for x in _len:
                    _item = {}
                    if "tank" in tag:
                        _type = tag.split("_")[0].title()
                        _item["label"] = f"{_type} Tank {x+1}"
                    else:
                        _item["label"] = names[x].title()
                    _item["value"] = points[x]
                    all_rows.append(
                        copy.deepcopy(
                            html.Tr(
                                [
                                    html.Td(_item["label"]),
                                    html.Td(
                                        f"{get_data(type_b, [_item['value']], _item['label'], start_date, end_date, trucked='NO').iloc[-1].values[0].round(2)} {units}"
                                    ),
                                ]
                            )
                        )
                    )
            else:
                all_rows.append(
                    copy.deepcopy(
                        html.Tr(
                            [
                                html.Td(names),
                                html.Td(
                                    f"{get_data(type_b, points, names, start_date, end_date, trucked='NO').iloc[-1].values[0].round(2)} {units}"
                                ),
                            ]
                        )
                    )
                )
        else:
            names = configs[type_b][tag][0]["name"].title()
            all_rows.append(copy.deepcopy(html.Tr([html.Td(names), html.Td("N/A")])))
    table_body = [html.Tbody(all_rows)]
    return table_body


area_1_page = dbc.Container(
    [
        dbc.Row(
            dcc.Link("Back to Home", href="/", style={"color": "#fff"}),
            style={"margin-top": "10px"},
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            html.H2(
                                "Area 1 Dashboard",
                                style={
                                    "border": "2px solid #20354b",
                                    "border-radius": "15px",
                                    "background": "#2b4664",
                                },
                            ),
                        ),
                        dbc.Row(
                            dbc.Col(
                                dbc.Button(
                                    html.Img(
                                        src="/assets/refresh.png",
                                        style={"height": "90%", "width": "100%"},
                                    ),
                                    color="light",
                                    size="lg",
                                    className="mr-1",
                                    href="/area_2-page",
                                    external_link=True,
                                    id="cs-refresh-btn",
                                ),
                                style={
                                    "text-align": "center",
                                    "margin-top": "10px",
                                    "margin-bottom": "0px",
                                },
                            ),
                        ),
                    ],
                    xs=10,
                    sm=10,
                    md=10,
                    lg=8,
                    xl=8,
                ),
            ],
            style={
                "text-align": "center",
                "justify-content": "center",
                "margin-top": "15px",
                "margin-bottom": "20px",
            },
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Location A",
                                    style={"text-align": "center", "font-size": "20px"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Table(
                                            table_header
                                            + create_rows("Location_A", TABLE_TAGS),
                                            bordered=True,
                                            dark=True,
                                            hover=True,
                                            responsive=True,
                                            striped=True,
                                        )
                                    ],
                                ),
                            ],
                            className="card border-secondary mb-3",
                            style={"width": "90%", "margin-top": "15px"},
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg="2",
                    xl="2",
                    style={"text-align": "-webkit-center"},
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Location B",
                                    style={"text-align": "center", "font-size": "20px"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Table(
                                            table_header
                                            + create_rows("Location_B", TABLE_TAGS),
                                            bordered=True,
                                            dark=True,
                                            hover=True,
                                            responsive=True,
                                            striped=True,
                                        )
                                    ],
                                ),
                            ],
                            className="card border-secondary mb-3",
                            style={"width": "90%", "margin-top": "15px"},
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=2,
                    xl=2,
                    style={"text-align": "-webkit-center"},
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Location C",
                                    style={"text-align": "center", "font-size": "20px"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Table(
                                            table_header
                                            + create_rows("Location_C", TABLE_TAGS),
                                            bordered=True,
                                            dark=True,
                                            hover=True,
                                            responsive=True,
                                            striped=True,
                                        )
                                    ],
                                ),
                            ],
                            className="card border-secondary mb-3",
                            style={"width": "90%", "margin-top": "15px"},
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=2,
                    xl=2,
                    style={"text-align": "-webkit-center"},
                ),
            ],
            style={"justify-content": "center"},
        ),
        html.A(href="/area_1-page"),
    ],
    fluid=True,
)

area_2_page = dbc.Container(
    [
        dbc.Row(
            dcc.Link("Back to Home", href="/", style={"color": "#fff"}),
            style={"margin-top": "10px"},
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            html.H2(
                                "Area 2 Dashboard",
                                style={
                                    "border": "2px solid #20354b",
                                    "border-radius": "15px",
                                    "background": "#2b4664",
                                },
                            ),
                        ),
                        dbc.Row(
                            dbc.Col(
                                dbc.Button(
                                    html.Img(
                                        src="/assets/refresh.png",
                                        style={"height": "90%", "width": "100%"},
                                    ),
                                    color="light",
                                    size="lg",
                                    className="mr-1",
                                    href="/area_2-page",
                                    external_link=True,
                                    id="cs-refresh-btn",
                                ),
                                style={
                                    "text-align": "center",
                                    "margin-top": "10px",
                                    "margin-bottom": "0px",
                                },
                            ),
                        ),
                    ],
                    xs=10,
                    sm=10,
                    md=10,
                    lg=8,
                    xl=8,
                ),
            ],
            style={
                "text-align": "center",
                "justify-content": "center",
                "margin-top": "15px",
                "margin-bottom": "20px",
            },
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Location D",
                                    style={"text-align": "center", "font-size": "20px"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Table(
                                            table_header
                                            + create_rows("Location D", TABLE_TAGS),
                                            bordered=True,
                                            dark=True,
                                            hover=True,
                                            responsive=True,
                                            striped=True,
                                        )
                                    ],
                                ),
                            ],
                            className="card border-secondary mb-3",
                            style={"width": "90%", "margin-top": "15px"},
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=2,
                    xl=2,
                    style={"text-align": "-webkit-center"},
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Location E",
                                    style={"text-align": "center", "font-size": "20px"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Table(
                                            table_header
                                            + create_rows("Location_E", TABLE_TAGS),
                                            bordered=True,
                                            dark=True,
                                            hover=True,
                                            responsive=True,
                                            striped=True,
                                        )
                                    ],
                                ),
                            ],
                            className="card border-secondary mb-3",
                            style={"width": "90%", "margin-top": "15px"},
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=2,
                    xl=2,
                    style={"text-align": "-webkit-center"},
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Location F",
                                    style={"text-align": "center", "font-size": "20px"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Table(
                                            table_header
                                            + create_rows("Location_F", TABLE_TAGS),
                                            bordered=True,
                                            dark=True,
                                            hover=True,
                                            responsive=True,
                                            striped=True,
                                        )
                                    ],
                                ),
                            ],
                            className="card border-secondary mb-3",
                            style={"width": "90%", "margin-top": "15px"},
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=2,
                    xl=2,
                    style={"text-align": "-webkit-center"},
                ),
            ],
            style={"justify-content": "center"},
        ),
        html.A(href="/area_2-page"),
    ],
    fluid=True,
)

area_3_page = dbc.Container(
    [
        dbc.Row(
            dcc.Link("Back to Home", href="/", style={"color": "#fff"}),
            style={"margin-top": "10px"},
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            html.H2(
                                "Area 3 Dashboard",
                                style={
                                    "border": "2px solid #20354b",
                                    "border-radius": "15px",
                                    "background": "#2b4664",
                                },
                            ),
                        ),
                        dbc.Row(
                            dbc.Col(
                                dbc.Button(
                                    html.Img(
                                        src="/assets/refresh.png",
                                        style={"height": "90%", "width": "100%"},
                                    ),
                                    color="light",
                                    size="lg",
                                    className="mr-1",
                                    href="/area_3-page",
                                    external_link=True,
                                    id="cs-refresh-btn",
                                ),
                                style={
                                    "text-align": "center",
                                    "margin-top": "10px",
                                    "margin-bottom": "0px",
                                },
                            ),
                        ),
                    ],
                    xs=10,
                    sm=10,
                    md=10,
                    lg=8,
                    xl=8,
                ),
            ],
            style={
                "text-align": "center",
                "justify-content": "center",
                "margin-top": "15px",
                "margin-bottom": "20px",
            },
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Location H",
                                    style={"text-align": "center", "font-size": "20px"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Table(
                                            table_header
                                            + create_rows("Location_H", TABLE_TAGS),
                                            bordered=True,
                                            dark=True,
                                            hover=True,
                                            responsive=True,
                                            striped=True,
                                        )
                                    ],
                                ),
                            ],
                            className="card border-secondary mb-3",
                            style={"width": "90%", "margin-top": "15px"},
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=2,
                    xl=2,
                    style={"text-align": "-webkit-center"},
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Location I",
                                    style={"text-align": "center", "font-size": "20px"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Table(
                                            table_header
                                            + create_rows("Location_I", TABLE_TAGS),
                                            bordered=True,
                                            dark=True,
                                            hover=True,
                                            responsive=True,
                                            striped=True,
                                        )
                                    ],
                                ),
                            ],
                            className="card border-secondary mb-3",
                            style={"width": "90%", "margin-top": "15px"},
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=2,
                    xl=2,
                    style={"text-align": "-webkit-center"},
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Location J",
                                    style={"text-align": "center", "font-size": "20px"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Table(
                                            table_header
                                            + create_rows("Location_J", TABLE_TAGS),
                                            bordered=True,
                                            dark=True,
                                            hover=True,
                                            responsive=True,
                                            striped=True,
                                        )
                                    ],
                                ),
                            ],
                            className="card border-secondary mb-3",
                            style={"width": "90%", "margin-top": "15px"},
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=2,
                    xl=2,
                    style={"text-align": "-webkit-center"},
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Location K",
                                    style={"text-align": "center", "font-size": "20px"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Table(
                                            table_header
                                            + create_rows("Location_K", TABLE_TAGS),
                                            bordered=True,
                                            dark=True,
                                            hover=True,
                                            responsive=True,
                                            striped=True,
                                        )
                                    ],
                                ),
                            ],
                            className="card border-secondary mb-3",
                            style={"width": "90%", "margin-top": "15px"},
                        ),
                    ],
                    xs=12,
                    sm=12,
                    md=12,
                    lg=2,
                    xl=2,
                    style={"text-align": "-webkit-center"},
                ),
            ],
            style={"justify-content": "center"},
        ),
        html.A(href="/area_3-page"),
    ],
    fluid=True,
)
