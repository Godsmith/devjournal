from devjournal.entry import get_entries


def find(words: list[str]):
    for entry in get_entries():
        if any(word in entry.text for word in words):
            print(entry)
