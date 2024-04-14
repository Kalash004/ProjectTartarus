from src.__models_for_all_layers.exceptions.BadConnectionProtocolException import BadConnectionProtocolException
from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse


class Parse_CheckEventExists(IChainParse):
    events = ["post", "get", "delete", "update"]

    def parse(self, data: dict[str]) -> dict[str]:
        if "event" not in data.keys():
            raise BadConnectionProtocolException(f"Request doesnt contain must have part EVENT")
        if data["event"] not in self.events:
            raise BadConnectionProtocolException(f"No such event exists: '{data['event']}'")
        return data
