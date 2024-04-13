from src.program_layers.api_layer.factory.ApiServerFactory import ApiServerFactory


class ApiLayerMain:
    """Starter point for api layer"""

    def __init__(self):
        self.api_server = ApiServerFactory().produce()

    def start(self):
        self.api_server.run()
