from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.program_layers.database_layer.RequestToDbObjMapper import RequestToDbObjMapper
from src.program_layers.database_layer.tables.tables import all_tables

if __name__ == "__main__":
    mapper = RequestToDbObjMapper()
    req = ParsedRequest(event='POST', table='admin_users', parameters=None, data=[{
        'admin_id': '1',
        'name': 'Anton',
        'surename': 'Kalashnikov',
        'password': 'test'
    }, {
        'admin_id': '1',
        'name': 'Notna',
        'surename': 'Kalashnikov',
        'password': 'test'
    }])
    for table in all_tables.all_talbes:
        table(skip_setup=True)
    result = mapper.request_to_obj(req)
    for it in result:
        print(it)
