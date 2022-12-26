import pytest
from pytest import MonkeyPatch


@pytest.fixture(autouse=True)
def mock_devjournal_dir(monkeypatch: MonkeyPatch, tmp_path):
    monkeypatch.setenv("DEVJOURNAL_DIR", tmp_path)
    return tmp_path
