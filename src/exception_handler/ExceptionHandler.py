from src.__models_for_all_layers.exceptions.APIKeyException import APIKeyException
from src.__models_for_all_layers.exceptions.UnknownClientException import UnknownClientException
from src.__models_for_all_layers.exceptions.UnknownException import UnknownException
from src.__models_for_all_layers.interfaces.IHandleClientException import IHandleClientException
from src.__models_for_all_layers.interfaces.IHandleException import IHandleException
from src.exception_handler.exception_handle_instructions.backend_except_handlers.UnknownExceptionHandler import \
    UnknownExceptionHandler
from src.exception_handler.exception_handle_instructions.client_except_handlers.ApiExceptionHandler import \
    ApiExceptionHandler
from src.exception_handler.exception_handle_instructions.client_except_handlers.UnknownClientExceptionHandler import \
    UnknownClientExceptionHandler
from src.program_layers.api_layer.http_server.connection_manager.ConnectionManager import ConnectionManager
from src.utils.SingletonMeta import SingletonMeta


class ExceptionHandler(IHandleException, IHandleClientException, metaclass=SingletonMeta):

    def __init__(self):
        self._client_exception_instructions: dict[BaseException:IHandleClientException] = {
            UnknownClientException: UnknownClientExceptionHandler(),
            APIKeyException: ApiExceptionHandler(),
        }
        self._exception_instructions: dict[BaseException:IHandleException] = {
            UnknownException: UnknownExceptionHandler()
        }

    def handle_exceptions(self, exception: BaseException):
        if type(exception) not in self._exception_instructions:
            self._exception_instructions[UnknownException].handle_exceptions(exception)
        self._exception_instructions[type(exception)].handle_exceptions(exception)  # type: ignore

    def handle_client_exception(self, exception: BaseException, connection_manager: ConnectionManager):
        if type(exception) not in self._client_exception_instructions:
            self._client_exception_instructions[UnknownClientException].handle_client_exception(exception,
                                                                                                connection_manager)
        self._client_exception_instructions[type(exception)].handle_client_exception(exception,  # type: ignore
                                                                                     connection_manager)
