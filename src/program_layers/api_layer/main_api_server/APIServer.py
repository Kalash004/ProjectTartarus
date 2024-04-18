import socket

# Importing specific classes and methods from various modules
from src.__models_for_all_layers.exceptions.BaseExceptions.ServiceBaseException import ServiceBaseException
from src.__utils.SingletonMeta import SingletonMeta
from src.config_loader.ConfigLoader import ConfigLoader
from src.exception_handler.ExceptionHandler import ExceptionHandler
from src.program_layers.api_layer.factory.ConnectionManagerFactory import ConnectionManagerFactory


class APIServer(metaclass=SingletonMeta):
    """This class represents the API server, which accepts requests from clients."""
    CONFIG_LOADER_SINGLETON = ConfigLoader()

    def __init__(self, address: str, port: int, maximum_connections: int):
        """
        Initializes the APIServer with the provided address, port, and maximum connections.

        Args:
        - address (str): The IP address on which the server will listen.
        - port (int): The port on which the server will listen.
        - maximum_connections (int): The maximum number of simultaneous connections the server will accept.
        """
        self.PORT: int = port
        self.ADRESS: str = address  # Corrected spelling from 'adress' to 'address'
        self.stop: bool = False  # Flag to control server termination
        self.max_conns = maximum_connections
        self.connections = []  # List to store active connections

    def run(self):
        """Starts the server and listens for incoming connections."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _soc:
                _soc.bind((self.ADRESS, self.PORT))  # Binds the socket to the provided address and port
                _soc.listen(self.max_conns)  # Listens for incoming connections with a maximum backlog of 5
                print(f"Running on {self.ADRESS}:{self.PORT}")
                while not self.stop:  # Continuously accepts connections until 'stop' flag is set
                    connection, address = _soc.accept()  # Accepts incoming connection
                    connection_manager = ConnectionManagerFactory(connection,
                                                                  address).produce()  # Creates a connection manager for the accepted connection
                    connection_manager.start()  # Starts the connection manager
                    self.connections.append(connection_manager)  # Adds the connection manager to the list of active connections
        except ServiceBaseException as e:  # Handles service-specific exceptions
            ExceptionHandler().handle_exceptions(e)

    def stop(self):
        """Stops the server."""
        self.stop = True  # Sets the 'stop' flag to terminate the server
        for conn in self.connections:
            conn.stop_flag()  # Stops all active connections

# The following methods are not utilized in the current implementation of the APIServer class. They seem to be placeholders for future use.

# def __get_port_from_config(self) -> int:
#     # self.CONFIG_LOADER_SINGLETON
#     pass

# def __get_host_from_config(self) -> str:
#     pass

# def __get_listening_limit(self) -> int:
#     pass