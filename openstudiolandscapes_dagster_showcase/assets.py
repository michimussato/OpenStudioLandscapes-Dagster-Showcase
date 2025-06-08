import io
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
    # isinstance = context.instance
    # materialization
    # temp_dir_: str = tempfile.mkdtemp()
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

    if pathlib.Path(temp_dir, "i_was_here").exists():
        context.log.error(f"File {temp_dir} already exists")
        return temp_dir / "i_was_here"
    with open(temp_dir / "i_was_here", "w") as f:
        f.write("i_was_here")

    context.log.info(f"File created in {temp_dir.as_posix()}")

    return temp_dir / "i_was_here"


@asset(
    ins={
        "temp_dir": AssetIn(),
    }
)
def delete_file(
        context: AssetExecutionContext,
        temp_dir: pathlib.Path,
) -> bool:
    try:
        os.remove(temp_dir / "i_was_here")
    except FileNotFoundError as e:
        context.log.exception(f"File {temp_dir.as_posix()} not found.")
    context.log.info(f"File deleted from {temp_dir.as_posix()}")

    return True
