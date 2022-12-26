import re

from typer.testing import CliRunner

from devjournal.__main__ import app

runner = CliRunner()


def test_shows_all_entries():
    runner.invoke(app, ["add", "hello", "world"], catch_exceptions=False)
    runner.invoke(app, ["add", "goodbye", "world"], catch_exceptions=False)

    result = runner.invoke(app, ["log"], catch_exceptions=False)

    expected_pattern2 = """20..-..-.. ..:..:.*

hello world
20..-..-.. ..:..:.*

goodbye world
"""

    assert re.match(expected_pattern2, result.stdout)
