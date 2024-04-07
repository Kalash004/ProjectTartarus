from src.__models_for_all_layers.interfaces.ICommand import ICommand


class DisplayErrorCommand(ICommand):

    def __init__(self, error_message: str):
        self.error_message = error_message

    def execute(self):
        return self.error_message
