from src.program_layers.api_layer.__models.enums.ProtocolEnum import ProtocolEnum
from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse


class Parse_SetNoDataToNone(IChainParse):
    def parse(self, data: dict[str]) -> dict[str]:
        if ProtocolEnum.DATA.value not in data:
            data[ProtocolEnum.DATA.value] = None
        return data
