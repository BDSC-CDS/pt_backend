from dataclasses import dataclass, asdict,field
from typing import List

@dataclass
class ConfigGenerator:
    id: int = None
    userid:int = None
    tenantid:int = None
    questionnaireid:int = None
    hasScrambleField: bool = False # useful? if boolean but not list
    hasDateShift: bool = False
    hassubFieldList: bool = False
    hassubFieldRegex: bool = False
    scrambleField_fields: List[str] = field(default_factory=list)
    dateShift_lowrange: int = None
    dateShift_highrange: int = None
    subFieldList_fields: List[str] = field(default_factory=list)
    subFieldList_substitute: List[str] = field(default_factory=list)
    subFieldList_replacement: str = None
    subFieldRegex_fields: List[str] = field(default_factory=list)
    subFieldRegex_regex: str = None
    subFieldRegex_replacement: str = None
    created_at: str = ""

    def to_dict(self):
        return asdict(self)
