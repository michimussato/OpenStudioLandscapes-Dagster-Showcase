from dagster import (
    AssetSelection,
    define_asset_job,
)


# Asset Selections
asset_selection_create_file = AssetSelection.assets("temp_dir", "create_file")
asset_selection_delete_file = AssetSelection.assets("temp_dir", "delete_file")


job_create_file = define_asset_job(
    name="job_create_file",
    selection=asset_selection_create_file,
)


job_delete_file = define_asset_job(
    name="job_delete_file",
    selection=asset_selection_delete_file,
)
