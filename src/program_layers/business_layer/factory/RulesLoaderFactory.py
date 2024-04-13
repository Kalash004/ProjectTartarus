from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.__utils.SingletonMeta import SingletonMeta
from src.config_loader.ConfigLoader import ConfigLoader
from src.program_layers.business_layer.rules_loader.RulesLoader import RulesLoader


class RulesLoaderFactory(IFactory, metaclass=SingletonMeta):
    def __init__(self, controller):
        self.rule_names = ConfigLoader().rule_conf_loader.load_rule_names()
        self.controller = controller

    def produce(self):
        return RulesLoader(self.rule_names, self.controller)
