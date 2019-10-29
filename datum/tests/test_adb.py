import logging
import sys
import os

import time
import pytest

from datum.access import AccessDataBase

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def test_adb(file_path, table_name, my_query):
    start = time.time()
    data_base = AccessDataBase(file_path, table_name)
    results = data_base.query(db_query=my_query)
    row = results.iloc[0]
    logger.debug("time: {:6.4f}".format(time.time() - start))
    logger.debug("Sex: {}".format(row.Sex))
    assert row.Sex == "F"


def test_exception(file_path, table_name, foo):
    with pytest.raises(TypeError):
        data_base = AccessDataBase(file_path, table_name)
        data_base.query(foo)
