import pytest
from pytest import MonkeyPatch

import devjournal.entry
from devjournal.entry import Entry


class MockPrintEntries:
    def __call__(self, entries: list[Entry]):
        self.entries = entries


@pytest.fixture(autouse=True)
def mock_devjournal_dir(monkeypatch: MonkeyPatch, tmp_path):
    monkeypatch.setenv("DEVJOURNAL_DIR", str(tmp_path))
    return tmp_path


@pytest.fixture()
def mock_print_entries(monkeypatch: MonkeyPatch):

    return_value = MockPrintEntries()
    monkeypatch.setattr(devjournal.entry, "print_entries", return_value)

    return return_value
