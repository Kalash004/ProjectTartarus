import abc


class IFactory:

    @abc.abstractmethod
    def produce(self):
        raise NotImplemented
