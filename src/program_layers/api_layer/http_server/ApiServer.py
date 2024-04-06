import socket

from src.config_loader.ConfigLoader import ConfigLoader
from src.program_layers.api_layer.http_server.ConnectionManager import ConnectionManager


class APIServer:
    """This accepts the requests from clients,
    creates a ConnectionManager object which then manages given connection"""
    CONFIG_LOADER_SINGLETON = ConfigLoader()

    def __init__(self, host: str, port: int):
        # self.HTTP_REQ_REGEX: re.Pattern = re.compile(r"^([A-Z]+)\s*(.*)(\s+HTTP/\\d\\.\\d)$")
        self.PORT: int = self.__get_port_from_config()
        self.HOST: str = self.__get_host_from_config()
        self.stop: bool = False
        self.connections: [ConnectionManager] = []

    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _soc:
                _soc.bind((self.HOST, self.PORT))
                _soc.listen(self.__get_listening_limit())
                print(f"Running on {self.HOST}:{self.PORT}")
                while not self.stop:
                    connection, addres = _soc.accept()
                    connection_manager = ConnectionManager(connection, addres)
                    connection_manager.start()
                    self.connections.append(connection_manager)
        except:
            # TODO: try catch
            pass

    def stop(self):
        self.stop = True

    def __get_port_from_config(self) -> int:
        # self.CONFIG_LOADER_SINGLETON
        pass

    def __get_host_from_config(self) -> str:
        pass

    def __get_listening_limit(self) -> int:
        pass
