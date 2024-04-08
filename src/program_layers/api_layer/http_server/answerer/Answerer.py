import socket


class Answerer:
    """
        This answers the requester.
        Created from ConnectionManager
    """

    def __init__(self, connection: socket.socket, adress: str):
        self.connection: socket.socket = connection
        self.adress = adress
        self.message = None
        self.stop = False

    def run(self):
        # TODO: add life time checker
        while not self.stop:
            self.__main_loop()

    def __main_loop(self):
        # TODO: main loop, check if needs to send message, if so send message
        if self.message is None:
            return
        self._send_and_clean()

    def stop(self):
        self.send_specific_message("Service was stopped, bye.")
        self.stop = True

    def _send_and_clean(self):
        self.connection.send(self.message)
        self.message = None

    def send_specific_message(self, message):
        self.connection.send(message)
