from src.program_layers.api_layer.__models.interfaces.IParse import IParse
from src.program_layers.api_layer.request_parser.ParserFactory import ParserFactory

if __name__ == "__main__":
    # "APIKEY=testkey;EVENT=GET;TABLE=USERS;PARAMETERS=(NAME=ANTON,TOP=1)"
    parser_factory = ParserFactory()
    parser: IParse = parser_factory.create_parser()
    prsed = parser.parse("APIKEY=testkey;EVENT=GET;TABLE=USERS;PARAMETERS=(NAME=ANTON,TOP=1)")
    print(prsed)
