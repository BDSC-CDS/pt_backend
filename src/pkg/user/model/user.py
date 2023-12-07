from enum import Enum
from dataclasses import dataclass, field

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
    tenantid: int = 0
    username: str = ""
    email: str = ""
    password: str = ""
    firstname: str = ""
    lastname: str = ""
    status: Status = Status.ACTIVE
    source: Source = Source.INTERNAL

    id: int = None
    roles: list[Role] = field(default_factory=list)
    totpsecret: str = ""
    createdat: str = ""
    updatedat: str = ""



