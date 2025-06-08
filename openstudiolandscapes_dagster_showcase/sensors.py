import datetime
import tempfile

from dagster import (
    RunRequest,
    SensorResult,
    sensor,
    SensorEvaluationContext,
    AssetSelection,
    AutomationConditionSensorDefinition,
    DefaultSensorStatus,
)

import os
import json
import pathlib
import shutil

# from Deadline.dagster_job_processor import settings

from openstudiolandscapes_dagster_showcase.jobs import (
    # job_get_temp_dir,
    job_create_file,
    job_delete_file
)


TEMPFILE = pathlib.Path(tempfile.gettempdir(), "i_was_here")


@sensor(
    job=job_create_file,
    default_status=DefaultSensorStatus.RUNNING,
    minimum_interval_seconds=30,
)
def sensor_create_file(
        context: SensorEvaluationContext,
):
    # path_to_submission_files = pathlib.Path(settings.OUTPUT_ROOT)

    # previous_state = json.loads(context.cursor) if context.cursor else {}
    # current_state = {}

    runs_to_request = []

    context.log.info("Running sensor_create_file...")

    if not TEMPFILE.exists():

        context.log.info(f"TEMPFILE does not exist. Creating...")

        # # this is for older versions.
        # # once every folder has this file,
        # # this part can be removed
        # # with open(combine_dict_path, 'r+') as f:
        # #     combined_dict = json.load(f)
        # #
        # #     current_state[str(file_path)] = str(combine_dict_path)
        # #
        # #     # if the file is new or has been modified since the last run, add it to the request queue
        # #     # if file_path not in previous_state or previous_state[file_path] != last_modified:
        # #     if file_path not in previous_state:
        # #
        # #         context.log.info(f'Submission file is new: {file_path}...')
        #
        # runs_to_request.append(RunRequest(
        #     run_key=f"submit_synced_jobs_{str(file_path).replace(os.sep, '__')}",
        #     run_config={
        #         "ops": {
        #             "submit_job": {
        #                 "config": {
        #                     "filename": str(file_path),
        #                     "combine_dict_path": str(combine_dict_path),
        #                     # **request_config
        #                     }
        #                 }
        #             }
        #         }
        #     )
        # )
        #
        # # # This is just the Dagster Job, not the actual
        # # # submission to deadline.
        # # combined_dict['deadline_job_queued'] = True
        # #
        # # f.seek(0)  # rewind
        # # json.dump(combined_dict, f, ensure_ascii=False, indent=4)
        # # f.truncate()

    return SensorResult(
        run_requests=runs_to_request,
        # cursor=json.dumps(current_state),
    )


@sensor(
    job=job_delete_file,
    default_status=DefaultSensorStatus.RUNNING,
    minimum_interval_seconds=15,
)
def sensor_delete_file(
        context: SensorEvaluationContext,
):

    runs_to_request = []

    context.log.info("Running sensor_delete_file...")

    if TEMPFILE.exists():

        context.log.info(f"TEMPFILE exists. Deleting...")

        # runs_to_request.append(RunRequest(
        #     # whether or not a run will skip is based on the run_key that was assigned to previous ones
        #     run_key=f"ingested_jobs__{datetime.datetime.timestamp(datetime.datetime.now())}__{str(job_py).replace(os.sep, '__')}",
        #     run_config={
        #         "ops": {
        #             "read_job_py": {
        #                 "config": {
        #                     "filename": str(output_file),
        #                     }
        #                 }
        #             }
        #         }
        #     )
        # )

        # moves.append({'src': job_py, 'dst': output_file})

    # for i in moves:
    #     shutil.move(i['src'], i['dst'])

    return SensorResult(
        run_requests=runs_to_request,
    )


# Custom AutoMaterialize Sensor
# https://docs.dagster.io/concepts/assets/asset-auto-execution#auto-materialize-sensors
my_custom_auto_materialize_sensor = AutomationConditionSensorDefinition(
    "my_custom_auto_materialize_sensor",
    target=AssetSelection.all(include_sources=True),
    minimum_interval_seconds=15,
    default_status=DefaultSensorStatus.RUNNING,
)
