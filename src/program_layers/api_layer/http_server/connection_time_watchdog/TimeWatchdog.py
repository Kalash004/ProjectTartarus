import time

from src.__models_for_all_layers.interfaces.IStopable import IStopable


class TimeWatchdog:
    def __init__(self, longevity_sec: int, connection_manager: IStopable):
        self.longevity_sec = longevity_sec
        self.conn_manager: IStopable = connection_manager
        self.TIME_OUT_PERIOD = 75

    def worker(self):
        """
        Worker function for multiprocessing. Monitors the duration and updates the time_flag accordingly.
        """
        timeout: float = self.longevity_sec / self.TIME_OUT_PERIOD
        end_time: float = time.time() + self.longevity_sec
        current_time = time.time()
        while current_time < end_time:
            time.sleep(timeout)
            current_time = time.time()
        self.conn_manager.stop()
