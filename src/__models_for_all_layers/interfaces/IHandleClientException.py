import abc

from src.program_layers.api_layer.http_server.connection_manager.ConnectionManager import ConnectionManager


class IHandleClientException:

    @abc.abstractmethod
    def handle_client_exception(self, exception: BaseException, connection_manager: ConnectionManager):
        raise NotImplemented
