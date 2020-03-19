import logging
import os
from pathlib import Path

import pytest
import sqlalchemy as db

from datum.access import Access

log_fmt = "[%(asctime)s %(levelname)-8s] [%(filename)s:%(lineno)s - %(funcName)s()] %(message)s"  # noqa
logging.basicConfig(level=logging.DEBUG, format=log_fmt)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def file_path():
    pardir = Path(__file__).parents[0]
    return os.path.join(pardir, "data.db")


@pytest.fixture(scope="session")
def table_name():
    return "IOC"


@pytest.fixture(scope="session")
def my_query():
    return "SELECT Age, Sex FROM IOC WHERE IOC.Sex = F"


@pytest.fixture(scope="session")
def foo():
    return foo


@pytest.fixture(scope="session")
def date_parse():
    return ["1/11/1996", "01-11-1996"]
