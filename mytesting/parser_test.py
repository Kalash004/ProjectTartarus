from src.program_layers.api_layer.request_parser.RequestParser import RequestParser

if __name__ == "__main__":
    prsr = RequestParser()
    lins = prsr.parse("abcdapikey123;GET;USERS;USERS.NAME=ANTON;TOP=1")
    print(lins)