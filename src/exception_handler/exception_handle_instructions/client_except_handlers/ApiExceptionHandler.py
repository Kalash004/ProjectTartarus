from src.__models_for_all_layers.interfaces.IHandleClientException import IHandleClientException


class ApiExceptionHandler(IHandleClientException):
    def handle_client_exception(self, exception: BaseException, connection_manager):
        connection_manager.answerer.send_specific_message(f"Api key was not specified or was wrong {exception.args}")
