from src.program_layers.api_layer.authentificator.Authentificator import Authentificator
from src.program_layers.api_layer.request_parser.RequestParser import RequestParser

if __name__ == "__main__":
    auth = Authentificator("lol")
    prsr = RequestParser(auth)
    lins = prsr.parse("APIKEY=testkey;EVENT=GET;TABLE=USERS;PARAMETERS=(NAME=ANTON,TOP=1)")
    print(lins)
