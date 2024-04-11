import abc


class IRule:

    @staticmethod
    @abc.abstractmethod
    def use():
        raise NotImplemented
