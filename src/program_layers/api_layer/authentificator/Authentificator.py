from src.utils.Singleton import singleton


@singleton
class Authentificator:
    def __init__(self, config_file_path):
        self.file_path = config_file_path

    def check_api_key(self, key) -> bool:
        return key == self.__get_api_key()

    def __get_api_key(self) -> str:
        # todo: do key import
        return "testkey"
