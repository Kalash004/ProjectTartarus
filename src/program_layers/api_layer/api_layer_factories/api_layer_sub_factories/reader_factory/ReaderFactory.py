import socket

from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.program_layers.api_layer.__models.interfaces.IParse import IParse
from src.program_layers.api_layer.http_server.reader.Reader import Reader
from src.utils.SingletonMeta import SingletonMeta


class ReaderFactory(metaclass=SingletonMeta, IFactory):
    def __init__(self, connection: socket.socket, address: str, parser: IParse, life_time_sec: int):
        self.connection = connection
        self.address = address
        self.parser = parser
        self.life_time_sec = life_time_sec

    def produce(self):
        return Reader(connection=self.connection, address=self.address, parser=self.parser)
