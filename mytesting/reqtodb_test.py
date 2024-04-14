from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.program_layers.database_layer.RequestToDbObjMapper import RequestToDbObjMapper
from src.program_layers.database_layer.SimpleSQL.package_src import Base
from src.program_layers.database_layer.tables.tables import all_tables

if __name__ == "__main__":
    mapper = RequestToDbObjMapper()
    req = ParsedRequest(event='POST', table='admin_users', parameters=None, data=[{
        'admin_id': 'None',
        'name': 'Anton',
        'surename': 'Kalashnikov',
        'password': 'test'
    }, {
        'admin_id': 'None',
        'name': 'Notna',
        'surename': 'Kalashnikov',
        'password': 'test'
    }])
    for table in all_tables.all_talbes:
        table(skip_setup=True)
    result: Base = mapper.request_to_obj(req)[0]
    print(result.find_primary_key_val())
    # for it in result:
    #     print(it)
