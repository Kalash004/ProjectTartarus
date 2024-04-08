import socket

from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.config_loader.ConfigLoader import ConfigLoader
from src.program_layers.api_layer.http_server.answerer.Answerer import Answerer
from src.utils.SingletonMeta import SingletonMeta


class AnswererFactory(IFactory, metaclass=SingletonMeta):
    def __init__(self, connection: socket.socket, address: str):
        self.conn = connection
        self.adr = address
        self.life_time_sec = ConfigLoader().get_connection_life_sec()

    def produce(self):
        return Answerer(connection=self.conn, adress=self.adr, life_time_sec=self.life_time_sec)
