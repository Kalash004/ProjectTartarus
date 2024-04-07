from src.__models_for_all_layers.exceptions.APIKeyException import APIKeyException
from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse
from src.program_layers.api_layer.api_layer_factories.api_layer_sub_factories.a_main_api_layer_factory.ApiLayerFactory import \
    ApiLayerFactory


class Parse_APIKeyCheck(IChainParse):
    def __init__(self):
        self.authentificator = ApiLayerFactory().produce_auth_factory().produce()

    def parse(self, data: dict[str]) -> dict[str]:
        if not data["apikey"]:
            raise APIKeyException("API Key was not found")
        recived_key = data["apikey"].lower()
        if not self.authentificator.check_api_key(recived_key):
            raise APIKeyException("API Key was wrong")
        return data
