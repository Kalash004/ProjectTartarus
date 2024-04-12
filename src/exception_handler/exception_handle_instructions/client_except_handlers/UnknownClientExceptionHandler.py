from src.__models_for_all_layers.interfaces.IHandleClientException import IHandleClientException
from src.program_layers.api_layer.commands.DisplayErrorCommand import DisplayErrorCommand


class UnknownClientExceptionHandler(IHandleClientException):
    def handle_client_exception(self, exception: BaseException, connection_manager):
        DisplayErrorCommand(f"An unknown exception has happened: {exception.args[0]}", connection_manager).execute()
