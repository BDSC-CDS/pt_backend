# Assuming AuditLog is a model representing an audit log entry
import datetime
from dataclasses import dataclass, field, fields, asdict

@dataclass
class AuditLog:
    userid: int = 0
    action: str = ""

    id: int = None
    created_at: str = ""

    def to_dict(self):
        return asdict(self)

# TODO more?
