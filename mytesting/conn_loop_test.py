from src.program_layers.api_layer.api_layer_factories.api_server_factory.ApiServerFactory import ApiServerFactory
from src.program_layers.api_layer.http_server.api_server.APIServer import APIServer

if __name__ == "__main__":
    api_server: APIServer = ApiServerFactory().produce()
    api_server.run()