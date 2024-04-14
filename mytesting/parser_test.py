from src.program_layers.api_layer.__models.interfaces.IParse import IParse
from src.program_layers.api_layer.factory.ParserFactory import ParserFactory

if __name__ == "__main__":
    # "APIKEY=testkey;EVENT=GET;TABLE=USERS;PARAMETERS=(NAME=ANTON,TOP=1)"
    parser_factory = ParserFactory()
    parser: IParse = parser_factory.produce()
    prsed = parser.parse("APIKEY=apitestkey2;EVENT=POST;TABLE=days;DATA=[{id:1,name:Anton},{id:2,name:Notna}]")
    print(prsed.data)
    print(prsed)

    prsed2 = parser.parse("APIKEY=apitestkey1;EVENT=GET;TABLE=OFFICE_USERS;PARAMETERS=(ID=1,TOP=1)")
    print(prsed2)
