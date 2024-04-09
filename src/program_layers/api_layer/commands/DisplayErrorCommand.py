from src.__models_for_all_layers.interfaces.ICommand import ICommand
from src.program_layers.api_layer.http_server.connection_manager.ConnectionManager import ConnectionManager


class DisplayErrorCommand(ICommand):

    def __init__(self, error_message: str, connection_manager: ConnectionManager):
        self.error_message = error_message
        self.conn_man = connection_manager

    def execute(self):
        self.conn_man.answerer.send_specific_message(self.error_message)
