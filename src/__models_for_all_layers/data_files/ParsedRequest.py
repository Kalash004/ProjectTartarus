import dataclasses


@dataclasses.dataclass
class ParsedRequest:
    event: str
    table: str
    parameters: str
    data: [dict]
