import unittest

from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.__models_for_all_layers.exceptions.BusinessRuleNotPassedException import BusinessRuleNotPassedException
from src.program_layers.business_layer.controller.BusinessRuleController import BusinessRuleController


class TestBusinessRuleController(unittest.TestCase):

    def test_execute(self):
        req = ParsedRequest(event='POST', table='admin_users', parameters=None, data=[{
            'id': '1',
            'name': 'Anton'
        }, {
            'id': '2',
            'name': 'Notna'
        }])
        brc = BusinessRuleController()
        with self.assertRaises(BusinessRuleNotPassedException) as context:
            brc.execute(req)
        self.assertTrue("Request had name Anton in data" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
