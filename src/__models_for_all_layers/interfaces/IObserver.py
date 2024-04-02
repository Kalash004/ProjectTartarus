from abc import abstractmethod


class IObserve:

    @abstractmethod
    def observe_event(self, context: str, data: tuple) -> None:
        """
        Observes
        :param context: type of event
        :param data: tuple with data needed for event
        :return: None
        """
        raise NotImplemented
