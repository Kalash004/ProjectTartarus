import socket

from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.program_layers.api_layer.main_api_server.Writer import Answerer


class AnswererFactory(IFactory):
    def __init__(self, connection: socket.socket, address: str):
        self.conn = connection
        self.adr = address

    def produce(self):
        return Answerer(connection=self.conn, adress=self.adr)
