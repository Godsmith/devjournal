from dataclasses import dataclass
from datetime import datetime

from devjournal.constants import TIME_FORMAT, entries_directory


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
