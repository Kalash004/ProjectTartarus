import socket
from dataclasses import dataclass


@dataclass
class Task:
    connection: socket.socket
    finished: bool = False
