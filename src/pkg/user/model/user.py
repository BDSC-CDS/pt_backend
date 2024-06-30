from enum import Enum
from dataclasses import dataclass, field, fields, asdict

class StrEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __str__(self):
        return self.value

    def __deepcopy__(self, memo):
        return self.value

class Status(StrEnum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

class Source(StrEnum):
    INTERNAL = "INTERNAL"

@dataclass
class Role:
    id: str

def dataclass_from_dict(cls, d):
    try:
        fieldtypes = {f.name:f.type for f in fields(cls)}
        return cls(**{f:dataclass_from_dict(fieldtypes[f],d[f]) for f in d})
    except:
        return d

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

    def drop_sensitive_fields(self):
        self.password = ""
        self.status = None
        self.source = None
        self.totpsecret = ""
        return self

    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, d):
        u = dataclass_from_dict(cls, d)
        if d["status"]:
            u.status = Status(d["status"])
        if d["source"]:
            u.source = Source(d["source"])
        if d["roles"]:
            u.roles = [Role(id=e['id']) for e in d["roles"]]
        return u