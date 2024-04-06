from src.utils import SingletonMeta


class ConfigLoader(metaclass=SingletonMeta):
    AUTHENTIFICATOR_CONF_FILE_PATH = None
    DATABASE_CONF_FILE_PATH = None

    def get_authentification_parameters(self):
        raise NotImplemented

    def get_database_parameters(self):
        raise NotImplemented

    def get_server_port(self) -> int:
        raise NotImplemented

    def get_server_hostname(self) -> str:
        raise NotImplemented

    def get_server_listening_limit(self) -> int:
        raise NotImplemented
