from src.__models_for_all_layers.interfaces.ICommand import ICommand


class DisplayErrorCommand(ICommand):

    def __init__(self, error_message: str, connection_manager):
        self.error_message = error_message
        self.conn_man = connection_manager

    def execute(self):
        self.conn_man.answerer.send_specific_message(self.error_message)
