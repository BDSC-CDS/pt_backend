from typing import List
from src.pkg.config_generator.model.config_generator import ConfigGenerator
import json

class ConfigGeneratorService:
    def __init__(self, config_generator_store):
        self.config_generator_store = config_generator_store

    def export_config(self,user,id: int):
        return self.config_generator_store.export_config(user.id,user.tenantid,id)

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

    def delete_config(self,user,config_id:int):
        success = self.config_generator_store.delete_config(user,config_id)
        return success
