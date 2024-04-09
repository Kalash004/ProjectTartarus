from src.__models_for_all_layers.interfaces.IHandleException import IHandleException


class BadConnectionHandling(IHandleException):
    def handle_exceptions(self, exception: Exception):
        raise NotImplemented
