import socket
import threading

from src.__models_for_all_layers.interfaces.IStopable import IStopable
from src.program_layers.api_layer.api_layer_factories.AnswererFactory import \
    AnswererFactory
from src.program_layers.api_layer.api_layer_factories.ReaderFactory import ReaderFactory
from src.program_layers.api_layer.api_layer_factories.WatchdogFactory import WatchdogFactory
from src.program_layers.api_layer.http_server.Reader import Reader
from src.program_layers.api_layer.http_server.Writer import Answerer


class ConnectionManager(IStopable):
    """This holds and manipulates writer and reader objects."""

    def __init__(self, connection: socket.socket, address: str):
        self.connection: socket.socket = connection
        self.address = address
        self.reader: Reader = ReaderFactory(connection, address, self).produce()
        self.answerer: Answerer = AnswererFactory(connection, address).produce()
        self.threads: dict[str:threading.Thread] = {}
        self.conn_timeout_watchdog = WatchdogFactory(self).produce()

    def start(self):
        self.__start_threads()
        self.__check_stop()

    def __create_threads(self):
        self.threads["watchdog"] = threading.Thread(target=self.conn_timeout_watchdog.worker)
        self.threads["reader"] = threading.Thread(target=self.reader.run)
        self.threads["writer"] = threading.Thread(target=self.answerer.run)

    def __start_threads(self):
        self.__create_threads()
        for t in self.threads.values():
            t.start()

    def stop(self):
        print("Stopping")
        self.reader.stop()
        self.answerer.stop()
        # self._stop_threads()

    def __check_stop(self):
        while not self.stop:
            pass
        # TODO: Finish

    def _stop_threads(self):
        for t in self.threads.values():
            t.join()
