# Assuming AuditLog is a model representing an audit log entry
import datetime
from dataclasses import dataclass, asdict

@dataclass
class AuditLog:
    userid: int = None
    service: str = ""
    action: str = ""
    body: str = ""
    response: str = ""
    id: int = None
    created_at: str = ""
    error: bool = False

    def to_dict(self):
        return asdict(self)
