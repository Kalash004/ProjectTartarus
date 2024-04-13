import socket

from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.program_layers.api_layer.__models.interfaces.IParse import IParse
from src.program_layers.api_layer.factory.ParserFactory import \
    ParserFactory
from src.program_layers.api_layer.main_api_server.Reader import Reader


class ReaderFactory(IFactory):
    def __init__(self, connection: socket.socket, address: str, conn_manager, exception_handler):
        self.connection = connection
        self.address = address
        self.conn_manager = conn_manager
        self.exception_handler = exception_handler
        self.parser: IParse = ParserFactory().produce()

    def produce(self):
        return Reader(connection=self.connection, address=self.address, parser=self.parser,
                      conn_manager=self.conn_manager, exception_handler=self.exception_handler)
