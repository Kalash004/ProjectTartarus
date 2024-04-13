import abc


class IPlugin:

    @abc.abstractmethod
    def initialize(self, initialize_to) -> None:
        """Initialize the plugin"""
        raise NotImplemented
