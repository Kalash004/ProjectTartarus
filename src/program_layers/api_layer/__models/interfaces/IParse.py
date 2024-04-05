from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest


class IParse:

    def parse(self, data: str) -> ParsedRequest:
        raise NotImplemented
