from datetime import datetime

from src.pkg.transform_config.model.transform_config import TransformConfig, DateShiftConfig, ScrambleFieldConfig, SubFieldListConfig, SubFieldRegexConfig
from server_template.models import TemplatebackendTransformConfig
from server_template.models import TemplatebackendDateShiftConfig
from server_template.models import TemplatebackendScrambleFieldConfig
from server_template.models import TemplatebackendSubstituteFieldListConfig
from server_template.models import TemplatebackendSubstituteFieldRegexConfig


def transform_config_to_business(config: TemplatebackendTransformConfig) -> TransformConfig:
    c = TransformConfig(
        id=config.id,
        userid=config.userid,
        tenantid=config.tenantid,
        name=config.name,
        questionnaireid=config.questionnaireid,
        dateShift=DateShiftConfig(
            lowrange=config.date_shift.lowrange if config.date_shift else None,
            highrange=config.date_shift.highrange
        ) if config.date_shift else None,
        scrambleField=ScrambleFieldConfig(
            fields=config.scramble_field.fields
        ) if config.scramble_field else None,
        subFieldListList=[
            sub_field_list_to_business(sub_field_list) for sub_field_list in config.sub_field_list_list
        ] if config.sub_field_list_list else None,
        subFieldRegexList=[
            sub_field_regex_to_business(sub_field_regex) for sub_field_regex in config.sub_field_regex_list
        ] if config.sub_field_regex_list else None,
        createdat=config.created_at,
        deletedat=config.deleted_at
    )

    return c

def sub_field_list_to_business(sub_field_list: TemplatebackendSubstituteFieldListConfig) -> SubFieldListConfig:
    return SubFieldListConfig(
        name=sub_field_list.name,
        field=sub_field_list.field,
        substituteList=sub_field_list.substitution_list,
        replacement=sub_field_list.replacement
    )

def sub_field_regex_to_business(sub_field_regex: TemplatebackendSubstituteFieldRegexConfig) -> SubFieldRegexConfig:
    return SubFieldRegexConfig(
        name=sub_field_regex.name,
        field=sub_field_regex.field,
        regex=sub_field_regex.regex,
        replacement=sub_field_regex.replacement
    )

def transform_config_from_business(config: TransformConfig) -> TemplatebackendTransformConfig:
    c = TemplatebackendTransformConfig(
        id=config.id,
        userid=config.userid,
        tenantid=config.tenantid,
        name=config.name,
        questionnaireid=config.questionnaireid,
        date_shift=TemplatebackendDateShiftConfig(
            lowrange=config.dateShift.lowrange,
            highrange=config.dateShift.highrange
        ) if config.dateShift else None,
        scramble_field=TemplatebackendScrambleFieldConfig(
            fields=config.scrambleField.fields
        ) if config.scrambleField else None,
        sub_field_list_list=[
            sub_field_list_from_business(sub_field_list) for sub_field_list in config.subFieldListList
        ] if config.subFieldListList else None,
        sub_field_regex_list=[
            sub_field_regex_from_business(sub_field_regex) for sub_field_regex in config.subFieldRegexList
        ] if config.subFieldRegexList else None,
        created_at=config.createdat,
        deleted_at=config.deletedat
    )
    
    return c

def sub_field_list_from_business(sub_field_list: SubFieldListConfig) -> TemplatebackendSubstituteFieldListConfig:
    return TemplatebackendSubstituteFieldListConfig(
        name=sub_field_list.name,
        field=sub_field_list.field,
        substitution_list=sub_field_list.substituteList,
        replacement=sub_field_list.replacement
    )

def sub_field_regex_from_business(sub_field_regex: SubFieldRegexConfig) -> TemplatebackendSubstituteFieldRegexConfig:
    return TemplatebackendSubstituteFieldRegexConfig(
        name=sub_field_regex.name,
        field=sub_field_regex.field,
        regex=sub_field_regex.regex,
        replacement=sub_field_regex.replacement
    )