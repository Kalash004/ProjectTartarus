import unittest

from src.__models_for_all_layers.exceptions.BadConnectionProtocolException import BadConnectionProtocolException
from src.program_layers.api_layer.__models.interfaces.IParse import IParse
from src.program_layers.api_layer.factory.ParserFactory import ParserFactory


class TestRequestParser(unittest.TestCase):

    def test_parse_exception(self):
        parser_factory = ParserFactory()
        parser: IParse = parser_factory.produce()
        with self.assertRaises(BadConnectionProtocolException):
            parser.parse("APIKEY=apitestkey2;EVENT=POST;TABLE=USERS;DATA=[{id:1,name:Anton},{id:2,name:Notna}]")

    def test_parse_no_exception(self):
        parser_factory = ParserFactory()
        parser: IParse = parser_factory.produce()
        prsed = parser.parse("APIKEY=apitestkey2;EVENT=POST;TABLE=admin_users;DATA=[{id:1,name:Anton},{id:2,name:Notna}]")
        print("/n")
        print(prsed)


if __name__ == '__main__':
    unittest.main()
