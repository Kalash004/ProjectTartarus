from src.__models_for_all_layers.exceptions.BadConnectionProtocolException import BadConnectionProtocolException
from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse
from src.program_layers.database_layer.RequestToDbObjMapper import RequestToDbObjMapper
from src.program_layers.database_layer.SimpleSQL.package_src import Base


class Parse_CheckDataAttributes(IChainParse):

    def parse(self, data: dict[str]) -> dict[str]:
        if data["event"] == "delete":
            return data
        if data["data"] is None:
            return data
        table_obj: Base = RequestToDbObjMapper().get_obj_type_from_name(data["table"])
        attrs_count = len(table_obj.get_structure()) - 1
        for in_data in data["data"]:
            data_attr_count = len(in_data)
            if attrs_count != data_attr_count:
                raise BadConnectionProtocolException(
                    f"Attribute count in request is not the same as attribute count in the table: {attrs_count}")
        attr_names = table_obj.get_structure().keys()
        for in_data in data["data"]:
            for k in in_data.keys():
                if k not in attr_names:
                    raise BadConnectionProtocolException(
                        f"Attribute in request doesnt exist in the table: '{k}'")
        return data
