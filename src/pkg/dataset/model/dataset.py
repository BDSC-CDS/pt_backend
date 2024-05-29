# Assuming AuditLog is a model representing an audit log entry
import datetime
from dataclasses import dataclass, asdict
from typing import Union

@dataclass
class Dataset:
    userid: int = None
    tenantid:int = None
    name: str = ""
    data : dict[str, Union[int, str, float, bool]] = None
    id: int = None
    created_at: str = ""
    updated_at:str = ""
    deleted_at:str = ""

    def to_dict(self):
        return asdict(self)
