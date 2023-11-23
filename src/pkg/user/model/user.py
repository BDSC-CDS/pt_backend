from enum import Enum
from dataclasses import dataclass

class StrEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __str__(self):
        return self.value

class Status(StrEnum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

class Source(StrEnum):
    INTERNAL = "INTERNAL"

@dataclass
class Role:
    id: str

@dataclass
class User:
    id: int
    username: str
    password: str
    firstname: str
    lastname: str
    roles: list[Role]
    status: Status
    source: Source
    totpsecret: str
    createdat: str
    updatedat: str



