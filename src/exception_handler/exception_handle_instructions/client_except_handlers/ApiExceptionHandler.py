from src.__models_for_all_layers.interfaces.IHandleClientException import IHandleClientException
from src.program_layers.api_layer.commands.DisplayErrorCommand import DisplayErrorCommand


class ApiExceptionHandler(IHandleClientException):
    def handle_client_exception(self, exception: BaseException, connection_manager):
        DisplayErrorCommand(f"Api key was not specified or was wrong {exception.args}", connection_manager).execute()
