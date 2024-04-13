from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__models_for_all_layers.interfaces.ICommand import ICommand
from src.program_layers.database_layer.access.DbAccess import DbAccess
from src.program_layers.database_layer.args_mapper.ArgsMapper import ArgsMapper


class start_database(ICommand):
    def execute(self):
        DbAccess(initialize=True)


class GetAllCommand(ICommand):
    def __init__(self, parsed_req):
        self.obj = parsed_req
        super().__init__()

    def execute(self):
        db = DbAccess()
        return db.read_all(self.obj)


class SelectWhereCommand(ICommand):

    def __init__(self, parsed_req: ParsedRequest):
        self.obj = parsed_req
        self.arg = ArgsMapper().map(parsed_req)
        super().__init__()

    def execute(self):
        db = DbAccess()
        return db.select_where(self.obj, self.arg)


class get_last_index(ICommand):
    def __init__(self, parsed_req: ParsedRequest):
        self.obj = parsed_req
        super().__init__()

    def execute(self):
        db = DbAccess()
        return db.get_last_index(self.obj)


class InsertCommand(ICommand):
    def __init__(self, parsed_req: ParsedRequest):
        self.obj = parsed_req
        super().__init__()

    def execute(self):
        db = DbAccess()
        return db.insert(self.obj)


class DeleteCommand(ICommand):
    def __init__(self, parsed_req: ParsedRequest):
        self.obj = parsed_req
        self.obj_id = parsed_req.get_params_id()
        if self.obj_id is None:
            # TODO: better handling
            raise Exception()
        super().__init__()

    def execute(self):
        db = DbAccess()
        return db.delete(self.obj, self.obj_id)


class UpdateCommand(ICommand):
    def __init__(self, parsed_req):
        self.obj = parsed_req
        super().__init__()

    def execute(self):
        db = DbAccess()
        return db.update(self.obj)
