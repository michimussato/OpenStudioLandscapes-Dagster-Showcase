<!-- TOC -->
* [Openstudiolandscapes-Dagster-Showcase](#openstudiolandscapes-dagster-showcase)
  * [Getting started](#getting-started)
  * [Development](#development)
    * [Adding new Python dependencies](#adding-new-python-dependencies)
    * [Unit testing](#unit-testing)
    * [Schedules and sensors](#schedules-and-sensors)
<!-- TOC -->

---

# Openstudiolandscapes-Dagster-Showcase

This is a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/getting-started/create-new-project).

Dagster is a powerful automation (orchestration) platform
and it (if not explicitly disabled) comes with every
[OpenStudioLandscapes Landscape](https://github.com/michimussato/OpenStudioLandscapes).

This is a dummy showcase Dagster package for the 
[OpenStudioLandscapes-Dagster](https://github.com/michimussato/OpenStudioLandscapes-Dagster) Feature. 
It does nothing productive:

```mermaid
graph TB
    start([Start])
    file_found{File Found}
    create_file[Create File]
    delete_file[Delete File]
    
    start --> file_found 
    file_found -- Yes --> delete_file
    file_found -- No --> create_file
    
    create_file --> file_found
    delete_file --> file_found
```

However, the project implements Dagster sensors just to show that I can do it's
work autonously - without human interaction.

## Getting started

First, install your Dagster code location as a Python package. By using the --editable flag, pip will install your Python package in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.

```bash
pip install -e ".[dev]"
```

Then, start the Dagster UI web server:

```bash
dagster dev
```

Open http://localhost:3000 with your browser to see the project.

You can start writing assets in `openstudiolandscapes_dagster_showcase/assets.py`. The assets are automatically loaded into the Dagster code location as you define them.

## Development

### Adding new Python dependencies

You can specify new Python dependencies in `setup.py`.

### Unit testing

Tests are in the `openstudiolandscapes_dagster_showcase_tests` directory and you can run tests using `pytest`:

```bash
pytest openstudiolandscapes_dagster_showcase_tests
```

### Schedules and sensors

If you want to enable Dagster [Schedules](https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules) or [Sensors](https://docs.dagster.io/concepts/partitions-schedules-sensors/sensors) for your jobs, the [Dagster Daemon](https://docs.dagster.io/deployment/dagster-daemon) process must be running. This is done automatically when you run `dagster dev`.

Once your Dagster Daemon is running, you can start turning on schedules and sensors for your jobs.
