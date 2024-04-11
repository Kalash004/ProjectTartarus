from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.program_layers.business_layer.controller.BusinessRuleController import BusinessRuleController


class BusinessRuleCtrlFactory(IFactory):
    """This creates BusinessRuleController instance"""

    def __init__(self):
        pass

    def produce(self):
        return BusinessRuleController()
