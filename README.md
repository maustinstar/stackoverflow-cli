# Stack Overflow CLI

![Python 3.7](https://github.com/maustinstar/stackoverflow-cli/workflows/Lint%20and%20Test/badge.svg)

Browse Stack Overflow from your terminal. Look cool.

![screenshot of cli in action](images/screenshot.001.png)

## Getting Started

### Installing dependencies

`$ pip install beautifulsoup4 requests tox`

Or to install all dependencies, use:

`$ pip install -r requirements.txt`

### Building

Using Python 3.x, this command creates the stackoverflow package,
making `stackoverflow` and `so` executable.

`$ python setup.py develop`

### Testing

The tox command executes the test suite.

`$ tox`

## Usage

`$ stackoverflow <your search>`

OR shorthand:

`$ so <your search>`

## Flags

`-h, --help` help

`-l, --limit` limit number of search results

`-s, --sort` sort by relevance, newest, votes, or active
