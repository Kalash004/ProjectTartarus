import importlib
import os.path
import sys

from src.__utils.SingletonMeta import SingletonMeta
from src.program_layers.business_layer.__models.Interfaces.IPlugin import IPlugin


class RulesLoader(metaclass=SingletonMeta):
    """
    A simple rule loader
    Plugin Pattern
    """

    def __init__(self, rules_to_init: [str], controller):
        self.rules_modules_to_init = rules_to_init
        self.controller = controller
        current_dir = os.path.dirname(os.path.abspath(__file__))
        relative_path = os.path.join(current_dir, 'rules')
        sys.path.append(relative_path)

    def load_plugins(self):
        """Loads rules and initializes them"""
        for module in self.rules_modules_to_init:
            module_import_name = f"{module}"
            rule = self.import_module(module_import_name)
            rule_class = getattr(rule, module)
            instance = rule_class()
            instance.initialize(self.controller)

    @staticmethod
    def import_module(name) -> IPlugin:
        importlib.invalidate_caches()
        return importlib.import_module(name)  # type: ignore
