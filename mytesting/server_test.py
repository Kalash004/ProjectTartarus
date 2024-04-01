import socket

from src.program_layers.api_layer.http_server.ApiServer import HttpServer


class ConnectionToServerTester:
    def __init__(self, host: str, port: int):
        self.HOST = host
        self.PORT = port

    def send_message(self, target: (str, int), msg: str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            soc.bind((self.HOST, self.PORT))
            soc.connect(target)
            soc.send(msg)


if __name__ == "__main__":
    api_server = HttpServer("127.0.0.1", 4444)
    api_server.run()
