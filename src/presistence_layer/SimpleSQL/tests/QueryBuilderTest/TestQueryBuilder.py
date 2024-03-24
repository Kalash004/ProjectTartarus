import unittest

from ...src import Param, Types, Base, Constraints, App, Config


class Test(Base):
    table_name = "Table"
    test_Id = Param(Types.INT, Constraints.PK)
    stuff = Param(Types.STRING, Constraints.UNIQUE, Constraints.NOT_NULL)


class TestQueryBuilderMethods(unittest.TestCase):
    def setUp(self):
        self.__CONNECTION_CONFIG = Config(username="root", password="Ka32167890", hostname="localhost",
                                          port=0,
                                          database_name="Testing", character_set="Testing")
        self.test = Test(test_Id=1, stuff="Stuff")
        self.app = App(self.__CONNECTION_CONFIG)

    def testBuilder(self):
        self.app.start()
