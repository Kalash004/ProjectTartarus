import dataclasses


@dataclasses.dataclass
class ParsedRequest:
    event: str
    table: str
    parameters: str | None
    data: [dict]
