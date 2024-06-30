import datetime
from src.pkg.user.model.user import User
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
    error: bool = False,
    user: User = None

    def to_dict(self):
        return asdict(self)
