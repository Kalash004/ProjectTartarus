from src.__models_for_all_layers.exceptions.BaseExceptions.ServiceBaseException import ServiceBaseException


class UnknownException(ServiceBaseException):
    def __init__(self, msg):
        self.msg = msg
