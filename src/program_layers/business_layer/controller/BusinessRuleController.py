from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.program_layers.business_layer.__models.Interfaces.IRule import IRule
from src.program_layers.business_layer.business_layer_factories.RulesLoaderFactory import RulesLoaderFactory


class BusinessRuleController:

    def __init__(self):
        self.rules_loader = RulesLoaderFactory().produce()
        self.rules_loader.load_plugins()
        self.rules: [IRule] = []

    def execute(self, parsed_request: ParsedRequest):
        pass
