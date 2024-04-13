from src.__models_for_all_layers.exceptions.APIKeyException import APIKeyException
from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse

from src.program_layers.api_layer.factory.AuthentificatorFactory import \
    AuthentificatorFactory


class Parse_APIKeyCheck(IChainParse):
    def __init__(self):
        self.authentificator = AuthentificatorFactory().produce()

    def parse(self, data: dict[str]) -> dict[str]:
        if not data["apikey"]:
            raise APIKeyException("API Key was not found")
        recived_key = data["apikey"].lower()
        if not self.authentificator.check_api_key(recived_key):
            raise APIKeyException("API Key was wrong")
        return data
