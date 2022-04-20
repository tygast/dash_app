import dash_bootstrap_components as dbc

from dash import html
from configs.components import *


type_a_tab = (
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Card(
                        dbc.CardBody(
                            [
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                dbc.Row(
                                                    dcc.Link(
                                                        "Back to Home",
                                                        href="/",
                                                        style={"color": "#fff"},
                                                    )
                                                ),
                                            ],
                                            xs=12,
                                            sm=3,
                                            md=4,
                                            lg=4,
                                            xl=4,
                                            style={
                                                "text-align": "left",
                                                "margin-bottom": "10px",
                                            },
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Row(
                                                    html.H2(
                                                        "Type A Dashboard",
                                                        style={
                                                            "border": "2px solid #20354b",
                                                            "border-radius": "25px",
                                                            "background": "#2b4664",
                                                        },
                                                    ),
                                                    style={"text-align": "center"},
                                                ),
                                            ],
                                            xs=12,
                                            sm=6,
                                            md=4,
                                            lg=4,
                                            xl=4,
                                        ),
                                        dbc.Col(
                                            [
                                                html.Img(
                                                    src="/assets/dash.png",
                                                    style={
                                                        "border-radius": "10px",
                                                        "border": "2px solid #D3D3D3",
                                                        "background": "#fff",
                                                        "width": "100%",
                                                    },
                                                ),
                                            ],
                                            xs=12,
                                            sm={"size": 2, "offset": 1},
                                            md={"size": 1, "offset": 3},
                                            lg={"size": 1, "offset": 3},
                                            xl={"size": 1, "offset": 3},
                                            style={
                                                "text-align": "right",
                                                "margin-bottom": "10px",
                                                "margin-top": "0px",
                                            },
                                        ),
                                    ],
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.Col(
                                                [
                                                    dbc.Row(
                                                        type_a_drop,
                                                        style={
                                                            "margin-bottom": "10px",
                                                            "width": "100%",
                                                        },
                                                    ),
                                                    dbc.Row(
                                                        type_a_date_picker,
                                                        style={
                                                            "margin-bottom": "10px",
                                                            "width": "100%",
                                                        },
                                                    ),
                                                ],
                                                xs=12,
                                                sm="auto",
                                                md="auto",
                                                lg="auto",
                                                xl="auto",
                                                style={"padding": "0px"},
                                            ),
                                            xs=7,
                                            sm="auto",
                                            md=2,
                                            lg=2,
                                            xl=2,
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Button(
                                                    html.Img(
                                                        src="/assets/refresh.png",
                                                        style={
                                                            "height": "90%",
                                                            "width": "100%",
                                                        },
                                                    ),
                                                    color="light",
                                                    size="lg",
                                                    className="mr-1",
                                                    href="/charts",
                                                    external_link=True,
                                                    id="type_a-refresh-btn",
                                                ),
                                            ],
                                            align="center",
                                            xs=4,
                                            sm="auto",
                                            md={"size": 6, "offset": 1},
                                            lg={"size": 6, "offset": 1},
                                            xl={"size": 6, "offset": 1},
                                            style={
                                                "text-align": "center",
                                                "border-radius": "50%",
                                            },
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                                html.Div(
                                                                    id="type_a-lrate-label"
                                                                ),
                                                            ],
                                                            xs=9,
                                                            sm="auto",
                                                            md="auto",
                                                            lg="auto",
                                                            xl="auto",
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                html.Div(
                                                                    id="type_a-lrate"
                                                                ),
                                                            ],
                                                            xs=3,
                                                            sm=4,
                                                            md=2,
                                                            lg=2,
                                                            xl=2,
                                                        ),
                                                    ],
                                                    style={"padding-top": "0px"},
                                                    justify="end",
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                                html.Div(
                                                                    id="type_a-composition_1-label"
                                                                ),
                                                            ],
                                                            xs=9,
                                                            sm="auto",
                                                            md="auto",
                                                            lg="auto",
                                                            xl="auto",
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                html.Div(
                                                                    id="type_a-composition_1"
                                                                ),
                                                            ],
                                                            xs=3,
                                                            sm=4,
                                                            md=2,
                                                            lg=2,
                                                            xl=2,
                                                        ),
                                                    ],
                                                    justify="end",
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                                html.Div(
                                                                    id="type_a-composition_2-label"
                                                                ),
                                                            ],
                                                            xs=9,
                                                            sm="auto",
                                                            md="auto",
                                                            lg="auto",
                                                            xl="auto",
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                html.Div(
                                                                    id="type_a-composition_2"
                                                                ),
                                                            ],
                                                            xs=3,
                                                            sm=4,
                                                            md=2,
                                                            lg=2,
                                                            xl=2,
                                                        ),
                                                    ],
                                                    justify="end",
                                                ),
                                            ],
                                            xs=12,
                                            sm="auto",
                                            md=3,
                                            lg=3,
                                            xl=3,
                                        ),
                                    ],
                                    justify="between",
                                    style={"vertical-align": "middle"},
                                ),
                            ],
                            className="card text-white bg-primary mb-3",
                        ),
                    ),
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Row(
                                dbc.Col(
                                    type_a_gas_tag_drop, xs=12, sm=6, md=4, lg=4, xl=4,
                                ),
                                style={"margin-bottom": "10px"},
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [dcc.Graph(id="type_a-gas-graph"),],
                                        xs=12,
                                        sm=12,
                                        md=10,
                                        lg=10,
                                        xl=10,
                                        style={"margin-bottom": "10px"},
                                    ),
                                    dbc.Col(
                                        [
                                            dbc.Col(
                                                html.H5(html.U("Current Values:")),
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                                style={"margin-bottom": "10px"},
                                            ),
                                            dbc.Col(
                                                id="type_a-gas-values",
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                            ),
                                        ],
                                        xs=12,
                                        sm=12,
                                        md=2,
                                        lg=2,
                                        xl=2,
                                        style={"padding": "0px"},
                                    ),
                                ],
                                style={"margin-bottom": "10px"},
                            ),
                        ],
                        xs=12,
                        sm=12,
                        md=6,
                        lg=6,
                        xl=6,
                    ),
                    dbc.Col(
                        [
                            dbc.Row(
                                dbc.Col(
                                    type_a_psi_tag_drop, xs=12, sm=6, md=4, lg=4, xl=4,
                                ),
                                style={"margin-bottom": "10px"},
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [dcc.Graph(id="type_a-psi-graph"),],
                                        xs=12,
                                        sm=12,
                                        md=10,
                                        lg=10,
                                        xl=10,
                                        style={"margin-bottom": "10px"},
                                    ),
                                    dbc.Col(
                                        [
                                            dbc.Col(
                                                html.H5(html.U("Current Values:")),
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                                style={"margin-bottom": "10px"},
                                            ),
                                            dbc.Col(
                                                id="type_a-psi-values",
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                            ),
                                        ],
                                        xs=12,
                                        sm=12,
                                        md=2,
                                        lg=2,
                                        xl=2,
                                        style={"padding": "0px"},
                                    ),
                                ],
                                style={"margin-bottom": "10px"},
                            ),
                        ],
                        xs=12,
                        sm=12,
                        md=6,
                        lg=6,
                        xl=6,
                    ),
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Row(
                                dbc.Col(
                                    type_a_product_tag_drop,
                                    xs=12,
                                    sm=6,
                                    md=4,
                                    lg=4,
                                    xl=4,
                                ),
                                style={"margin-bottom": "10px"},
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [dcc.Graph(id="type_a-product-graph"),],
                                        xs=12,
                                        sm=12,
                                        md=10,
                                        lg=10,
                                        xl=10,
                                        style={"margin-bottom": "10px"},
                                    ),
                                    dbc.Col(
                                        [
                                            dbc.Col(
                                                html.H5(html.U("Current Values:")),
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                                style={"margin-bottom": "10px"},
                                            ),
                                            dbc.Col(
                                                id="type_a-product-values",
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                            ),
                                        ],
                                        xs=12,
                                        sm=12,
                                        md=2,
                                        lg=2,
                                        xl=2,
                                        style={"padding": "0px"},
                                    ),
                                ],
                                style={"margin-bottom": "10px"},
                            ),
                        ],
                        xs=12,
                        sm=12,
                        md=6,
                        lg=6,
                        xl=6,
                    ),
                    dbc.Col(
                        [
                            dbc.Row(
                                dbc.Col(
                                    type_a_tank_tag_drop, xs=12, sm=6, md=4, lg=4, xl=4,
                                ),
                                style={"margin-bottom": "10px"},
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [dcc.Graph(id="type_a-tank-graph"),],
                                        xs=12,
                                        sm=12,
                                        md=10,
                                        lg=10,
                                        xl=10,
                                        style={"margin-bottom": "10px"},
                                    ),
                                    dbc.Col(
                                        [
                                            dbc.Col(
                                                html.H5(html.U("Current Values:")),
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                                style={"margin-bottom": "10px"},
                                            ),
                                            dbc.Col(
                                                id="type_a-tank-values",
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                            ),
                                        ],
                                        xs=12,
                                        sm=12,
                                        md=2,
                                        lg=2,
                                        xl=2,
                                        style={"padding": "0px"},
                                    ),
                                ],
                                style={"margin-bottom": "10px"},
                            ),
                        ],
                        xs=12,
                        sm=12,
                        md=6,
                        lg=6,
                        xl=6,
                    ),
                ],
            ),
        ],
        fluid=True,
    ),
)

