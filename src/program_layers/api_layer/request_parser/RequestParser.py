from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__models_for_all_layers.exceptions.APIKeyException import APIKeyException
from src.__models_for_all_layers.exceptions.BadConnectionProtocolException import BadConnectionProtocolException
from src.program_layers.api_layer.__models.enums.ProtocolEnum import ProtocolEnum
from src.program_layers.api_layer.__models.interfaces.IParserBehaviour import IParserBehaviour
from src.program_layers.api_layer.authentificator.Authentificator import Authentificator


class RequestParser(IParserBehaviour):
    def __init__(self, authentificator: Authentificator):
        self.DELIMITER = ";"
        self.parse_chain = []
        self.authentificator = authentificator
        self.add_method(self.api_key_check).add_method(self.set_no_params_none).add_method(
            self.set_no_data_none).add_method(self.parse_params)

    def parse(self, data: str) -> ParsedRequest:
        dictionary = self.split_to_key_value(self.split_to_lines(data))
        for method in self.parse_chain:
            method(dictionary)
        return ParsedRequest(dictionary[ProtocolEnum.EVENT.value], dictionary[ProtocolEnum.TABLE.value],
                             dictionary[ProtocolEnum.PARAMS.value], dictionary[ProtocolEnum.DATA.value])

    def add_method(self, func):
        self.parse_chain.append(func)
        return self

    def split_to_lines(self, data: str):
        return data.split(self.DELIMITER)

    def api_key_check(self, data: dict[str]):
        if not data["apikey"]:
            raise APIKeyException("API Key was not found")
        recived_key = data["apikey"].lower()
        if not self.authentificator.check_api_key(recived_key):
            raise APIKeyException("API Key was wrong")

    @staticmethod
    def split_to_key_value(lines: [str]):
        dictionary = {}
        for line in lines:
            key_value = line.split("=", 1)
            if len(key_value) != 2:
                raise BadConnectionProtocolException("Format key=value was not met")
            dictionary[key_value[0].lower()] = key_value[1]
        return dictionary

    @staticmethod
    def set_no_data_none(data: dict[str]):
        if not ProtocolEnum.DATA.value in data:
            data[ProtocolEnum.DATA.value] = None

    @staticmethod
    def set_no_params_none(data: dict[str]):
        if not ProtocolEnum.PARAMS.value in data:
            data[ProtocolEnum.PARAMS.value] = None

    @staticmethod
    def parse_params(data: dict[str]):
        if data[ProtocolEnum.PARAMS.value] is None:
            return
        params = data[ProtocolEnum.PARAMS.value].split(",")
        params_dict = {}
        for param in params:
            key_val_param = param.split("=")
            params_dict[key_val_param[0]] = key_val_param[1]
        data[ProtocolEnum.PARAMS.value] = params_dict
