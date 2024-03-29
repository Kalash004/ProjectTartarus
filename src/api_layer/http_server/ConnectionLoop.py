import socket
class ConnectionLoop:

    def __init__(self, connection: socket.socket, address):
        self.CONNECTION: socket.socket = connection
        self.ADDRESS = address
        self.stop = False

    def run(self):
        with self.CONNECTION as conn:
            while not self.stop:
                data = conn.recv(1024)

