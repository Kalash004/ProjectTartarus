from src.__models_for_all_layers.exceptions.BaseExceptions.ClientBaseException import ClientBaseException


class BusinessRuleNotPassedException(ClientBaseException):
    def __init__(self, msg):
        self.msg = msg
