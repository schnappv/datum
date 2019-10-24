import logging
import typing

import pandas as pd
import sqlalchemy as db
from sqlalchemy import exc

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler)

FilePath = typing.NewType("FileType", str)
SQLSelect = typing.NewType("SQLSelect", db.sql.selectable.Select)


class AccessDataBase(object):
    """
    Used to query a database and convert into a DataFrame
    """

    def __init__(
        self,
        data_base: FilePath,
        table_name: str
    ):
        """
        Args:
            data_base (str): the name of the SQLite database

            table_name (str): the name of the table in the database
        """
        self.db_name = data_base
        self.table_name = table_name

        self.engine = None
        self.connection = None
        self.table = None

        self.__db_connect()

    def __db_connect(self):
        """
        Creates a database connection
        """
        try:
            md = db.MetaData()
            engine_name = "sqlite:///" + self.db_name
            self.engine = db.create_engine(engine_name)

            self.connection = self.engine.connect()
            self.table = db.Table(
                self.table_name, md, autoload=True, autoload_with=self.engine
            )

        except exc.SQLAlchemyError as e:
            logger.error("{}: {}".format(type(e), str(e)))
            raise

    @property
    def db_properties(self):
        """
        Gives properties of the database for the user to use

        Returns:
            engine, connection, table
        """
        engine = self.engine
        connection = self.connection

        return engine, connection

    def _exc_query(self, query: SQLSelect):
        """
        Executes some query

        Args:
            query (sqlalchemy.sql.selectable.Select): sqlalchemy query command
    
        Returns:
            result_set
        """
        try:
            result_proxy = self.connection.execute(query)
            result_set = result_proxy.fetchall()

            return result_set

        except exc.SQLAlchemyError as e:
            logger.error("{}: {}".format(type(e), str(e)))
            raise

    def _make_dframe(self, query_results: list):
        """
        Converts queried database results into a dataframe

        Args:
            query_result (list): the queried database in a list format

        Returns:
            result_df
        """
        try:
            result_df = pd.DataFrame(query_results)
            result_df.columns = query_results[0].keys()

            return result_df

        except exc.SQLAlchemyError as e:
            logger.error("{}: {}".format(type(e), str(e)))
            raise

    def query(self, db_query: SQLSelect):
        """
        Queries the selected database with some sqlalchemy select statement

        Args:
            db_query (sqlalchemy.sql.selectable.Select): the sql query

        Returns:
            result_set
        """
        try:
            result_set = self._exc_query(db_query)
            results_df = self._make_dframe(result_set)

            return results_df

        except exc.SQLAlchemyError as e:
            logger.error("{}: {}".format(type(e), str(e)))
            raise
