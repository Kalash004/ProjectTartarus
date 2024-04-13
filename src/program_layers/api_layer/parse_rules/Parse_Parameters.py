from src.program_layers.api_layer.__models.enums.ProtocolEnum import ProtocolEnum
from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse


class Parse_Parameters(IChainParse):
    def parse(self, data: dict[str]) -> dict[str]:
        if data[ProtocolEnum.PARAMS.value] is None:
            return data
        param_data: str = data[ProtocolEnum.PARAMS.value]
        param_data = param_data.removeprefix("(")
        param_data = param_data.removesuffix(")")
        params = param_data.split(",")
        params_dict = {}
        for param in params:
            key_val_param = param.split("=")
            params_dict[key_val_param[0].lower()] = key_val_param[1]
        data[ProtocolEnum.PARAMS.value] = params_dict
        return data
