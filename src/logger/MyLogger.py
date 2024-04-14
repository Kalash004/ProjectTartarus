import os
from datetime import datetime

from src.__utils.SingletonMeta import SingletonMeta


class MyLogger(metaclass=SingletonMeta):
    """Not implemented. Facade to logging"""

    def __init__(self):
        self.__LOGS_PATH = os.path.join(os.path.dirname(__file__), "../../logs/logs.log")

    def log_exception(self, exception, trace_back):
        formatted_time = self.get_formatted_time()
        with open(self.__LOGS_PATH, "a") as f:
            f.write(f"\n {formatted_time} - Exception happened : {exception} | traceback: {trace_back} \n\r End |")

    @staticmethod
    def get_formatted_time():
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time
