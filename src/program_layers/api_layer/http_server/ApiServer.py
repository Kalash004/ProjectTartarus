import socket

from src.program_layers.api_layer.http_server.ConnectionLoop import ConnectionLoop


class APIServer:

    def __init__(self, host: str, port: int):
        # self.HTTP_REQ_REGEX: re.Pattern = re.compile(r"^([A-Z]+)\s*(.*)(\s+HTTP/\\d\\.\\d)$")
        self.PORT: int = port
        self.HOST: str = host
        self.stop: bool = False
        self.connections: [ConnectionLoop] = []

    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _soc:
                _soc.bind((self.HOST, self.PORT))
                _soc.listen(10)
                print(f"Running on {self.HOST}:{self.PORT}")
                while not self.stop:
                    connection, addres = _soc.accept()
                    conn_loop = ConnectionLoop(connection, addres)
                    conn_loop.start_thread()
                    self.connections.append(conn_loop)
        except:
            # TODO: try catch
            pass
