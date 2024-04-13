from src.__models_for_all_layers.interfaces.IFactory import IFactory
from src.config_loader.ConfigLoader import ConfigLoader
from src.program_layers.api_layer.main_api_server.TimeWatchdog import TimeWatchdog


class WatchdogFactory(IFactory):
    def __init__(self, connection_manager):
        self.longevity_sec = ConfigLoader().api_conf_loader.get_connection_timeout_sec()
        self.connection_manager = connection_manager

    def produce(self):
        return TimeWatchdog(self.longevity_sec, self.connection_manager)
