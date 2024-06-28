from server_template.models import TemplatebackendConfig

# from server_template.models import TemplatebackendUpdatePasswordRequest
from src.internal.api.controllers.config_generator_controller import ConfigGeneratorController
from src.internal.util.interface.implements import implements_interface
from .authorization import *

class ConfigGeneratorControllerAuthentication():
    def __init__(self, next: ConfigGeneratorController):
        self.next = next
        implements_interface(ConfigGeneratorController, ConfigGeneratorControllerAuthentication)

    def config_service_get_configs(self, user):
        if not is_authenticated(user): # TODO admin?
            return None, 403
        return self.next.config_service_get_configs(user)

    def config_service_create_config(self,user,body: TemplatebackendConfig):
        if not is_authenticated(user): # TODO admin?
            return None, 403
        return self.next.config_service_create_config(user,body)
