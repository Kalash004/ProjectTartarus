import socket
import threading

# Importing specific classes and methods from various modules
from src.exception_handler.ExceptionHandler import ExceptionHandler
from src.program_layers.api_layer.__models.interfaces.IParse import IParse
from src.program_layers.api_layer.executor.Executor import Executor


class Reader:
    """This class reads requests from clients."""

    lock = threading.Lock()  # Class-level lock for thread safety

    def __init__(self, connection: socket.socket, address: str, parser: IParse, conn_manager, exception_handler):
        """
        Initializes the Reader with the provided connection, address, parser, and other dependencies.

        Args:
        - connection (socket.socket): The socket object representing the client connection.
        - address (str): The address of the client.
        - parser (IParse): The parser object used to parse incoming data.
        - conn_manager: The connection manager object associated with this reader.
        - exception_handler: The exception handler object for handling exceptions.
        """
        self.CONNECTION: socket.socket = connection  # Client socket connection
        self.ADDRESS = address  # Client address
        self.parser: IParse = parser  # Parser object
        self.thread = threading.Thread(target=self.run)  # Thread for running the reader
        self.connection_manager = conn_manager  # Connection manager associated with this reader
        self.stop_flag = False  # Flag to control the reader's termination
        self.exception_handler = exception_handler  # Exception handler object

    def run(self):
        """Main method that runs the reader."""
        with self.CONNECTION as conn:
            while not self.stop_flag:
                try:
                    self.__main_loop(conn)  # Enters the main loop to handle incoming data
                except Exception as e:
                    # Handles exceptions and informs the client through the connection manager
                    ExceptionHandler().handle_exception_inform_client(e, self.connection_manager)
            conn.close()  # Closes the connection
            return

    def start_thread(self):
        """Starts the reader thread."""
        self.thread.start()  # Starts the reader thread

    def __main_loop(self, connection):
        """Main loop for handling incoming data."""
        data = self.receive_data()  # Receives data from the client
        if data is None:
            return  # Exits if no data is received
        parsed_request = self.parser.parse(data)  # Parses the received data
        Executor().execute(parsed_request, self.connection_manager, self.lock)  # Executes the parsed request

    def receive_data(self):
        """Receives data from the client."""
        if not self.stop_flag:
            data = self.CONNECTION.recv(1024)  # Receives data from the client
            if data == b'':
                self.stop_flag = True  # Sets the stop flag if no data is received
                return None
            return data.decode("ascii")  # Decodes and returns the received data

    def stop(self):
        """Stops the reader."""
        self.stop_flag = True  # Sets the stop flag to terminate the reader
