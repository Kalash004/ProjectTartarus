from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse
from src.program_layers.api_layer.__models.interfaces.IParse import IParse
from src.program_layers.api_layer.request_parser.RequestParser import RequestParser
from src.utils.Singleton import singleton
from src.program_layers.api_layer.authentificator.Authentificator import Authentificator

@singleton
class ParserFactory:

    def create_parser(self, parsing_chain: [IChainParse]) -> IParse:
        authentificator = Authentificator()
        return RequestParser()
