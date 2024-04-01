from enum import Enum


class ConnectionState(Enum):
    CLOSED = "Conenction was closed"
    CONNECTED = "Connected to the database"
    ERROR = "Error occured"
