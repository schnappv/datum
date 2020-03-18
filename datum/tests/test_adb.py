import logging
import sys
import os
from pathlib import Path

import time
import pytest
import numpy as np

from datum.create import create_db
from datum.access import Access, sql_a

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def data_loc(file_name):
    pardir = Path(__file__).parents[0]
    return os.path.join(pardir, file_name)


def test_generate_db(table_name):
    start = time.time()
    if not os.path.exists(data_loc("data.db")):
        logger.debug("This will take a minute...")
        create_db("athlete_events.csv", "data.db", table_name, data_loc)
        logger.debug("Database generated!")
    logger.debug("time: {:6.4f}".format(time.time() - start))

    assert os.path.exists(data_loc("data.db"))


def test_adb(file_path, table_name, my_query):
    start = time.time()
    a = Access(file_path, table_name)
    q = sql_a(my_query, a)
    results = a.query(db_query=q)
    logger.debug("time: {:6.4f}".format(time.time() - start))
    logger.debug("Sex: {}".format(results.iloc[0].Sex))

    assert np.all(results.Sex == "F")
