from dagster import Definitions, load_assets_from_modules

from openstudiolandscapes_dagster_showcase import assets  # noqa: TID252
from openstudiolandscapes_dagster_showcase.sensors import sensor_create_file, sensor_delete_file

all_assets = load_assets_from_modules([assets])

all_sensors = [sensor_create_file, sensor_delete_file]

defs = Definitions(
    assets=all_assets,
    sensors=all_sensors,
)
