import socket


class Answerer:
    """
        This answers the requester.
        Created from ConnectionManager
    """

    def __init__(self, connection: socket.socket, adress):
        self.connection: socket.socket = connection
        self.adress = adress
        self.message = None
        self.stop = False

    def run(self):
        while not self.stop:
            self.__main_loop()

    def __main_loop(self):
        # TODO: main loop, check if needs to send message, if so send message
        pass
