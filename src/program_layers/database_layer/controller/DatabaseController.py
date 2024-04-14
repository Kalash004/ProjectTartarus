from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__response_builder.ResponseBuilder import ResponseBuilder
from src.__utils.SingletonMeta import SingletonMeta
from src.program_layers.database_layer.access.DbAccess import DbAccess
from src.program_layers.database_layer.commands.DatabaseManipulationCommands import DeleteCommand
from src.program_layers.database_layer.commands.DatabaseManipulationCommands import GetAllCommand
from src.program_layers.database_layer.commands.DatabaseManipulationCommands import InsertCommand
from src.program_layers.database_layer.commands.DatabaseManipulationCommands import SelectWhereCommand
from src.program_layers.database_layer.commands.DatabaseManipulationCommands import UpdateCommand


class DatabaseController(metaclass=SingletonMeta):
    """This allows clients control the database using parsed requests"""

    def __init__(self):
        self.access = DbAccess(initialize=True)
        self.__events_mapper = {
            "post": self.post,
            "get": self.get,
            "delete": self.delete,
            "update": self.update
        }

    def execute_request(self, request: ParsedRequest, connection_loop):
        event = request.event.lower()
        if event not in self.__events_mapper.keys():
            # TODO: Better exception
            raise Exception
        response = self.__events_mapper[event](request)
        print(response)
        # TODO: send response
        connection_loop.answerer.message = ResponseBuilder().build_succes(response)

    def delete(self, request: ParsedRequest):
        return DeleteCommand(request).execute()

    def post(self, request: ParsedRequest):
        return InsertCommand(request).execute()

    def update(self, request: ParsedRequest):
        return UpdateCommand(request).execute()

    def get(self, request: ParsedRequest):
        if request.parameters is None:
            return GetAllCommand(request).execute()
        return SelectWhereCommand(request).execute()
