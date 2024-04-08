from src.program_layers.api_layer.__models.enums.ProtocolEnum import ProtocolEnum
from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse


class Parse_SetNoParamsToNone(IChainParse):

    def parse(self, data: dict[str]) -> dict[str]:
        if ProtocolEnum.PARAMS.value not in data:
            data[ProtocolEnum.PARAMS.value] = None
        return data
