import os
from pathlib import Path

TIME_FORMAT = "%Y-%m-%d %H_%M_%S.%f"


def devjournal_dir():
    if directory := os.getenv("DEVJOURNAL_DIR"):
        return Path(directory)
    return Path.home() / ".devjournal"


def entries_directory():
    return devjournal_dir() / "entries"
