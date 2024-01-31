import datetime
from dataclasses import dataclass

@dataclass
class Medication:
    id: int = None

    tenantid: int = 0
    userid: int = 0
    name: str = ""
    dosage: str = ""
    frequency: str = ""

    createdat: datetime.datetime
    updatedat: datetime.datetime
    deletedat: datetime.datetime = None

