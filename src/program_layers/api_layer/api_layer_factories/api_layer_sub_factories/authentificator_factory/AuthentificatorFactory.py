from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.program_layers.api_layer.authentificator.Authentificator import Authentificator
from src.utils.SingletonMeta import SingletonMeta


class AuthentificatorFactory(metaclass=SingletonMeta, IFactory):
    """
    This is factory for authentificator object
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def produce(self):
        return Authentificator(self.filepath)
