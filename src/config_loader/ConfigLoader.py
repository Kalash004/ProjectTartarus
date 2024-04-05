from src.utils.Singleton import singleton


@singleton
class ConfigLoader:
    AUTHENTIFICATOR_CONF_FILE_PATH = None
    DATABASE_CONF_FILE_PATH = None

    def get_authentification_parameters(self):
        raise NotImplemented

    def get_database_parameters(self):
        raise NotImplemented
