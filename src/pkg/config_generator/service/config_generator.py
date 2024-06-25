from typing import List
from src.pkg.config_generator.model.config_generator import ConfigGenerator
import json

class ConfigGeneratorService:
    def __init__(self, config_generator_store):
        self.config_generator_store = config_generator_store

    def format_json_config(config: ConfigGenerator):
        result = {}
        if config.hasScrambleField:
            result["scrambleField"] = {"defaultScrambling": {"applies_to_fields": config.scrambleField_fields}}
        if config.hasDateShift:
            result["dateShift"] = {"defaultDateShift": {"low_range": config.dateShift_lowrange,
                                                        "high_range":config.dateShift_highrange}}
        if config.hassubFieldList: #TODO list
            result["substituteFieldList"] = {"subIDlist": {
                "applies_to_field":config.subFieldList_fields,
                "substitution_list":config.subFieldList_substitute,
                "replacement": config.subFieldList_replacement
            }}
        if config.hassubFieldRegex: #TODO list
            result["substituteFieldRegex"] = {"substituteFieldRegex" : {
                "applies_to_field": config.subFieldRegex_fields,
                "regex": config.subFieldRegex_regex,
                "replacement": config.subFieldRegex_replacement
            }}

        return json.dumps(result)

    def create_config(self, user,config: ConfigGenerator):
        response = self.config_generator_store.create_config(user,config)
        return response

    def get_configs(self,userid:int,tenantid:int) -> List[ConfigGenerator]:
        configs = self.config_generator_store.get_configs(userid,tenantid)
        # result = [self.format_json_config(config) for config in configs]
        # return result
        return configs

    def get_configs_for_questionnaire(self, userid:int,questionnaireid:int,offset:int,limit:int) -> List[ConfigGenerator]:
        configs = self.config_generator_store.get_configs_for_questionnaire(userid=userid,questionnaireid=questionnaireid,offset=offset,limit=limit)
        # result = [self.format_json_config(config) for config in configs]
        # return result
        return configs
