import os

from src.__utils.SingletonMeta import SingletonMeta


def read_json_file(path: str, var_name: str) -> [int | str]:
    import json
    with open(path, "r") as file:
        response = []
        data = json.load(file)
        if type(data[var_name]) is list:
            for i in data[var_name]:
                response.append(i)
            return response
        response = [data[var_name]]
        return response


class AuthLoader(metaclass=SingletonMeta):
    def __init__(self, path):
        self.FILE_PATH = path
        self.__API_KEYS_VAR_NAME = "api_keys"

    def get_auth_api_keys(self) -> [str]:
        return read_json_file(self.FILE_PATH, self.__API_KEYS_VAR_NAME)


class DatabaseLoader(metaclass=SingletonMeta):
    def __init__(self, path):
        self.FILE_PATH = path

    def get_username(self) -> str:
        return read_json_file(self.FILE_PATH, "username")[0]

    def get_password(self) -> str:
        return read_json_file(self.FILE_PATH, "password")[0]

    def get_db_host(self) -> str:
        return read_json_file(self.FILE_PATH, "database_host")[0]

    def get_port(self) -> int:
        return read_json_file(self.FILE_PATH, "port")[0]

    def get_db_name(self) -> str:
        return read_json_file(self.FILE_PATH, "database_name")[0]

    def get_char_set(self) -> str:
        return read_json_file(self.FILE_PATH, "char_set")[0]


class ApiLoader:
    def __init__(self, path):
        self.FILE_PATH = path

    def get_port(self) -> int:
        return read_json_file(self.FILE_PATH, "api_server_running_port")[0]

    def get_host(self) -> str:
        return read_json_file(self.FILE_PATH, "api_server_address")[0]

    def get_connection_timeout_sec(self) -> int:
        return read_json_file(self.FILE_PATH, "connection_life_sec")


class RuleConfLoader:
    def __init__(self, path):
        self.FILE_PATH = path

    def load_rule_names(self) -> [str]:
        return read_json_file(self.FILE_PATH, "rules")


class ConfigLoader(metaclass=SingletonMeta):
    """This loads parameters from config files"""

    def __init__(self):
        self.__AUTHENTIFICATOR_CONF_FILE_PATH = os.path.join(os.path.dirname(__file__), "../../config/auth_conf.json")
        self.__DATABASE_CONF_FILE_PATH = os.path.join(os.path.dirname(__file__), "../../config/database_connection_config.json.json")
        self.__API_SERVER_FILE_PATH = os.path.join(os.path.dirname(__file__), "../../config/api_server.json")
        self.__RULES_LOADER_CONFIG = os.path.join(os.path.dirname(__file__), "../../config/rules_to_load.json")

        self.auth_conf_loader = AuthLoader(self.__AUTHENTIFICATOR_CONF_FILE_PATH)
        self.db_conf_loader = DatabaseLoader(self.__DATABASE_CONF_FILE_PATH)
        self.api_conf_loader = ApiLoader(self.__API_SERVER_FILE_PATH)
        self.rule_conf_loader = RuleConfLoader(self.__RULES_LOADER_CONFIG)
