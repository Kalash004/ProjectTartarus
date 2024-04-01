from dataclasses import dataclass


@dataclass
class SimpleSQLDbConfig:
    username: str
    password: str
    hostname: str
    port: int
    database_name: str
    character_set: str

    def __post_init__(self):
        self.database_name = self.database_name.lower()
        self.character_set = self.character_set.lower()