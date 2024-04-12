import importlib

from src.__utils.SingletonMeta import SingletonMeta
from src.program_layers.business_layer.__models.Interfaces.IPlugin import IPlugin


class RulesLoader(metaclass=SingletonMeta):
    """
    A simple rule loader
    Plugin Pattern
    """

    def __init__(self, rules_to_init: [str]):
        self.rules_modules_to_init = rules_to_init

    def load_plugins(self):
        """Loads rules and initializes them"""
        for module in self.rules_modules_to_init:
            rule = self.import_module(module)
            rule.initialize()

    @staticmethod
    def import_module(name) -> IPlugin:
        return importlib.import_module(name)  # type: ignore
