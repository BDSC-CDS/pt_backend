from dataclasses import dataclass, asdict
from dataclasses import field as field_
from typing import List

@dataclass
class DateShiftConfig:
    lowrange: int = None
    highrange: int = None

    def to_dict(self):
        return asdict(self)
    
@dataclass
class ScrambleFieldConfig:
    fields: List[str] = field_(default_factory=list)

    def to_dict(self):
        return asdict(self)

@dataclass
class SubFieldListConfig:
    name: str = ""
    field: str = None
    substituteList: List[str] = field_(default_factory=list)
    replacement: str = None

    def to_dict(self):
        return asdict(self)
@dataclass
class SubFieldRegexConfig:
    name: str = ""
    field: str = None
    regex: str = None
    replacement: str = None

    def to_dict(self):
        return asdict(self)

@dataclass
class TransformConfig:
    id: int = None
    userid:int = None
    tenantid:int = None
    name:str = ""
    questionnaireid:int = None
    dateShift: DateShiftConfig = None
    scrambleField: ScrambleFieldConfig = None
    subFieldListList: List[SubFieldListConfig] = field_(default_factory=list)
    subFieldRegexList: List[SubFieldRegexConfig] = field_(default_factory=list)
    createdat: str = ""
    updatedat: str = ""
    deletedat: str = ""

    def to_dict(self):
        return asdict(self)
