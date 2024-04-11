import socket

from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.program_layers.api_layer.http_server.ConnectionManager import ConnectionManager


class ConnectionManagerFactory(IFactory):
    def __init__(self, connection: socket.socket, address: str):
        self.connection = connection
        self.address = address

    def produce(self):
        return ConnectionManager(self.connection, self.address)
