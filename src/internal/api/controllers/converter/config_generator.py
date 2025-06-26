from datetime import datetime

from src.pkg.config_generator.model.config_generator import ConfigGenerator
from server_template.models import TemplatebackendConfig


def config_to_business(config: TemplatebackendConfig) -> ConfigGenerator:
    c = ConfigGenerator(
        id=config.id,
        userid=config.userid,
        tenantid=config.tenantid,
        config_name=config.config_name,
        questionnaireid=config.questionnaireid,
        hasScrambleField=config.has_scramble_field,
        hasDateShift=config.has_date_shift,
        hassubFieldList=config.hassub_field_list,
        hassubFieldRegex=config.hassub_field_regex,
        scrambleField_fields=config.scramble_field_fields,
        dateShift_lowrange=config.date_shift_lowrange,
        dateShift_highrange=config.date_shift_highrange,
        subFieldList_field=config.sub_field_list_field,
        subFieldList_substitute=config.sub_field_list_substitute,
        subFieldList_replacement=config.sub_field_list_replacement,
        subFieldRegex_field=config.sub_field_regex_field,
        subFieldRegex_regex=config.sub_field_regex_regex,
        subFieldRegex_replacement=config.sub_field_regex_replacement,
        created_at=config.created_at,
        deleted_at=config.deleted_at
    )

    return c

def config_from_business(config: ConfigGenerator) -> TemplatebackendConfig:
    c = TemplatebackendConfig(
        id=config.id,
        userid=config.userid,
        tenantid=config.tenantid,
        config_name=config.config_name,
        questionnaireid=config.questionnaireid,
        has_scramble_field=config.hasScrambleField,
        has_date_shift=config.hasDateShift,
        hassub_field_list=config.hassubFieldList,
        hassub_field_regex=config.hassubFieldRegex,
        scramble_field_fields=config.scrambleField_fields,
        date_shift_lowrange=config.dateShift_lowrange,
        date_shift_highrange=config.dateShift_highrange,
        sub_field_list_field=config.subFieldList_field,
        sub_field_list_substitute=config.subFieldList_substitute,
        sub_field_list_replacement=config.subFieldList_replacement,
        sub_field_regex_field=config.subFieldRegex_field,
        sub_field_regex_regex=config.subFieldRegex_regex,
        sub_field_regex_replacement=config.subFieldRegex_replacement,
        created_at=config.created_at,
        deleted_at=config.deleted_at
    )
    return c
