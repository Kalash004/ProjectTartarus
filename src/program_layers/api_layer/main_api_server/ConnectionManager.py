import socket
import threading

# Importing specific classes and methods from various modules
from src.__models_for_all_layers.interfaces.IStopable import IStopable
from src.exception_handler.ExceptionHandler import ExceptionHandler
from src.program_layers.api_layer.factory.AnswererFactory import AnswererFactory
from src.program_layers.api_layer.factory.ReaderFactory import ReaderFactory
from src.program_layers.api_layer.factory.WatchdogFactory import WatchdogFactory


class ConnectionManager(IStopable):
    """This class manages the communication with a single client connection."""

    def __init__(self, connection: socket.socket, address: str):
        """
        Initializes the ConnectionManager with the provided connection and client address.

        Args:
        - connection (socket.socket): The socket object representing the client connection.
        - address (str): The address of the client.
        """
        self.connection: socket.socket = connection  # Client socket connection
        self.address = address  # Client address
        self.exception_handler = ExceptionHandler()  # Exception handler instance
        # Creates reader and answerer objects for handling incoming and outgoing data
        self.reader = ReaderFactory(connection, address, self).produce()
        self.answerer = AnswererFactory(connection, address, self).produce()
        self.threads: dict[str: threading.Thread] = {}  # Dictionary to hold thread objects
        # Creates a watchdog object for managing connection timeouts
        self.conn_timeout_watchdog = WatchdogFactory(self).produce()

    def start(self):
        """Starts the connection manager by starting its internal threads."""
        self.__start_threads()

    def __create_threads(self):
        """Creates threads for reader, answerer, and connection timeout watchdog."""
        self.threads["watchdog"] = threading.Thread(target=self.conn_timeout_watchdog.worker)
        self.threads["reader"] = threading.Thread(target=self.reader.run)
        self.threads["writer"] = threading.Thread(target=self.answerer.run)

    def __start_threads(self):
        """Starts all the threads created for managing the connection."""
        self.__create_threads()
        for t in self.threads.values():
            t.start()

    def stop(self):
        """Stops the connection manager by stopping its reader and answerer."""
        self.reader.stop()  # Stops the reader
        self.answerer.stop()  # Stops the answerer
        # self._stop_threads()  # Optionally stops all threads, but currently unused

    def _stop_threads(self):
        """Stops all threads managed by the connection manager."""
        for t in self.threads.values():
            t.join()

    def kill_connection(self):
        """Closes the connection."""
        self.connection.close()  # Closes the client connection
