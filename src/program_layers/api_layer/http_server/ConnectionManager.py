import socket
import threading

from src.program_layers.api_layer.__models.interfaces.IParse import IParse
from src.program_layers.api_layer.api_layer_factories.api_layer_sub_factories.a_main_api_layer_factory.ApiLayerFactory import \
    ApiLayerFactory
from src.program_layers.api_layer.http_server.Answerer import Answerer
from src.program_layers.api_layer.http_server.Reader import Reader


class ConnectionManager:
    """This holds and manipulates answerer and reader objects."""

    def __init__(self, connection: socket.socket, address: str):
        self.connection: socket.socket = connection
        self.address = address
        self.parser: IParse = ApiLayerFactory().produce_parser_factory().produce()
        self.reader: Reader = ApiLayerFactory().produce_reader_factory(connection, address).produce()
        self.answerer: Answerer = ApiLayerFactory().produce_answerer_factory(connection, address).produce()
        self.threads: dict[str:threading.Thread] = {}
        self.stop = False

    def start(self):
        self.__start_threads()
        self.__check_stop()

    def __create_threads(self):
        self.threads["reader"] = threading.Thread(target=self.reader.run)
        self.threads["answerer"] = threading.Thread(target=self.answerer.run)

    def __start_threads(self):
        self.__create_threads()
        for t in self.threads.values():
            t.start()

    def stop(self):
        self.reader.stop()
        self.answerer.stop()
        self.stop = True

    def __check_stop(self):
        while not self.stop:
            pass
        # TODO: Finish
