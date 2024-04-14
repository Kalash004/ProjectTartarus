from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.__utils.SingletonMeta import SingletonMeta
from src.config_loader.ConfigLoader import ConfigLoader
from src.program_layers.api_layer.main_api_server.APIServer import APIServer


class ApiServerFactory(IFactory, metaclass=SingletonMeta):
    def __init__(self):
        try:
            self.port = ConfigLoader().api_conf_loader.get_port()
            self.address = ConfigLoader().api_conf_loader.get_host()
            self.max_cons = ConfigLoader().api_conf_loader.get_max_connections()
        except Exception as e:
            # TODO: new handle
            # Possible missing file exception
            pass

    def produce(self):
        return APIServer(port=self.port, adress=self.address, maximum_connections=self.max_cons)
