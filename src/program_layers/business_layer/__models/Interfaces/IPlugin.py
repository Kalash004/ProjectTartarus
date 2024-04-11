import abc


class IPlugin:

    @staticmethod
    @abc.abstractmethod
    def initialize() -> None:
        """Initialize the plugin"""
        raise NotImplemented
