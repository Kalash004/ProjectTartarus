import inspect

from ... import App


class SimpleBaseTable:

    def __init__(self, pre_struct):
        self.struct = self.__get_structure(pre_struct)
        # check structure for errors
        # send self to the controller singleton
        self.__send_table_to_control()

    def __send_table_to_control(self):
        app = App()
        app._add_table(self)
        # Send table object to the controller singleton

    # TODO: here
    def __get_structure(self, pre_struct):
        structure = []
        for i in inspect.getmembers(pre_struct):
            if i[0].startswith('_'):
                continue
            if inspect.ismethod(i[1]):
                continue
            structure.append(i)
        return structure

    def __repr__(self):
        return str(self.struct)
