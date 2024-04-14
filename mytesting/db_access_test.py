from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.program_layers.database_layer.access.DbAccess import DbAccess

if __name__ == "__main__":
    db_access = DbAccess(initialize=True)
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
    db_access.insert(req)
