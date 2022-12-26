from datetime import datetime

from devjournal.constants import TIME_FORMAT, entries_directory


def add(text: str):
    entries_directory().mkdir(parents=True, exist_ok=True)
    now = datetime.now().strftime(TIME_FORMAT)
    entry_file = entries_directory() / now
    entry_file.write_text(text)
