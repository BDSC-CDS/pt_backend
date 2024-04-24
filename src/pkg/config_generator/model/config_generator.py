from dataclasses import dataclass, asdict

@dataclass
class ConfigGenerator:
    id: int = None
    questionnaireid:int = None
    hasScrambleField: bool = False # useful? if boolean but not list
    hasDateShift: bool = False
    hassubFieldList: bool = False
    hassubFieldRegex: bool = False
    scrambleField_fields : list = []
    dateShift_lowrange: int = None
    dateShift_highrange: int = None
    subFieldList_fields: list = []
    subFieldList_substitute: list = []
    subFieldList_replacement: str = None
    subFieldRegex_fields: list = []
    subFieldRegex_regex: str = None
    subFieldRegex_replacement: str = None
    created_at: str = ""

    def to_dict(self):
        return asdict(self)
