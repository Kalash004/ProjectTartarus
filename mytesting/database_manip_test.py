from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.program_layers.database_layer.commands.SendParsedReqToDatabaseLayer import SendParsedReqToDatabaseLayer

if __name__ == "__main__":
    req = ParsedRequest(event='post', table='admin_users', parameters=None, data=[{
        'admin_id': '1',
        'name': 'Anton',
        'surename': 'Kalashnikov',
        'password': 'test'
    }, {
        'admin_id': '2',
        'name': 'Notna',
        'surename': 'Kalashnikov',
        'password': 'test'
    }])
    SendParsedReqToDatabaseLayer(request=req, connection=None).execute()
