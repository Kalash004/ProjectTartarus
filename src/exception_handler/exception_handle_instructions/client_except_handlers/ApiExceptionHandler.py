from src.__models_for_all_layers.interfaces.IHandleClientException import IHandleClientException
from src.__response_builder.ResponseBuilder import ResponseBuilder
from src.program_layers.api_layer.commands.CloseConnectionCommand import CloseConnectionCommand
from src.program_layers.api_layer.commands.DisplayErrorCommand import DisplayErrorCommand


class ApiExceptionHandler(IHandleClientException):
    """Deprecated untill i find a better way"""

    def handle_exception_inform_client(self, exception: BaseException, connection_manager):
        message = ResponseBuilder().build_error("client")
        DisplayErrorCommand(message, connection_manager).execute()
        CloseConnectionCommand(connection_manager).execute()
