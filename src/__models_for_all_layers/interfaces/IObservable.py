from abc import abstractmethod

from IObserver import IObserve


class IObservable:

    @abstractmethod
    def subscribe(self, who: IObserve) -> None:
        '''
        Subscribes an object with IObserve behavioure
        :param who: The object to subscribe | IObserve
        :return: None
        '''
        raise NotImplemented

    @abstractmethod
    def unsubscribe(self, who: IObserve) -> None:
        """
        Unsubscribes an object with IObserve behavioure
        :param who: The object to unsubscribe | IObserve
        :return: None
        """
        raise NotImplemented
