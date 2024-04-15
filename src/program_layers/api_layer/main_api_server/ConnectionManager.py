import socket
import threading

from src.__models_for_all_layers.interfaces.IStopable import IStopable
from src.exception_handler.ExceptionHandler import ExceptionHandler
from src.program_layers.api_layer.factory.AnswererFactory import \
    AnswererFactory
from src.program_layers.api_layer.factory.ReaderFactory import ReaderFactory
from src.program_layers.api_layer.factory.WatchdogFactory import WatchdogFactory


class ConnectionManager(IStopable):
    """This holds and manipulates writer and reader objects."""

    def __init__(self, connection: socket.socket, address: str):
        self.connection: socket.socket = connection
        self.address = address
        self.exception_handler = ExceptionHandler()
        self.reader = ReaderFactory(connection, address, self).produce()
        self.answerer = AnswererFactory(connection, address, self).produce()
        self.threads: dict[str:threading.Thread] = {}
        self.conn_timeout_watchdog = WatchdogFactory(self).produce()

    def start(self):
        self.__start_threads()

    def __create_threads(self):
        self.threads["watchdog"] = threading.Thread(target=self.conn_timeout_watchdog.worker)
        self.threads["reader"] = threading.Thread(target=self.reader.run)
        self.threads["writer"] = threading.Thread(target=self.answerer.run)

    def __start_threads(self):
        self.__create_threads()
        for t in self.threads.values():
            t.start()

    def stop(self):
        self.reader.stop()
        self.answerer.stop()
        # self._stop_threads()

    def _stop_threads(self):
        for t in self.threads.values():
            t.join()

    def kill_connection(self):
        self.connection.close()
