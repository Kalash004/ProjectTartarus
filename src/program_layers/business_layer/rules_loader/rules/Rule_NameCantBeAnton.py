from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__models_for_all_layers.exceptions.BusinessRuleNotPassedException import BusinessRuleNotPassedException
from src.program_layers.business_layer.__models.Interfaces.IPlugin import IPlugin
from src.program_layers.business_layer.__models.Interfaces.IRule import IRule


class Rule_NameCantBeAnton(IRule, IPlugin):
    """Testing rule - doenst allow creating users with name Tony"""

    def __init__(self):
        self.rule_type = "post"
        self.rule_table = "admin_users"

    def initialize(self, controller) -> None:
        controller.register(self.rule_type, self.rule_table, self)

    def use(self, request: ParsedRequest):
        for data in request.data:
            if data["name"].lower() == "anton":
                # TODO: Better exception
                raise BusinessRuleNotPassedException(f"Request had name Anton in data {request.data}")
