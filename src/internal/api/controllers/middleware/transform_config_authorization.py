from server_template.models import TemplatebackendCreateTransformConfigRequest
from controllers.transform_config_controller import (
    TransformConfigServiceController,
)
from src.internal.util.interface.implements import implements_interface
from .authorization import *


class TransformConfigServiceControllerAuthentication:
    def __init__(self, next: TransformConfigServiceController):
        self.next = next
        implements_interface(
            TransformConfigServiceController,
            TransformConfigServiceControllerAuthentication,
        )

    def transform_config_service_create_transform_config(self, user, body: TemplatebackendCreateTransformConfigRequest):
        if not is_authenticated(user):
            return None, 403
        return self.next.transform_config_service_create_transform_config(user, body)

    def transform_config_service_list_transform_configs(self, user, offset: int=None, limit: int=None):
        if not is_authenticated(user):
            return None, 403
        return self.next.transform_config_service_list_transform_configs(user, offset, limit)

    def transform_config_service_delete_transform_config(self, user, id: int):
        if not is_authenticated(user):
            return None, 403
        return self.next.transform_config_service_delete_transform_config(user, id)

    def transform_config_service_export_transform_config(self, user, id: int):
        if not is_authenticated(user):
            return None, 403
        return self.next.transform_config_service_export_transform_config(user, id)

    def transform_config_service_export_transform_config_json(self, user, id: int):
        if not is_authenticated(user):
            return None, 403
        return self.next.transform_config_service_export_transform_config_json(user, id)
