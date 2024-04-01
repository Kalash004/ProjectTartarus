from src.program_layers.api_layer.models.interfaces.IParserBehaviour import IParserBehaviour


class RequestParser(IParserBehaviour):
    def __init__(self):
        self.DELIMITER = ";"
        self.method_chain = []

    def parse(self, data: str):
        lines = self.split_to_lines(data)

        for method in self.method_chain:
            method(lines)

    def add_method(self, func):
        self.method_chain.append(func)

    def split_to_lines(self, data: str):
        return data.split(self.DELIMITER)

    def api_key_check(self, lines: [str]):

    def split_to_key_value(self, lines: str):
        dictionary = {}
        for line in lines:
            key_value = line.split("=")
