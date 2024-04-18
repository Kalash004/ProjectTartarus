from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__models_for_all_layers.exceptions.BadConnectionProtocolException import BadConnectionProtocolException
from src.program_layers.api_layer.__models.enums.ProtocolEnum import ProtocolEnum
from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse
from src.program_layers.api_layer.__models.interfaces.IParse import IParse

class RequestParser(IParse):
    """
    This class parses incoming requests into ParsedRequest objects.
    """

    def __init__(self, parse_chain: [IChainParse]):
        """
        Initializes the RequestParser with the provided parse chain.

        Args:
        - parse_chain ([IChainParse]): List of objects implementing IChainParse interface for parsing.
        """
        self.DELIMITER = ";"  # Delimiter used for splitting data
        self.parse_chain = parse_chain  # List of parse chain objects

    def parse(self, data: str) -> ParsedRequest:
        """
        Parses the incoming data into a ParsedRequest object.

        Args:
        - data (str): The incoming data to be parsed.

        Returns:
        - ParsedRequest: The parsed request object.
        """
        # Preprocess the data by stripping whitespace and delimiters
        data = data.rstrip()
        data = data.lstrip()
        data = data.rstrip("/r/n")  # Fix: Should be "\r\n" instead of "/r/n"
        data = data.rstrip(";")

        # Split data into key-value pairs and parse through the chain
        dictionary = self.split_to_key_value(self.split_to_lines(data))
        for parse_class in self.parse_chain:
            dictionary = parse_class.parse(dictionary)

        # Construct the ParsedRequest object
        parsed = ParsedRequest(dictionary[ProtocolEnum.EVENT.value],
                               dictionary[ProtocolEnum.TABLE.value],
                               dictionary[ProtocolEnum.PARAMS.value],
                               dictionary[ProtocolEnum.DATA.value])

        # Print parsed object for testing
        print(parsed)

        return parsed

    def split_to_lines(self, data: str):
        """
        Splits the data into lines using the delimiter.

        Args:
        - data (str): The data to be split.

        Returns:
        - list: List of lines.
        """
        return data.split(self.DELIMITER)

    @staticmethod
    def split_to_key_value(lines: [str]):
        """
        Splits lines into key-value pairs.

        Args:
        - lines ([str]): List of lines.

        Returns:
        - dict: Dictionary of key-value pairs.
        """
        dictionary = {}
        for line in lines:
            key_value = line.split("=", 1)
            if len(key_value) != 2:
                raise BadConnectionProtocolException("Format key=value was not met")
            key = key_value[0].lower()
            value = key_value[1]
            dictionary[key] = value
        return dictionary
