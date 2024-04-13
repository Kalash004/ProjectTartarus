from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.program_layers.database_layer.args_mapper.ArgsMapper import ArgsMapper

if __name__ == "__main__":
    req = ParsedRequest(event='GET', table='OFFICE_USERS', parameters={
        'ID': '1',
        'NAME': 'Anton'
    }, data=None)
    argsm = ArgsMapper()
    print(argsm.map(req))
