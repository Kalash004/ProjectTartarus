from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.config_loader.ConfigLoader import ConfigLoader
from src.program_layers.api_layer.http_server.TimeWatchdog import TimeWatchdog


class WatchdogFactory(IFactory):
    def __init__(self, connection_manager):
        self.longevity_sec = ConfigLoader().get_connection_life_sec()
        self.connection_manager = connection_manager

    def produce(self):
        return TimeWatchdog(self.longevity_sec, self.connection_manager)
