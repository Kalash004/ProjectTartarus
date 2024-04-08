import socket
import threading

from src.program_layers.api_layer.__models.interfaces.IParse import IParse


class Reader:
    """This reads requests from clients"""

    def __init__(self, connection: socket.socket, address: str, parser: IParse):
        self.CONNECTION: socket.socket = connection
        self.ADDRESS = address
        self.parser: IParse = parser
        self.thread = threading.Thread(target=self.run)
        self.stop = False

    def run(self):
        # TODO: add life time checker
        with self.CONNECTION as conn:
            while not self.stop:
                self.__main_loop(conn)

    def start_thread(self):
        self.thread.start()

    def __main_loop(self, connection):
        data = self.recieve_data()
        if data is not None:
            parsed_data = self.parser.parse(data)
        # TODO: send parsed data to domain rules engine

    def recieve_data(self):
        data = self.CONNECTION.recv(1024)
        if data == b'':
            self.stop = True
            return None
        return data.decode("ascii")

    def stop(self):
        self.stop = True
