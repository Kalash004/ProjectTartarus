from src.__models_for_all_layers.interfaces.IHandleClientException import IHandleClientException
from src.program_layers.api_layer.http_server.connection_manager.ConnectionManager import ConnectionManager


class UnknownClientExceptionHandler(IHandleClientException):
    def handle_client_exception(self, exception: BaseException, connection_manager: ConnectionManager):
        # TODO: Add unknown exception handling
        print(f"Unknown exception handling: {exception.args}")
        raise NotImplemented
