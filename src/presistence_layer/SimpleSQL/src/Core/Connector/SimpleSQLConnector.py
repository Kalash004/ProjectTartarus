from __future__ import annotations

import typing

import mysql.connector
from mysql.connector import DatabaseError

from ... import Config, ConnectionException, ConnectionState


class SimpleSQLConnector:
    _instance = None

    def __new__(cls, *args, **kwargs):
        try:
            kwargs['db_config']
        except Exception as err:
            raise Exception(f"db_config was not given: {err}") from err
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_config: Config):
        self.__connection: mysql.connector.connection
        self.state: ConnectionState
        self.config: Config = db_config
        self.__connection = self.connect(db_config=self.config)
        self.state = ConnectionState.CONNECTED

    def query(self, query_args: typing.Dict[str: [str]]) -> [str, ]:
        global cursor
        try:
            if not self.check_connection():
                self.connect(self.config)
            cursor = self.__connection.cursor(dictionary=True)
            responses = []
            self.__connection.start_transaction()
            for query, args in query_args.items():
                if args is None:
                    cursor.execute(query)
                else:
                    cursor.execute(query, args)
                responses.append(cursor.fetchall())
            self.__connection.commit()
            return responses
        except DatabaseError as err:
            if err.errno == 1826:
                return err
            else:
                self.__connection.rollback()
                raise err
        except Exception as err:
            self.state = ConnectionState.ERROR
            self.__connection.rollback()
            raise Exception(f"Error occured while quering the database: {err}") from err
        finally:
            cursor.close()

    def connect(self, db_config: Config):
        try:
            connection = self.__generate_conenction(db_config)
            if not connection.is_connected():
                raise ConnectionException("Could not create connection to the database")
            self.state = ConnectionState.CONNECTED
            return connection
        except ConnectionException:
            e = None
            for i in range(0, 2):
                try:
                    connection = self.__generate_conenction(db_config)
                except Exception as err:
                    e = err
                    continue
                if connection.is_connected():
                    return connection
            raise Exception(
                f"Retried connecting 3 times, couldnt connect to the database {self.config.hostname}: {e}") from e
        except Exception as err:
            self.state = ConnectionState.ERROR
            raise Exception(f"Error happened while initializing connection to the database server: {err}") from err

    @staticmethod
    def __generate_conenction(db_config: Config):
        try:
            connection = mysql.connector.connect(
                host=db_config.hostname,
                user=db_config.username,
                password=db_config.password
            )
            return connection
        except Exception as err:
            raise ConnectionException(err)

    def set_conn_state(self, state: ConnectionState):
        if not isinstance(state, ConnectionState):
            raise Exception(f"State {state} is not of ConnectionState")
        self.state = state

    def check_connection(self):
        if not self.__connection.is_connected():
            self.state = ConnectionState.CLOSED
            return False
        self.state = ConnectionState.CONNECTED
        return True
