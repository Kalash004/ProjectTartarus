from src.program_layers.api_layer.__models.interfaces.IChainParse import IChainParse
from src.program_layers.database_layer.tables.tables import all_tables


class Parse_CheckTableExists(IChainParse):
    # TODO: make better way to check this
    def parse(self, data: dict[str]) -> dict[str]:
        table_names = [item.table_name for item in all_tables.all_talbes]
        if data["table"] not in table_names:
            # TODO: Better handling
            raise Exception("Handle this better")
