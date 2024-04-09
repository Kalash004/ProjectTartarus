from src.__models_for_all_layers.interfaces.IHandleClientException import IHandleClientException


class UnknownClientExceptionHandler(IHandleClientException):
    def handle_client_exception(self, exception: BaseException, connection_manager):
        connection_manager.answerer.send_specific_message(f"An unknown exception has happened: {exception.args[0]}")
