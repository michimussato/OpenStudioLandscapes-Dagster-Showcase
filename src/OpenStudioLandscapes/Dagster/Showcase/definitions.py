from dagster import Definitions, load_assets_from_modules

from src.OpenStudioLandscapes.Dagster.Showcase import assets  # noqa: TID252
from src.OpenStudioLandscapes.Dagster.Showcase.sensors import sensor_create_file, sensor_delete_file

all_assets = load_assets_from_modules([assets])

all_sensors = [sensor_create_file, sensor_delete_file]

defs = Definitions(
    assets=all_assets,
    sensors=all_sensors,
)
