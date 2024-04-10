import abc


class IStopable:

    @abc.abstractmethod
    def stop(self):
        raise NotImplemented
