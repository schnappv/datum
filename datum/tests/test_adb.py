import logging
import sys
import os

import time
import pytest
import numpy as np

from datum.access import Access

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def test_adb(file_path, table_name, my_query):
    start = time.time()
    a = Access(file_path, table_name)
    results = a.query(db_query=my_query)
    logger.debug("time: {:6.4f}".format(time.time() - start))
    logger.debug("Sex: {}".format(results.iloc[0].Sex))
    logger.debug(results.Sex)
    assert np.all(results.Sex == "F")
