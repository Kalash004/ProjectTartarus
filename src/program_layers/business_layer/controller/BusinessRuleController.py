from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__models_for_all_layers.exceptions.UnknownClientException import UnknownClientException
from src.__utils.SingletonMeta import SingletonMeta
from src.program_layers.business_layer.__models.Interfaces.IRule import IRule
from src.program_layers.business_layer.controller.TypeRules import TypeRules
from src.program_layers.business_layer.factory.RulesLoaderFactory import RulesLoaderFactory


class BusinessRuleController(metaclass=SingletonMeta):
    """
    Singleton class responsible for managing and executing business rules based on parsed requests.
    """

    def __init__(self):
        """
        Initializes the BusinessRuleController.

        - Initializes rules dictionary with table names as keys and TypeRules instances as values.
        - Initializes the RulesLoader to load plugins.
        """
        self.rules: dict[str:dict[str:[IRule]]] = {
            "admin_users": TypeRules(),  # Initializing TypeRules for admin_users table
            "office_users": TypeRules(),  # Initializing TypeRules for office_users table
            "days": TypeRules(),  # Initializing TypeRules for days table
            "system_messages": TypeRules(),  # Initializing TypeRules for system_messages table
            "system_log_ins": TypeRules(),  # Initializing TypeRules for system_log_ins table
            "enterences_to_office": TypeRules()  # Initializing TypeRules for enterences_to_office table
        }
        self.rules_loader = RulesLoaderFactory(self).produce()  # Creating RulesLoader instance
        self.rules_loader.load_plugins()  # Loading plugins using RulesLoader

    def execute(self, parsed_request: ParsedRequest):
        """
        Executes business rules for the given parsed request.

        Args:
        - parsed_request (ParsedRequest): The parsed request object.

        - Retrieves rules corresponding to the table and event from the rules dictionary.
        - Executes each rule for the parsed request.
        """
        rules = self.rules[parsed_request.table.lower()].types_dict[parsed_request.event.lower()]
        for rule in rules:
            rule.use(request=parsed_request)

    def register(self, rule_type, table, rule: IRule):
        """
        Registers a new business rule.

        Args:
        - rule_type: The type of the rule.
        - table: The table to which the rule applies.
        - rule (IRule): The rule object to register.

        - Checks if the table exists in the rules dictionary.
        - Adds the rule to the corresponding TypeRules instance.
        """
        if table not in self.rules.keys():
            raise UnknownClientException(f"Table not in rule dict")
        rule_types = self.rules[table]
        rule_types.add_rule(rule_type, rule)
