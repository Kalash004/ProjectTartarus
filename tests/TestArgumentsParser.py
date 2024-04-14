import unittest

from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.program_layers.database_layer.args_mapper.ArgsMapper import ArgsMapper


class TestArgsMapper(unittest.TestCase):

    def test_map(self):
        req = ParsedRequest(event='GET', table='OFFICE_USERS', parameters={
            'ID': '1',
            'NAME': 'Anton'
        }, data=None)
        argsm = ArgsMapper()
        result = argsm.map(req)
        expected_result = [['users_id', '=', '1'], ['name', '=', 'Anton']]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
