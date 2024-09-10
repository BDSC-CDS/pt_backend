
import traceback
from typing import List
from src.pkg.config_generator.model.config_generator import ConfigGenerator
from src.pkg.config_generator.service.config_generator import ConfigGeneratorService
from server_template.models import TemplatebackendGetConfigsReply
from server_template.models import TemplatebackendGetConfigsResult
from server_template.models import TemplatebackendCreateConfigReply
from server_template.models import TemplatebackendCreateConfigResult
from server_template.models import TemplatebackendDeleteConfigReply
from server_template.models import TemplatebackendDeleteConfigResult
from server_template.models import TemplatebackendExportConfigReply


from server_template.models import TemplatebackendConfig
import src.internal.api.controllers.converter.config_generator as config_converter

class ConfigGeneratorController():
    def __init__(self,  config_generator_service):
        self.config_generator_service = config_generator_service

    def config_service_get_configs(self,user):
        try:
            configs_backend: List[ConfigGenerator] = self.config_generator_service.get_configs(user.id,user.tenantid)
            configs_frontend : List[TemplatebackendConfig] = [config_converter.config_from_business(c) for c in configs_backend]
            return TemplatebackendGetConfigsReply(TemplatebackendGetConfigsResult(config=configs_frontend))

        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

    def config_service_create_config(self,user,body: TemplatebackendConfig):
        config : ConfigGenerator =  config_converter.config_to_business(body)
        try:
            response = self.config_generator_service.create_config(user,config)
            return TemplatebackendCreateConfigReply(TemplatebackendCreateConfigResult(id=response))

        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500


    def config_service_delete_config(self,user,id:int):
        try:
            response = self.config_generator_service.delete_config(user,id)
            return TemplatebackendDeleteConfigReply(TemplatebackendDeleteConfigResult(success=response))
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

    def config_service_export_config(self,user,id:int):
        try:
            response = self.config_generator_service.export_config(user,id)
            return TemplatebackendExportConfigReply(config=response)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
