import typer

from devjournal import devjournal

app = typer.Typer()


@app.command()
def add(text: list[str]):
    devjournal.add(" ".join(text))
    # TODO: Do a git pull --rebase and then git push here


@app.command()
def log():
    # TODO: Do a git pull --rebase here
    devjournal.log()


@app.command()
def find(words: list[str]):
    # TODO: Do a git pull --rebase here
    devjournal.find(words)


if __name__ == "__main__":
    app()
