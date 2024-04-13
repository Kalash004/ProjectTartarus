import dataclasses


@dataclasses.dataclass
class ParsedRequest:
    event: str
    table: str
    parameters: [dict]
    data: [dict]

    def get_params_id(self):
        if "ID" not in self.parameters.keys():
            return None
        return self.parameters["ID"]
