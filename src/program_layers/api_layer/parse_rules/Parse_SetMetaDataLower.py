from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse


class Parse_SetMetaDataLower(IChainParse):
    def parse(self, data: dict[str]) -> dict[str]:
        data["apikey"] = data["apikey"].lower()
        data["event"] = data["event"].lower()
        data["table"] = data["table"].lower()
        return data
