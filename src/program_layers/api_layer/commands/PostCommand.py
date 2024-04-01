from src.models_for_all_layers.interfaces.ICommand import ICommand


class PostCommand(ICommand):
    def __init__(self, data):
        self.data = data

    def execute(self):
        pass
