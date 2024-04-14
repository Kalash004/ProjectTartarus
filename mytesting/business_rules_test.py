from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.program_layers.business_layer.controller.BusinessRuleController import BusinessRuleController

if __name__ == "__main__":
    req = ParsedRequest(event='POST', table='admin_users', parameters=None, data=[{
        'id': '1',
        'name': 'Anton'
    }, {
        'id': '2',
        'name': 'Notna'
    }])
    brc = BusinessRuleController()
    brc.execute(req)
