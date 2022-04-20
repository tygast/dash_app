import dash_bootstrap_components as dbc

from dash import html


home_page = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Container(
                    [
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src="/assets/mountains.jpg",
                                    top=True,
                                    style={"border-radius": "25px 25px 0px 0px"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Row(
                                            dbc.Col(
                                                dbc.Button(
                                                    "Trending Tool",
                                                    href="/charts",
                                                    style={
                                                        "background-color": "#4b7eb4",
                                                        "line-height": "1.2",
                                                        "width": "90%",
                                                        "padding": "0.975rem 0.75rem",
                                                    },
                                                ),
                                                xs=12,
                                                sm=12,
                                                md=12,
                                                lg=8,
                                                xl=8,
                                            ),
                                            style={
                                                "text-align": "center",
                                                "justify-content": "center",
                                                "margin-top": "25px",
                                                "margin-bottom": "25px",
                                            },
                                        ),
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dbc.Button(
                                                        "Area 1",
                                                        href="/area_1-page",
                                                        style={
                                                            "border-radius": "75px",
                                                            "height": "fit-content",
                                                            "width": "70%",
                                                            "line-height": "1.5",
                                                        },
                                                    ),
                                                    xs=10,
                                                    sm=8,
                                                    md=4,
                                                    lg=4,
                                                    xl=4,
                                                    style={
                                                        "text-align": "center",
                                                        "margin-bottom": "25px",
                                                        "vertical-align": "middle",
                                                    },
                                                ),
                                                dbc.Col(
                                                    dbc.Button(
                                                        "Area 2",
                                                        href="/area_2-page",
                                                        style={
                                                            "border-radius": "75px",
                                                            "height": "fit-content",
                                                            "width": "70%",
                                                            "line-height": "1.5",
                                                        },
                                                    ),
                                                    xs=10,
                                                    sm=8,
                                                    md=4,
                                                    lg=4,
                                                    xl=4,
                                                    style={
                                                        "text-align": "center",
                                                        "margin-bottom": "25px",
                                                        "vertical-align": "middle",
                                                    },
                                                ),
                                                dbc.Col(
                                                    dbc.Button(
                                                        "Area 3",
                                                        href="/area_3-page",
                                                        style={
                                                            "border-radius": "75px",
                                                            "height": "fit-content",
                                                            "width": "70%",
                                                            "line-height": "1.5",
                                                        },
                                                    ),
                                                    xs=10,
                                                    sm=8,
                                                    md=4,
                                                    lg=4,
                                                    xl=4,
                                                    style={
                                                        "text-align": "center",
                                                        "margin-bottom": "25px",
                                                        "vertical-align": "middle",
                                                    },
                                                ),
                                            ],
                                            justify="center",
                                        ),
                                    ],
                                ),
                            ],
                            id="home-page",
                            style={
                                "text-align": "left",
                                "border-radius": "25px",
                                "margin-top": "30px",
                            },
                            className="card text-white bg-primary mb-3",
                        ),
                        html.A(href="/"),
                    ],
                    fluid=True,
                ),
            ],
            xs=12,
            sm=12,
            md=8,
            lg=8,
            xl=8,
        ),
    ],
    justify="center",
)
