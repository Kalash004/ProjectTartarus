import socket

from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.program_layers.api_layer.main_api_server.Writer import Answerer


class AnswererFactory(IFactory):
    def __init__(self, connection: socket.socket, address: str, conn_manager):
        self.conn = connection
        self.adr = address
        self.con_manager = conn_manager

    def produce(self):
        return Answerer(connection=self.conn, address=self.adr, connection_manager=self.con_manager)
