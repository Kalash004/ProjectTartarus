import socket
import threading

from src.program_layers.api_layer.__models.interfaces.IParse import IParse


class Reader:
    """This reads requests from clients"""

    def __init__(self, connection: socket.socket, address: str, parser: IParse):
        self.CONNECTION: socket.socket = connection
        self.ADDRESS = address
        self.stop = False
        self.parser: IParse = parser
        self.thread = threading.Thread(target=self.run)

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

    def __main_loop(self, connection):
        data = self.recieve_data()
        self.send_data()
        parsed_data = self.parser.parse(data)
        # TODO: send parsed data to domain rules engine

    def recieve_data(self, connection: socket.socket):
        data = connection.recv(1024)
        if data == b'':
            self.stop = True
            return
