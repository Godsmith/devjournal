import re

from typer.testing import CliRunner

from devjournal.__main__ import app

runner = CliRunner()


def test_file_is_created(mock_devjournal_dir):
    runner.invoke(app, ["add", "hello", "world"], catch_exceptions=False)

    entry_files = list(mock_devjournal_dir.glob("entries/*"))
    assert len(entry_files) == 1
    assert re.match("20..-..-.. .._.._.........", entry_files[0].name)


def test_text_is_added_to_entry_file(mock_devjournal_dir):
    runner.invoke(app, ["add", "hello", "world"], catch_exceptions=False)

    entry_files = list(mock_devjournal_dir.glob("entries/*"))
    assert "hello world" in entry_files[0].read_text()
