from src.__models_for_all_layers.exceptions.UnknownClientException import UnknownClientException
from src.program_layers.business_layer.__models.Interfaces.IRule import IRule


class TypeRules:

    def __init__(self):
        self.types_dict: dict[str:[IRule]] = {
            "get": [],
            "post": [],
            "delete": [],
            "update": []
        }

    def add_rule(self, event_type: str, object: IRule):
        if event_type not in self.types_dict.keys():
            raise UnknownClientException(f"Table not in type dict")
        self.types_dict[event_type].append(object)
