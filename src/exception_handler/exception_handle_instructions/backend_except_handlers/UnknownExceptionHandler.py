from src.__models_for_all_layers.interfaces.IHandleException import IHandleException


class UnknownExceptionHandler(IHandleException):
    def handle_exceptions(self, exception: BaseException):
        # TODO: Add some kind of logging
        raise NotImplemented
