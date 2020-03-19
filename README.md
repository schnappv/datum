# `datum` v 0.0.5
Ingest and generate queries of large databases.

![](datum/doc/datum.png)

The repo is located [here](https://github.com/schnappv/datum)

## About
A package to ingest a large csv file into a SQLIte database, and return a 
pandas data frame of a specified query. This query must be a `sqlalchemy` 
select function, but can be converted easily from SQLite using the `sql` 
function. The `sql` function pulls from the `sqlitis` package which has been
pulled into this repository for usage outside of the command line.

More about the `sqlitis` package can be found [here](https://github.com/pglass/sqlitis).

## Quickstart

```bash
pip install -r requirements.txt

python setup.py install
```

## Usage



## Test

To run tests: 

```bash
py.test -v
```

If you're on Windows

```bash
python -m pytest -v
```

Note: the first time you test, it will take about a minute due to generating a database as it tests. After it is there, it will only take less than a second to test.

## Feature Requests and Bug Reporting

Please open an issue on GitHub.

## Authors

- [Valerie Schnapp](valerie.f.schnapp@gmail.com) - Repo Owner / Architect

__Sqlitis Author__: Paul Glass
