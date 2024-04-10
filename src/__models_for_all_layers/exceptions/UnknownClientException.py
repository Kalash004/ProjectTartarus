from src.__models_for_all_layers.exceptions.BaseExceptions.ClientBaseException import ClientBaseException


class UnknownClientException(ClientBaseException):
    def __init__(self):
        pass
