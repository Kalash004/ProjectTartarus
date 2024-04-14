from src.__models_for_all_layers.interfaces.IHandleException import IHandleException


class UnknownExceptionHandler(IHandleException):
    # TODO: Make better
    def handle_exceptions(self, exception: BaseException):
        pass
