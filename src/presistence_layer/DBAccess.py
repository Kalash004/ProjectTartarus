from src.presistence_layer.tables.tables import all_tables
from src.presistence_layer.SimpleSQL import App as Orm

class DBAccess():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, database_config=None, **kwargs):
        init_needed = True
        try:
            init_needed = kwargs["initialize"]
        except Exception:
            init_needed = True
        if init_needed:
            self.orm = Orm(database_config)
            self.start_orm()

    def start_orm(self):
        for table in all_tables.all_talbes:
            table(skip_setup=True)
        self.orm.start()

    def read_all(self, obj):
        return self.orm.select_all_from(obj)

    def select_where(self, obj, arg):
        resp = self.orm.select_data_where(obj, arg)
        return resp

    def get_last_index(self, obj):
        resp = self.orm.last_inserted_instance(obj)
        return resp

    def insert(self, obj):
        # TODO: Possible exception
        resp = self.orm.insert_data(obj)
        return resp

    def delete(self, obj, id):
        resp = self.orm.delete_data_id(obj, id)
        return resp

    def update(self, obj):
        resp = self.orm.update_data(obj)
        return resp