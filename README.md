# devjournal

Slick terminal-based journal for developers.


## Feature comparison

|                                        | devjournal           | Evernote           |
| -------------------------------------- | -------------------- | ------------------ |
| Creating, editing and deleting entries | :white_check_mark:   | :white_check_mark: |
| Closed source                          | :white_large_square: | :white_check_mark: |
| Data stored outside your control       | :white_large_square: | :white_check_mark: |
| Overly bloated and impractical CLI     | :white_large_square: | :white_check_mark: |


## Installation

```sh
pip install devjournal
```


## Optional configuration

### Directory

The default directory for storing configuration and journal entries is `~/.devjournal`.
This can be overridden with the `DEVJOURNAL_DIR` environment variable.

### Git synchronization

Optionally, run `dj setup` to specify a Git repo and branch to be used for syncing. 
It is required that 
- you have ssh access to the server,
- the repo has at least one commit already, and
- you have push rights on to the specified branch.

### Editor

If running on Windows, consider setting the environment variable `EDITOR` to an editor
of your choice, to make devjournal use that editor when editing journal entries.


## Usage

### Adding new journal entry

```sh
$ dj add
```

This command will open the entry in the editor specified by the environment variable 
`EDITOR`. If that variable is not set, it will use the `start` command instead, which 
on Windows opens the editor for .txt files (by default Notepad).

Alternatively, you can add the text of the entry directly on the command line:

```sh
$ dj add This is my journal entry
```


### Listing entries

#### Listing all entries

```sh
$ dj log
1 | 2022-12-25 16:15:56.536078 | add hello world
```

#### Listing only entries containing any of the search terms

```sh
$ dj find hello
1 | 2022-12-25 16:15:56.536078 | add hello world
```

### Editing entries

#### Editing a journal entry

```sh
$ dj edit 1
```

#### Amending the last journal entry

```sh
$ dj amend
```

#### Deleting a journal entry

```sh
$ dj delete 1
```


## Low-level control

Each run of `dj add` creates a new file in `~/.devjournal/entries`. In case of unexpected events, you can always edit the files and do git commands in that folder manually.


## Developing

```sh
# Setup pre-commit and pre-push hooks
hatch run pre-commit install -t pre-commit
hatch run pre-commit install -t pre-push
```

### Running tests

```sh
hatch run cov
```
