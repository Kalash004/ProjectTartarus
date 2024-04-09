import socket

from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.program_layers.api_layer.http_server.writer.Writer import Answerer
from src.utils.SingletonMeta import SingletonMeta


class AnswererFactory(IFactory, metaclass=SingletonMeta):
    def __init__(self, connection: socket.socket, address: str):
        self.conn = connection
        self.adr = address

    def produce(self):
        return Answerer(connection=self.conn, adress=self.adr)
