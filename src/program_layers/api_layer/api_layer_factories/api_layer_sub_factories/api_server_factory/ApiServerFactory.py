from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.program_layers.api_layer.http_server.api_server.APIServer import APIServer
from src.utils.SingletonMeta import SingletonMeta


class ApiServerFactory(metaclass=SingletonMeta, IFactory):
    def __init__(self, port: int, address: str):
        self.port = port
        self.address = address

    def produce(self):
        return APIServer(port=self.port, adress=self.address)
