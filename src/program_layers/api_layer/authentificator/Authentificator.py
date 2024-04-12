from src.__utils.SingletonMeta import SingletonMeta


class Authentificator(metaclass=SingletonMeta):
    """
    This is used to authentificate requests from clients
    """

    def __init__(self, api_keys):
        self.api_keys = api_keys

    def check_api_key(self, key) -> bool:
        """
        This checks if given api key is the same as in config file
        :param key: Api key from client
        :return: True if the key is same
        """
        return key in self.api_keys
