from src.program_layers.api_layer.__models.interfaces.IParse import IParse
from src.program_layers.api_layer.api_layer_factories.ParserFactory import ParserFactory

if __name__ == "__main__":
    # "APIKEY=testkey;EVENT=GET;TABLE=USERS;PARAMETERS=(NAME=ANTON,TOP=1)"
    parser_factory = ParserFactory()
    parser: IParse = parser_factory.produce()
    prsed = parser.parse("APIKEY=apitestkey2;EVENT=POST;TABLE=USERS;DATA=[{id:1,name:Anton},{id:2,name:Notna}]")
    print(prsed.data)
    print(prsed)
