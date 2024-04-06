from src.config_loader.ConfigLoader import ConfigLoader
from src.utils.SingletonMeta import SingletonMeta


class Authentificator(metaclass=SingletonMeta):
    conf_loader = ConfigLoader()

    def __init__(self):
        # TODO: implement
        self.file_path = self.conf_loader.get_authentification_parameters()

    def check_api_key(self, key) -> bool:
        return key == self.__get_api_key()

    def __get_api_key(self) -> str:
        # todo: do key import
        return "testkey"
