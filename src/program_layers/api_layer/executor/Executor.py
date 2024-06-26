from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__utils.SingletonMeta import SingletonMeta
from src.program_layers.business_layer.commands.SendToBusinessLayerCommand import SendToBusinessLayerCommand
from src.program_layers.database_layer.commands.SendParsedReqToDatabaseLayer import SendParsedReqToDatabaseLayer


class Executor(metaclass=SingletonMeta):
    def __init__(self):
        pass

    @staticmethod
    def execute(request: ParsedRequest, connection_loop, lock):
        with lock:
            SendToBusinessLayerCommand(parsed_request=request).execute()
            SendParsedReqToDatabaseLayer(request, connection_loop).execute()
