from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.program_layers.business_layer.__models.Interfaces.IPlugin import IPlugin
from src.program_layers.business_layer.__models.Interfaces.IRule import IRule
from src.program_layers.business_layer.controller.BusinessRuleController import BusinessRuleController


class Rule_NameCantBeTony(IRule, IPlugin):
    """Testing rule - doenst allow creating users with name Tony"""

    def __init__(self):
        self.rule_type = "post"
        self.rule_table = "admin_users"

    def initialize(self) -> None:
        BusinessRuleController().register(self.rule_type, self.rule_table, self)

    def use(self, request: ParsedRequest):
