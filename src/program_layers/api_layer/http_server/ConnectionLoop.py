import socket
import threading

from src.program_layers.api_layer.__models.interfaces.IParserBehaviour import IParserBehaviour


class ConnectionLoop:

    def __init__(self, connection: socket.socket, address: str, parser: IParserBehaviour):
        self.CONNECTION: socket.socket = connection
        self.ADDRESS = address
        self.stop = False
        self.parser: IParserBehaviour = parser
        self.thread = threading.Thread(target=self.run)
        self.answer: str = None

    def run(self):
        with self.CONNECTION as conn:
            while not self.stop:
                data = conn.recv(1024)
                if data == b'':
                    self.stop = True
                    return
                self.__main_loop(data)

    def start_thread(self):
        self.thread.start()

    def __main_loop(self, data):
        self.answer = None
        parsed_data = self.parser.parse(data)
        # TODO: send parsed data to domain rules engine
