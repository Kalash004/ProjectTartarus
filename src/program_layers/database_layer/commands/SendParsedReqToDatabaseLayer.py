from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__models_for_all_layers.interfaces.ICommand import ICommand


class SendParsedReqToDatabaseLayer(ICommand):
    """Send Parsed request instance to database layer"""

    def __init__(self, request: ParsedRequest, connection):
        self.request = request
        self.connection = connection

    def execute(self):
        DatabaseController().execute_request(self.request, self.connection)
