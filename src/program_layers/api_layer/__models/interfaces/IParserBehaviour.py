import abc

from src.__models_for_all_layers.interfaces.ICommand import ICommand


class IParserBehaviour:

    @abc.abstractmethod
    def parse(self, data) -> ICommand:
        '''
        Parses data from API server
        :param data: str
        :return: ICommand
        '''
        raise NotImplemented()
