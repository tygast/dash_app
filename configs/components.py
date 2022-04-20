# %%
import datetime as dt
import toml

from dash import dcc
from pathlib import Path

# %%
config_folder = Path(__file__).resolve().parents[1] / "configs"
config_file = config_folder / "config.toml"

with config_file.open() as f:
    configs = toml.load(f)

# %%
TYPE_A_LOCATIONS = [
    location
    for location in configs
    if configs[location]["connection_args"][0]["type"] == "connection_2"
]

TYPE_A = {}
for name in TYPE_A_LOCATIONS:
    TYPE_A[name] = configs[name]


TYPE_B_LOCATIONS = [
    location
    for location in configs
    if configs[location]["connection_args"][0]["type"] == "connection_1"
]

TYPE_B = {}
for name in TYPE_B_LOCATIONS:
    TYPE_B[name] = configs[name]

GAS_TAGS = ["inlet", "discharge", "fuel"]
PSI_TAGS = ["pipeline_pressure"]
PRODUCT_TAGS = ["product_tank_vol"]
WATER_TAGS = ["water_tank_vol"]
TANK_TAGS = ["tank_level", "tank_interface"]
LIQUID_PRODUCT_FLOWRATE_TAGS = "liquid_product_flowrate_flowrate"
ALARM_1 = "alarm_1"
ALARM_2 = "alarm_2"
COMPOSITION_1 = "composition_1"
COMPOSITION_2 = "composition_2"

AREA_1 = ["Location_A", "Location_B", "Location_C"]
AREA_2 = ["Location_D", "Location_E", "Location_F"]
AREA_3 = ["Location_G", "Location_H", "Location_I", "Location_J"]

TABLE_TAGS = [
    "inlet",
    "discharge",
    "fuel",
    "pipeline_pressure",
    "product_tank_vol",
    "water_tank_vol",
]
SPECIAL_TABLE_TAGS = [
    "inlet",
    "pipeline_pressure",
    "product_tank_vol",
    "water_tank_vol",
]


type_a_drop = (
    dcc.Dropdown(
        id="type_a",
        options=[
            {"label": k + " Location", "value": k} for k, v in TYPE_A_LOCATIONS.items()
        ],
        placeholder="Select a Location...",
        value="Location F",
    ),
)

type_b_drop = (
    dcc.Dropdown(
        id="type_b",
        options=[
            {"label": k.replace("_", " ") + " Location", "value": k}
            for k, v in TYPE_B_LOCATIONS.items()
        ],
        placeholder="Select a Location...",
        value="Location_A",
    ),
)

type_a_gas_tag_drop = (
    dcc.Dropdown(id="type_a-gas-tags", multi=True, placeholder="Select Tags...",),
)

type_b_gas_tag_drop = (
    dcc.Dropdown(id="type_b-gas-tags", multi=True, placeholder="Select Tags...",),
)

type_a_psi_tag_drop = (
    dcc.Dropdown(id="type_a-psi-tags", multi=True, placeholder="Select Tags...",),
)

type_b_psi_tag_drop = (
    dcc.Dropdown(id="type_b-psi-tags", multi=True, placeholder="Select Tags...",),
)

type_a_product_tag_drop = (
    dcc.Dropdown(id="type_a-product-tags", multi=True, placeholder="Select Tags...",),
)

type_b_product_tag_drop = (
    dcc.Dropdown(id="type_b-product-tags", multi=True, placeholder="Select Tags...",),
)

type_a_tank_tag_drop = (
    dcc.Dropdown(id="type_a-tank-tags", multi=True, placeholder="Select Tags...",),
)

type_b_water_tag_drop = (
    dcc.Dropdown(id="type_b-water-tags", multi=True, placeholder="Select Tags...",),
)

type_a_date_picker = dcc.DatePickerRange(
    id="type_a-date-range",
    start_date_placeholder_text="Start Date",
    end_date_placeholder_text="End Date",
    initial_visible_month=dt.datetime.today().replace(
        hour=0, minute=0, second=0, microsecond=0
    ),
    end_date=dt.datetime.today(),
    start_date=dt.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    - dt.timedelta(days=1),
)

type_b_date_picker = dcc.DatePickerRange(
    id="type_b-date-range",
    start_date_placeholder_text="Start Date",
    end_date_placeholder_text="End Date",
    initial_visible_month=dt.datetime.today().replace(
        hour=0, minute=0, second=0, microsecond=0
    ),
    end_date=dt.datetime.today(),
    start_date=dt.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    - dt.timedelta(days=1),
)
