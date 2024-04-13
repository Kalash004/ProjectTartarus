import os

from src.__utils.SingletonMeta import SingletonMeta


class ConfigLoader(metaclass=SingletonMeta):
    """This loads parameters from config files"""

    def __init__(self):
        self.AUTHENTIFICATOR_CONF_FILE_PATH = os.path.join(os.path.dirname(__file__), "../../config/auth_conf.json")
        self.DATABASE_CONF_FILE_PATH = os.path.join(os.path.dirname(__file__), "../../config/database_connection_config.json.json")
        self.API_SERVER_FILE_PATH = os.path.join(os.path.dirname(__file__), "../../config/api_server.json")
        self.RULES_LOADER_CONFIG = os.path.join(os.path.dirname(__file__), "../../config/rules_to_load.json")

        self.API_SERVER_RUNNING_PORT_VAR_NAME = "api_server_running_port"
        self.API_SERVER_RUNNING_ADDRESS_VAR_NAME = "api_server_address"
        self.CONNECTION_LIFE_SEC_VAR_NAME = "connection_life_sec"
        self.API_KEYS_VAR_NAME = "api_keys"
        self.RULES_VAR_NAME = "rules"

    def get_auth_api_keys(self) -> [str]:
        return self.read_json_file(self.AUTHENTIFICATOR_CONF_FILE_PATH, self.API_KEYS_VAR_NAME)

    def get_database_parameters(self):
        raise NotImplemented

    def get_server_port(self) -> int:
        return self.read_json_file(self.API_SERVER_FILE_PATH, self.API_SERVER_RUNNING_PORT_VAR_NAME)[0]

    def get_server_address(self) -> str:
        return self.read_json_file(self.API_SERVER_FILE_PATH, self.API_SERVER_RUNNING_ADDRESS_VAR_NAME)[0]

    def get_server_listening_limit(self) -> int:
        raise NotImplemented

    def get_connection_life_sec(self) -> int:
        return self.read_json_file(self.API_SERVER_FILE_PATH, self.CONNECTION_LIFE_SEC_VAR_NAME)[0]

    def load_rule_names(self) -> [str]:
        return self.read_json_file(self.RULES_LOADER_CONFIG, self.RULES_VAR_NAME)

    @staticmethod
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
