from typing import List
from src.pkg.transform_config.model.transform_config import TransformConfig

class TransformConfigService:
    def __init__(self, transform_config_store):
        self.transform_config_store = transform_config_store

    def create_transform_config(self, userid: int, tenantid: int, config: TransformConfig):
        response = self.transform_config_store.create_transform_config(userid, tenantid, config)
        return response
    
    def list_transform_configs(self, userid:int, tenantid:int, offset: int=None, limit: int=None) -> List[TransformConfig]:
        configs = self.transform_config_store.list_transform_configs(userid, tenantid, offset, limit)
        return configs
    
    def delete_transform_config(self, userid: int, tenantid: int, config_id:int):
        success = self.transform_config_store.delete_transform_config(userid, tenantid, config_id)
        return success

    def export_transform_config(self, userid: int, tenantid: int, id: int):
        return self.transform_config_store.export_transform_config(userid, tenantid, id)

    # def get_transform_configs_for_questionnaire(self, userid:int,questionnaireid:int,offset:int,limit:int) -> List[TransformConfig]:
    #     configs = self.transform_config_store.get_transform_configs_for_questionnaire(userid=userid,questionnaireid=questionnaireid,offset=offset,limit=limit)
    #     # result = [self.format_json_config(config) for config in configs]
    #     # return result
    #     return configs