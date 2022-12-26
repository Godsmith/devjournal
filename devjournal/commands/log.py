from devjournal.entry import get_entries


def log():
    for entry in get_entries():
        print(entry)
