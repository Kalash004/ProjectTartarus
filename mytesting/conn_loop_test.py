from src.program_layers.api_layer.factory.ApiServerFactory import ApiServerFactory
from src.program_layers.api_layer.main_api_server.APIServer import APIServer

if __name__ == "__main__":
    api_server: APIServer = ApiServerFactory().produce()
    api_server.run()
