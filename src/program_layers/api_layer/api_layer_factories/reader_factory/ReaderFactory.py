import socket

from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.program_layers.api_layer.__models.interfaces.IParse import IParse
from src.program_layers.api_layer.api_layer_factories.request_parser_factory.ParserFactory import \
    ParserFactory
from src.program_layers.api_layer.http_server.reader.Reader import Reader
from src.utils.SingletonMeta import SingletonMeta


class ReaderFactory(IFactory, metaclass=SingletonMeta):
    def __init__(self, connection: socket.socket, address: str, conn_manager):
        self.connection = connection
        self.address = address
        self.conn_manager = conn_manager
        self.parser: IParse = ParserFactory().produce()

    def produce(self):
        return Reader(connection=self.connection, address=self.address, parser=self.parser)
