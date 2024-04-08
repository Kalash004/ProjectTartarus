import socket
import threading

from src.program_layers.api_layer.api_layer_factories.answerer_factory.AnswererFactory import \
    AnswererFactory
from src.program_layers.api_layer.api_layer_factories.reader_factory.ReaderFactory import ReaderFactory
from src.program_layers.api_layer.http_server.answerer.Answerer import Answerer
from src.program_layers.api_layer.http_server.reader.Reader import Reader


class ConnectionManager:
    """This holds and manipulates answerer and reader objects."""

    def __init__(self, connection: socket.socket, address: str, connection_live_time_sec):
        self.connection: socket.socket = connection
        self.address = address
        self.connection_live_time_sec = connection_live_time_sec
        self.reader: Reader = ReaderFactory(connection, address).produce()
        self.answerer: Answerer = AnswererFactory(connection, address).produce()
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
        self._stop_threads()
        self.stop = True

    def __check_stop(self):
        while not self.stop:
            pass
        # TODO: Finish

    def _stop_threads(self):
        for t in self.threads.values():
            t.join(1)
