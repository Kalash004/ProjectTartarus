from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.config_loader.ConfigLoader import ConfigLoader
from src.program_layers.api_layer.http_server.APIServer import APIServer
from src.utils.SingletonMeta import SingletonMeta


class ApiServerFactory(IFactory, metaclass=SingletonMeta):
    def __init__(self):
        self.port = ConfigLoader().get_server_port()
        self.address = ConfigLoader().get_server_address()

    def produce(self):
        return APIServer(port=self.port, adress=self.address)
