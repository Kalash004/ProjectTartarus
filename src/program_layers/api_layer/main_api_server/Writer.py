import socket

from src.__utils.socket_utils import socket_open


class Answerer:
    """
        This answers the requester.
        Created from ConnectionManager
    """

    def __init__(self, connection: socket.socket, adress: str):
        self.connection: socket.socket = connection
        self.adress = adress
        self.message = None
        self.stop_flag = False

    def run(self):
        with self.connection as conn:
            while not self.stop_flag:
                self.__main_loop()
            conn.close()
            return

    def __main_loop(self):
        if self.message is None:
            return
        self._send_and_clean()

    def stop(self):
        self.send_specific_message("Service was stopped, bye.")
        self.stop_flag = True

    def _send_and_clean(self):
        if not socket_open(self.connection):
            return
        self.connection.send(self.message)
        self.message = None

    def send_specific_message(self, message):
        if not socket_open(self.connection):
            return
        self.connection.send(message.encode())
