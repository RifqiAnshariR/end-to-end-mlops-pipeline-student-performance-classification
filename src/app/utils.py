from pathlib import Path
import shutil


def empty_temp_dir(dir_name: Path):
    for item in dir_name.iterdir():
        if item.name == ".gitkeep":
            continue

        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)
