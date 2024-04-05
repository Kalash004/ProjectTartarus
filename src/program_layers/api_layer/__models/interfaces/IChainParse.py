import abc


class IChainParse:

    @abc.abstractmethod
    def parse(self, data: dict[str]) -> dict[str]:
        raise NotImplemented
