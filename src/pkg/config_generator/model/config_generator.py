from dataclasses import dataclass, asdict,field
from typing import List

@dataclass
class ConfigGenerator:
    id: int = None
    userid:int = None
    tenantid:int = None
    config_name:str = ""
    questionnaireid:int = None
    hasScrambleField: bool = False # useful? if boolean but not list
    hasDateShift: bool = False
    hassubFieldList: bool = False
    hassubFieldRegex: bool = False
    scrambleField_fields: List[str] = field(default_factory=list)
    dateShift_lowrange: int = None
    dateShift_highrange: int = None
    subFieldList_field: str = None
    subFieldList_substitute: List[str] = field(default_factory=list)
    subFieldList_replacement: str = None
    subFieldRegex_field: str = None
    subFieldRegex_regex: str = None
    subFieldRegex_replacement: str = None
    created_at: str = ""
    deleted_at: str = ""

    def to_dict(self):
        return asdict(self)
