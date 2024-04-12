from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__utils.SingletonMeta import SingletonMeta
from src.program_layers.business_layer.commands.ExecuteCommand import ExecuteCommand


class BusinessLayerConnector(metaclass=SingletonMeta):
    def __init__(self):
        pass

    @staticmethod
    def execute(request: ParsedRequest, connection_loop, lock):
        with lock:
            ExecuteCommand(parsed_request=request, connection_loop=connection_loop).execute()
