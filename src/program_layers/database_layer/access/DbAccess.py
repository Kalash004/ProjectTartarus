from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__utils.SingletonMeta import SingletonMeta
from src.program_layers.database_layer.RequestToDbObjMapper import RequestToDbObjMapper
from src.program_layers.database_layer.SimpleSQL.package_src import Base
from src.program_layers.database_layer.factory.OrmFactory import OrmFactory
from src.program_layers.database_layer.tables.tables import all_tables


class DbAccess(metaclass=SingletonMeta):
    """This works with ORM"""

    def __init__(self, initialize=False):
        if initialize:
            self.orm = OrmFactory().produce()
            self.mapper = RequestToDbObjMapper()
            self.start_orm()

    def start_orm(self):
        for table in all_tables.all_talbes:
            table(skip_setup=True)
        self.orm.start()

    def read_all(self, parsed_request: ParsedRequest):
        obj = self.mapper.get_request_obj_type(parsed_request)
        return self.orm.select_all_from(obj)

    def select_where(self, parsed_request: ParsedRequest, arg):
        obj = self.mapper.get_request_obj_type(parsed_request)
        resp = self.orm.select_data_where(obj, arg)
        return resp

    def get_last_index(self, parsed_request: ParsedRequest):
        obj = self.mapper.get_request_obj_type(parsed_request)
        resp = self.orm.last_inserted_instance(obj)
        return resp

    def insert(self, parsed_req):
        objs: [Base] = self.mapper.request_to_obj(parsed_req)
        obj: Base
        new_id = 0
        for obj in objs:
            # check if obj has None id -> request for last inserted id, set objs id +1
            # TODO: Kills performence
            # TODO: Exception might happen if same id already exists
            if obj.find_primary_key_val().lower() == "none":
                resp: Base = self.get_last_index(parsed_request=parsed_req)
                last_id = resp.find_primary_key_val()
                if last_id > new_id:
                    new_id = last_id
                new_id += 1
                obj.set_primary_key_val(new_id)
        resp = self.orm.insert_data(objs)
        return resp

    def delete(self, parsed_request: ParsedRequest, obj_id):
        obj = self.mapper.get_request_obj_type(parsed_request)
        resp = self.orm.delete_data_id(obj, obj_id)
        return resp

    def update(self, parsed_request: ParsedRequest):
        obj = self.mapper.request_to_obj(parsed_request)[0]
        resp = self.orm.update_data(obj)
        return resp
