# Assuming AuditLog is a model representing an audit log entry
import datetime
from dataclasses import dataclass, asdict
from typing import Union

@dataclass
class Dataset:
    userid: int = None
    name: str = ""
    data : dict[str, Union[int, str, float, bool]] = None
    id: int = None
    created_at: str = ""

    def to_dict(self):
        return asdict(self)
