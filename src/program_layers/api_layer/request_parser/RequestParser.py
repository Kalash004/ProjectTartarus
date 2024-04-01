from src.models_for_all_layers.exceptions.APIKeyException import APIKeyException
from src.models_for_all_layers.exceptions.BadConnectionProtocolException import BadConnectionProtocolException
from src.program_layers.api_layer.authentificator.Authentificator import Authentificator
from src.program_layers.api_layer.models.interfaces.IParserBehaviour import IParserBehaviour


class RequestParser(IParserBehaviour):
    def __init__(self, authentificator: Authentificator):
        self.DELIMITER = ";"
        self.method_chain = []
        self.authentificator = authentificator
        self.add_method(self.api_key_check)

    def parse(self, data: str):
        lines = self.split_to_lines(data)
        dictionary = self.split_to_key_value(lines)
        for method in self.method_chain:
            method(dictionary)

    def add_method(self, func):
        self.method_chain.append(func)
        return self

    def split_to_lines(self, data: str):
        return data.split(self.DELIMITER)

    def api_key_check(self, data: dict):
        if not data["apikey"]:
            raise APIKeyException("API Key was not found")
        recived_key = data["apikey"].lower()
        if not self.authentificator.check_api_key(recived_key):
            raise APIKeyException("API Key was wrong")

    def split_to_key_value(self, lines: [str]):
        dictionary = {}
        for line in lines:
            key_value = line.split("=", 1)
            if len(key_value) != 2:
                raise BadConnectionProtocolException("Format key=value was not met")
            dictionary[key_value[0].lower()] = key_value[1]
        return dictionary
