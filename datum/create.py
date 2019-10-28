import logging
import os
from pathlib import Path

import numpy as np
import pandas as pd
import sqlite3
import sqlalchemy as db

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def default_data_loc(file_name):
    """
    Locates the path of a file in the data folder

    Args:
        file_name (str): the name of a file in the data folder

    Returns:
        pardir
    """
    try:
        pardir = Path(__file__).parents[0]
        return os.path.join(pardir, "data", file_name)

    except (FileNotFoundError, NameError, Exception) as e:
        logger.error("{}: ".format(type(e)), exc_info=True)
        raise


def create_db(file_name, db_name, table_name, data_loc=default_data_loc):
    """
    Creates a SQLite3 database table from the exxcel file specified

    Args:
        file_name (str): the name of the excel file

        db_name (str): the name of the database

        table_name (str): the name of the database table

        data_loc (func): a function pointing to data path

    Returns:
        *None*
    """
    file_path = data_loc(file_name)
    new_path = data_loc(db_name)
    df = pd.read_csv(file_path)

    try:
        conn = sqlite3.connect(new_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        logger.debug("Database created.")

    except (
        FileNotFoundError,
        NameError,
        TypeError,
        ValueError,
        Exception
    ) as e:
        logger.error("{}: ".format(type(e)), exc_info=True)
        raise
