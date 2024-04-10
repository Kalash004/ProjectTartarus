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
        self.stop_flag = False

    def run(self):
        # TODO: add life time checker
        with self.connection as conn:
            while not self.stop_flag:
                self.__main_loop(conn)
            conn.close()
            return

    def __main_loop(self, conn):
        # TODO: main loop, check if needs to send message, if so send message
        if self.message is None:
            return
        self._send_and_clean(conn)

    def stop(self):
        self.send_specific_message("Service was stopped, bye.")
        self.stop_flag = True

    def _send_and_clean(self, conn):
        conn.send(self.message)
        self.message = None

    def send_specific_message(self, message):
        self.connection.send(message.encode())
