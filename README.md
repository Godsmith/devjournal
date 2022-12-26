# devjournal

**Table of Contents**

- [Installation](#installation)

## Installation

```sh
pip install devjournal
```

## Configuration

The default directory for storing configuration and journal entries is `~/.devjournal`.
This can be overridden with the `DEVJOURNAL_DIR` environment variable.

## Usage

### Adding new journal entry

```sh
$ dj add This is my journal entry
```
### Showing all entries

```sh
$ dj log
2022-12-25 16:15:56.536078

add hello world
```

### Show only entries containing any of the search terms

```sh
$ dj find hello
2022-12-25 16:15:56.536078

add hello world
```


## Development

```sh
# Setup pre-commit and pre-push hooks
hatch run pre-commit install -t pre-commit
hatch run pre-commit install -t pre-push
```

### Running tests

```sh
hatch run cov
```

## TODO

- tests
- update readme
- Filter for specific dates in log
- sync with repo
- use rich for better output colors
- use textual for better log browsing - type to filter?
- add with no arguments starts editor
- editing previous days
- make find nicer which textual. Low prio.
- Log and find should work like git log, opening on something like less if longer than a screen.
