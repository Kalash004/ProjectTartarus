import re

from src.program_layers.api_layer.__models.enums.ProtocolEnum import ProtocolEnum
from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse


class Parse_Data(IChainParse):
    def parse(self, data: dict[str]) -> dict[str]:
        data_body = data[ProtocolEnum.DATA.value]
        if not data_body:
            return data
        pattern = r'\{(.*?)\}'

        # Find all matches
        matches = re.findall(pattern, data_body)

        # Parse each match as a dictionary
        result = [dict(kv.split(':') for kv in match.split(',')) for match in matches]

        data[ProtocolEnum.DATA.value] = result
        return data
