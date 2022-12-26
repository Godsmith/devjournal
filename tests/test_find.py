import re

from typer.testing import CliRunner

from devjournal.__main__ import app

runner = CliRunner()


def test_show_only_entries_with_the_search_string():
    runner.invoke(app, ["add", "hello", "world"], catch_exceptions=False)
    runner.invoke(app, ["add", "goodbye", "world"], catch_exceptions=False)

    result = runner.invoke(app, ["find", "hello"], catch_exceptions=False)

    expected_pattern2 = """20..-..-.. ..:..:.*

hello world
"""

    assert re.match(expected_pattern2, result.stdout)
