from typer.testing import CliRunner

from devjournal.__main__ import app

runner = CliRunner()


def test_directory_is_created_automatically(mock_home_directory):
    runner.invoke(app, ["add", "hello", "world"], catch_exceptions=False)

    folders_in_home_directory = mock_home_directory.glob("*")
    folder_names_in_home_directory = [
        folder.name for folder in folders_in_home_directory
    ]
    assert folder_names_in_home_directory == [".devjournal"]


def test_text_is_added_to_entry_file(mock_home_directory):
    runner.invoke(app, ["add", "hello", "world"], catch_exceptions=False)

    files_in_entries_directory = list(
        (mock_home_directory / ".devjournal/entries").glob("*")
    )
    assert len(files_in_entries_directory) == 1
    assert "hello world" in files_in_entries_directory[0].read_text()
