import abc

from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest


class IRule:

    @abc.abstractmethod
    def use(self, request: ParsedRequest):
        raise NotImplemented


