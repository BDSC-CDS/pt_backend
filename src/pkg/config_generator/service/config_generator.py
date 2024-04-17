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
        if config.hassubFieldList:
            result["substituteFieldList"] = {"subIDlist": {
                "applies_to_field":config.subFieldList_fields,
                "substitution_list":config.subFieldList_substitute,
                "replacement": config.subFieldList_replacement
            }}
        if config.hassubFieldRegex:
            result["substituteFieldRegex"] = {"substituteFieldRegex" : {
                "applies_to_field": config.subFieldRegex_fields,
                "regex": config.subFieldRegex_regex,
                "replacement": config.subFieldRegex_replacement
            }}

        return json.dumps(result)

    def create_config(self, config: ConfigGenerator):
        self.config_generator_store.create_config(config)

    def get_configs(self,offset:int,limit:int):
        configs = self.config_generator_store.get_configs(offset,limit)
        result = [self.format_json_config(config) for config in configs]
        return result

    def get_configs_for_user(self, identifier:int,offset:int,limit:int):
        configs = self.config_generator_store.get_configs_for_user(identifier=identifier,offset=offset,limit=limit)
        result = [self.format_json_config(config) for config in configs]
        return result
