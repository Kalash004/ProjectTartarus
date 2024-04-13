from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__models_for_all_layers.interfaces.ICommand import ICommand
from src.program_layers.business_layer.controller.BusinessRuleController import BusinessRuleController


class SendToBusinessLayerCommand(ICommand):
    """Executes parsed request"""

    def __init__(self, parsed_request):
        self.request = parsed_request

    def execute(self):
        BusinessRuleController().execute(self.request)
