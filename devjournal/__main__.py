from typing import Optional

import typer

from .commands.add import add as add_command
from .commands.find import find as find_command
from .commands.log import log as log_command

app = typer.Typer()


@app.command()
def add(text: Optional[list[str]] = typer.Argument(None)):
    if text:
        add_command(" ".join(text))
    else:
        add_command()
    # TODO: Do a git pull --rebase and then git push here


@app.command()
def log():
    # TODO: Do a git pull --rebase here
    log_command()


@app.command()
def find(words: list[str]):
    # TODO: Do a git pull --rebase here
    find_command(words)


if __name__ == "__main__":
    app()
