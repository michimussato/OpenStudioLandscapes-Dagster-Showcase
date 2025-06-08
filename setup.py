from setuptools import find_packages, setup

setup(
    name="openstudiolandscapes_dagster_showcase",
    packages=find_packages(exclude=["openstudiolandscapes_dagster_showcase_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
