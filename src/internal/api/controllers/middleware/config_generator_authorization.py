from server_template.models import TemplatebackendConfig
from src.internal.api.controllers.config_generator_controller import ConfigGeneratorServiceController
from src.internal.util.interface.implements import implements_interface
from .authorization import *

class ConfigGeneratorServiceControllerAuthentication():
    def __init__(self, next: ConfigGeneratorServiceController):
        self.next = next
        implements_interface(ConfigGeneratorServiceController, ConfigGeneratorServiceControllerAuthentication)

    def configuration_service_get_configs(self, user):
        if not is_authenticated(user):
            return None, 403
        return self.next.configuration_service_get_configs(user)

    def configuration_service_create_config(self,user,body: TemplatebackendConfig):
        if not is_authenticated(user):
            return None, 403
        return self.next.configuration_service_create_config(user,body)

    def configuration_service_delete_config(self,user,id:int):
        if not is_authenticated(user):
            return None, 403
        return self.next.configuration_service_delete_config(user,id)

    def configuration_service_export_config(self,user,id:int):
        if not is_authenticated(user):
            return None, 403
        return self.next.configuration_service_export_config(user,id)
