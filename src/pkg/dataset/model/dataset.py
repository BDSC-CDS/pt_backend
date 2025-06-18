# Assuming AuditLog is a model representing an audit log entry
import datetime
from dataclasses import dataclass, asdict
from typing import Union

@dataclass
class Dataset:
    userid: int = None
    tenantid:int = None
    dataset_name: str = ""
    original_filename: str = ""
    id: int = None
    created_at: str = ""
    deleted_at:str = ""

    def to_dict(self):
        return asdict(self)

@dataclass
class Metadata:
    userid: int = None
    tenantid:int = None
    dataset_id:int = None
    column_id:int = None
    column_name:str = ""
    type_:str = ""
    identifier:str = ""
    is_id:bool = False

    def to_dict(self):
        return asdict(self)

@dataclass
class Dataset_content:
    userid: int = None
    tenantid:int = None
    dataset_id:int = None
    column_id:int = None
    line_id:int = None
    val:str = ""

    def to_dict(self):
            return asdict(self)
