import socket

from src.__utils.socket_utils import socket_open
from src.exception_handler.ExceptionHandler import ExceptionHandler


class Answerer:
    """
        This answers the requester.
        Created from ConnectionManager
    """

    def __init__(self, connection: socket.socket, adress: str, connection_manager):
        self.connection: socket.socket = connection
        self.adress = adress
        self.message = None
        self.stop_flag = False
        self.connection_manager = connection_manager

    def run(self):
        with self.connection as conn:
            while not self.stop_flag:
                try:
                    self.__main_loop()
                except Exception as e:
                    ExceptionHandler().handle_exception_inform_client(e, self.connection_manager)
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
        self.message = "\n\r" + self.message
        if not socket_open(self.connection):
            self.stop_flag = True
            return
        self.connection.send(self.message.encode())
        self.message = None

    def send_specific_message(self, message):
        msg = "\n\r" + message
        if not socket_open(self.connection):
            return
        self.connection.send(msg.encode())
