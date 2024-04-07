import socket

from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.config_loader.ConfigLoader import ConfigLoader
from src.program_layers.api_layer.api_layer_factories.api_layer_sub_factories.answerer_factory.AnswererFactory import \
    AnswererFactory
from src.program_layers.api_layer.api_layer_factories.api_layer_sub_factories.api_server_factory.ApiServerFactory import \
    ApiServerFactory
from src.program_layers.api_layer.api_layer_factories.api_layer_sub_factories.authentificator_factory.AuthentificatorFactory import \
    AuthentificatorFactory
from src.program_layers.api_layer.api_layer_factories.api_layer_sub_factories.connection_manager_factory.ConnectionManagerFactory import \
    ConnectionManagerFactory
from src.program_layers.api_layer.api_layer_factories.api_layer_sub_factories.reader_factory.ReaderFactory import \
    ReaderFactory
from src.program_layers.api_layer.api_layer_factories.api_layer_sub_factories.request_parser_factory.ParserFactory import \
    ParserFactory
from src.utils.SingletonMeta import SingletonMeta


class ApiLayerFactory(metaclass=SingletonMeta):
    def __init__(self):
        self.__CONF_LOADER = ConfigLoader()
        self.__SERVER_PORT = self.__CONF_LOADER.get_server_port()
        self.__SERVER_ADDRESS = self.__CONF_LOADER.get_server_address()
        self.__AUTH_FILE_PATH = self.__CONF_LOADER.get_authentification_file_path()
        self.CONNECTION_LIVE_TIME_SEC = self.__CONF_LOADER.get_connection_life_sec()

        self.factory_holder: [IFactory] = []  # note: Might not be needed

    def produce_api_server_factory(self) -> IFactory:
        api_server_factory = ApiServerFactory(port=self.__SERVER_PORT, address=self.__SERVER_ADDRESS)
        self.factory_holder.append(api_server_factory)
        return api_server_factory

    def produce_parser_factory(self) -> IFactory:
        parser_factory = ParserFactory()
        self.factory_holder.append(parser_factory)
        return parser_factory

    def produce_auth_factory(self) -> IFactory:
        auth_factory = AuthentificatorFactory(filepath=self.__AUTH_FILE_PATH)
        self.factory_holder.append(auth_factory)
        return auth_factory

    def produce_answerer_factory(self, connection: socket.socket, address: str) -> IFactory:
        answerer_factory = AnswererFactory(connection=connection, address=address,
                                           life_time_sec=self.CONNECTION_LIVE_TIME_SEC)
        self.factory_holder.append(answerer_factory)
        return answerer_factory

    def produce_reader_factory(self, connection: socket.socket, address: str) -> IFactory:
        parser = self.produce_parser_factory().produce()
        reader_factory = ReaderFactory(connection=connection, address=address,
                                       life_time_sec=self.CONNECTION_LIVE_TIME_SEC, parser=parser)
        self.factory_holder.append(reader_factory)
        return reader_factory

    def produce_connection_manager_factory(self, connection: socket.socket, address: str) -> IFactory:
        connection_manager_factory = ConnectionManagerFactory(connection, address)
        self.factory_holder.append(connection_manager_factory)
        return connection_manager_factory
