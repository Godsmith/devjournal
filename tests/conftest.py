import pytest
from pytest import MonkeyPatch


@pytest.fixture(autouse=True)
def mock_home_directory(monkeypatch: MonkeyPatch, tmp_path):
    monkeypatch.setattr("devjournal.devjournal.HOME_DIRECTORY", tmp_path)
    return tmp_path
