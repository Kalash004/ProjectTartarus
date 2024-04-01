import socket
import threading

from src.program_layers.api_layer.models.interfaces.IParserBehaviour import IParserBehaviour


class ConnectionLoop:

    def __init__(self, connection: socket.socket, address: str, parser: IParserBehaviour):
        self.CONNECTION: socket.socket = connection
        self.ADDRESS = address
        self.stop = False
        self.parser: IParserBehaviour = parser
        self.thread: threading.Thread
        self.answer: str = None

    def run(self):
        with self.CONNECTION as conn:
            while not self.stop:
                data = conn.recv(1024)
                if data == b'':
                    return
                self.answer = None
                get_response = self.parser.parse(data)
                data = get_response.execute()
                # conn.send(data)

    def start_thread(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.start()
