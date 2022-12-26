from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from .constants import devjournal_dir

TIME_FORMAT = "%Y-%m-%d %H_%M_%S.%f"
HOME_DIRECTORY = Path.home()


def entries_directory():
    return devjournal_dir() / "entries"


@dataclass
class Entry:
    datetime: datetime
    text: str

    def __str__(self):
        return f"{self.datetime}\n\n{self.text}"


def get_entries() -> list[Entry]:
    paths = entries_directory().glob("*")
    return [
        Entry(datetime.strptime(path.name, TIME_FORMAT), path.read_text())
        for path in paths
    ]


def add(text: str):
    entries_directory().mkdir(parents=True, exist_ok=True)
    now = datetime.now().strftime(TIME_FORMAT)
    entry_file = entries_directory() / now
    entry_file.write_text(text)


def log():
    for entry in get_entries():
        print(entry)


def find(words: list[str]):
    for entry in get_entries():
        if any(word in entry.text for word in words):
            print(entry)
