from typing import Any

from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.program_layers.database_layer.SimpleSQL.package_src import Base
from src.program_layers.database_layer.tables.tables import admin_users
from src.program_layers.database_layer.tables.tables import days
from src.program_layers.database_layer.tables.tables import enterences_to_office
from src.program_layers.database_layer.tables.tables import office_users
from src.program_layers.database_layer.tables.tables import system_log_ins
from src.program_layers.database_layer.tables.tables import system_messages


class RequestToDbObjMapper:
    __map = {
        "admin_users": admin_users,
        "office_users": office_users,
        "days": days,
        "system_messages": system_messages,
        "system_log_ins": system_log_ins,
        "enterences_to_office": enterences_to_office
    }

    # TODO: Can be remade with func to dynamically map from tables.all_tables.all_tables ^

    def request_to_obj(self, request: ParsedRequest) -> [Base]:
        objs = []
        table = request.table
        if table not in self.__map:
            # TODO: Better exceptions
            raise Exception
        obj: Base = self.__map[table]
        for d in request.data:
            mapped = obj.map_new(data=d)
            objs.append(mapped)
        return objs

    def get_request_obj_type(self, request: ParsedRequest) -> Any:
        table = request.table.lower()
        if table not in self.__map:
            # TODO: Better exceptions
            raise Exception
        obj = self.__map[table]
        return obj

    def get_obj_type_from_name(self, name) -> Base:
        if name not in self.__map.keys():
            return
        return self.__map[name]
