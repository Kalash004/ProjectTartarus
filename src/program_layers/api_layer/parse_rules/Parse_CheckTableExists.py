from src.__models_for_all_layers.exceptions.BadConnectionProtocolException import BadConnectionProtocolException
from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse
from src.program_layers.database_layer.tables.tables import all_tables


class Parse_CheckTableExists(IChainParse):
    # TODO: make better way to check this
    def parse(self, data: dict[str]) -> dict[str]:
        if "table" not in data.keys():
            raise BadConnectionProtocolException(f"Request doesnt contain must have part TABLE")
        table_names = [item.table_name for item in all_tables.all_talbes]
        if data["table"] not in table_names:
            raise BadConnectionProtocolException(f"Such table does not exist: '{data['table']}'")
        return data
