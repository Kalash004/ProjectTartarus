from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__models_for_all_layers.exceptions.UnknownClientException import UnknownClientException
from src.program_layers.business_layer.__models.Interfaces.IRule import IRule
from src.program_layers.business_layer.business_layer_factories.RulesLoaderFactory import RulesLoaderFactory
from src.program_layers.business_layer.controller.TypeRules import TypeRules


class SingletonMeta:
    pass


class BusinessRuleController(metaclass=SingletonMeta):

    def __init__(self):
        self.rules_loader = RulesLoaderFactory().produce()
        self.rules_loader.load_plugins()
        # dict[table:dict[action type:Rule]]
        self.rules: dict[str:dict[str:[IRule]]] = {
            "admin_users": TypeRules(),
            "office_users": TypeRules(),
            "days": TypeRules(),
            "system_messages": TypeRules(),
            "system_log_ins": TypeRules(),
            "enterences_to_office": TypeRules()
        }

    def execute(self, parsed_request: ParsedRequest):
        rules = self.rules[parsed_request.table.lower()].types_dict[parsed_request.event.lower()]
        for rule in rules:
            rule.use()

    def register(self, rule_type, table, rule: IRule):
        if table not in self.rules.keys():
            # TODO: implement proper exception
            raise UnknownClientException(f"Table not in rule dict")
        rule_types = self.rules[table]
        rule_types.add_rule(rule_type, rule)
