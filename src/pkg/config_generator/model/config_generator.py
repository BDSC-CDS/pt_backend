from dataclasses import dataclass, asdict

@dataclass
class ConfigGenerator:
    id: int = None
    userid:int = None
    hasScrambleField: bool = False
    hasDateShift: bool = False
    hasSubstituteFieldList: bool = False
    hasSubstituteFieldRegex: bool = False
    scrambleField_fields : list = []
    dateShift_lowrange: int = None
    dateShift_highrange: int = None
    substituteFieldList_fields: list = []
    substituteFieldList_substitute: list = []
    substituteFieldList_replacement: str = None
    substituteFieldRegex_fields: list = []
    substituteFieldRegex_regex: str = None
    substituteFieldRegex_replacement: str = None
    created_at: str = ""

    def to_dict(self):
        return asdict(self)
