import copy
import dash_bootstrap_components as dbc
import datetime as dt
import pandas as pd
import plotly.express as px

from dash import html, callback
from dash.dependencies import Input, Output

from configs.components import *
from data_tools.utilities.alter_table import get_location_data as get_data


@callback(
    Output("type_a-date-range", "start_date"),
    Output("type_a-date-range", "end_date"),
    [Input("type_a-date-range", "start_date"), Input("type_a-date-range", "end_date")],
)
def update_type_a_output(start_date, end_date):
    return start_date, end_date


@callback(
    Output("type_b-date-range", "start_date"),
    Output("type_b-date-range", "end_date"),
    [Input("type_b-date-range", "start_date"), Input("type_b-date-range", "end_date")],
)
def update_type_b_output(start_date, end_date):
    return start_date, end_date


@callback(
    [Output("type_a-gas-tags", "options"), Output("type_a-gas-tags", "value")],
    Input("type_a", "value"),
)
def select_type_a_gas_tags(type_a):
    all_tags = []
    for tag in GAS_TAGS:
        _item = {}

        _item["label"] = TYPE_A[type_a][tag][0]["name"].replace("_", " ").title()
        _item["value"] = TYPE_A[type_a][tag][0]["name"]

        all_tags.append(copy.deepcopy(_item))
    values = GAS_TAGS
    return all_tags, values


@callback(
    [Output("type_b-gas-tags", "options"), Output("type_b-gas-tags", "value")],
    Input("type_b", "value"),
)
def select_type_b_gas_tags(type_b):
    all_tags = []
    for tag in GAS_TAGS:
        _item = {}

        _item["label"] = TYPE_B[type_b][tag][0]["name"].replace("_", " ").title()
        _item["value"] = TYPE_B[type_b][tag][0]["name"]

        all_tags.append(copy.deepcopy(_item))
    values = GAS_TAGS
    return all_tags, values


@callback(
    [Output("type_a-psi-tags", "options"), Output("type_a-psi-tags", "value")],
    Input("type_a", "value"),
)
def select_type_a_psi_tags(type_a):
    all_tags = []
    for tag in PSI_TAGS:

        names = TYPE_A[type_a][tag][0]["name"]
        points = TYPE_A[type_a][tag][0]["tags"]
        _len = list(range(0, len(names)))
        for x in _len:
            _item = {}
            _item["label"] = names[x]
            _item["value"] = points[x]
            all_tags.append(copy.deepcopy(_item))
    values = [x.get("value") for x in all_tags]
    return all_tags, values


@callback(
    [Output("type_b-psi-tags", "options"), Output("type_b-psi-tags", "value")],
    Input("type_b", "value"),
)
def select_type_b_psi_tags(type_b):
    all_tags = []
    for tag in PSI_TAGS:

        names = TYPE_B[type_b][tag][0]["name"]
        points = TYPE_B[type_b][tag][0]["tags"]
        _len = list(range(0, len(names)))
        for x in _len:
            _item = {}
            _item["label"] = names[x]
            _item["value"] = points[x]
            all_tags.append(copy.deepcopy(_item))
    values = [x.get("value") for x in all_tags]
    return all_tags, values


@callback(
    [Output("type_a-product-tags", "options"), Output("type_a-product-tags", "value")],
    Input("type_a", "value"),
)
def select_type_a_product_tags(type_a):
    all_tags = []
    for tag in PRODUCT_TAGS:

        points = TYPE_A[type_a][tag][0]["tags"]
        _len = list(range(0, len(points)))
        for x in _len:
            _item = {}
            _item["label"] = f"Tank {x+1}"
            _item["value"] = points[x]
            all_tags.append(copy.deepcopy(_item))
    values = [x.get("value") for x in all_tags]
    return all_tags, values


@callback(
    [Output("type_b-product-tags", "options"), Output("type_b-product-tags", "value")],
    Input("type_b", "value"),
)
def select_type_b_product_tags(type_b):
    all_tags = []
    for tag in PRODUCT_TAGS:

        points = TYPE_B[type_b][tag][0]["tags"]
        _len = list(range(0, len(points)))
        for x in _len:
            _item = {}
            _item["label"] = f"Tank {x+1}"
            _item["value"] = points[x]
            all_tags.append(copy.deepcopy(_item))
    values = [x.get("value") for x in all_tags]
    return all_tags, values


