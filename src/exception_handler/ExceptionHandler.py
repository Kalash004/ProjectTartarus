import traceback

from src.__models_for_all_layers.exceptions.UnknownException import UnknownException
from src.__models_for_all_layers.interfaces.IHandleClientException import IHandleClientException
from src.__models_for_all_layers.interfaces.IHandleException import IHandleException
from src.__utils.SingletonMeta import SingletonMeta
from src.exception_handler.exception_handle_instructions.UnknownHandler import UnknownHandler
from src.logger.MyLogger import MyLogger


class ExceptionHandler(IHandleClientException, metaclass=SingletonMeta):

    def __init__(self, initialize=False):
        if initialize:
            self.logger = MyLogger()
            self._client_exception_instructions: dict[BaseException:IHandleClientException] = {
                UnknownException: UnknownHandler()
            }
            self._exception_instructions: dict[BaseException:IHandleException] = {

            }

    # def handle_exceptions(self, exception: BaseException):
    #     """Deprecated"""
    #     self.basic_logging(exception)
    #     if type(exception) not in self._exception_instructions:
    #         self._exception_instructions[UnknownException].handle_exceptions(exception)
    #         return
    #     self._exception_instructions[type(exception)].handle_exceptions(exception)  # type: ignore

    def handle_exception_inform_client(self, exception: BaseException, connection_manager):
        """
        Used to handle the exception and inform the client
        :param exception:
        :param connection_manager:
        :return:
        """
        trace_back = traceback.format_exc()
        self.basic_logging(exception, trace_back)
        if type(exception) not in self._client_exception_instructions:
            self._client_exception_instructions[UnknownException].handle_exception_inform_client(exception, connection_manager)
            return
        self._client_exception_instructions[type(exception)].handle_exception_inform_client(exception,  # type:ignore
                                                                                            connection_manager)  # type: ignore

    def basic_logging(self, exception, tb):
        self.logger.log_exception(exception, tb)
