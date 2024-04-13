import socket
import threading

from src.__models_for_all_layers.exceptions.BaseExceptions.ClientBaseException import ClientBaseException
from src.__models_for_all_layers.exceptions.BaseExceptions.ServiceBaseException import ServiceBaseException
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
                # try:
                    self.__main_loop(conn)
                # except ClientBaseException as ce:
                #     TODO: Fix exception handling - not many different exceptions, just one
                    # self.exception_handler.handle_client_exception(ce, self.connection_manager)
                # except ServiceBaseException as se:
                #     ExceptionHandler().handle_exceptions(se)
                #     conn.close()
                # except Exception as e:
                #     ExceptionHandler().handle_exceptions(e)
                # except BaseException as be:
                #     ExceptionHandler().handle_exceptions(be)
                #     conn.close()
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
