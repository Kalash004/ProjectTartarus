import socket

from src.config_loader.ConfigLoader import ConfigLoader
from src.program_layers.api_layer.api_layer_factories.connection_manager_factory.ConnectionManagerFactory import \
    ConnectionManagerFactory
from src.program_layers.api_layer.http_server.connection_manager.ConnectionManager import ConnectionManager
from src.utils.SingletonMeta import SingletonMeta


class APIServer(metaclass=SingletonMeta):
    """This accepts the requests from clients,
    creates a ConnectionManager object which then manages given connection"""
    CONFIG_LOADER_SINGLETON = ConfigLoader()

    def __init__(self, adress: str, port: int):
        # self.HTTP_REQ_REGEX: re.Pattern = re.compile(r"^([A-Z]+)\s*(.*)(\s+HTTP/\\d\\.\\d)$")
        self.PORT: int = port
        self.ADRESS: str = adress
        self.stop: bool = False
        self.connections: [ConnectionManager] = []

    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _soc:
                _soc.bind((self.ADRESS, self.PORT))
                _soc.listen(5)
                print(f"Running on {self.ADRESS}:{self.PORT}")
                while not self.stop:
                    connection, addres = _soc.accept()
                    connection_manager = ConnectionManagerFactory(connection, addres).produce()
                    connection_manager.start()
                    self.connections.append(connection_manager)
        except Exception as e:
            # TODO: try catch
            print(e)

    def stop(self):
        self.stop = True
        for conns in self.connections:
            conns.stop()


def __get_port_from_config(self) -> int:
    # self.CONFIG_LOADER_SINGLETON
    pass


def __get_host_from_config(self) -> str:
    pass


def __get_listening_limit(self) -> int:
    pass
