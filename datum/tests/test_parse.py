import logging
import sys
import os

import time
import pytest

from datum.create import is_date

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def test_is_date(date_parse):
    start = time.time()
    for date in date_parse:
        logger.debug("time: {:6.4f}".format(time.time() - start))
        assert(is_date(date) is True)
