import importlib
import os.path
import sys

from src.__utils.SingletonMeta import SingletonMeta
from src.program_layers.business_layer.__models.Interfaces.IPlugin import IPlugin


class RulesLoader(metaclass=SingletonMeta):
    """
    A simple rule loader implementing the Plugin Pattern.
    """

    def __init__(self, rules_to_init: [str], controller):
        """
        Initializes the RulesLoader with the provided rules to initialize and controller.

        Args:
        - rules_to_init ([str]): List of rule modules to initialize.
        - controller: The controller object to which the rules will be initialized.
        """
        self.rules_modules_to_init = rules_to_init  # List of rule modules to initialize
        self.controller = controller  # Controller object
        # Adds the directory containing rule modules to the Python path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        relative_path = os.path.join(current_dir, 'rules')
        sys.path.append(relative_path)

    def load_plugins(self):
        """Loads and initializes the rules."""
        for module in self.rules_modules_to_init:
            module_import_name = f"{module}"
            rule = self.import_module(module_import_name)  # Imports the rule module
            rule_class = getattr(rule, module)  # Gets the rule class from the module
            instance = rule_class()  # Creates an instance of the rule class
            instance.initialize(self.controller)  # Initializes the rule with the controller

    @staticmethod
    def import_module(name) -> IPlugin:
        """
        Imports a module with the given name.

        Args:
        - name (str): The name of the module to import.

        Returns:
        - IPlugin: The imported module.
        """
        importlib.invalidate_caches()  # Clears the import cache to ensure latest changes are reflected
        return importlib.import_module(name)  # Imports and returns the module
