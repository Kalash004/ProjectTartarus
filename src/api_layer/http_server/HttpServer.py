import re
import socket
from ConnectionLoop import ConnectionLoop


class HttpServer:

    def __init__(self, port: int, host: str):
        self.HTTP_REQ_REGEX: re.Pattern = re.compile(r"^([A-Z]+)\s*(.*)(\s+HTTP/\\d\\.\\d)$")
        self.PORT: int = port
        self.HOST: str = host
        self.stop: bool = True
        self.connections: [ConnectionLoop] = []


    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _soc:
                _soc.bind((self.HOST, self.PORT))
                _soc.listen(10)
                connection, addres = _soc.accept()
                self.connections.append(ConnectionLoop)
                #TODO: add multithreading
        except:
            #TODO: try catch
            pass