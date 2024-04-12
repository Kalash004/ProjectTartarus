from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.config_loader.ConfigLoader import ConfigLoader
from src.program_layers.api_layer.authentificator.Authentificator import Authentificator
from src.__utils.SingletonMeta import SingletonMeta


class AuthentificatorFactory(IFactory, metaclass=SingletonMeta):
    """
    This is factory for authentificator object
    """

    def __init__(self):
        self.api_keys = ConfigLoader().get_auth_api_keys()

    def produce(self):
        return Authentificator(self.api_keys)