type_b_tab = (
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Card(
                        dbc.CardBody(
                            [
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                dbc.Row(
                                                    dcc.Link(
                                                        "Back to Home",
                                                        href="/",
                                                        style={"color": "#fff"},
                                                    )
                                                ),
                                            ],
                                            xs=12,
                                            sm=3,
                                            md=4,
                                            lg=4,
                                            xl=4,
                                            style={
                                                "text-align": "left",
                                                "margin-bottom": "10px",
                                            },
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Row(
                                                    html.H2(
                                                        "Compressor Station Dashboard",
                                                        style={
                                                            "border": "2px solid #20354b",
                                                            "border-radius": "25px",
                                                            "background": "#2b4664",
                                                        },
                                                    ),
                                                    style={"text-align": "center"},
                                                ),
                                            ],
                                            xs=12,
                                            sm=6,
                                            md=4,
                                            lg=4,
                                            xl=4,
                                        ),
                                        dbc.Col(
                                            [
                                                html.Img(
                                                    src="/assets/dash.png",
                                                    style={
                                                        "border-radius": "10px",
                                                        "border": "2px solid #D3D3D3",
                                                        "background": "#fff",
                                                        "width": "100%",
                                                    },
                                                ),
                                            ],
                                            xs=12,
                                            sm={"size": 2, "offset": 1},
                                            md={"size": 1, "offset": 3},
                                            lg={"size": 1, "offset": 3},
                                            xl={"size": 1, "offset": 3},
                                            style={
                                                "text-align": "right",
                                                "margin-bottom": "10px",
                                                "margin-top": "0px",
                                            },
                                        ),
                                    ],
                                    justify="between",
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.Col(
                                                [
                                                    dbc.Row(
                                                        type_b_drop,
                                                        style={
                                                            "margin-bottom": "10px",
                                                            "width": "100%",
                                                        },
                                                    ),
                                                    dbc.Row(
                                                        type_b_date_picker,
                                                        style={
                                                            "margin-bottom": "10px",
                                                            "width": "100%",
                                                        },
                                                    ),
                                                ],
                                                xs=12,
                                                sm="auto",
                                                md="auto",
                                                lg="auto",
                                                xl="auto",
                                                style={"padding": "0px"},
                                            ),
                                            xs=7,
                                            sm="auto",
                                            md=2,
                                            lg=2,
                                            xl=2,
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Button(
                                                    html.Img(
                                                        src="/assets/refresh.png",
                                                        style={
                                                            "height": "90%",
                                                            "width": "100%",
                                                        },
                                                    ),
                                                    color="light",
                                                    size="lg",
                                                    className="mr-1",
                                                    href="/charts",
                                                    external_link=True,
                                                    id="type_a-refresh-btn",
                                                ),
                                            ],
                                            align="center",
                                            xs=4,
                                            sm="auto",
                                            md={"size": 6, "offset": 1},
                                            lg={"size": 6, "offset": 1},
                                            xl={"size": 6, "offset": 1},
                                            style={
                                                "text-align": "center",
                                                "border-radius": "50%",
                                            },
                                        ),
                                        dbc.Col(
                                            [
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                                html.Div(
                                                                    id="type_b-lrate-label"
                                                                ),
                                                            ],
                                                            xs=9,
                                                            sm="auto",
                                                            md="auto",
                                                            lg="auto",
                                                            xl="auto",
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                html.Div(
                                                                    id="type_b-lrate"
                                                                ),
                                                            ],
                                                            xs=3,
                                                            sm=4,
                                                            md=2,
                                                            lg=2,
                                                            xl=2,
                                                        ),
                                                    ],
                                                    style={"padding-top": "0px"},
                                                    justify="end",
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                                html.Div(
                                                                    id="type_b-composition_1-label"
                                                                ),
                                                            ],
                                                            xs=9,
                                                            sm="auto",
                                                            md="auto",
                                                            lg="auto",
                                                            xl="auto",
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                html.Div(
                                                                    id="type_b-composition_1"
                                                                ),
                                                            ],
                                                            xs=3,
                                                            sm=4,
                                                            md=2,
                                                            lg=2,
                                                            xl=2,
                                                        ),
                                                    ],
                                                    justify="end",
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                                html.Div(
                                                                    id="type_b-cont-alarm-label"
                                                                ),
                                                            ],
                                                            xs=9,
                                                            sm="auto",
                                                            md="auto",
                                                            lg="auto",
                                                            xl="auto",
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                html.Div(
                                                                    id="type_b-cont-alarm"
                                                                ),
                                                            ],
                                                            xs=3,
                                                            sm=4,
                                                            md=2,
                                                            lg=2,
                                                            xl=2,
                                                        ),
                                                    ],
                                                    justify="end",
                                                ),
                                            ],
                                            xs=12,
                                            sm="auto",
                                            md=3,
                                            lg=3,
                                            xl=3,
                                        ),
                                    ],
                                    justify="between",
                                    style={"vertical-align": "middle"},
                                ),
                            ],
                            className="card text-white bg-primary mb-3",
                        ),
                    ),
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Row(
                                dbc.Col(
                                    type_b_gas_tag_drop, xs=12, sm=6, md=4, lg=4, xl=4,
                                ),
                                style={"margin-bottom": "10px"},
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [dcc.Graph(id="type_b-gas-graph"),],
                                        xs=12,
                                        sm=12,
                                        md=10,
                                        lg=10,
                                        xl=10,
                                        style={"margin-bottom": "10px"},
                                    ),
                                    dbc.Col(
                                        [
                                            dbc.Col(
                                                html.H5(html.U("Current Values:")),
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                                style={"margin-bottom": "10px"},
                                            ),
                                            dbc.Col(
                                                id="type_b-gas-values",
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                            ),
                                        ],
                                        xs=12,
                                        sm=12,
                                        md=2,
                                        lg=2,
                                        xl=2,
                                        style={"padding": "0px"},
                                    ),
                                ],
                                style={"margin-bottom": "10px"},
                            ),
                        ],
                        xs=12,
                        sm=12,
                        md=6,
                        lg=6,
                        xl=6,
                    ),
                    dbc.Col(
                        [
                            dbc.Row(
                                dbc.Col(
                                    type_b_psi_tag_drop, xs=12, sm=6, md=4, lg=4, xl=4,
                                ),
                                style={"margin-bottom": "10px"},
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [dcc.Graph(id="type_b-psi-graph"),],
                                        xs=12,
                                        sm=12,
                                        md=10,
                                        lg=10,
                                        xl=10,
                                        style={"margin-bottom": "10px"},
                                    ),
                                    dbc.Col(
                                        [
                                            dbc.Col(
                                                html.H5(html.U("Current Values:")),
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                                style={"margin-bottom": "10px"},
                                            ),
                                            dbc.Col(
                                                id="type_b-psi-values",
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                            ),
                                        ],
                                        xs=12,
                                        sm=12,
                                        md=2,
                                        lg=2,
                                        xl=2,
                                        style={"padding": "0px"},
                                    ),
                                ],
                                style={"margin-bottom": "10px"},
                            ),
                        ],
                        xs=12,
                        sm=12,
                        md=6,
                        lg=6,
                        xl=6,
                    ),
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Row(
                                dbc.Col(
                                    type_b_product_tag_drop,
                                    xs=12,
                                    sm=6,
                                    md=4,
                                    lg=4,
                                    xl=4,
                                ),
                                style={"margin-bottom": "10px"},
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [dcc.Graph(id="type_b-product-graph"),],
                                        xs=12,
                                        sm=12,
                                        md=10,
                                        lg=10,
                                        xl=10,
                                        style={"margin-bottom": "10px"},
                                    ),
                                    dbc.Col(
                                        [
                                            dbc.Col(
                                                html.H5(html.U("Current Values:")),
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                                style={"margin-bottom": "10px"},
                                            ),
                                            dbc.Col(
                                                id="type_b-product-values",
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                            ),
                                        ],
                                        xs=12,
                                        sm=12,
                                        md=2,
                                        lg=2,
                                        xl=2,
                                        style={"padding": "0px"},
                                    ),
                                ],
                                style={"margin-bottom": "10px"},
                            ),
                        ],
                        xs=12,
                        sm=12,
                        md=6,
                        lg=6,
                        xl=6,
                    ),
                    dbc.Col(
                        [
                            dbc.Row(
                                dbc.Col(
                                    type_b_water_tag_drop,
                                    xs=12,
                                    sm=6,
                                    md=4,
                                    lg=4,
                                    xl=4,
                                ),
                                style={"margin-bottom": "10px"},
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [dcc.Graph(id="type_b-water-graph"),],
                                        xs=12,
                                        sm=12,
                                        md=10,
                                        lg=10,
                                        xl=10,
                                        style={"margin-bottom": "10px"},
                                    ),
                                    dbc.Col(
                                        [
                                            dbc.Col(
                                                html.H5(html.U("Current Values:")),
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                                style={"margin-bottom": "10px"},
                                            ),
                                            dbc.Col(
                                                id="type_b-water-values",
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=12,
                                                xl=12,
                                            ),
                                        ],
                                        xs=12,
                                        sm=12,
                                        md=2,
                                        lg=2,
                                        xl=2,
                                        style={"padding": "0px"},
                                    ),
                                ],
                                style={"margin-bottom": "10px"},
                            ),
                        ],
                        xs=12,
                        sm=12,
                        md=6,
                        lg=6,
                        xl=6,
                    ),
                ],
            ),
        ],
        fluid=True,
    ),
)


chart_page = html.Div(
    [
        dbc.Tabs(
            [dbc.Tab(type_a_tab, label="Type A"), dbc.Tab(type_b_tab, label="Type B"),],
        ),
        html.A(href="/charts"),
    ],
)
