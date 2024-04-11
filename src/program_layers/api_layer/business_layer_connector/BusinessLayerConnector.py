from threading import Lock

from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.program_layers.business_layer.commands.ExecuteCommand import ExecuteCommand
from src.utils.SingletonMeta import SingletonMeta


class BusinessLayerConenctor(metaclass=SingletonMeta):
    def __init__(self):
        pass

    @staticmethod
    def execute(request: ParsedRequest):
        with Lock() as lock:
            ExecuteCommand(parsed_request=request).execute()
