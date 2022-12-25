# devjournal

**Table of Contents**

- [Installation](#installation)

## Installation

```sh
pip install devjournal
```

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

dj command installed with pyproject
tests
update readme
Filter for specific dates in log
sync with repo
