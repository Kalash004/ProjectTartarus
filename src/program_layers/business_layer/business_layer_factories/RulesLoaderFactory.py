from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.config_loader.ConfigLoader import ConfigLoader
from src.program_layers.business_layer.rules_loader.RulesLoader import RulesLoader
from src.utils.SingletonMeta import SingletonMeta


class RulesLoaderFactory(IFactory, metaclass=SingletonMeta):
    def __init__(self):
        self.rule_names = ConfigLoader().load_rule_names()

    def produce(self):
        return RulesLoader(self.rule_names)