@callback(
    [Output("type_a-tank-tags", "options"), Output("type_a-tank-tags", "value")],
    Input("type_a", "value"),
)
def select_type_a_tank_tags(type_a):
    all_tags = []
    for tag in TANK_TAGS:

        points = TYPE_A[type_a][tag][0]["tags"]
        labels = {
            "TAG6101": "Product Tank 1",
            "TAG6103": "Water Tank 1",
            "TAG6102": "Product Tank 2",
            "TAG6104": "Water Tank 2",
        }
        _len = list(range(0, len(points)))
        for x in _len:
            _item = {}
            _item["label"] = labels[points[x]]
            _item["value"] = points[x]
            all_tags.append(copy.deepcopy(_item))
    values = [x.get("value") for x in all_tags if "Water" not in x.get("label")]
    return all_tags, values


@callback(
    [Output("type_b-water-tags", "options"), Output("type_b-water-tags", "value")],
    Input("type_b", "value"),
)
def select_type_b_water_tags(type_b):
    all_tags = []
    for tag in WATER_TAGS:

        points = TYPE_B[type_b][tag][0]["tags"]
        _len = list(range(0, len(points)))
        for x in _len:
            _item = {}
            _item["label"] = f"Tank {x+1}"
            _item["value"] = points[x]
            all_tags.append(copy.deepcopy(_item))
    values = [x.get("value") for x in all_tags]
    return all_tags, values


@callback(
    Output("type_a-gas-graph", "figure"),
    Input("type_a", "value"),
    Input("type_a-gas-tags", "value"),
    Input("type_a-date-range", "start_date"),
    Input("type_a-date-range", "end_date"),
)
def update_type_a_gas_chart(type_a, tagname, start_date, end_date):

    tags = [TYPE_A[type_a][tag][0]["tags"] for tag in tagname]
    columns = [TYPE_A[type_a][tag][0]["name"] for tag in tagname]
    df = get_data(type_a, tags, columns, start_date, end_date, trucked="NO").squeeze()
    fig = px.line(
        df,
        labels={"variable": "Legend:", "value": "scf", "x": "Datetime"},
        title=f"{type_a} Gas Volume",
        template="plotly_dark",
    )
    fig.update_layout(
        hovermode="x unified", legend=dict(yanchor="top", y=1.3, xanchor="right", x=1.1)
    )
    return fig


@callback(
    Output("type_a-gas-values", "children"),
    Input("type_a", "value"),
    Input("type_a-gas-tags", "options"),
)
def get_type_a_gas_current_values(type_a, options):

    tags = [TYPE_A[type_a][tag["value"]][0]["tags"] for tag in options]
    columns = [TYPE_A[type_a][tag["value"]][0]["name"].title() for tag in options]
    end_date = dt.datetime.today()
    start_date = end_date - dt.timedelta(minutes=5)
    df = get_data(type_a, tags, columns, start_date, end_date, trucked="NO").squeeze()
    current_values = df.iloc[-1].to_dict()
    return dbc.Row(
        [
            dbc.Col(
                [f"{k}: ", dbc.Badge(f"{v:.2f} SCF", color="info", className="mr-1")],
                xs="auto",
                sm="auto",
                md=12,
                lg=12,
                xl=12,
                style={"padding-right": "0px"},
            )
            for k, v in current_values.items()
        ]
    )


