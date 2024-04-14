from src.__models_for_all_layers.interfaces.ICommand import ICommand


class CloseConnectionCommand(ICommand):
    def __init__(self, connection_manager):
        from src.program_layers.api_layer.main_api_server.ConnectionManager import ConnectionManager
        self.conn_loop: ConnectionManager = connection_manager

    def execute(self):
        self.conn_loop.stop()
        self.conn_loop.kill_connection()
