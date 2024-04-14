from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__models_for_all_layers.exceptions.BadConnectionProtocolException import BadConnectionProtocolException
from src.program_layers.api_layer.__models.enums.ProtocolEnum import ProtocolEnum
from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse
from src.program_layers.api_layer.__models.interfaces.IParse import IParse


class RequestParser(IParse):
    def __init__(self, parse_chain: [IChainParse]):
        self.DELIMITER = ";"
        self.parse_chain = parse_chain

    def parse(self, data: str) -> ParsedRequest:
        data = data.rstrip()
        data = data.lstrip()
        data = data.rstrip("/r/n")
        data = data.rstrip(";")
        dictionary = self.split_to_key_value(self.split_to_lines(data))
        for parse_class in self.parse_chain:
            dictionary = parse_class.parse(dictionary)
        return ParsedRequest(dictionary[ProtocolEnum.EVENT.value], dictionary[ProtocolEnum.TABLE.value],
                             dictionary[ProtocolEnum.PARAMS.value], dictionary[ProtocolEnum.DATA.value])

    def split_to_lines(self, data: str):
        return data.split(self.DELIMITER)

    @staticmethod
    def split_to_key_value(lines: [str]):
        dictionary = {}
        for line in lines:
            key_value = line.split("=", 1)
            if len(key_value) != 2:
                raise BadConnectionProtocolException("Format key=value was not met")
            key = key_value[0].lower()
            value = key_value[1]
            dictionary[key] = value
        return dictionary