@callback(
    Output("type_b-gas-graph", "figure"),
    Input("type_b", "value"),
    Input("type_b-gas-tags", "value"),
    Input("type_b-date-range", "start_date"),
    Input("type_b-date-range", "end_date"),
)
def update_type_b_gas_chart(type_b, tagname, start_str, end_str):

    tags = [TYPE_B[type_b][tag][0]["tags"] for tag in tagname]
    columns = [TYPE_B[type_b][tag][0]["name"] for tag in tagname]
    try:
        start_date = dt.datetime.strptime(
            start_str.replace("T", " ").split(".")[0], "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        start_date = dt.datetime.strptime(start_str + " 00:00:00", "%Y-%m-%d %H:%M:%S")
    try:
        end_date = dt.datetime.strptime(
            end_str.replace("T", " ").split(".")[0], "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        end_date = dt.datetime.strptime(end_str + " 00:00:00", "%Y-%m-%d %H:%M:%S")
    df = get_data(type_b, tags, columns, start_date, end_date, trucked="NO").squeeze()

    start_zeros = dt.datetime.today() + dt.timedelta(minutes=1)
    if isinstance(df, pd.DataFrame):
        for col in df:
            df.loc[df.index >= start_zeros, col] = 0
    else:
        df.loc[df.index >= start_zeros] = 0

    fig = px.line(
        df,
        labels={"variable": "Legend:", "value": "MMscf", "x": "Datetime"},
        title=f"{type_b} Gas Volume",
        template="plotly_dark",
    )
    fig.update_layout(
        hovermode="x unified", legend=dict(yanchor="top", y=1.3, xanchor="right", x=1.1)
    )
    return fig


@callback(
    Output("type_b-gas-values", "children"),
    Input("type_b", "value"),
    Input("type_b-gas-tags", "options"),
)
def get_type_b_gas_current_values(type_b, options):

    tags = [TYPE_B[type_b][tag["value"]][0]["tags"] for tag in options]
    columns = [TYPE_B[type_b][tag["value"]][0]["name"].title() for tag in options]
    end_date = dt.datetime.today() - dt.timedelta(minutes=1)
    start_date = end_date - dt.timedelta(minutes=5)
    df = get_data(type_b, tags, columns, start_date, end_date, trucked="NO").squeeze()
    current_values = df.iloc[-1].to_dict()
    return dbc.Row(
        [
            dbc.Col(
                [f"{k}: ", dbc.Badge(f"{v:.2f} SCF", color="info", className="mr-1")],
                xs="auto",
                sm="auto",
                md=12,
                lg=12,
                xl=12,
                style={"padding-right": "0px"},
            )
            for k, v in current_values.items()
        ]
    )


@callback(
    Output("type_a-psi-graph", "figure"),
    Input("type_a", "value"),
    Input("type_a-psi-tags", "value"),
    Input("type_a-psi-tags", "options"),
    Input("type_a-date-range", "start_date"),
    Input("type_a-date-range", "end_date"),
)
def update_type_a_psi_chart(type_a, tags, options, start_date, end_date):
    tags = [[tag] for tag in tags]
    columns = []
    for tag in tags:

        columns.append([x.get("label") for x in options if x.get("value") == tag[0]])
    df = get_data(
        type_a, tags, columns, start_date, end_date, trucked="NO", sum_values=False
    ).squeeze()
    fig = px.line(
        df,
        labels={"variable": "Legend:", "value": "PSI", "x": "Datetime"},
        title=f"{type_a} Pressure Trend",
        template="plotly_dark",
    )
    fig.update_layout(
        hovermode="x unified", legend=dict(yanchor="top", y=1.3, xanchor="right", x=1.1)
    )
    return fig


@callback(
    Output("type_a-psi-values", "children"),
    Input("type_a", "value"),
    Input("type_a-psi-tags", "options"),
)
def get_type_a_psi_current_values(type_a, options):

    tags = [tag["value"] for tag in options]
    columns = [tag["label"].title() for tag in options]
    end_date = dt.datetime.today()
    start_date = end_date - dt.timedelta(minutes=5)
    df = get_data(type_a, tags, columns, start_date, end_date, trucked="NO").squeeze()
    current_values = df.iloc[-1].to_dict()
    return dbc.Row(
        [
            dbc.Col(
                [f"{k}: ", dbc.Badge(f"{v:.2f} psi", color="info", className="mr-1")],
                xs="auto",
                sm="auto",
                md=12,
                lg=12,
                xl=12,
                style={"padding-right": "0px"},
            )
            for k, v in current_values.items()
        ]
    )


@callback(
    Output("type_b-psi-graph", "figure"),
    Input("type_b", "value"),
    Input("type_b-psi-tags", "value"),
    Input("type_b-psi-tags", "options"),
    Input("type_b-date-range", "start_date"),
    Input("type_b-date-range", "end_date"),
)
def update_type_b_psi_chart(type_b, tags, options, start_str, end_str):
    tags = [[tag] for tag in tags]
    columns = []
    for tag in tags:

        columns.append([x.get("label") for x in options if x.get("value") == tag[0]])
    try:
        start_date = dt.datetime.strptime(
            start_str.replace("T", " ").split(".")[0], "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        start_date = dt.datetime.strptime(start_str + " 00:00:00", "%Y-%m-%d %H:%M:%S")
    try:
        end_date = dt.datetime.strptime(
            end_str.replace("T", " ").split(".")[0], "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        end_date = dt.datetime.strptime(end_str + " 00:00:00", "%Y-%m-%d %H:%M:%S")
    df = get_data(
        type_b, tags, columns, start_date, end_date, trucked="NO", sum_values=False
    ).squeeze()

    start_zeros = dt.datetime.today() + dt.timedelta(minutes=1)
    if isinstance(df, pd.DataFrame):
        for col in df:
            df.loc[df.index >= start_zeros, col] = 0
    else:
        df.loc[df.index >= start_zeros] = 0

    fig = px.line(
        df,
        labels={"variable": "Legend:", "value": "PSI", "x": "Datetime"},
        title=f"{type_b} Pressure Trend",
        template="plotly_dark",
    )
    fig.update_layout(
        hovermode="x unified", legend=dict(yanchor="top", y=1.3, xanchor="right", x=1.1)
    )
    return fig


@callback(
    Output("type_b-psi-values", "children"),
    Input("type_b", "value"),
    Input("type_b-psi-tags", "options"),
)
def get_type_b_psi_current_values(type_b, options):

    tags = [tag["value"] for tag in options]
    columns = [tag["label"].title() for tag in options]
    end_date = dt.datetime.today() - dt.timedelta(minutes=1)
    start_date = end_date - dt.timedelta(minutes=5)
    df = get_data(type_b, tags, columns, start_date, end_date, trucked="NO").squeeze()
    current_values = df.iloc[-1].to_dict()
    return dbc.Row(
        [
            dbc.Col(
                [f"{k}: ", dbc.Badge(f"{v:.2f} psi", color="info", className="mr-1")],
                xs="auto",
                sm="auto",
                md=12,
                lg=12,
                xl=12,
                style={"padding-right": "0px"},
            )
            for k, v in current_values.items()
        ]
    )


@callback(
    Output("type_a-product-graph", "figure"),
    Input("type_a", "value"),
    Input("type_a-product-tags", "value"),
    Input("type_a-product-tags", "options"),
    Input("type_a-date-range", "start_date"),
    Input("type_a-date-range", "end_date"),
)
def update_type_a_product_chart(type_a, tags, options, start_date, end_date):
    tags = [[tag] for tag in tags]
    columns = []
    for tag in tags:

        columns.append([x.get("label") for x in options if x.get("value") == tag[0]])
    df = get_data(
        type_a, tags, columns, start_date, end_date, trucked="NO", sum_values=False
    ).squeeze()
    fig = px.line(
        df,
        labels={"variable": "Legend:", "value": "gal", "x": "Datetime"},
        title=f"{type_a} Product Tank Volume",
        template="plotly_dark",
    )
    fig.update_layout(
        hovermode="x unified", legend=dict(yanchor="top", y=1.3, xanchor="right", x=1.1)
    )
    return fig


@callback(
    Output("type_a-product-values", "children"),
    Input("type_a", "value"),
    Input("type_a-product-tags", "options"),
)
def get_type_a_product_current_values(type_a, options):

    tags = [tag["value"] for tag in options]
    columns = [tag["label"].title() for tag in options]
    end_date = dt.datetime.today()
    start_date = end_date - dt.timedelta(minutes=5)
    df = get_data(type_a, tags, columns, start_date, end_date, trucked="NO").squeeze()
    current_values = df.iloc[-1].to_dict()
    return dbc.Row(
        [
            dbc.Col(
                [f"{k}: ", dbc.Badge(f"{v:.2f} gal", color="info", className="mr-1")],
                xs="auto",
                sm="auto",
                md=12,
                lg=12,
                xl=12,
                style={"padding-right": "0px"},
            )
            for k, v in current_values.items()
        ]
    )


@callback(
    Output("type_b-product-graph", "figure"),
    Input("type_b", "value"),
    Input("type_b-product-tags", "value"),
    Input("type_b-product-tags", "options"),
    Input("type_b-date-range", "start_date"),
    Input("type_b-date-range", "end_date"),
)
def update_type_b_product_chart(type_b, tags, options, start_str, end_str):
    tags = [[tag] for tag in tags]
    columns = []
    for tag in tags:

        columns.append([x.get("label") for x in options if x.get("value") == tag[0]])
    try:
        start_date = dt.datetime.strptime(
            start_str.replace("T", " ").split(".")[0], "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        start_date = dt.datetime.strptime(start_str + " 00:00:00", "%Y-%m-%d %H:%M:%S")
    try:
        end_date = dt.datetime.strptime(
            end_str.replace("T", " ").split(".")[0], "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        end_date = dt.datetime.strptime(end_str + " 00:00:00", "%Y-%m-%d %H:%M:%S")
    df = get_data(
        type_b, tags, columns, start_date, end_date, trucked="NO", sum_values=False
    ).squeeze()

    start_zeros = dt.datetime.today() + dt.timedelta(minutes=1)
    if isinstance(df, pd.DataFrame):
        for col in df:
            df.loc[df.index >= start_zeros, col] = 0
    else:
        df.loc[df.index >= start_zeros] = 0

    fig = px.line(
        df,
        labels={"variable": "Legend:", "value": "GAL", "x": "Datetime"},
        title=f"{type_b} Product Tank Volume ",
        template="plotly_dark",
    )
    fig.update_layout(
        hovermode="x unified", legend=dict(yanchor="top", y=1.3, xanchor="right", x=1.1)
    )
    return fig


@callback(
    Output("type_b-product-values", "children"),
    Input("type_b", "value"),
    Input("type_b-product-tags", "options"),
)
def get_type_b_product_current_values(type_b, options):

    tags = [tag["value"] for tag in options]
    columns = [tag["label"].title() for tag in options]
    end_date = dt.datetime.today() - dt.timedelta(minutes=1)
    start_date = end_date - dt.timedelta(minutes=5)
    df = get_data(type_b, tags, columns, start_date, end_date, trucked="NO").squeeze()
    current_values = df.iloc[-1].to_dict()
    return dbc.Row(
        [
            dbc.Col(
                [f"{k}: ", dbc.Badge(f"{v:.2f} GAL", color="info", className="mr-1")],
                xs="auto",
                sm="auto",
                md=12,
                lg=12,
                xl=12,
                style={"padding-right": "0px"},
            )
            for k, v in current_values.items()
        ]
    )


@callback(
    Output("type_a-tank-graph", "figure"),
    Input("type_a", "value"),
    Input("type_a-tank-tags", "value"),
    Input("type_a-tank-tags", "options"),
    Input("type_a-date-range", "start_date"),
    Input("type_a-date-range", "end_date"),
)
def update_type_a_tank_chart(type_a, tags, options, start_date, end_date):
    tags = [[tag] for tag in tags]
    columns = []
    for tag in tags:

        columns.append([x.get("label") for x in options if x.get("value") == tag[0]])
    df = get_data(
        type_a, tags, columns, start_date, end_date, trucked="NO", sum_values=False
    ).squeeze()
    fig = px.line(
        df,
        labels={"variable": "Legend:", "value": "Level %", "x": "Datetime"},
        title=f"{type_a} Tank Volume",
        template="plotly_dark",
    )
    fig.update_layout(
        hovermode="x unified", legend=dict(yanchor="top", y=1.3, xanchor="right", x=1.1)
    )
    return fig


@callback(
    Output("type_a-tank-values", "children"),
    Input("type_a", "value"),
    Input("type_a-tank-tags", "options"),
)
def get_type_a_tank_current_values(type_a, options):

    tags = [tag["value"] for tag in options]
    columns = [tag["label"].upper() for tag in options]
    end_date = dt.datetime.today()
    start_date = end_date - dt.timedelta(minutes=5)
    df = get_data(type_a, tags, columns, start_date, end_date, trucked="NO").squeeze()
    current_values = df.iloc[-1].to_dict()
    return dbc.Row(
        [
            dbc.Col(
                [f"{k}: ", dbc.Badge(f"{v:.2f} %", color="info", className="mr-1")],
                xs="auto",
                sm="auto",
                md=12,
                lg=12,
                xl=12,
                style={"padding-right": "0px"},
            )
            for k, v in current_values.items()
        ]
    )


@callback(
    Output("type_b-water-graph", "figure"),
    Input("type_b", "value"),
    Input("type_b-water-tags", "value"),
    Input("type_b-water-tags", "options"),
    Input("type_b-date-range", "start_date"),
    Input("type_b-date-range", "end_date"),
)
def update_type_b_water_chart(type_b, tags, options, start_str, end_str):
    tags = [[tag] for tag in tags]
    columns = []
    for tag in tags:

        columns.append([x.get("label") for x in options if x.get("value") == tag[0]])
    try:
        start_date = dt.datetime.strptime(
            start_str.replace("T", " ").split(".")[0], "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        start_date = dt.datetime.strptime(start_str + " 00:00:00", "%Y-%m-%d %H:%M:%S")
    try:
        end_date = dt.datetime.strptime(
            end_str.replace("T", " ").split(".")[0], "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        end_date = dt.datetime.strptime(end_str + " 00:00:00", "%Y-%m-%d %H:%M:%S")
    df = get_data(
        type_b, tags, columns, start_date, end_date, trucked="NO", sum_values=False
    ).squeeze()

    start_zeros = dt.datetime.today() + dt.timedelta(minutes=1)
    if isinstance(df, pd.DataFrame):
        for col in df:
            df.loc[df.index >= start_zeros, col] = 0
    else:
        df.loc[df.index >= start_zeros] = 0

    fig = px.line(
        df,
        labels={"variable": "Legend:", "value": "GAL", "x": "Datetime"},
        title=f"{type_b} Water Tank Volume",
        template="plotly_dark",
    )
    fig.update_layout(
        hovermode="x unified", legend=dict(yanchor="top", y=1.3, xanchor="right", x=1.1)
    )
    return fig


@callback(
    Output("type_b-water-values", "children"),
    Input("type_b", "value"),
    Input("type_b-water-tags", "options"),
)
def get_type_b_water_current_values(type_b, options):

    tags = [tag["value"] for tag in options]
    columns = [tag["label"].title() for tag in options]
    end_date = dt.datetime.today()
    start_date = end_date - dt.timedelta(minutes=5)
    df = get_data(type_b, tags, columns, start_date, end_date, trucked="NO").squeeze()
    current_values = df.iloc[-1].to_dict()
    return dbc.Row(
        [
            dbc.Col(
                [f"{k}: ", dbc.Badge(f"{v:.2f} GAL", color="info", className="mr-1")],
                xs="auto",
                sm="auto",
                md=12,
                lg=12,
                xl=12,
                style={"padding-right": "0px"},
            )
            for k, v in current_values.items()
        ]
    )


@callback(
    [Output("type_a-lrate-label", "children"), Output("type_a-lrate", "children")],
    Input("type_a", "value"),
)
def get_type_a_lrate(type_a):
    tags = TYPE_A[type_a][LIQUID_PRODUCT_FLOWRATE_TAGS][0]["tags"]
    columns = (
        TYPE_A[type_a][LIQUID_PRODUCT_FLOWRATE_TAGS][0]["name"]
        .replace("_", " ")
        .title()
    )
    end_date = dt.datetime.today() - dt.timedelta(minutes=1)
    start_date = end_date - dt.timedelta(minutes=5)
    df = get_data(type_a, tags, columns, start_date, end_date, trucked="NO").squeeze()
    current_value = df.iloc[-1]
    return (
        html.H5(f"{columns}: "),
        dbc.Badge(f"{current_value:.2f} gpm", className="ml-1"),
    )


@callback(
    [
        Output("type_a-composition_1-label", "children"),
        Output("type_a-composition_1", "children"),
    ],
    Input("type_a", "value"),
)
def get_type_a_composition_1(type_a):
    tags = TYPE_A[type_a][COMPOSITION_1][0]["tags"]
    columns = TYPE_A[type_a][COMPOSITION_1][0]["name"].replace("_", " ").title()
    end_date = dt.datetime.today() - dt.timedelta(minutes=1)
    start_date = end_date - dt.timedelta(minutes=5)
    df = get_data(type_a, tags, columns, start_date, end_date, trucked="NO").squeeze()
    current_value = df.iloc[-1]
    if current_value >= 5:
        badge_color = "danger"
    elif 2 < current_value < 5:
        badge_color = "warning"
    else:
        badge_color = "success"
    return (
        html.H5(f"{columns}: "),
        dbc.Badge(f"{current_value:.2f} ppm", color=badge_color, className="ml-1"),
    )


@callback(
    [
        Output("type_a-composition_2-label", "children"),
        Output("type_a-composition_2", "children"),
    ],
    Input("type_a", "value"),
)
def get_type_a_composition_2(type_a):
    tags = TYPE_A[type_a][COMPOSITION_2][0]["tags"]
    columns = TYPE_A[type_a][COMPOSITION_2][0]["name"].replace("_", " ").title()
    end_date = dt.datetime.today() - dt.timedelta(minutes=1)
    start_date = end_date - dt.timedelta(minutes=5)
    df = get_data(type_a, tags, columns, start_date, end_date, trucked="NO").squeeze()
    current_value = df.iloc[-1]
    if current_value >= 5:
        badge_color = "danger"
    elif 2 < current_value < 5:
        badge_color = "warning"
    else:
        badge_color = "success"
    return (
        html.H5(f"{columns}: "),
        dbc.Badge(f"{current_value:.2f} lbs", color=badge_color, className="ml-1"),
    )


@callback(
    [Output("type_b-lrate-label", "children"), Output("type_b-lrate", "children")],
    Input("type_b", "value"),
)
def get_type_b_lrate(type_b):
    tags = TYPE_B[type_b][LIQUID_PRODUCT_FLOWRATE_TAGS][0]["tags"]
    columns = (
        TYPE_B[type_b][LIQUID_PRODUCT_FLOWRATE_TAGS][0]["name"]
        .replace("_", " ")
        .title()
    )
    if tags == [""]:
        current_value = "N/A"

        header = html.H5(f"{columns}: {current_value}")
    else:
        end_date = dt.datetime.today()
        start_date = end_date - dt.timedelta(minutes=5)

        df = get_data(
            type_b, tags, columns, start_date, end_date, trucked="NO"
        ).squeeze()
        current_value = df.iloc[-1]
        header = (
            html.H5(f"{columns}: "),
            dbc.Badge(f"{current_value:.2f} gpm", className="ml-1"),
        )
    return header


@callback(
    [Output("type_b-alarm_1-label", "children"), Output("type_b-alarm_1", "children")],
    Input("type_b", "value"),
)
def get_type_b_alarm_1(type_b):
    tags = TYPE_B[type_b][ALARM_1][0]["tags"]
    columns = "Alarm 1 Sensor"
    if tags:
        end_date = dt.datetime.today() - dt.timedelta(minutes=1)
        start_date = end_date - dt.timedelta(minutes=5)
        df = get_data(
            type_b, tags, columns, start_date, end_date, trucked="NO"
        ).squeeze()
        current_value = df.iloc[-1]
    else:
        current_value = "N/A"
    badge_color = {
        "N/A": "light",
        "Off": "success",
        "Normal": "success",
        "On": "danger",
    }
    return (
        html.H5(f"{columns}: "),
        dbc.Badge(
            f"{current_value}", color=badge_color[current_value], className="mr-1"
        ),
    )


@callback(
    [Output("type_b-alarm_2-label", "children"), Output("type_b-alarm_2", "children")],
    Input("type_b", "value"),
)
def get_type_b_alarm_2(type_b):
    tags = TYPE_B[type_b][ALARM_2][0]["tags"]

    columns = "Alarm 2 Sensor"
    if tags:
        end_date = dt.datetime.today() - dt.timedelta(minutes=1)
        start_date = end_date - dt.timedelta(minutes=5)

        df = get_data(
            type_b, tags, columns, start_date, end_date, trucked="NO"
        ).squeeze()
        current_value = df.iloc[-1]
    else:
        current_value = "N/A"
    badge_color = {
        "N/A": "light",
        "Off": "success",
        "Normal": "success",
        "On": "danger",
    }
    return (
        html.H5(f"{columns}: "),
        dbc.Badge(
            f"{current_value}", color=badge_color[current_value], className="mr-1"
        ),
    )
