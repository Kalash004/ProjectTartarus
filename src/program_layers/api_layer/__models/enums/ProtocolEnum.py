import enum


class ProtocolEnum(enum.Enum):
    EVENT = "event"
    APIKEY = "apikey"
    TABLE = "table"
    PARAMS = "parameters"
    DATA = "data"