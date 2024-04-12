from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse
from src.program_layers.api_layer.__models.interfaces.IParse import IParse
from src.program_layers.api_layer.parse_rules.Parse_APIKeyCheck import \
    Parse_APIKeyCheck
from src.program_layers.api_layer.parse_rules.Parse_Data import Parse_Data
from src.program_layers.api_layer.parse_rules.Parse_Parameters import \
    Parse_Parameters
from src.program_layers.api_layer.parse_rules.Parse_SetNoDataToNone import \
    Parse_SetNoDataToNone
from src.program_layers.api_layer.parse_rules.Parse_SetNoParamsToNone import \
    Parse_SetNoParamsToNone
from src.program_layers.api_layer.request_parser.RequestParser import RequestParser


class ParserFactory(IFactory):
    prasing_chain: [IChainParse] = [Parse_APIKeyCheck(), Parse_SetNoParamsToNone(), Parse_SetNoDataToNone(),
                                    Parse_Parameters(), Parse_Data()]

    def produce(self):
        return self._create_parser()

    def _create_parser(self) -> IParse:
        return RequestParser(parse_chain=self.prasing_chain)

    def register(self, chainParser: IChainParse):
        self.prasing_chain.append(chainParser)  # type: ignore
