from typer.testing import CliRunner

from devjournal.__main__ import app
from tests.conftest import MockPrintIdsAndEntries

runner = CliRunner()


def test_shows_all_entries(mock_print_ids_and_entries: MockPrintIdsAndEntries):
    runner.invoke(app, ["add", "hello", "world"], catch_exceptions=False)
    runner.invoke(app, ["add", "goodbye", "world"], catch_exceptions=False)

    runner.invoke(app, ["log"], catch_exceptions=False)

    entries = mock_print_ids_and_entries.entries
    assert len(entries) == 2
    assert entries[0].text == "hello world"
    assert entries[1].text == "goodbye world"


class TestGit:
    def test_pulls_before_if_config_file(
        self, config_file, mock_repo, mock_run_git_script
    ):
        result = runner.invoke(app, ["log"], catch_exceptions=False)
        assert result.exit_code == 0
        assert mock_repo.origin.pull_called
