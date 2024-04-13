from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.config_loader.ConfigLoader import ConfigLoader
from src.program_layers.database_layer.SimpleSQL import App as Orm
from src.program_layers.database_layer.SimpleSQL.package_src.Models.Configs.SimpleSQLDbConfig import SimpleSQLDbConfig


class OrmFactory(IFactory):
    def __init__(self):
        username = ConfigLoader().db_conf_loader.get_username()
        passwrd = ConfigLoader().db_conf_loader.get_password()
        hostname = ConfigLoader().db_conf_loader.get_db_host()
        port = ConfigLoader().db_conf_loader.get_port()
        db_name = ConfigLoader().db_conf_loader.get_db_name()
        char_set = ConfigLoader().db_conf_loader.get_char_set()

        self.db_config = SimpleSQLDbConfig(username, passwrd, hostname, port, db_name, char_set)

    def produce(self):
        return Orm(db_config=self.db_config)
