from src.utils.SingletonMeta import SingletonMeta


class Authentificator(metaclass=SingletonMeta):
    """
    This is used to authentificate requests from clients
    """

    def __init__(self, filepath):
        self.file_path = filepath

    def check_api_key(self, key) -> bool:
        """
        This checks if given api key is the same as in config file
        :param key: Api key from client
        :return: True if the key is same
        """
        return key == self.__get_api_key()

    def __get_api_key(self) -> str:
        """
        Reads data file and obtains current api key
        :return: Api key
        """
        # todo: do key import
        return "testkey"
