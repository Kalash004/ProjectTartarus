from __future__ import annotations

import typing
from typing import TYPE_CHECKING

from ..Connector.SimpleSQLConnector import SimpleSQLConnector as Connector
from ..QueryBuilder.QueryBuilder import SimpleQueryBuilder as Builder
from ...Models.Enums.SimpleConstraintsEnum import SimpleConstraints as Constraints
from ...Models.Models.SQLHolder import SimpleSQLHolder as Holder

if TYPE_CHECKING:
    from ... import Base
    from ... import Config


class Controller:
    # TODO: Add an initiating sql commands for queries that are not supported by the library
    _instance = None
    __tables = dict()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_config: Config = None):
        # TODO: ADD INPUT CHECK
        if db_config is not None:
            self.config = db_config
            self.connector: Connector
            self.__query_obj: Holder

    def _add_table(self, table):
        # TODO: ADD INPUT CHECK
        table_name = self._find_tablename(table)
        if not self.__tables.__contains__(table_name):
            self.__tables[table_name] = table

    @staticmethod
    def _find_tablename(table):
        # TODO: ADD INPUT CHECK
        struct = table.struct
        for item in struct:
            if item[0] == "table_name":
                return item[1]

    def start(self):
        # check if table users creates
        try:
            # Build queries
            if self.config is None:
                raise Exception("Database config was not given")
            self.connector = Connector(db_config=self.config)
            self.__query_obj = self.build_queries()
            # Check if database exists
            if not self.database_exists():
                self.__create_database()
            self.use_database()
            self.starter_dml()

        except Exception as err:
            raise err
            # TODO: Better exception cases

    def build_queries(self):
        builder = Builder()
        basic_sql_commands = builder.build_sql(self.__tables)
        return basic_sql_commands

    def database_exists(self) -> bool:
        # TODO: Separate query building to QueryBuilder
        query = f"SHOW DATABASES"
        response = self.connector.query({
            query: None
        })[0]
        for schema in response:
            if self.config.database_name in schema.values():
                return True
        return False

    def __create_database(self):
        # TODO: Separate query building to QueryBuilder
        query = f"CREATE DATABASE {self.config.database_name}"
        response = self.connector.query(
            {
                query: None
            }
        )
        return response

    def create_tables(self):
        for table_name, item in self.__query_obj.items():
            if not self.table_exists(table_name):
                self.connector.query(
                    {
                        item.table_builder_DDL: None
                    }
                )

    def reference_tables(self):
        for item in self.__query_obj.values():
            for ref in item.references.values():
                self.connector.query(
                    {
                        ref: None
                    }
                )

    def use_database(self):
        # TODO: Separate query building to QueryBuilder
        query = f"USE {self.config.database_name}"
        self.connector.query(
            {
                query: None
            }
        )

    def table_exists(self, table_name):
        # TODO: ADD INPUT CHECK
        # TODO: Separate query building to QueryBuilder
        query = (f"SELECT COUNT(*) "
                 f"FROM information_schema.tables "
                 f"WHERE table_name = '{table_name}' ")
        respones = self.connector.query(
            {
                query: None
            }
        )
        resp = respones[0][0]["COUNT(*)"]
        return int(resp) >= 1

    def starter_dml(self):
        self.create_tables()
        self.reference_tables()

    def insert_data(self, to_insert):
        for item in to_insert:
            name = item.table_name
            table = self.__tables[name]
            query = self.__query_obj[name].insert
            values = []
            for attr in self.__tables[name].struct:
                if attr[0] == "table_name":
                    continue
                values.append(item.__dict__[attr[0]])
            resp = self.connector.query({
                query: values
            })
            if isinstance(resp, Exception):
                raise resp

    def select_data_where(self, obj: type(Base), selectors: []) -> object:
        # TODO: ADD INPUT CHECK
        # TODO: Possibility of sql injections, try to fix
        # TODO: Separate query building to QueryBuilder
        """
        :param obj: Class of the table: SimpleSQL.Base
        :param selectors: [field, operator, value],[...]
        :return:
        """
        for item in selectors:
            if not isinstance(item, type([])):
                raise Exception(f"Bad input type, need array got {type(item)}")

        query = self.__query_obj[obj.table_name].select
        query = query.rstrip(";")
        query += " WHERE"
        query_addition = ""
        for item in selectors:
            for index, query_part in enumerate(item):
                if index != 2:
                    query_addition += f" {query_part} "
                else:
                    query_addition += f" '{query_part}' "
            query_addition += "AND"
        query_addition = query_addition.rstrip(" AND")
        query_addition += ";"
        query += query_addition
        try:
            resp = self.connector.query({
                query: None
            })[0]
            return self.__map_arrays_to_obj_array(obj, resp)
        except Exception:
            # TODO: Better exceptions
            raise

    def select_all_from(self, obj: type(Base)):
        # TODO: ADD INPUT CHECK
        query = self.__query_obj[obj.table_name].select
        try:
            resp = self.connector.query(
                {
                    query: None
                }
            )[0]
            return self.__map_arrays_to_obj_array(obj, resp)
        except Exception:
            # TODO: Better exceptions
            raise

    @DeprecationWarning
    def __select_data_join(self, from_table_name, join_params):
        # NOT WORKING
        query = self.__query_obj[from_table_name].select
        # SELECT * FROM `Test2`;
        query = query.rstrip(";")
        join_query = ""
        for table_name, join in join_params.items():
            join_query += f" INNER JOIN `{table_name}` ON {join[0]} = {join[1]}"
        query += join_query
        try:
            resp = self.connector.query(
                {
                    query: None
                }
            )
            return resp[0]
        except Exception:
            raise

    def update_data(self, new: Base):
        # TODO: ADD INPUT CHECK
        table_name = new.table_name
        query = self.__query_obj[table_name].update
        values = []
        pk = self.__find_primary_key_value(new)
        for attr in self.__tables[table_name].struct:
            if attr[0] == "table_name":
                continue
            values.append(new.__dict__[attr[0]])
        values.append(pk)
        try:
            resp = self.connector.query(
                {
                    query: values
                }
            )
            return resp
        except Exception:
            raise
            # TODO: Better exceptions handling

    def delete_data_id(self, obj, obj_id):
        table_name = obj.table_name
        pk = self.__find_primary_key_name(obj)
        query = self.__query_obj[table_name].delete
        try:
            resp = self.connector.query(
                {
                    query: [obj_id, ]
                }
            )
            return resp
        except Exception:
            # TODO: Better exceptions handling
            raise

    def delete_data(self, to_delete: Base):
        # TODO: ADD INPUT CHECK
        table_name = to_delete.table_name
        pk = self.__find_primary_key_value(to_delete)
        query = self.__query_obj[table_name].DeleteCommand
        try:
            resp = self.connector.query(
                {
                    query: [pk, ]
                }
            )
            return resp
        except Exception:
            # TODO: Better exceptions handling
            raise

    def query(self, query: typing.Dict[str: [str]]):
        """

        :param query: {query:[bindable_values]}
        :return:
        """
        try:
            return self.connector.query(query)
        except Exception:
            raise
            # TODO: Better exceptions handling

    def last_inserted_instance(self, instance):
        pk = self.__find_primary_key_name(instance)
        query = f"SELECT * FROM {instance.table_name} ORDER BY {pk} DESC LIMIT 1"
        resp = self.connector.query(
            {
                query: None
            }
        )[0]
        if len(resp) > 0:
            return self.__map_to_obj(instance, resp[0])
        return []

    def __find_primary_key_name(self, instance: Base):
        table_name = instance.table_name
        pk = None
        for attr in self.__tables[table_name].struct:
            if attr[0] == "table_name":
                continue
            if Constraints.PK in attr[1].constraints:
                pk = attr[0]
                break
        return pk

    def __find_primary_key_value(self, instance: Base):
        pk = self.__find_primary_key_name(instance)
        return instance.__dict__[pk]

    @staticmethod
    def __map_to_obj(obj, resp):
        hold = obj
        hold = type(obj)
        if hold.__name__ == "type":
            hold = obj
        mapped_obj = hold(skip_setup=True)
        mapped_obj.map(resp)
        return mapped_obj

    def __map_arrays_to_obj_array(self, obj, resp):
        returner = []
        for instance in resp:
            returner.append(self.__map_to_obj(obj, instance))
        return returner
