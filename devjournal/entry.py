from dataclasses import dataclass
from datetime import datetime

from rich import print
from rich.table import Table

from devjournal.constants import datetime_from_filename, entries_directory

TIME_FORMAT_FOR_PRINTING = "%Y-%m-%d %H:%M:%S"


@dataclass
class Entry:
    datetime: datetime
    text: str


def get_ids_and_entries() -> list[tuple[int, Entry]]:
    paths = entries_directory().glob("*.txt")
    return [
        (i, Entry(datetime_from_filename(path.name), path.read_text()))
        for i, path in enumerate(paths, 1)
    ]


def print_ids_and_entries(ids_and_entries: list[tuple[int, Entry]]):
    table = Table(show_header=False, show_edge=False, highlight=True)
    for i, entry in ids_and_entries:
        time = entry.datetime.strftime(TIME_FORMAT_FOR_PRINTING)
        table.add_row(str(i), time, entry.text)
    print(table)
