from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__models_for_all_layers.interfaces.ICommand import ICommand
from src.program_layers.business_layer.business_layer_factories.BusinessRuleCtrlFactory import BusinessRuleCtrlFactory


class ExecuteCommand(ICommand):
    """Executes parsed request"""

    def __init__(self, parsed_request: ParsedRequest, connection_loop):
        self.request = parsed_request
        self.conn_loop = connection_loop

    def execute(self):
        BusinessRuleCtrlFactory().produce().execute(self.request, self.conn_loop)
