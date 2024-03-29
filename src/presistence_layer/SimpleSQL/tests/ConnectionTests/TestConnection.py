import unittest

from ...package_src import Config, Connector


class TestConnectionMethods(unittest.TestCase):
    def setUp(self):
        self.__CONNECTION_CONFIG = Config(username="root", password="Ka32167890", hostname="localhost",
                                                     port=0,
                                                     database_name="Testing", character_set="Testing")

    def test_connection(self):
        connector: Connector = Connector(db_config=self.__CONNECTION_CONFIG)
        self.assertEquals(connector.check_connection(), True)

    def test_query(self):
        connector: Connector = Connector(db_config=self.__CONNECTION_CONFIG)
        resp = connector.query({
            "SHOW DATABASES": None
        })
        self.assertTrue(resp is not None)
