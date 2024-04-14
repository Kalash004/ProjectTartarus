import socket
import threading

from src.exception_handler.ExceptionHandler import ExceptionHandler
from src.program_layers.api_layer.__models.interfaces.IParse import IParse
from src.program_layers.api_layer.executor.Executor import Executor


class Reader:
    """This reads requests from clients"""
    lock = threading.Lock()

    def __init__(self, connection: socket.socket, address: str, parser: IParse, conn_manager, exception_handler):
        self.CONNECTION: socket.socket = connection
        self.ADDRESS = address
        self.parser: IParse = parser
        self.thread = threading.Thread(target=self.run)
        self.connection_manager = conn_manager
        self.stop_flag = False
        self.exception_handler = exception_handler

    def run(self):
        with self.CONNECTION as conn:
            while not self.stop_flag:
                try:
                    self.__main_loop(conn)
                except BaseException as e:
                    ExceptionHandler().handle_exception_inform_client(e, self.connection_manager)
            conn.close()
            return

    def start_thread(self):
        self.thread.start()

    def __main_loop(self, connection):
        data = self.recieve_data()
        if data is None:
            return
        parsed_request = self.parser.parse(data)
        Executor().execute(parsed_request, self.connection_manager, self.lock)

    def recieve_data(self):
        if not self.stop_flag:
            data = self.CONNECTION.recv(1024)
            if data == b'':
                self.stop_flag = True
                return None
            return data.decode("ascii")

    def stop(self):
        self.stop_flag = True
