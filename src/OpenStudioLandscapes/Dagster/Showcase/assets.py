import os
import pathlib
import tempfile

from dagster import (
    asset,
    AssetIn,
    AssetExecutionContext,
)


@asset
def temp_dir(
        context: AssetExecutionContext,
) -> pathlib.Path:
    temp_dir_ = tempfile.gettempdir()
    context.log.info(f"Temp dir: {temp_dir_}")
    return pathlib.Path(temp_dir_)


@asset(
    ins={
        "temp_dir": AssetIn(),
    }
)
def create_file(
        context: AssetExecutionContext,
        temp_dir: pathlib.Path,
) -> pathlib.Path:

    i_was_here = pathlib.Path(temp_dir, "i_was_here")

    if i_was_here.exists():
        context.log.error(f"File {i_was_here.as_posix()} already exists")
        return i_was_here
    with open(i_was_here, encoding="utf-8", mode="w") as f:
        f.write("i_was_here")

    context.log.info(f"File {i_was_here.as_posix()} created.")

    return i_was_here


@asset(
    ins={
        "temp_dir": AssetIn(),
    }
)
def delete_file(
        context: AssetExecutionContext,
        temp_dir: pathlib.Path,
) -> None:

    i_was_here = pathlib.Path(temp_dir, "i_was_here")

    try:
        os.remove(i_was_here.as_posix())
    except FileNotFoundError as e:
        context.log.exception(f"File {i_was_here.as_posix()} not found.")

    context.log.info(f"File {i_was_here.as_posix()} deleted.")

    return None
