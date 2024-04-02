import abc


class ICommand:

    @abc.abstractmethod
    def execute(self):
        raise NotImplemented
