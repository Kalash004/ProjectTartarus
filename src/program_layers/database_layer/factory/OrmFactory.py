from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.config_loader.ConfigLoader import ConfigLoader
from src.program_layers.database_layer.SimpleSQL import App as Orm
from src.program_layers.database_layer.SimpleSQL.package_src.Models.Configs.SimpleSQLDbConfig import SimpleSQLDbConfig


class OrmFactory(IFactory):
    """
    A factory class for creating ORM instances.
    """

    def __init__(self):
        """
        Initializes the OrmFactory with the database configuration.
        """
        # Retrieves database configuration parameters using ConfigLoader
        username = ConfigLoader().db_conf_loader.get_username()
        passwrd = ConfigLoader().db_conf_loader.get_password()
        hostname = ConfigLoader().db_conf_loader.get_db_host()
        port = ConfigLoader().db_conf_loader.get_port()
        db_name = ConfigLoader().db_conf_loader.get_db_name()
        char_set = ConfigLoader().db_conf_loader.get_char_set()

        # Creates a database configuration object
        self.db_config = SimpleSQLDbConfig(username, passwrd, hostname, port, db_name, char_set)

    def produce(self):
        """
        Produces and returns an instance of the ORM.

        Returns:
        - Orm: An instance of the ORM.
        """
        return Orm(db_config=self.db_config)
