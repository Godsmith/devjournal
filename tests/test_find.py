from typer.testing import CliRunner

from devjournal.__main__ import app
from tests.conftest import MockPrintEntries

runner = CliRunner()


def test_show_only_entries_with_the_search_string(mock_print_entries: MockPrintEntries):
    runner.invoke(app, ["add", "hello", "world"], catch_exceptions=False)
    runner.invoke(app, ["add", "goodbye", "world"], catch_exceptions=False)

    runner.invoke(app, ["find", "hello"], catch_exceptions=False)

    entries = mock_print_entries.entries
    assert len(entries) == 1
    assert entries[0].text == "hello world"
