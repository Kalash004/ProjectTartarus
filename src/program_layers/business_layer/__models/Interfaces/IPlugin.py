import abc


class IPlugin:

    @abc.abstractmethod
    def initialize(self) -> None:
        """Initialize the plugin"""
        raise NotImplemented
