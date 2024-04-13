from __future__ import annotations

from typing import TYPE_CHECKING

from ...Models.Enums.SimpleConstraintsEnum import SimpleConstraints as Constraints
from ...Models.Models.SQLHolder import SimpleSQLHolder as Holder

if TYPE_CHECKING:
    from ... import SimpleReference


class SimpleQueryBuilder:
    def __init__(self):
        self.changeable_sign = "%s"

    def build_sql(self, tables) -> dict[str:Holder]:
        built = dict()
        for table_name, _table in tables.items():
            table_copy = _table.struct.copy()
            self.__remove_tablename(table_copy)
            ddl = self.__build_creation(table_name, table_copy)
            referencing = self.__build_referencing(table_name, table_copy)
            insert = self.__build_insert(table_name, table_copy)
            select = self.__build_select(table_name)
            update = self.__build_update(table_name, table_copy)
            delete = self.__build_delete(table_name, table_copy)
            built[table_name] = Holder(table_name, table_builder_DDL=ddl, references=referencing, insert=insert,
                                       select=select, update=update,
                                       delete=delete)
        return built

    def __build_creation(self, table_name, table_copy):
        middle = ""
        for attribute in table_copy:
            name = attribute[0]
            data_type = attribute[1].datatype
            constraints = attribute[1].constraints
            middle += f"`{name}` "
            middle = self.__set_contraints(middle, data_type, constraints)
        else:
            middle = middle.rstrip(" ,")

        query = (f"CREATE TABLE `{table_name}`("
                 f"{middle}"
                 f");")
        return query

    def __build_insert(self, table_name, table_copy):
        bindable_string = ""
        for attribute in table_copy:
            bindable_string += f"{self.changeable_sign}, "
        else:
            bindable_string = bindable_string.rstrip(" ").rstrip(",")
        return f"INSERT INTO `{table_name}` VALUES ({bindable_string});"

    def __build_select(self, table_name):
        return f"SELECT * FROM `{table_name}`;"

    def __build_update(self, table_name, table_copy):
        middle = ""
        pk = None
        for attribute in table_copy:
            if Constraints.PK in attribute[1].constraints:
                pk = attribute
            name = attribute[0]
            middle += f" `{name}`={self.changeable_sign}, "
        middle = middle.rstrip(", ")
        query = (f"UPDATE `{table_name}` "
                 f"SET{middle} "
                 f"WHERE `{pk[0]}` = {self.changeable_sign};")
        return query

    def __build_delete(self, table_name, table_copy):
        pk = None
        for attribute in table_copy:
            if Constraints.PK in attribute[1].constraints:
                pk = attribute
        return f"DELETE FROM `{table_name}` WHERE {pk[0]} = {self.changeable_sign};"

    def __find_tablename(self, struct):
        for item in struct:
            if item[0] == "table_name":
                return item

    def __remove_tablename(self, table):
        name = self.__find_tablename(table)
        table.remove(name)

    def __set_contraints(self, query: str, data_type, constraints) -> str:
        query += f"{data_type.value} "
        clean_constraints = ""
        try:
            for constraint in constraints:
                # TODO: Possible error, leave for future
                clean_constraints += f"{constraint.value} "
            else:
                clean_constraints += ","
        except Exception:
            # TODO: Better exception check
            clean_constraints += ","
        finally:
            return query + clean_constraints

    def __build_referencing(self, table_name, table_copy):
        ref_queries = dict()
        for item in table_copy:
            if not item[1].references:
                continue
            for reference in item[1].references:
                reference: SimpleReference = reference
                referenced_table_name = reference.table_name
                attr_name = reference.attribute_name
                query = (f"ALTER TABLE `{table_name}` "
                         f"ADD CONSTRAINT FK_{item[0]}_{table_name} "
                         f"FOREIGN KEY ({item[0]}) "
                         f"REFERENCES {referenced_table_name}({attr_name});")
                ref_queries[referenced_table_name] = query
        return ref_queries
