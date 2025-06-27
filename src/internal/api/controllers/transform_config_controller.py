
import traceback
import flask
from typing import List
from src.pkg.transform_config.model.transform_config import TransformConfig
from server_template.models import TemplatebackendListTransformConfigsReply
from server_template.models import TemplatebackendListTransformConfigsResult
from server_template.models import TemplatebackendCreateTransformConfigReply
from server_template.models import TemplatebackendCreateTransformConfigResult
from server_template.models import TemplatebackendDeleteTransformConfigReply
from server_template.models import TemplatebackendDeleteTransformConfigResult
from server_template.models import TemplatebackendExportTransformConfigReply
from server_template.models import TemplatebackendCreateTransformConfigRequest

import src.internal.api.controllers.converter.transform_config as transform_config_converter

class TransformConfigServiceController():
    def __init__(self,  transform_config_service):
        self.transform_config_service = transform_config_service

    def transform_config_service_create_transform_config(self, user, body: TemplatebackendCreateTransformConfigRequest):
        config: TransformConfig =  transform_config_converter.transform_config_to_business(body.config)
        try:
            response = self.transform_config_service.create_transform_config(user.id, user.tenantid, config)
            return TemplatebackendCreateTransformConfigReply(TemplatebackendCreateTransformConfigResult(id=response))

        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

    def transform_config_service_list_transform_configs(self, user, offset: int=None, limit: int=None):
        try:
            configs_backend: List[TransformConfig] = self.transform_config_service.list_transform_configs(user.id, user.tenantid, offset, limit)
            configs_frontend : List[TemplatebackendCreateTransformConfigRequest] = [transform_config_converter.transform_config_from_business(c) for c in configs_backend] if configs_backend else []
            return TemplatebackendListTransformConfigsReply(TemplatebackendListTransformConfigsResult(configs=configs_frontend))

        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

    def transform_config_service_delete_transform_config(self, user, id:int):
        try:
            response = self.transform_config_service.delete_transform_config(user.id, user.tenantid, id)
            return TemplatebackendDeleteTransformConfigReply(TemplatebackendDeleteTransformConfigResult(success=response))
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500

    def transform_config_service_export_transform_config(self, user, id:int):
        try:
            response = self.transform_config_service.export_transform_config(user.id, user.tenantid, id)
            if response is None:
                return TemplatebackendExportTransformConfigReply(config=None), 404
            return TemplatebackendExportTransformConfigReply(config=response)
        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
        
    def transform_config_service_export_transform_config_json(self, user, id:int):
        try:
            config_str = self.transform_config_service.export_transform_config(user.id, user.tenantid, id)

            if config_str is None:
                return None, 404

            config_bytes = config_str.encode('utf-8')

            headers = {
                "Content-Type": "application/json",
            }

            resp = flask.Response(config_bytes, headers=headers)
            return resp, 200, headers

        except Exception as e:
            print("error", e)
            traceback.print_exception(e)
            return str(e), 500
